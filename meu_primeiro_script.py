# 1. Definição de uma função para saudar e analisar o objetivo
def verificar_objetivo(nome, foco):
    print(f"\nOlá, {nome}! Bem-vindo ao seu ambiente Python.")

    # 2. Estrutura condicional para verificar o foco escolhido
    if foco.lower() == "pentest":
        print("Excelente! Você começará aprendendo a lógica e depois avançará para segurança de redes.")
    elif foco.lower() == "web":
        print("Ótimo! Python é incrível para desenvolvimento e automação web.")
    else:
        print(f"Muito bem! O foco em '{foco}' é um ótimo caminho para dominar a linguagem.")

# 3. Fluxo principal do programa
def main():
    print("=== Painel de Início do Aprendiz ===")

    # Captura de dados informados pelo usuário
    nome_usuario = input("Digite o seu nome: ")
    foco_estudo = input("Qual o seu foco principal hoje? (pentest / web / outro): ")

    # Chamada da função passando os dados capturados
    verificar_objetivo(nome_usuario, foco_estudo)

# Execução do programa
main()