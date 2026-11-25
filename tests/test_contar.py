def test_contar_atendimentos(atendimentos, medico):
    quantidade = 0

    for atendimento in atendimentos:
        if atendimento.medico == medico:
            quantidade += 1

    return quantidade

atendimentos = [
        relatorio.Atendimento("Dr. Silva", "Paciente A", 100.0),
        relatorio.Atendimento("Dr. Silva", "Paciente B", 150.0),
        relatorio.Atendimento("Dr. Souza", "Paciente C", 200.0)
    ]

relatorio = relatorio.RelatorioDoMes()
relatorio.avaliar(atendimentos)
    
# Teste
assert test_contar_atendimentos(atendimentos, "Dr. Silva") == 2
assert test_contar_atendimentos(atendimentos, "Dr. Souza") == 1