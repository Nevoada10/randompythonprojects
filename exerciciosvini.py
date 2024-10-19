#######################################################################################################################
# Nevoada
#######################################################################################################################
import random


class EstruturaQ2:
    numero_casa_padrao = 0
    cep_padrao = 0

    def __init__(self, nome_rua, numero_casa=None, cep=None):
        self.nome_rua = nome_rua
        self._numero_casa = numero_casa or self.numero_casa_padrao
        self._cep = cep or self.cep_padrao

    def obter_numero_casa(self):
        return self._numero_casa

    def obter_cep(self):
        return self._cep

    def demolir(self):
        print("Essa estrutura foi demolida.")

    def imprimir_atributos(self):
        for atributo in self.__dict__.keys():
            atributo = atributo[1:].title()
            print(f"{atributo}: {getattr(self, atributo)}")


class CasaQ3(EstruturaQ2):
    quartos_padrao = 1
    quintal_padrao = False

    def __init__(self, nome_rua, numero_casa=None, cep=None, quartos=None, quintal=None):
        super().__init__(nome_rua, numero_casa, cep)
        self.quartos = quartos or self.quartos_padrao
        self.quintal = quintal or self.quintal_padrao

    def obter_numero_quartos(self):
        return self.quartos

    def tem_quintal(self):
        return self.quintal

    def demolir(self):
        print("Essa casa foi demolida.")
        print(f"Nome da Rua: {self.nome_rua.title()}")
        print(f"Número de Quartos: {self.quartos}")


casa = CasaQ3("Rua das Laranjeiras")


def bob_o_construtor(numero_de_estruturas, classe):
    estruturas = []
    for _ in range(numero_de_estruturas):
        nome_rua = random.choice(["Rua das Laranjeiras",
                                  "Rua dos Pinheiros",
                                  "Rua da Consolação, "
                                  "Rua do Sossego",
                                  "Rua da Fé",
                                  "Rua do Groove",
                                  "Rua da Rua"])
        numero_casa = random.randint(69, 420)
        cep = random.randint(0, 999999)
        quartos = random.randint(0, 10)
        quintal = random.choice([True, False])
        estrutura = classe(nome_rua, numero_casa, cep, quartos, quintal)
        estruturas.append(estrutura)
    return estruturas


estruturas = bob_o_construtor(3, CasaQ3)
counter = 0

print(estruturas)


def demolir(lista):
    for estrutura in lista:
        estrutura.demolir()
        print()


demolir(estruturas)

for estrutura in estruturas:
    counter = counter + 1

print(f"Número de estruturas na cidade: {counter}")
# blank line.
