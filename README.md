Job Insights Project 🚀

Neste projeto, desenvolvi uma série de análises sobre um conjunto de dados de empregos extraídos do Glassdoor. As implementações foram integradas a um aplicativo Web utilizando o framework Flask. O foco principal foi aplicar conceitos de manipulação de arquivos CSV, tratamento de exceções, filtros de dados e escrita de testes com Pytest em Python.

🛠 Habilidades Desenvolvidas

Manipulação de arquivos (Leitura de CSV).

Uso de estruturas condicionais e de repetição para filtragem de dados.

Tratamento de exceções com raise ValueError.

Escrita de módulos e importações customizadas.

Desenvolvimento de testes unitários com Pytest.

Criação de rotas e views básicas em Flask.

📂 Estrutura do Projeto

O código principal está organizado da seguinte forma:

src/jobs.py: Responsável pela carga e leitura dos dados.

src/insights.py: Contém as lógicas de negócio e filtros (salário, indústria, tipo de vaga).

src/sorting.py: Algoritmos de ordenação das vagas.

src/routes_and_views.py: Definição das rotas Flask (incluindo o requisito bônus da página individual).

tests/: Testes automatizados para garantir a confiabilidade das funções.

🚀 Como Executar o Projeto

1. Clonar o Repositório

git clone https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git

cd NOME_DO_REPOSITORIO

2. Configurar o Ambiente Virtual

python3 -m venv .venv && source .venv/bin/activate

3. Instalar Dependências

pip install -r dev-requirements.txt

4. Executar a Aplicação Flask

Para ver o projeto funcionando no navegador:

flask run
Acesse em: http://localhost:5000

🧪 Executando Testes e Linter

Para rodar todos os testes:

python3 -m pytest

Para rodar o Linter (Flake8):

python3 -m flake8

✅ Requisitos Implementados

read: Leitura de arquivos CSV.

get_unique_job_types: Identificação de tipos únicos de empregos.

get_unique_industries: Identificação de indústrias únicas.

get_max_salary / get_min_salary: Busca pelos limites salariais.

filter_by_job_type / filter_by_industry: Filtros específicos de busca.

matches_salary_range: Validação se um salário está dentro da faixa.

filter_by_salary_range: Filtragem baseada em valores numéricos.

test_sorting_by_criteria: Testes para a função de ordenação.

Job Page (Bônus): Rota dinâmica para exibir detalhes de uma vaga específica.

Nota: Este projeto foi desenvolvido individualmente como parte do currículo da Trybe.