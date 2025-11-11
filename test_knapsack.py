from knapsack_portfolio import (
    greedy_portfolio,
    recursive_portfolio_value,
    memoized_portfolio,
    bottomup_portfolio,
)

def sample_projects():
    return [
        {"name": "A", "value": 12, "hours": 4},
        {"name": "B", "value": 10, "hours": 3},
        {"name": "C", "value": 7, "hours": 2},
        {"name": "D", "value": 4, "hours": 3},
    ]

def test_bottomup_vs_memoized_equal():
    """
    Bottom-Up e Memoizada devem dar o mesmo valor ótimo.
    """
    projects = sample_projects()
    cap = 10
    _, val_memo = memoized_portfolio(projects, cap)
    _, val_bu = bottomup_portfolio(projects, cap)
    assert val_memo == val_bu, "Bottom-Up e Memoizada devem coincidir"


def test_recursive_small_instance():
    """
    A recursiva pura deve dar o mesmo resultado para instâncias pequenas.
    """
    projects = sample_projects()
    cap = 10
    val_rec = recursive_portfolio_value(projects, cap)
    _, val_bu = bottomup_portfolio(projects, cap)
    assert val_rec == val_bu, "Recursiva pura deve coincidir com Bottom-Up"


def test_greedy_fails_case():
    """
    Caso onde a gulosa falha (valor subótimo).
    """
    projects = [
        {"name": "X", "value": 40, "hours": 3},
        {"name": "Y", "value": 100, "hours": 20},
        {"name": "Z", "value": 100, "hours": 20},
    ]
    cap = 40
    _, val_g = greedy_portfolio(projects, cap)
    _, val_opt = bottomup_portfolio(projects, cap)
    assert val_opt == 200
    assert val_g < val_opt, "Gulosa deve falhar neste caso (valor menor que ótimo)"


def test_selected_projects_bottomup():
    """
    Verifica se a lista de projetos selecionados contém apenas itens válidos.
    """
    projects = sample_projects()
    cap = 10
    selected, val = bottomup_portfolio(projects, cap)
    total_hours = sum(p["hours"] for p in projects if p["name"] in selected)
    assert total_hours <= cap, "Horas totais não podem ultrapassar a capacidade"
    assert val > 0, "Valor total deve ser positivo"