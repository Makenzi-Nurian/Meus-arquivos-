def calcular_imc(peso, altura):   
    imc = peso / (altura ** 2)

    if imc < 18.5:
        return "Abaixo do peso", imc
    elif 18.5 <= imc < 25:
        return "Peso normal", imc
    elif 25 <= imc < 30:
        return "Sobrepeso", imc
    else:
        return "Obesidade", imc

def principal():
    dados_atendimentos = []
    while True:
        entrada = str(input("Deseja inserir dados: (Sim/Sair): "))
        if entrada == 'Sair':
            break

        print("***** DADOS PACIENTE UPA *****")
        cpf = int(input("Digite cpf: "))
        nome = str(input("Nome do Paciente: "))
        data_nascimento = str(input("Data Nascimento: "))

        print("***** DADOS ENFERMEIRO UPA *****")
        nome_enfermeiro = str(input("Nome do Enfermeiro: "))
        coren = int(input("COREN: "))
        
        print("***** DADOS CONSULTA UPA *****")
        peso = float(input("Peso do Paciente: "))
        altura = float(input("Altura do Paciente: "))
        
        saturacao = int(input("SPO2 (Saturação) do Paciente: "))
        fc =  int(input("Frequência Cardíaca do Paciente: "))
        has = str(input("Paciente tem Hipertenção Arterial? "))
        dm = str(input("Paciente tem Diabete Mellitus? "))

        imc = calcular_imc(peso, altura)
        atendimento = {
            'paciente': {'cpf': cpf, 'nome': nome, 'data_nascimento': data_nascimento},
            'enfermeiro': {'nome': nome_enfermeiro, 'coren': coren},
            'consulta': {'peso': peso, 'altura': altura, 'saturacao': saturacao, 'fc': fc, 'has': has, 'dm': dm, 'imc': imc}

        }
        dados_atendimentos.append(atendimento)

    return dados_atendimentos

pessoas = principal()

for atendimento in pessoas:
    print("-" * 20)
    print("Dados do Paciente:")
    print("CPF:", atendimento['paciente']['cpf'])
    print("Nome:", atendimento['paciente']['nome'])
    print("Data Nascimento:", atendimento['paciente']['data_nascimento'])
    print("-" * 20)
    print("Dados do Enfermeiro:")
    print("Nome:", atendimento['enfermeiro']['nome'])
    print("COREN:", atendimento['enfermeiro']['coren'])
    print("-" * 20)
    print("Dados da Consulta:")
    print("Peso:", atendimento['consulta']['peso'])
    print("Altura:", atendimento['consulta']['altura'])
    print("Saturação:", atendimento['consulta']['saturacao'])
    print("Frequência Cardíaca:", atendimento['consulta']['fc'])
    print("Hipertensão Arterial:", atendimento['consulta']['has'])
    print("Diabetes Mellitus:", atendimento['consulta']['dm'])
    print("IMC:", atendimento['consulta']['imc'])