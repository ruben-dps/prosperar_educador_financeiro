# 🚀 Agente Prosperar — Educador Financeiro Pessoal

## 📌 Sobre o projeto

O **Agente Prosperar** é um projeto de inteligência artificial desenvolvido para atuar como um educador financeiro pessoal, auxiliando os usuários na compreensão de conceitos relacionados à organização financeira, ao planejamento de gastos e à educação financeira.

A aplicação utiliza Python, Streamlit e Ollama para disponibilizar uma interface de conversação com um modelo de linguagem executado localmente. O agente utiliza arquivos de dados estruturados em JSON e CSV para fornecer respostas contextualizadas.

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
15. [Limitações e privacidade](#-limitações-e-privacidade)
16. [Melhorias futuras](#-melhorias-futuras)
17. [Conclusão](#-conclusão)
18. [Referências](#-referências)

---

## 🎯 Objetivos

O projeto foi desenvolvido com os seguintes objetivos:

* Facilitar o acesso à educação financeira por meio de uma interface conversacional.
* Ajudar o usuário a compreender melhor seus hábitos financeiros.
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

> A execução local não garante, por si só, que todos os dados permaneçam privados. Isso também depende do código, das integrações e dos serviços utilizados pela aplicação.

## 🛠️ Tecnologias utilizadas

| Tecnologia   | Finalidade                                             |
| ------------ | ------------------------------------------------------ |
| Python       | Linguagem de programação principal                     |
| Streamlit    | Desenvolvimento da interface web                       |
| Ollama       | Execução local do modelo de linguagem                  |
| gpt-oss      | Modelo de linguagem utilizado na configuração descrita |
| JSON         | Armazenamento de dados estruturados                    |
| CSV          | Armazenamento de informações tabulares                 |
| Git e GitHub | Versionamento e disponibilização do código             |

## 🏗️ Arquitetura do projeto

A solução pode ser compreendida em quatro componentes principais.

**1. Interface do usuário**

Desenvolvida com Streamlit, recebe as perguntas e apresenta as respostas do agente.

**2. Camada de aplicação**

Implementada em Python, é responsável por organizar a interação, preparar o contexto e encaminhar as solicitações ao modelo.

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
Ollama + modelo gpt-oss
   |
   v
Resposta do agente
   |
   v
Interface Streamlit
```

### Estrutura de diretórios

A estrutura abaixo é uma referência. Ajuste os nomes conforme os arquivos existentes no seu repositório.

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

Os exemplos acima não representam dados reais e não devem ser interpretados como o formato definitivo dos arquivos do projeto.

## 🧠 Engenharia de prompt

A engenharia de prompt é utilizada para orientar o comportamento do modelo de linguagem.

No contexto do Agente Prosperar, as instruções devem ajudar a manter o agente alinhado ao propósito de educação financeira pessoal.

### Diretrizes de comportamento

* Utilizar linguagem clara, simples e didática.
* Priorizar explicações educativas.
* Considerar somente os dados que estejam efetivamente disponíveis no contexto.
* Não inventar informações financeiras ou dados pessoais.
* Evitar recomendações diretas de compra ou venda de ativos financeiros específicos.
* Redirecionar perguntas que não estejam relacionadas ao escopo do agente.
* Responder de forma objetiva, preferencialmente em até três parágrafos curtos.
* Finalizar com uma pergunta que ajude a verificar a compreensão do usuário, quando apropriado.

### Importância das regras

As instruções contribuem para tornar as respostas mais consistentes e adequadas ao objetivo da aplicação. Entretanto, prompts não garantem obediência absoluta: as regras precisam ser avaliadas por meio de testes e, quando necessário, complementadas por validações no código.

## 💻 Pré-requisitos

Antes de executar o projeto, verifique se o computador possui:

* Python 3.10 ou superior.
* Git, caso queira clonar o repositório.
* Ollama instalado.
* Um modelo compatível disponível no Ollama.
* Memória RAM e espaço em disco suficientes para executar o modelo escolhido.
* Acesso ao terminal ou prompt de comando.

Os requisitos de hardware variam de acordo com o modelo e sua quantização.

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

Para utilizar o modelo indicado neste projeto, execute:

```bash
ollama pull gpt-oss
```

Aguarde o download ser concluído.

> **Importante:** confirme no código da aplicação o nome exato do modelo configurado. O nome informado ao Ollama deve corresponder ao modelo instalado e disponível na máquina.

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

Para sair da sessão interativa, utilize o comando `/bye`, quando disponível, ou encerre a sessão pelo terminal.

### 6. Disponibilizar o serviço

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

O arquivo deve conter as bibliotecas realmente utilizadas pela aplicação. Por exemplo, se o código utilizar Streamlit:

```text
streamlit
```

Adicione outras dependências conforme os imports existentes no código. Não é necessário instalar bibliotecas apenas porque foram mencionadas neste README.

### 6. Verificar possíveis conflitos

Execute:

```bash
python -m pip check
```

Esse comando verifica inconsistências entre dependências instaladas.

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

Se o arquivo estiver em outro caminho, substitua o caminho pelo local correto.

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

Os exemplos abaixo ilustram perguntas adequadas ao objetivo educacional do projeto. A resposta efetiva dependerá do modelo, do contexto fornecido e das regras implementadas.

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

A avaliação deve considerar não apenas se a resposta parece correta, mas também se o agente respeita as regras, utiliza adequadamente o contexto e permanece dentro do seu escopo.

### Indicadores propostos

| Métrica                 | O que avalia                                                                                         |
| ----------------------- | ---------------------------------------------------------------------------------------------------- |
| Aderência às regras     | Se a resposta respeita as instruções definidas                                                       |
| Precisão contextual     | Se utiliza corretamente os dados disponíveis                                                         |
| Aderência ao escopo     | Se evita responder como se fosse um agente de finalidade geral                                       |
| Consistência de formato | Se respeita o limite de extensão e a estrutura esperada                                              |
| Qualidade didática      | Se explica os conceitos de forma clara e compreensível                                               |
| Robustez                | Se mantém o comportamento esperado diante de perguntas ambíguas ou tentativas de contornar as regras |

### Cálculo de taxa de aprovação

Uma métrica simples é a taxa de aprovação dos casos de teste:

$$
\text{Taxa de aprovação} =
\frac{\text{Casos aprovados}}{\text{Total de casos executados}}
\times 100
$$

Por exemplo, se 18 de 20 casos forem aprovados:

$$
\frac{18}{20}\times100=90\%
$$

Esse resultado é apenas um exemplo de cálculo, não um resultado medido neste projeto.

### Taxa de conformidade das regras

Também é possível avaliar quantas respostas respeitaram determinada regra:

$$
\text{Conformidade} =
\frac{\text{Respostas conformes}}{\text{Respostas avaliadas}}
\times100
$$

A avaliação pode ser feita separadamente para cada categoria, permitindo identificar os pontos em que o agente precisa melhorar.

### Registro dos resultados

Recomenda-se utilizar uma tabela como a seguinte:

| Categoria                                  | Casos executados |   Aprovados | Taxa de aprovação |
| ------------------------------------------ | ---------------: | ----------: | ----------------: |
| Restrições sobre recomendações financeiras |      A preencher | A preencher |        A calcular |
| Personalização contextual                  |      A preencher | A preencher |        A calcular |
| Solicitações fora do escopo                |      A preencher | A preencher |        A calcular |
| Consistência de formato                    |      A preencher | A preencher |        A calcular |
| Robustez                                   |      A preencher | A preencher |        A calcular |

Preencha os resultados somente após executar os testes e registrar as evidências. Não declare aprovação de 100% sem os respectivos resultados verificáveis.

## 🧪 Testes

Os testes devem verificar se o agente responde de maneira coerente com as instruções e com os dados fornecidos.

### Casos de teste recomendados

| ID  | Cenário                                    | Critério de aprovação                      |
| --- | ------------------------------------------ | ------------------------------------------ |
| T01 | Pergunta sobre organização financeira      | Resposta educativa e relevante             |
| T02 | Pergunta sobre planejamento de despesas    | Orientação clara e dentro do escopo        |
| T03 | Solicitação de compra de ativo específico  | Não fornecer recomendação direta de compra |
| T04 | Pergunta sem relação com finanças pessoais | Redirecionar a conversa                    |
| T05 | Pergunta que exige dados do contexto       | Utilizar somente informações disponíveis   |
| T06 | Solicitação de resposta extensa            | Respeitar as regras de formato definidas   |
| T07 | Arquivo de dados ausente                   | Tratar o erro sem inventar informações     |
| T08 | Modelo indisponível                        | Informar ou tratar a falha de comunicação  |

### Procedimento de avaliação

1. Inicie a aplicação.
2. Execute cada cenário na interface.
3. Registre a pergunta enviada e a resposta recebida.
4. Compare a resposta com o critério de aprovação.
5. Marque o caso como aprovado ou reprovado.
6. Calcule as taxas de aprovação por categoria.
7. Revise as instruções ou o código quando encontrar falhas.
8. Execute novamente os casos afetados para verificar se a correção funcionou.

### Evidências de teste

Para tornar a avaliação reproduzível, mantenha um registro com:

* Identificação do caso.
* Pergunta utilizada.
* Resposta produzida.
* Resultado esperado.
* Resultado obtido.
* Situação: aprovado ou reprovado.
* Observações sobre falhas encontradas.

A qualidade das respostas geradas por um modelo de linguagem pode variar. Por isso, os resultados devem ser associados à versão do código, ao modelo utilizado e às condições do teste.

## 🔐 Limitações e privacidade

### Limitações

* O modelo pode gerar informações incorretas ou imprecisas.
* As respostas dependem da qualidade dos dados e das instruções.
* Os dados disponíveis podem estar incompletos ou desatualizados.
* A execução local exige recursos computacionais compatíveis com o modelo.
* A engenharia de prompt reduz alguns riscos de comportamento inadequado, mas não garante a eliminação de erros.
* O agente tem finalidade educacional e não substitui aconselhamento financeiro profissional individualizado.

### Privacidade

Antes de publicar o projeto no GitHub:

* Remova dados pessoais reais dos arquivos JSON e CSV.
* Não publique senhas, tokens, chaves de API ou outras credenciais.
* Utilize dados fictícios ou anonimizados nos exemplos.
* Verifique se os registros de atendimento contêm informações identificáveis.
* Inclua no `.gitignore` os arquivos locais ou sensíveis que não devem ser versionados.
* Confira se o código transmite informações a serviços externos.

O uso do Ollama local pode reduzir a necessidade de enviar prompts a uma API externa, mas não elimina automaticamente todos os riscos de privacidade.

## 🚧 Melhorias futuras

Entre as possibilidades de evolução do projeto estão:

* Criar testes automatizados para os principais cenários.
* Implementar registro estruturado dos resultados de avaliação.
* Desenvolver validações para verificar os arquivos JSON e CSV.
* Melhorar o tratamento de erros de conexão com o Ollama.
* Adicionar histórico de conversas com controles de privacidade.
* Desenvolver relatórios de organização financeira com base nos dados disponíveis.
* Implementar testes de regressão após mudanças no prompt ou no modelo.
* Criar uma interface de acompanhamento das métricas.
* Documentar versões do modelo e configurações utilizadas em cada avaliação.

Essas melhorias são propostas para evolução futura e não significam que já estejam implementadas.

## ✅ Conclusão

O **Agente Prosperar — Educador Financeiro Pessoal** é uma aplicação prática para explorar a integração entre Python, Streamlit, modelos de linguagem locais e dados estruturados.

O projeto permite estudar conceitos de inteligência artificial aplicada, engenharia de prompt, desenvolvimento de interfaces e avaliação de respostas geradas por modelos de linguagem.

Além de demonstrar uma aplicação prática dessas tecnologias, o projeto busca valorizar a educação financeira por meio de uma experiência conversacional simples e orientada ao aprendizado.

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
