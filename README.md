Buscador de Licitações Públicas com Análise IA (BBTS)
Este projeto consiste em um script Python desenvolvido para a BBTS para automatizar a busca de licitações públicas no Portal Nacional de Contratações Públicas (PNCP), realizar uma análise inteligente dos dados coletados utilizando a API Gemini do Google e, por fim, gerar um relatório em PDF com os resultados.

Status do Projeto: Em Fase Teste

Funcionalidades Principais
Busca Automatizada: Navega no site PNCP e realiza buscas por licitações.
Filtragem: Permite a filtragem por palavra-chave (atualmente configurada para "microsoft") e modalidades de licitação (Pregão Presencial e Eletrônico).
Extração de Dados: Utiliza Playwright e BeautifulSoup4 para extrair informações relevantes das páginas de resultados.
Análise com Inteligência Artificial: Envia os dados das licitações para a API Gemini (modelo gemini-2.0-flash) para obter uma análise detalhada, incluindo resumo, requisitos, riscos, oportunidades e recomendações.
Geração de Relatório PDF: Cria um arquivo PDF (relatorio.pdf) contendo as licitações encontradas e a análise gerada pela IA, utilizando a biblioteca FPDF2 e fontes DejaVu para suporte a caracteres Unicode.
Tecnologias Utilizadas
Python 3.9
Bibliotecas Principais:
playwright==1.51.0: Para automação web e navegação.
beautifulsoup4==4.13.4: Para parsing de HTML.
google-generativeai: Para interação com a API Gemini do Google. 
fpdf2==2.8.3: Para geração de relatórios em PDF.
protobuf==6.31.0: (Provavelmente uma dependência do google-generativeai)
Pré-requisitos
Python 3.9
Navegador Chromium (o Playwright irá instalá-lo se necessário, mas é bom mencionar)
Uma chave de API válida do Google AI Studio para usar o modelo Gemini.
As fontes DejaVu TTF. O script espera encontrá-las em uma pasta dejavu-fonts-ttf-2.37/ttf/ relativa ao local do script. Você pode baixá-las em DejaVu Fonts.
Instalação
Clone o repositório (se aplicável):

Bash

git clone [URL_DO_REPOSITORIO]
cd [NOME_DO_REPOSITORIO]
Crie um ambiente virtual (recomendado):

Bash

python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
Instale as dependências:
Crie um arquivo requirements.txt com o seguinte conteúdo:

Plaintext

beautifulsoup4==4.13.4
fpdf2==2.8.3
playwright==1.51.0
protobuf==6.31.0
google-generativeai
E então execute:

Bash

pip install -r requirements.txt
Instale os navegadores do Playwright (se for a primeira vez usando):

Bash

playwright install chromium
Configure a Chave da API Gemini:
No arquivo Python ([NOME_DO_SEU_ARQUIVO_PYTHON].py), substitua "API_KEY" pela sua chave de API real na linha:

Python

client = genai.Client(api_key="SUA_CHAVE_API_AQUI")
Importante: Para maior segurança, considere usar variáveis de ambiente para armazenar sua chave API em vez de colocá-la diretamente no código.

Fontes DejaVu:
Baixe as fontes DejaVu (TTF) do site DejaVu Fonts e coloque os arquivos DejaVuSans.ttf e DejaVuSans-Bold.ttf dentro de uma estrutura de pastas dejavu-fonts-ttf-2.37/ttf/ no mesmo diretório do seu script, ou ajuste os caminhos no código:

Python

pdf.add_font('DejaVu', '', 'caminho/para/dejavu-fonts-ttf-2.37/ttf/DejaVuSans.ttf', uni=True)
pdf.add_font('DejaVu', 'B', 'caminho/para/dejavu-fonts-ttf-2.37/ttf/DejaVuSans-Bold.ttf', uni=True)
Como Usar
Ajuste os Parâmetros de Busca (Opcional):
No arquivo Python, você pode modificar:

A palavra-chave da busca na linha:
Python

pagina.fill('input[id="keyword"]', 'sua_palavra_chave_aqui')
Os filtros de modalidade, se necessário, alterando as linhas de pagina.click(...) correspondentes.
Execute o script:

Bash

python [NOME_DO_SEU_ARQUIVO_PYTHON].py
Verifique o Relatório:
Após a execução, um arquivo chamado relatorio.pdf será gerado no mesmo diretório do script, contendo as licitações encontradas e a análise da IA.

Exemplo de Saída do PDF
O PDF gerado incluirá:

Uma seção com "Licitações Disponíveis", listando os detalhes extraídos do PNCP.
Licitações Disponíveis
Portal Nacional de Contratações Públicas
...
Edital nº 27/2025
Id contratação PNCP: 00814574000101-1-000045/2025
Modalidade da Contratação: Pregão - Eletrônico
...
Uma seção com "Análise da IA - Relatório Inteligente", contendo o texto gerado pelo modelo Gemini.
Análise da IA - Relatório Inteligente
## Relatório de Análise de Licitações
**Data:** [Data da Geração]
...
Motivação / Objetivo
projeto academico motivado pela UCB e BBTS

Próximos Passos / Melhorias Futuras (Opcional)
formatação do texto gerado pela IA

Autores
Luan
