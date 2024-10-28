class Enfermeiro:
    def __init__(self, nome, coren):
        self.nome = nome
        self.coren = coren

class Paciente:
    def __init__(self, cpf, nome, data_nascimento, peso, altura, spo2, fc, has, dm):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.peso = peso
        self.altura = altura
        self.spo2 = spo2
        self.fc = fc
        self.has = has
        self.dm = dm

    def calcular_imc(self):
        imc = self.peso / (self.altura ** 2)
        return imc

    def classificacao_imc(self):
        imc = self.calcular_imc()
        if imc < 18.5:
            return "Abaixo do peso"
        elif 18.5 <= imc < 24.9:
            return "Peso normal"
        elif 25 <= imc < 29.9:
            return "Sobrepeso"
        else:
            return "Obesidade"

class Consulta:
    def __init__(self, paciente, enfermeiro):
        self.paciente = paciente
        self.enfermeiro = enfermeiro

    def imprimir_dados(self):
        print(f"\n--- Dados da Consulta ---")
        print(f"Paciente: {self.paciente.nome} (CPF: {self.paciente.cpf})")
        print(f"Data de Nascimento: {self.paciente.data_nascimento}")
        print(f"Peso: {self.paciente.peso} kg, Altura: {self.paciente.altura} m")
        print(f"SPO2: {self.paciente.spo2}%, FC: {self.paciente.fc} bpm")
        print(f"HAS: {'Sim' if self.paciente.has else 'Não'}, DM: {'Sim' if self.paciente.dm else 'Não'}")
        print(f"Enfermeiro: {self.enfermeiro.nome} (COREN: {self.enfermeiro.coren})")
        print(f"IMC: {self.paciente.calcular_imc():.2f} - Classificação: {self.paciente.classificacao_imc()}")

def cadastrar_enfermeiro():
    nome = input("Digite o nome do enfermeiro: ")
    coren = input("Digite o número do COREN: ")
    return Enfermeiro(nome, coren)

def cadastrar_paciente():
    cpf = input("Digite o CPF do paciente: ")
    nome = input("Digite o nome do paciente: ")
    data_nascimento = input("Digite a data de nascimento do paciente (dd/mm/aaaa): ")
    peso = float(input("Digite o peso do paciente (kg): "))
    altura = float(input("Digite a altura do paciente (m): "))
    spo2 = float(input("Digite a saturação SPO2 do paciente (%): "))
    fc = int(input("Digite a frequência cardíaca do paciente (bpm): "))
    has = input("O paciente tem hipertensão arterial sistêmica? (s/n): ").lower() == 's'
    dm = input("O paciente tem diabetes mellitus? (s/n): ").lower() == 's'
    
    return Paciente(cpf, nome, data_nascimento, peso, altura, spo2, fc, has, dm)

def main():
    print("Cadastro de Enfermeiro:")
    enfermeiro = cadastrar_enfermeiro()

    print("\nCadastro de Paciente:")
    paciente = cadastrar_paciente()

    consulta = Consulta(paciente, enfermeiro)
    consulta.imprimir_dados()

if __name__ == "__main__":
    main()