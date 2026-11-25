import pytest
from relatorio import Aluguel


# ==========================================
# TESTE 1 - VALORES POR DIA
# ==========================================

def test_valor_por_dia():

    dias_atrasado = [
        Aluguel("Dia 2", 10),
        Aluguel("Dia 3", 15),
        Aluguel("Dia 4", 20),
    ]

    valores = sorted(
        [aluguel.valor for aluguel in dias_atrasado]
    )

    assert valores == [10, 15, 20]


# ==========================================
# TESTE 2 - REGRA 1 DO MULTA.PY
# PREENCHER COM A REGRA ORIGINAL
# ==========================================

@pytest.mark.skip(reason="Aguardando a regra original do multa.py")
def test_regra1_antes_da_fronteira():
    pass


@pytest.mark.skip(reason="Aguardando a regra original do multa.py")
def test_regra1_na_fronteira():
    pass


@pytest.mark.skip(reason="Aguardando a regra original do multa.py")
def test_regra1_depois_da_fronteira():
    pass


@pytest.mark.skip(reason="Aguardando a regra original do multa.py")
def test_regra1_entrada_invalida():
    pass


# ==========================================
# TESTE 3 - REGRA 2 DO MULTA.PY
# PREENCHER COM A REGRA ORIGINAL
# ==========================================

@pytest.mark.skip(reason="Aguardando a regra original do multa.py")
def test_regra2_antes_da_fronteira():
    pass


@pytest.mark.skip(reason="Aguardando a regra original do multa.py")
def test_regra2_na_fronteira():
    pass


@pytest.mark.skip(reason="Aguardando a regra original do multa.py")
def test_regra2_depois_da_fronteira():
    pass


@pytest.mark.skip(reason="Aguardando a regra original do multa.py")
def test_regra2_entrada_invalida():
    pass