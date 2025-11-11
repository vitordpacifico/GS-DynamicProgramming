# Otimização de Portfólio de Projetos (Dynamic Programming)

**Curso:** Engenharia de Software  
**Disciplina:** Programação Dinâmica  
**Professor:** Marcelo Amorim  
**Entrega:** Global Solution 2025  

---

## Autores
- **Guilherme Abe** - RM 554743
- **Gustavo Paulino** - RM 554779
- **Victor Dias** - RM 558017

---

## Descrição
Este projeto resolve o problema de **otimização de portfólio de projetos**, modelado como o **problema da mochila 0/1 (Knapsack)**.  
O objetivo é selecionar os projetos de maior valor possível respeitando um limite máximo de horas disponíveis.

Foram desenvolvidas quatro abordagens:

1. **Gulosa (Greedy)** — seleciona pela razão `valor/horas`.  
2. **Recursiva Pura** — abordagem direta e exponencial.  
3. **Top-Down (Memoização)** — usa cache para armazenar subproblemas.  
4. **Bottom-Up (Iterativa)** — versão eficiente e estável da programação dinâmica.

---

## Estrutura do Projeto
knapsack_portfolio.py → implementação principal
test_knapsack.py → testes com pytest
README.md → documentação do projeto

---

## Como Executar

### Pré-requisitos
- Python **3.8+**
- (opcional) pytest:
  ```bash
  pip install pytest

  Casos de Teste

---

## Exemplo do enunciado (capacidade = 10h):
- A, B, C e D com diferentes valores e horas.

**Caso onde a gulosa falha:**

Projeto	 Valor	Horas
X	       40	   03
Y	      100	   20
Z	      100	   20

Capacidade = 40h
Gulosa → valor 140
Ótimo (DP) → valor 200 ✅

## Observações

**As abordagens Top-Down e Bottom-Up sempre retornam o mesmo valor ótimo.**

**A Recursiva Pura é demonstrativa (ineficiente).**

**A Gulosa serve como heurística e pode falhar em alguns cenários.**
