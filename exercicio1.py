# Regar minhas plantas
# regar 1 vez no dia se tiver mais umido
# se o dia estiver seco e ensolarado regar duas vezes no dia 
# se o dia dor chuvoso nao regar 

dia = input("Como está o dia hoje? quente/seco/úmido/chuvoso: ")

if dia == "quente" or dia == "seco":
    print("Regar duas vezes no dia")
elif dia == "úmido":
    print("Regar uma vez no dia")
elif dia == "chuvoso":
    print("Não regar")