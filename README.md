# 🎯 Jogo de Adivinhação em Python (Guessing Game)

## Visão Geral

Este é um projeto de demonstração desenvolvido para consolidar os fundamentos da linguagem Python, incluindo controle de fluxo (`if/elif/else`), laços de repetição (`for/while`), modularização com funções (`def`), e tratamento de erros (`try/except`).

**Principal Objetivo:** Atingir um número secreto aleatório (entre 1 e 100) dentro de um número limitado de tentativas, minimizando a perda de pontos.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Bibliotecas Padrão:** `random`
* **Versionamento:** Git & GitHub

## ⚙️ Funcionalidades e Diferenciais

O jogo inclui as seguintes características que demonstram o domínio dos fundamentos de programação:

1.  **Níveis de Dificuldade:** O usuário escolhe entre Fácil (20 tentativas), Médio (10 tentativas) e Difícil (5 tentativas).
2.  **Sistema de Pontuação:** O jogador inicia com 1000 pontos. O sistema calcula a diferença absoluta entre o chute e o número secreto e subtrai essa diferença da pontuação total a cada erro.
3.  **Feedback Direcional:** O jogo informa se o chute foi "MAIOR" ou "MENOR" que o número secreto.
4.  **Tratamento de Erros:** O código lida com entradas não numéricas e números fora do intervalo permitido (1-100) usando `try/except` e validações.

## 🚀 Como Executar

1.  **Clone o Repositório:**
    ```bash
    git clone [https://github.com/SeuNomeDeUsuario/jogo-adivinhacao-python.git](https://github.com/SeuNomeDeUsuario/jogo-adivinhacao-python.git)
    ```
2.  **Navegue até a Pasta:**
    ```bash
    cd jogo-adivinhacao-python
    ```
3.  **Execute o Jogo:**
    ```bash
    python adivinhacao.py
    ```

---
**Desenvolvedor:** [Seu Nome Completo]
**Diferencial:** Fluente em Inglês, com foco em Python e Back-end.
