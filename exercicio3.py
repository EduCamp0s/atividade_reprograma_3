# verifique se a pessoa pode dirigir no Brasil ou no estados unidos
# a partir da informação do ano de nascimento.
# Leve em consideração se a pessoa tem carteira de motorista

ano_nascimento = int(input("Qual é o seu ano de nascimento? "))
carteira_brasil = input("Você possui carteira de motorista brasileira? (sim/não): ").lower() == "sim"
carteira_eua = input("Você possui carteira de motorista dos EUA? (sim/não): ").lower() == "sim"
idade = 2024 - ano_nascimento

def pode_dirigir_brasil(idade, possui_carteira):
    if idade >= 18 and possui_carteira:
        return "Você pode dirigir no Brasil."
    elif idade >= 18:
        return "Você tem idade para dirigir no Brasil, mas precisa de uma carteira de motorista brasileira."
    else:
        return "Você ainda não tem idade suficiente para dirigir no Brasil."

def pode_dirigir_eua(idade, possui_carteira):
    if idade >= 16 and possui_carteira:
        return "Você pode dirigir nos Estados Unidos."
    elif idade >= 16:
        return "Você tem idade para dirigir nos Estados Unidos, mas precisa de uma carteira de motorista dos EUA."
    else:
        return "Você ainda não tem idade suficiente para dirigir nos Estados Unidos."
    
    
resultado_brasil = pode_dirigir_brasil(idade, carteira_brasil)
resultado_eua = pode_dirigir_eua(idade,carteira_eua)

print(resultado_brasil)
print(resultado_eua)