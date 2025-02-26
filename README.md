# Automação de Consulta de Horários de Ônibus ou Voos

Esta automação foi desenvolvida para realizar consultas automatizadas de horários de **ônibus ou voos** com base em informações fornecidas em uma planilha de entrada. A automação acessa sites de passagens, insere os dados necessários (como destino, data e horário) e extrai as informações de horários disponíveis. Os dados coletados são processados e inseridos em uma fila utilizando SQLite, permitindo o gerenciamento e processamento de consultas em paralelo.

## Tecnologias Utilizadas
- **Python**: Linguagem principal de desenvolvimento.
- **BotCity WebBot**: Framework utilizado para automação de navegação web.
- **Selenium**: Ferramenta usada para interação com os sites de consulta.
- **SQLite**: Banco de dados leve para gerenciar a fila de consultas.

## Como Usar

1. Clone este repositório.
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
