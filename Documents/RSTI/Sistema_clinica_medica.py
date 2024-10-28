def principal():
    dados_atendimentos = []
    while True:
        entrada = str(input("Deseja inserir dados: (Sim/Sair): "))
        if entrada == 'Sair':
            break

        print("***** DADOS DO MÉDICO *****")
        crm = int(input("Digite o CRM: "))
        nome_medico = str(input("Nome do Médico: "))
        especialidade = str(input("Especialidade: "))
        
        print("*****DADOS DO PACIENTE*****")
        nome = str(input("Digite o nome do paciente: "))
        data_nascimento = str(input("Data de nascimento: ")) 
        
        print("*****DADOS DA CONSULTA*****")
        data_consulta = str(input("Data da consulta: "))
        descricao = str(input("Descrição da consulta: "))
        
        
        atendimento = {
            'medico': {'crm': crm, 'nome': nome_medico, 'especialidade': especialidade},
            'paciente':{'nome': nome, 'data_nascimento': data_nascimento},    
            'consulta':{'data':data_consulta, 'descricao': descricao}     

         }
        dados_atendimentos.append(atendimento)

    return dados_atendimentos


pessoas = principal ()      
        
for atendimento in pessoas:
    print("-" * 20)
    print("Dados do Médico: ")
    print("crm:", atendimento['medico']['crm'])
    print("Nome:", atendimento['medico']['nome'])
    print("Especialidade:", atendimento['medico']['especialidade'])
    print("-" * 20)
    print("Dados do paciente: ")
    print("Nome", atendimento['paciente']['nome'])
    print("Data de Nascimento",atendimento ['paciente']['data_nascimento'])
    print("Dados da Consulta:")
    print("Data:", atendimento['consulta']['data'])
    print("Descrição:", atendimento['consulta']['descricao'])
    
        
                