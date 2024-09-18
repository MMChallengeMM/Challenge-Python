menuLogar = """
=====================================
Tela de login.
1. Administrador
2. Operador Geral
0. Sair
====================================="""

menuSistemaAdm = """
=====================================
Bem vindo ao sistema de histórico.
1. Registrar nova falha
2. Exibir histórico de falhas
3. Gerar relatório de falhas
4. Voltar para os logins
0. Sair
====================================="""

menuSistemaGeral = """
=====================================
Bem-vindo ao sistema de histórico.
1. Exibir histórico de falhas
2. Gerar relatório de falhas
3. Voltar para os logins
0. Sair
====================================="""

permissaoAdm = False

def opcaoPadrao():
    return "Opção inválida"

def opcaoSair():
    return "Agradeço por usar. Saindo..."

def logarAdm():
    global permissaoAdm
    permissaoAdm = True
    return "Logado como Administrador."

def logarGeral():
    global permissaoAdm
    permissaoAdm = False
    return "Logado como Operador Geral."

def voltarLogin():
    return "Logging off..."

def registrarFalha():
    return "Adicionou falha ao sistema"

def exibeHistorico():
    return "Exibe historico"

def exibeRelatorio():
    return "Exibe relatorio"

opcoesLogar = {
    0:opcaoSair,
    1:logarAdm,
    2:logarGeral
}

opcoesSistemaAdm = {
    0:opcaoSair,
    1:registrarFalha,
    2:exibeHistorico,
    3:exibeRelatorio,
    4:voltarLogin
}

opcoesSistemaGeral = {
    0:opcaoSair,
    1:exibeHistorico,
    2:exibeRelatorio,
    3:voltarLogin
}

opcao = -1
while not opcao == 0:
    print(menuLogar)
    try:
        opcao = int(input("Digite o número da opção desejada:\n"))
        resultado = opcoesLogar.get(opcao, opcaoPadrao)()
        print(resultado)

        if opcao in [1,2]:
            opcao = -1
            while not opcao == 0:
                try:
                    if permissaoAdm:
                        print(menuSistemaAdm)
                        opcao = int(input("Digite o número da opção desejada:\n"))
                        resultado = opcoesSistemaAdm.get(opcao,opcaoPadrao)()
                        print(resultado)
                        if opcao == 4:
                            break
                    else:
                        print(menuSistemaGeral)
                        opcao = int(input("Digite o número da opção desejada:\n"))
                        resultado = opcoesSistemaGeral.get(opcao,opcaoPadrao)()
                        print(resultado)
                        if opcao == 3:
                            break
                except ValueError:
                    print("Valor inválido")
    except ValueError:
        print("Valor inválido")
