from dotenv import load_dotenv
import os
from crewai import Agent, Task, Crew
from fastmcp import FastMCP

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Verifica se a API Key está configurada
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("Por favor, configure a OPENAI_API_KEY no arquivo .env")

# Configuração do FastMCP
mcp = FastMCP()

# Definição dos agentes
agente_pesquisador = Agent(
    name="Pesquisador",
    goal="Realizar pesquisas e análises detalhadas",
    backstory="Especialista em coletar e analisar informações",
    verbose=True
)

agente_analista = Agent(
    name="Analista",
    goal="Analisar dados e gerar insights",
    backstory="Especialista em análise de dados e geração de relatórios",
    verbose=True
)

# Definição das tarefas
tarefa_pesquisa = Task(
    description="Realizar pesquisa inicial sobre o tema",
    agent=agente_pesquisador
)

tarefa_analise = Task(
    description="Analisar os dados coletados",
    agent=agente_analista
)

# Criação da crew
crew = Crew(
    agents=[agente_pesquisador, agente_analista],
    tasks=[tarefa_pesquisa, tarefa_analise]
)

if __name__ == "__main__":
    resultado = crew.kickoff()
    print(resultado)