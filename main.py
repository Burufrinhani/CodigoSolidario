from pontos import pontosDoacoes

def mostrar_pontos(recurso, regiao):
    try:
        pontos_na_regiao = pontosDoacoes[recurso][regiao]
        print(f"\nPontos de {recurso} na {regiao}:")
        for ponto in pontos_na_regiao:
            print(f"{ponto['nome']} \n{ponto['endereco']} \n{ponto['telefone']}\n")
    except KeyError:
        print("Recurso ou região não encontrados. Por favor, verifique a entrada.")

def main():
    print("Escolha o recurso que deseja consultar:")
    print("1. Comida")
    print("2. Roupas e agasalhos")
    print("3. Higiene")
    print("4. Doação de sangue")

    opcaoUsuario = int(input("Digite o número do recurso desejado: "))

    if opcaoUsuario < 1 or opcaoUsuario > len(pontosDoacoes):
        print("Opção inválida. Saindo do programa.")
        return

    opcao = list(pontosDoacoes.keys())[opcaoUsuario - 1]

    print("\nEscolha a região que deseja consultar:")
    regioes_disponiveis = list(pontosDoacoes[opcao].keys())
    for i, regiao in enumerate(regioes_disponiveis, start=1):
        print(f"{i}. {regiao}")

    regiao_numero = int(input("Digite o número da região desejada: "))

    if regiao_numero < 1 or regiao_numero > len(regioes_disponiveis):
        print("Opção inválida. Saindo do programa.")
        return

    regiao_escolhida = regioes_disponiveis[regiao_numero - 1]

    mostrar_pontos(opcao, regiao_escolhida)

if __name__ == "__main__":
    main()


