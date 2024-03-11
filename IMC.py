def menu():
    print("Digite:\n1 para Homem\n2 para Mulher\n0 para Sair")

def calcular_peso_ideal(sexo, altura):
    if sexo == '1':  # Homem
        peso_ideal = (72.7 * altura) - 58
    elif sexo == '2':  # Mulher
        peso_ideal = (62.1 * altura) - 44.7
    else:
        peso_ideal = None
    return peso_ideal

while True:
    menu()
    ordem = input("Escolha uma opção: ")

    if ordem == '0':
        print("Saindo do programa...")
        break

    if ordem in ('1', '2'):
        try:
            altura = float(input("Digite sua altura em metros e centimetro: "))
            peso_ideal = calcular_peso_ideal(ordem, altura)
            if peso_ideal is not None:
                print("Seu peso ideal é:", peso_ideal)
            else:
                print("Opção inválida. Escolha 1 para Homem ou 2 para Mulher.")
        except ValueError:
            print("Altura inválida. Por favor, insira um número válido.")
    else:
        print("Opção inválida. Escolha 1 para Homem, 2 para Mulher ou 0 para Sair.")
