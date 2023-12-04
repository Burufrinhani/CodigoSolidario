from os import system
from pontos import pontosDoacoes
import saudacoes

saudacoes.definirSaudacao()

def mostrar_pontos(recurso, regiao):
    try:
        pontos_na_regiao = pontosDoacoes[recurso][regiao]
        print(f"\nPontos de {recurso} na {regiao}:")
        for ponto in pontos_na_regiao:
            print(f"{ponto['nome']} \n{ponto['endereco']} \n{ponto['telefone']}\n")
    except KeyError:
        print("Recurso ou região não encontrados. Por favor, verifique o número do que deseja consultar.")

def main():
    print("Escolha o recurso que deseja consultar:\n")
    print("1. Comida")
    print("2. Roupas e agasalhos")
    print("3. Higiene")
    print("4. Doação de sangue\n")

    opcaoUsuario = int(input("Digite o número do recurso desejado: "))

    if opcaoUsuario < 1 or opcaoUsuario > len(pontosDoacoes):
        print("Opção inválida. Saindo do programa.")
        return

    opcao = list(pontosDoacoes.keys())[opcaoUsuario - 1]

    system('cls')

    print("\nEscolha a região que deseja consultar:")
    regioes_disponiveis = list(pontosDoacoes[opcao].keys())
    for i, regiao in enumerate(regioes_disponiveis, start=1):
        print(f"{i}. {regiao}")

    regiao_numero = int(input("Digite o número da região: "))

    system('cls')

    if regiao_numero < 1 or regiao_numero > len(regioes_disponiveis):
        print("Opção inválida. Saindo do programa.")
        return

    regiao_escolhida = regioes_disponiveis[regiao_numero - 1]

    mostrar_pontos(opcao, regiao_escolhida)

if __name__ == "__main__":
    main()


