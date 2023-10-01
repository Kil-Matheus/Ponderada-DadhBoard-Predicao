### Código Fonte: `app.py`

**Resumo:**
O código `app.py` é um aplicativo web baseado em FastAPI e Streamlit para prever o número de acidentes de trânsito com base em várias variáveis de entrada. O aplicativo inclui um sistema de autenticação simples e integração com um modelo de Machine Learning treinado para fazer previsões.

**Dependências:**
- [FastAPI](https://fastapi.tiangolo.com/): Um framework para criar APIs web rápidas.
- [uvicorn](https://www.uvicorn.org/): Um servidor ASGI de alto desempenho para Python.
- [psycopg2](https://pypi.org/project/psycopg2/): Uma biblioteca Python para trabalhar com PostgreSQL.
- [Jinja2Templates](https://jinja.palletsprojects.com/): Um mecanismo de renderização de modelos para criação de páginas HTML.
- [jwt](https://pypi.org/project/PyJWT/): Uma biblioteca para gerar e verificar tokens JWT (JSON Web Tokens).
- [subprocess](https://docs.python.org/3/library/subprocess.html): Uma biblioteca para criar e gerenciar subprocessos.
- [streamlit](https://streamlit.io/): Uma biblioteca para criação de aplicativos web de forma rápida.
- [pandas](https://pandas.pydata.org/): Uma biblioteca para análise e manipulação de dados em Python.

**Configuração do Banco de Dados:**
O código inclui uma conexão com um banco de dados PostgreSQL usando a biblioteca psycopg2. A configuração do banco de dados, incluindo o nome do banco, usuário e senha, está no início do arquivo.

**Autenticação JWT:**
O aplicativo utiliza a autenticação JWT (JSON Web Token) para proteger a rota "/home". Um segredo (SECRET_KEY) é usado para assinar e verificar os tokens JWT. Os tokens têm uma expiração de 30 segundos a partir do momento em que são gerados.

**Roteamento de Endpoints:**

1. Rota "/" (Raiz):
   - Esta rota retorna uma página HTML de login.

2. Rota "/login" (Autenticação):
   - Aceita solicitações POST com dados de usuário e senha.
   - Verifica as credenciais no banco de dados PostgreSQL.
   - Se as credenciais forem válidas, gera um token JWT e o retorna como resposta.

3. Rota "/home":
   - Esta rota é protegida por autenticação JWT.
   - Inicia um aplicativo Streamlit em segundo plano através do subprocess.Popen.
   - Exibe um iframe incorporando o aplicativo Streamlit em uma página HTML.

**Inicialização do Aplicativo:**
O aplicativo FastAPI é inicializado usando o `uvicorn.run` no final do arquivo. Ele é configurado para ser executado na porta 80.

### Código Fonte: `teste.py`

Este arquivo contém o código do aplicativo Streamlit que permite aos usuários inserir dados para fazer previsões de acidentes com base em um modelo de Machine Learning. O aplicativo Streamlit é bastante interativo e inclui um formulário para inserção de dados e um botão para fazer previsões.

**Dependências:**
- [streamlit](https://streamlit.io/): Uma biblioteca para criação de aplicativos web de forma rápida.
- [pandas](https://pandas.pydata.org/): Uma biblioteca para análise e manipulação de dados em Python.
- [pycaret](https://pycaret.org/): Uma biblioteca para treinar e implantar modelos de Machine Learning.

**Funcionalidade:**
- O aplicativo permite que o usuário insira dados, incluindo data, quilômetros percorridos e várias outras variáveis relacionadas ao tráfego.
- Os dados inseridos são usados para fazer previsões de acidentes com base em um modelo de Machine Learning previamente treinado.
- As previsões são exibidas na interface do aplicativo Streamlit após o usuário clicar no botão "Fazer Previsão".

**Vídeo de Funcionamento na AWS**

https://drive.google.com/file/d/1mPe4PzE-Kaz3r0vOlDuH820S98VrjS04/view?usp=sharing

**Link do GitHub**
https://github.com/Kil-Matheus/Ponderada-DashBoard-Predicao

**Link do Docker Hub**
https://hub.docker.com/repository/docker/kilmatheus/ponderada-dash-predicao