from typing import List, Tuple, Dict

def greedy_portfolio(projects: List[Dict], capacity: int) -> Tuple[List[str], int]:
    """
    Fase 1: Abordagem Gulosa (Greedy).
    Regra: priorizar pela maior razão value/hours (V/E).
    Seleciona sequencialmente até acabar a capacidade.
    Retorna lista de nomes selecionados e valor total.
    Observação: não garante solução ótima para o problema 0/1.
    """
    items = []
    for p in projects:
        ratio = p["value"] / p["hours"] if p["hours"] > 0 else float("inf")
        items.append((ratio, p))
    items.sort(key=lambda x: x[0], reverse=True)

    selected = []
    rem = capacity
    total_value = 0
    for ratio, p in items:
        if p["hours"] <= rem:
            selected.append(p["name"])
            rem -= p["hours"]
            total_value += p["value"]
    return selected, total_value


def recursive_portfolio_value(projects: List[Dict], capacity: int) -> int:
    """
    Fase 2: Solução Recursiva Pura.
    Implementa a recorrência sem memoização. Retorna somente o valor máximo.
    """
    def rec(i: int, c: int) -> int:
        if i < 0 or c <= 0:
            return 0
        p = projects[i]
        if p["hours"] > c:
            return rec(i - 1, c)
        without = rec(i - 1, c)
        with_item = p["value"] + rec(i - 1, c - p["hours"])
        return max(without, with_item)

    return rec(len(projects) - 1, capacity)


def memoized_portfolio(projects: List[Dict], capacity: int) -> Tuple[List[str], int]:
    """
    Fase 3: Top-Down com Memoização.
    Retorna a lista de nomes selecionados e o valor máximo.
    Implementa reconstrução das escolhas usando os dados memorizados.
    """
    n = len(projects)
    memo = {}

    def rec(i: int, c: int) -> int:
        key = (i, c)
        if key in memo:
            return memo[key]
        if i < 0 or c <= 0:
            memo[key] = 0
            return 0
        p = projects[i]
        if p["hours"] > c:
            res = rec(i - 1, c)
            memo[key] = res
            return res
        without = rec(i - 1, c)
        with_item = p["value"] + rec(i - 1, c - p["hours"])
        res = max(without, with_item)
        memo[key] = res
        return res

    max_value = rec(n - 1, capacity)

    selected = []
    i, c = n - 1, capacity
    while i >= 0 and c > 0:
        key = (i, c)
        p = projects[i]
        without = memo.get((i - 1, c), 0)
        if p["hours"] > c:
            i -= 1
            continue
        with_item = p["value"] + memo.get((i - 1, c - p["hours"]), 0)
        if memo[key] == with_item:
            selected.append(p["name"])
            c -= p["hours"]
            i -= 1
        else:
            i -= 1

    selected.reverse()
    return selected, max_value


def bottomup_portfolio(projects: List[Dict], capacity: int) -> Tuple[List[str], int]:
    """
    Fase 4: Programação Dinâmica Bottom-Up (Iterativa).
    Constrói tabela T onde T[i][c] = melhor valor usando primeiros i itens (i de 0..n)
    e capacidade c (0..capacity).
    Retorna lista de nomes escolhidos e valor máximo.
    """
    n = len(projects)
    T = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        p = projects[i - 1]
        for c in range(0, capacity + 1):
            if p["hours"] > c:
                T[i][c] = T[i - 1][c]
            else:
                T[i][c] = max(T[i - 1][c], p["value"] + T[i - 1][c - p["hours"]])

    max_value = T[n][capacity]

    selected = []
    i, c = n, capacity
    while i > 0 and c > 0:
        if T[i][c] != T[i - 1][c]:
            p = projects[i - 1]
            selected.append(p["name"])
            c -= p["hours"]
            i -= 1
        else:
            i -= 1

    selected.reverse()
    return selected, max_value

def example_projects():
    """
    Dados de exemplo do enunciado:
    C = 10
    A: V=12, E=4
    B: V=10, E=3
    C: V=7,  E=2
    D: V=4,  E=3
    """
    return [
        {"name": "A", "value": 12, "hours": 4},
        {"name": "B", "value": 10, "hours": 3},
        {"name": "C", "value": 7, "hours": 2},
        {"name": "D", "value": 4, "hours": 3},
    ]


def run_examples():
    projects = example_projects()
    cap = 10
    print("=== Exemplo enunciado ===")
    g_sel, g_val = greedy_portfolio(projects, cap)
    print("Gulosa -> selecionados:", g_sel, "valor:", g_val)
    r_val = recursive_portfolio_value(projects, cap)
    print("Recursiva pura -> valor:", r_val)
    m_sel, m_val = memoized_portfolio(projects, cap)
    print("Memoizada -> selecionados:", m_sel, "valor:", m_val)
    b_sel, b_val = bottomup_portfolio(projects, cap)
    print("Bottom-Up -> selecionados:", b_sel, "valor:", b_val)
    print()

    print("=== Caso onde a gulosa falha ===")

    projects2 = [
        {"name": "X", "value": 40, "hours": 3},
        {"name": "Y", "value": 100, "hours": 20},
        {"name": "Z", "value": 100, "hours": 20},
    ]

    cap2 = 40
    g_sel2, g_val2 = greedy_portfolio(projects2, cap2)
    m_sel2, m_val2 = memoized_portfolio(projects2, cap2)
    b_sel2, b_val2 = bottomup_portfolio(projects2, cap2)
    print("Projetos:", projects2, "Capacidade:", cap2)
    print("Gulosa -> selecionados:", g_sel2, "valor:", g_val2)
    print("Memoizada -> selecionados:", m_sel2, "valor:", m_val2)
    print("Bottom-Up -> selecionados:", b_sel2, "valor:", b_val2)
    print("(Observação: a solução ótima é escolher Y e Z -> valor 200; a gulosa escolhe X + Y -> 140)")
    print()
    print("Nota: recursiva pura retorna apenas o valor (exponencial). Use memoizada/bottom-up para N razoável.")

if __name__ == "__main__":
    run_examples()