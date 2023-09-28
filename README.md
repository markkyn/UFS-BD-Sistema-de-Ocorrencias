# UFS-BD-Sistema-de-Ocorrencias
Programa em Django Python com objetivo de criar uma API seguindo os Projetos Conceitual e Lógico criados durante a disciplina.

## Contextualização
Projeto de sistema de ocorrências, idealizado por Marcos Gabriel e Vinícius Peroba, para disciplina de Banco de Dados da Universidade Federal de Sergipe (2023.1 - Turma 01)

O projeto consiste em aplicar os conhecimento de diagramação de projeto conceitual e lógico, e a implementação de uma API que realize CRUD`s, seguindo as regras de negócios estabelecidas na especificação.

## Atividades da Disciplina:
Para facilitar o trabalho avaliação do professor, estou disponibilizando nesse repositório os links para cada atividade proposta pelo SIGAA.

- Atividade 1: [Conexão com Banco AWS](./docs/atividades/etapa_1.py) 
- Atividade 2: Estudos sobre Bancos de Dados e Sistemas Gerenciamento de Banco de dados 
- Atividade 3: [Projeto Conceitual](./docs/diagrams/[Banco%20de%20Dados]%20Projeto%20Conceitual-1.pdf)
- Atividade 4: [Projeto Lógico](./docs/diagrams/projeto_logico.png)
- Atividade 5: [Consultas SQL](./docs/sql/consultas_atv5.sql)

## Instalação:
### Certifique-se de possuir os pre-requisitos:
- Faça instalação do [Docker e DockerCompose](https://docs.docker.com/get-docker/)
 
- Obtenha a versão do Python 3.8 ou superior - Possivelmente munciona em versões abaixo, porém não foi testada


### Clone o repositório
```shell
    git clone git@github.com:markkyn/UFS-BD-Sistema-de-Ocorrencias.git
    cd UFS-BD-Sistema-de-Ocorrencias
```

### Suba o container Docker
```shell
cd docker
./docker_container.sh
```
Concluida essa etapa sem erros, você deve ter um container docker funcionando com o sistema Django em questão.

Com um cliente HTTP ou pelo proprio navegador acesse: 
- **Módulo de Modelos Comuns:** http://localhost:8001/swagger/comum
- **Módulo de Ocorrências:** http://localhost:8001/swagger/ocorrencias

    
## Estrutura de Projeto:
    .
    ├── docker                  # Arquivos de Docker
    ├── docs                    # Arquivos de Documentação
    │   ├── diagrams        # Diagramas de Projeto
    │   └── sql                 # Scripts SQL 
    └── src                     # Projeto Django 
        └── core                # Core do Projeto
