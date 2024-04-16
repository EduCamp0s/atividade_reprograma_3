#  cada 2 produtos iguais comprados receba 5 reais de desconto,
# se forem diferente mas um dos produtos for o código 0054 ele tem 50% de desconto nesse produto
# se não valor não recebe desconto.

preco_do_produto = 10

def calcular_desconto(produto1, produto2):
    if produto1 == produto2:
        return 5
    elif produto1 == "0054" or produto2 == "0054":
        return preco_do_produto * 0.5
    else:
        return 0
    

def calcular_valor_final(produto1, produto2):
    desconto = calcular_desconto(produto1, produto2)
    if desconto:
        valor_sem_desconto = 2 * preco_do_produto
        return valor_sem_desconto - desconto
    else:
        return 2 * preco_do_produto

produto1 = input("Qual o código do primeiro produto? ")
produto2 = input("Qual o código do segundo produto? ")

valor_final = calcular_valor_final(produto1, produto2)
print(f"O valor final do produto é: R$ {valor_final}")