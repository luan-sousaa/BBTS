from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
from google import genai
from google.genai import types
import reportlab.lib.pagesizes as pagesizes
from reportlab.pdfgen import canvas
from textwrap import wrap
from reportlab.lib.pagesizes import A4
import re
from fpdf import FPDF
from fpdf.enums import XPos, YPos


def procurar_licitacoes():

    with sync_playwright() as p:
        navegador = p.chromium.launch(headless=False) #inicia nosso navegador , nesse caso o crhome
        pagina = navegador.new_page() #abre uma nova aba no nosso navegador
        pagina.goto("https://pncp.gov.br/app/editais?q=&status=recebendo_proposta&pagina=1") #vai ate nossa pagina de licitacoes
        # preenche o campo de palavras chaves
        pagina.fill('input[id="keyword"]', 'microsoft')

        #filtros principais
        #modalidades
        pagina.click('//*[@id="modalidades"]/div/div/div[2]/input')

        #filtro para pregão
        pagina.click('div[title="Pregão - Presencial"]')
        pagina.click('div[title="Pregão - Eletrônico"]')

        #botao de pesquisar
        pagina.click('//*[@id="main-content"]/pncp-list/pncp-results-panel/pncp-tab-set/div/pncp-top-panel/div/div/div[3]/div[2]/button')

        # Espera por um seletor específico (por segurança) , para garantir que toda a pagina carregou
        pagina.wait_for_timeout(4000)
        html = pagina.content()
        soup = BeautifulSoup(html, 'html.parser')

        # variavel auxiliar que ira armazenar o conteudo dos for
        licitacoes = []

        #encontra e printa o formulario do html
        for formulario in soup.find_all('a'):
            texto = formulario.get_text(separator='\n', strip=True)

            # Remove caracteres nulos e espaços invisíveis
            texto = texto.replace('\x00', '')
            texto = re.sub(r'\n+', '\n', texto)  # reduz múltiplas quebras de linha seguidas
            texto = re.sub(r'\s{2,}', ' ', texto)  # substitui vários espaços seguidos por um único

            licitacoes.append(texto)

        # vai esperar 15 segundo ate fechar meu navegador
        time.sleep(10)
        return licitacoes

# Recebe as licitações extraídas
dados = procurar_licitacoes()

# Cria o PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font('helvetica', size=12)

# Adiciona um tít ulo
pdf.set_font("helvetica", 'B', 16)
pdf.cell(0, 10, "Licitações Disponíveis", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
pdf.set_font("helvetica", size=12)
pdf.ln(10)

# Adiciona o conteúdo
for linha in dados:
    pdf.multi_cell(0, 10, linha)
    pdf.ln(5)

# Salva o arquivo
pdf.output("relatorio.pdf")
