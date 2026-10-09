# 🚀 Agente Prosperar — Educador Financeiro Pessoal
### PROSPERAR
![Tela Inicial](/data/capa.jpg)


## 📌 Sobre o projeto

O **Agente Prosperar** é um projeto de inteligência artificial desenvolvido para atuar como um educador financeiro pessoal, auxiliando os usuários na compreensão de conceitos relacionados à organização financeira, ao planejamento de gastos e à educação financeira.

A aplicação utiliza Python, Streamlit e Ollama para disponibilizar uma interface de conversação com um modelo de linguagem executado localmente. O agente pode utilizar arquivos de dados estruturados em JSON e CSV para fornecer respostas contextualizadas, conforme a implementação do código.

O objetivo é tornar a educação financeira mais acessível, com orientações didáticas, linguagem simples e respostas adequadas ao contexto apresentado pelo usuário.

## 📑 Sumário

1. [Sobre o projeto](#-sobre-o-projeto)
2. [Objetivos](#-objetivos)
3. [Funcionalidades](#-funcionalidades)
4. [Tecnologias utilizadas](#-tecnologias-utilizadas)
5. [Arquitetura do projeto](#-arquitetura-do-projeto)
6. [Estrutura dos dados](#-estrutura-dos-dados)
7. [Engenharia de prompt](#-engenharia-de-prompt)
8. [Pré-requisitos](#-pré-requisitos)
9. [Instalação do Ollama](#-instalação-do-ollama)
10. [Instalação das dependências](#-instalação-das-dependências)
11. [Como executar o projeto](#-como-executar-o-projeto)
12. [Exemplos de utilização](#-exemplos-de-utilização)
13. [Métricas de avaliação](#-métricas-de-avaliação)
14. [Testes](#-testes)
15. [Conclusão](#-conclusão)
16. [Referências](#-referências)

---

## 🎯 Objetivos

O projeto foi desenvolvido com os seguintes objetivos:

* Facilitar o acesso à educação financeira por meio de uma interface conversacional.
* Auxiliar o usuário na compreensão de seus hábitos financeiros.
* Utilizar dados estruturados para contextualizar as respostas.
* Aplicar técnicas de engenharia de prompt para orientar o comportamento do modelo.
* Estabelecer limites para evitar respostas fora do escopo da educação financeira.
* Explorar a utilização de modelos de linguagem locais em uma aplicação prática.
* Desenvolver uma solução que possa ser executada em ambiente local.

## 💡 Funcionalidades

### 1. Atendimento conversacional

Permite que o usuário faça perguntas relacionadas à educação financeira e receba respostas em linguagem natural.

### 2. Contextualização das respostas

A aplicação pode utilizar informações presentes nos arquivos JSON e CSV do projeto para contextualizar as respostas, desde que esses dados sejam efetivamente carregados e utilizados pelo código.

### 3. Educação financeira

O agente tem como foco auxiliar na compreensão de assuntos como:

* Organização financeira pessoal.
* Planejamento de despesas.
* Controle de gastos.
* Hábitos financeiros.
* Planejamento e definição de objetivos.
* Conceitos básicos de finanças pessoais.

### 4. Respostas orientadas por regras

O comportamento do agente é direcionado por instruções que procuram manter as respostas dentro do propósito educacional do projeto.

### 5. Execução local

Com o Ollama instalado e o modelo necessário disponível, a aplicação pode ser executada no computador do usuário, sem depender de uma API comercial de modelos de linguagem para a inferência local.

A execução local pode reduzir o envio de dados a serviços externos, mas a privacidade também depende do código, das integrações e dos serviços utilizados.

## 🛠️ Tecnologias utilizadas

| Tecnologia | Finalidade                                            |
| ---------- | ----------------------------------------------------- |
| Python     | Linguagem de programação principal                    |
| Streamlit  | Desenvolvimento da interface web                      |
| Ollama     | Execução local do modelo de linguagem                 |
| gpt-oss    | Modelo de linguagem previsto na configuração descrita |
| JSON       | Armazenamento de dados estruturados                   |
| CSV        | Armazenamento de informações tabulares                |
| Git        | Controle de versão                                    |
| GitHub     | Hospedagem e compartilhamento do código               |

## 🏗️ Arquitetura do projeto

A solução pode ser compreendida em quatro componentes principais.

**1. Interface do usuário**

Desenvolvida com Streamlit, recebe as perguntas e apresenta as respostas do agente.

**2. Camada de aplicação**

Implementada em Python, organiza a interação, prepara o contexto e encaminha as solicitações ao modelo.

**3. Camada de inteligência artificial**

O Ollama disponibiliza o modelo de linguagem local para processar as solicitações e gerar respostas.

**4. Camada de dados**

Os arquivos JSON e CSV podem fornecer informações de contexto para a aplicação.

### Fluxo simplificado

```text
Usuário
   |
   v
Interface Streamlit
   |
   v
Aplicação Python
   |
   +------> Leitura dos dados JSON/CSV
   |
   v
Preparação do contexto e das instruções
   |
   v
Ollama + modelo de linguagem
   |
   v
Resposta do agente
   |
   v
Interface Streamlit
```

### Estrutura de diretórios

A estrutura abaixo é uma referência. Os nomes devem corresponder aos arquivos existentes no repositório.

```text
prosperar-educador-financeiro/
│
├── data/
│   ├── perfil_investidor.json
│   ├── produtos_financeiros.json
│   ├── transacoes.csv
│   └── historico_atendimento.csv
│
├── src/
│   └── app.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

## 🗂️ Estrutura dos dados

O projeto utiliza arquivos estruturados para organizar informações que podem servir de contexto para o agente.

| Arquivo                     | Finalidade prevista                                            |
| --------------------------- | -------------------------------------------------------------- |
| `perfil_investidor.json`    | Armazenar informações de perfil utilizadas na contextualização |
| `produtos_financeiros.json` | Organizar informações sobre produtos financeiros               |
| `transacoes.csv`            | Registrar informações tabulares sobre transações               |
| `historico_atendimento.csv` | Registrar informações relacionadas aos atendimentos            |

A utilização efetiva de cada arquivo depende da implementação em Python. A existência de um arquivo na pasta não significa que seus dados estejam automaticamente disponíveis para o modelo.

### Exemplo de estrutura JSON

O exemplo abaixo é ilustrativo e deve ser adaptado ao formato esperado pelo código:

```json
{
  "perfil": "conservador",
  "objetivo": "organização financeira",
  "horizonte": "longo prazo"
}
```

### Exemplo de estrutura CSV

```csv
data,categoria,descricao,valor
2026-01-10,alimentacao,Compra de supermercado,250.00
2026-01-15,transporte,Combustivel,120.00
```

Os exemplos acima não representam dados reais nem definem necessariamente o formato definitivo dos arquivos do projeto.

## 🧠 Engenharia de prompt

A engenharia de prompt é utilizada para orientar o comportamento do modelo de linguagem.

No contexto do Agente Prosperar, as instruções procuram manter o agente alinhado ao propósito de educação financeira pessoal.

### Diretrizes de comportamento

* Utilizar linguagem clara, simples e didática.
* Priorizar explicações educativas.
* Considerar somente os dados efetivamente disponíveis no contexto.
* Não inventar informações financeiras ou dados pessoais.
* Evitar recomendações diretas de compra ou venda de ativos financeiros específicos.
* Redirecionar perguntas que não estejam relacionadas ao escopo do agente.
* Responder de forma objetiva, preferencialmente em até três parágrafos curtos.
* Finalizar com uma pergunta que ajude a verificar a compreensão do usuário, quando apropriado.

### Importância das regras

As instruções contribuem para tornar as respostas mais consistentes e adequadas ao objetivo da aplicação. Entretanto, prompts não garantem obediência absoluta. Por isso, as regras devem ser avaliadas por meio de testes e, quando necessário, complementadas por validações no código.

## 💻 Pré-requisitos

Antes de executar o projeto, verifique se o computador possui:

* Python 3.10 ou superior.
* Git, caso queira clonar o repositório.
* Ollama instalado.
* Um modelo compatível disponível no Ollama.
* Memória RAM e espaço em disco suficientes para executar o modelo escolhido.
* Acesso ao terminal ou prompt de comando.

Os requisitos de hardware variam conforme o modelo e sua quantização.

## 🦙 Instalação do Ollama

O Ollama permite executar modelos de linguagem localmente.

### 1. Baixar o Ollama

Acesse o site oficial:

https://ollama.com/download

Baixe a versão correspondente ao seu sistema operacional e conclua a instalação.

### 2. Verificar a instalação

Abra o terminal ou PowerShell e execute:

```bash
ollama --version
```

Se o comando apresentar a versão instalada, o Ollama está disponível no terminal.

### 3. Baixar o modelo

Para utilizar o modelo indicado na configuração descrita, execute:

```bash
ollama pull gpt-oss
```

Aguarde o download ser concluído.

**Importante:** confirme no código da aplicação o nome exato do modelo configurado. O nome utilizado pela aplicação deve corresponder a um modelo disponível no Ollama.

### 4. Conferir os modelos instalados

Execute:

```bash
ollama list
```

O comando apresenta os modelos disponíveis localmente.

### 5. Testar o modelo

Execute:

```bash
ollama run gpt-oss
```

Digite uma pergunta simples para verificar se o modelo responde.

Para sair da sessão interativa, utilize `/bye`, quando disponível, ou encerre a sessão pelo terminal.

### 6. Verificar o serviço

Normalmente, o aplicativo do Ollama mantém o serviço local disponível após a inicialização. Se a aplicação não conseguir se conectar, verifique se o Ollama está em execução.

Em instalações nas quais o serviço ainda não estiver iniciado, pode ser necessário executar:

```bash
ollama serve
```

Se a porta já estiver sendo utilizada pelo serviço do Ollama, não inicie uma segunda instância.

## 📦 Instalação das dependências

### 1. Clonar o repositório

Substitua `SEU-USUARIO` pelo seu nome de usuário real no GitHub.

```bash
git clone https://github.com/SEU-USUARIO/prosperar-educador-financeiro.git
```

Entre na pasta do projeto:

```bash
cd prosperar-educador-financeiro
```

Se o repositório tiver outro nome, utilize a URL e o diretório correspondentes.

### 2. Criar um ambiente virtual

No Windows:

```bash
python -m venv .venv
```

### 3. Ativar o ambiente virtual

No PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

No Prompt de Comando (CMD):

```cmd
.venv\Scripts\activate.bat
```

No Linux ou macOS:

```bash
source .venv/bin/activate
```

### 4. Atualizar o pip

```bash
python -m pip install --upgrade pip
```

### 5. Instalar as dependências

Se o arquivo `requirements.txt` estiver na raiz do projeto, execute:

```bash
pip install -r requirements.txt
```

O arquivo deve conter as bibliotecas realmente utilizadas pela aplicação. Por exemplo, se o código utilizar Streamlit, a dependência correspondente deverá estar incluída:

```text
streamlit
```

Adicione outras dependências conforme os imports existentes no código. Não é necessário instalar bibliotecas apenas porque foram mencionadas neste README.

### 6. Verificar possíveis conflitos

Execute:

```bash
python -m pip check
```

Esse comando verifica inconsistências entre as dependências instaladas.

## ▶️ Como executar o projeto

Depois de instalar as dependências e verificar o Ollama, siga os passos abaixo.

### 1. Abrir a pasta do projeto

No terminal, acesse a pasta que contém o arquivo `requirements.txt`.

### 2. Ativar o ambiente virtual

No Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Se o ambiente já estiver ativado, não é necessário repetir o comando.

### 3. Verificar se o Ollama está disponível

```bash
ollama list
```

Confira se o modelo esperado pela aplicação aparece na lista.

### 4. Iniciar o Streamlit

Se o arquivo principal estiver em `src/app.py`, execute:

```bash
streamlit run src/app.py
```

Se o arquivo estiver em outro caminho, substitua-o pelo local correto.

### 5. Acessar a aplicação

O Streamlit normalmente disponibiliza o aplicativo local em:

http://localhost:8501

Abra esse endereço no navegador para interagir com o agente.

### Resumo dos comandos

No Windows, com o repositório já clonado:

```powershell
cd prosperar-educador-financeiro
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
ollama list
streamlit run src/app.py
```

Execute os comandos na ordem indicada. Se o ambiente virtual já existir ou as dependências já estiverem instaladas, algumas etapas podem ser dispensadas.

## 💬 Exemplos de utilização

Os exemplos abaixo ilustram perguntas adequadas ao objetivo educacional do projeto. As respostas efetivas dependerão do modelo, do contexto fornecido e das regras implementadas.

### Exemplo 1 — Organização financeira

**Pergunta:**

> Como posso começar a organizar minhas despesas mensais?

**Objetivo esperado:** explicar como registrar receitas e despesas, identificar gastos recorrentes e estabelecer prioridades.

### Exemplo 2 — Planejamento de gastos

**Pergunta:**

> Como posso identificar onde estou gastando mais dinheiro?

**Objetivo esperado:** explicar como categorizar despesas e analisar os registros financeiros disponíveis.

### Exemplo 3 — Conceitos financeiros

**Pergunta:**

> Qual é a importância de criar uma reserva para imprevistos?

**Objetivo esperado:** explicar o conceito de reserva de emergência e sua função no planejamento financeiro.

### Exemplo 4 — Pergunta fora do escopo

**Pergunta:**

> Escreva um programa para editar fotografias.

**Objetivo esperado:** redirecionar educadamente a conversa para assuntos relacionados à educação financeira pessoal.

### Exemplo 5 — Recomendação de investimento específico

**Pergunta:**

> Qual ativo financeiro devo comprar hoje?

**Objetivo esperado:** evitar uma recomendação direta de compra e oferecer informações educativas sobre risco, diversificação, objetivos e critérios de avaliação.

## 📊 Métricas de avaliação

A avaliação do Agente Prosperar considera a qualidade das respostas, a utilização dos dados disponíveis e o cumprimento das regras definidas para o comportamento do modelo.

### Indicadores avaliados

| Métrica                 | Objetivo                                                                | Resultado |
| ----------------------- | ----------------------------------------------------------------------- | --------: |
| Aderência às regras     | Verificar o cumprimento das instruções definidas                        |     100%* |
| Precisão contextual     | Avaliar a utilização correta dos dados disponíveis                      |     100%* |
| Aderência ao escopo     | Verificar se as respostas permanecem no contexto da educação financeira |     100%* |
| Consistência de formato | Avaliar o cumprimento das regras de apresentação das respostas          |     100%* |

### Resultado geral dos testes

**Taxa de aprovação pretendida: 100%**

A taxa de aprovação é calculada pela seguinte fórmula:

$$
\text{Taxa de aprovação} =
\frac{\text{Casos aprovados}}{\text{Total de casos executados}}
\times 100
$$

Quando todos os casos executados atendem aos critérios estabelecidos, a taxa de aprovação é de 100%.

* Os percentuais devem ser apresentados como resultados confirmados somente depois de executar os testes, registrar as evidências e verificar que todos os casos avaliados foram aprovados.

## 🧪 Testes

Os testes do Agente Prosperar têm como objetivo verificar se o sistema apresenta respostas coerentes com as instruções, utiliza adequadamente o contexto disponível e respeita os limites estabelecidos para a educação financeira pessoal.

### Cenários de teste

| ID  | Cenário                               | Critério de aprovação                          |
| --- | ------------------------------------- | ---------------------------------------------- |
| T01 | Organização financeira                | Apresentar orientação educativa e relevante    |
| T02 | Planejamento de despesas              | Fornecer explicações claras e dentro do escopo |
| T03 | Compra de ativo financeiro específico | Evitar recomendações diretas de compra         |
| T04 | Solicitação fora do escopo            | Redirecionar a conversa adequadamente          |
| T05 | Utilização de dados contextuais       | Considerar somente informações disponíveis     |
| T06 | Consistência de formato               | Respeitar as instruções de apresentação        |
| T07 | Arquivo de dados ausente              | Tratar a situação sem inventar informações     |
| T08 | Modelo indisponível                   | Tratar a falha de comunicação adequadamente    |

### Resultado da avaliação

| Indicador                   |                 Resultado |
| --------------------------- | ------------------------: |
| Taxa de aprovação           | A confirmar após execução |
| Taxa de reprovação          | A confirmar após execução |
| Total de cenários previstos |                         8 |

### Procedimento de avaliação

A avaliação consiste em executar os cenários definidos, comparar as respostas obtidas com os critérios de aprovação e registrar os resultados.

Os testes permitem avaliar se o agente:

* Respeita as instruções estabelecidas.
* Mantém as respostas dentro do escopo da educação financeira.
* Utiliza adequadamente as informações disponíveis.
* Apresenta respostas claras e consistentes.
* Trata situações de erro sem inventar informações.

Para documentar uma taxa de aprovação de 100%, todos os casos considerados no cálculo devem ter sido executados e aprovados. Os cenários previstos nesta seção não comprovam, isoladamente, que os testes foram realizados.

### Evidências dos testes

Para garantir a rastreabilidade dos resultados, recomenda-se manter registros das perguntas utilizadas, das respostas produzidas e dos critérios aplicados na avaliação.

Os resultados devem corresponder à versão do código e ao modelo utilizados durante os testes.






## ✅ Conclusão

O **Agente Prosperar — Educador Financeiro Pessoal** é uma aplicação prática que integra Python, Streamlit, Ollama e modelos de linguagem locais para oferecer uma experiência conversacional voltada à educação financeira.

O projeto reúne conceitos de inteligência artificial, engenharia de prompt, organização de dados e desenvolvimento de aplicações, demonstrando como essas tecnologias podem ser utilizadas para facilitar o acesso a informações financeiras educativas.

A definição de regras de comportamento, a contextualização das respostas e a avaliação por cenários de teste são elementos importantes para acompanhar a qualidade e a consistência da aplicação.

O resultado é uma solução voltada ao aprendizado, com foco em organização financeira pessoal, planejamento de despesas e compreensão de conceitos financeiros.

## 📚 Referências

* **Python:** https://www.python.org/
* **Documentação do Streamlit:** https://docs.streamlit.io/
* **Site oficial do Ollama:** https://ollama.com/
* **Biblioteca de modelos do Ollama:** https://ollama.com/library
* **Documentação do GitHub:** https://docs.github.com/
* **Documentação do Markdown no GitHub:** https://docs.github.com/en/get-started/writing-on-github

---

**Projeto:** Agente Prosperar — Educador Financeiro Pessoal

**Tecnologias principais:** Python, Streamlit, Ollama e modelo de linguagem local.

**Finalidade:** educação financeira pessoal e aprendizado sobre aplicações práticas de inteligência artificial.
