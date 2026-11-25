import relatorio
def test_validar_preco_atendimento(valor):
    if valor < 0:
        valor = 0

    if valor > 150:
        valor = 150

    return valor
valores = [200.0, -10.0, 100.0]

relatorio = relatorio.RelatorioDoMes()
relatorio.avaliar(valores)

# Teste
assert test_validar_preco_atendimento(200.0) == 150.0
assert test_validar_preco_atendimento(-10.0) == 0.0
assert test_validar_preco_atendimento(100.0) == 100.0 

  