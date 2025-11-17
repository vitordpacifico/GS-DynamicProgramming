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

## Análise de Desempenho (Teórica)

[cite_start]Conforme solicitado no enunciado[cite: 160], segue a análise de complexidade de tempo (Notação Big O) para as quatro abordagens, onde $N$ é o número de projetos e $C$ é a capacidade máxima de horas.

1.  **Gulosa (Greedy):**
    * **Complexidade:** $O(N \log N)$
    * **Justificativa:** A etapa dominante é a ordenação (sort) dos projetos pela sua razão valor/horas. Após a ordenação, a seleção é uma passagem linear $O(N)$.

2.  **Recursiva Pura:**
    * **Complexidade:** $O(2^N)$ (Exponencial)
    * **Justificativa:** No pior caso, a função explora duas ramificações (incluir ou não incluir o projeto) para cada um dos $N$ projetos, levando a uma árvore de recursão com $2^N$ folhas.

3.  **Top-Down (Memoização):**
    * **Complexidade:** $O(N \cdot C)$ (Pseudo-polinomial)
    * **Justificativa:** A recursão é otimizada. Cada subproblema, definido pelo estado `(i, c)` (índice do projeto e capacidade restante), é calculado apenas uma vez e armazenado. Existem $N \times C$ subproblemas distintos.

4.  **Bottom-Up (Iterativa):**
    * **Complexidade:** $O(N \cdot C)$ (Pseudo-polinomial)
    * **Justificativa:** A solução constrói uma tabela (matriz) de tamanho $(N+1) \times (C+1)$. O preenchimento da tabela exige dois loops aninhados, um iterando pelos $N$ projetos e outro pela $C$ capacidade.

* **Qual é a mais eficiente?**
    As abordagens de Programação Dinâmica (**Memoização** e **Bottom-Up**) são as mais eficientes para garantir a solução ótima, ambas com complexidade $O(N \cdot C)$. Elas evitam o recálculo redundante da solução recursiva pura (exponencial).

    [cite_start]Embora a abordagem Gulosa seja mais rápida em tempo de execução ($O(N \log N)$), ela não é considerada "eficiente" para este problema, pois **não garante a solução ótima**[cite: 142, 163].

---

## Como Executar

### Pré-requisitos
- Python **3.8+**
- (opcional) pytest:
  ```bash
  pip install pytest
