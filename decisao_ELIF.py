nome = input("Digite o nome do paciente: ")
idade = int(input("Digite a idade do paciente: "))
doenca_contagiosa = input("Suspeita de doença contagiosa?").upper()

if idade >= 65 and doenca_contagiosa == "SIM":
    print("O paciente ", nome," estado de EMERGENCIA!")
elif idade >= 65:
    print("Paciente ",nome," tem prioridade no atendimento.")
elif doenca_contagiosa == "SIM":
    print("O paciente ",nome," deve ser direciona a sala reservada!")
else:
    print("O paciente ",nome," NÃO possui prioridade no atendimento")