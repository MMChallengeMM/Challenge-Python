from datetime import datetime

menuLogin = """\033[9m
=====================================\033[29m
\033[1m\033[4mTela de login.\033[22m\033[24m
1. Administrador
2. Operador
0. Sair
====================================="""

menuSistemaAdm = """\033[9m
=====================================\033[29m
\033[1m\033[4mBem vindo ao sistema de histórico.\033[22m\033[24m
1. Registrar nova falha
2. Exibir histórico de falhas
3. Gerar relatório de falhas
4. Voltar para os logins
0. Sair
====================================="""

menuSistema = """\033[9m
=====================================\033[29m
\033[1;4mBem-vindo ao sistema de histórico.\033[22m\033[24m
1. Exibir histórico de falhas
2. Gerar relatório de falhas
3. Voltar para os logins
0. Sair
====================================="""

# Acima os menus principais a serem mostrados | Abaixo as funções do sistema

listaFalhas = []
permissaoAdm = False


def opcaoInvalida():
    return "Opção inválida"


def opcaoSair():
    return "Agradeço por usar. Saindo..."


def logarAdm():
    global permissaoAdm
    permissaoAdm = True
    return "\033[93m" + "Logado como Administrador."


def logarOperador():
    global permissaoAdm
    permissaoAdm = False
    return "\033[92m" + "Logado como Operador."


def voltarLogin():
    return "Logging off..." + "\033[0m"


def registrarFalha():
    falha = {
        "idFalha": len(listaFalhas) + 1,
        "data": datetime.today().strftime("%d/%m/%Y - %H:%M"),
        "tipo": tipoFalha(),
        "descricao": input("Digite a descricao:\n")}
    listaFalhas.append(falha)
    return f"Falha #{falha["idFalha"]} adicionada ao sistema."


def exibeHistorico():
    historico = ""

    for falha in listaFalhas:
        idFalha = falha["idFalha"]
        dataFalha = falha["data"]
        tipo = falha["tipo"]
        descricaoFalha = falha["descricao"]
        historico += f"#{idFalha} ({dataFalha}) : {tipo} - {descricaoFalha}\n"

    if historico == "":
        historico = "Não há registros"

    return "Histórico de falhas:\n" + historico


def exibeRelatorio():
    listaTipos = []

    for falha in listaFalhas:
        listaTipos.append(falha["tipo"])

    return (f"Relatório de falhas:\n"
            f"Número de falhas: {len(listaFalhas)}\n"
            f"Falha mais frequente: {max(listaTipos, key=listaTipos.count)}")


def tipoFalha():
    menuTipoFalha = """
=====================================
Tipos de falhas:
1.MECANICA
2.ELETRICA
3.SOFTWARE
0.OUTRO"""

    def tipoFalhaOutro():
        return "OUTRO"

    def tipoFalhaMecanica():
        return "MECANICA"

    def tipoFalhaEletrica():
        return "ELETRICA"

    def tipoFalhaSoftware():
        return "SOFTWARE"

    opcoesTipoFalha = {
        0: tipoFalhaOutro,
        1: tipoFalhaMecanica,
        2: tipoFalhaEletrica,
        3: tipoFalhaSoftware
    }

    print(menuTipoFalha)
    escolha = int(input("Digite o número da opção desejada:\n"))
    if not escolha in [0, 1, 2, 3]:
        print(opcaoInvalida())
        return tipoFalha()
    else:
        resposta = opcoesTipoFalha.get(escolha)()
        return resposta


# Acima funções do sistema | Abaixo organização e lógica dos menus principais

opcoesLogin = {
    0: opcaoSair,
    1: logarAdm,
    2: logarOperador
}

opcoesSistemaAdm = {
    0: opcaoSair,
    1: registrarFalha,
    2: exibeHistorico,
    3: exibeRelatorio,
    4: voltarLogin
}

opcoesSistema = {
    0: opcaoSair,
    1: exibeHistorico,
    2: exibeRelatorio,
    3: voltarLogin
}

# Acima organização | Abaixo lógica do menu
"""
Login
=> Adm 
    => Add falha (adiciona falha ao sistema)
    => Ver falhas (mostra um historico de falhas)
    => Relatorio falhas (mostra o numero de falhas e o maior tipo de falha)
    => Voltar login (volta a tela de login)
    => Sair (sai do programa)
=> Geral
    => Ver falhas
    => Relatorio falhas
    => Voltar login
    => Sair
=> Sair
"""

opcao = -1
while not opcao == 0:
    try:
        print(menuLogin)
        opcao = int(input("Digite o número da opção desejada:\n"))
        if not opcao in [0, 1, 2]:
            print(opcaoInvalida())
        else:
            resultado = opcoesLogin.get(opcao)()
            print(resultado)
            if opcao in [1, 2]:
                opcao = -1
                while not opcao == 0:
                    try:
                        if permissaoAdm:
                            print(menuSistemaAdm)
                            opcao = int(input("Digite o número da opção desejada:\n"))
                            if not opcao in [0, 1, 2, 3, 4]:
                                print(opcaoInvalida())
                            else:
                                resultado = opcoesSistemaAdm.get(opcao)()
                                print(resultado)
                                if opcao == 4:
                                    break
                        else:
                            print(menuSistema)
                            opcao = int(input("Digite o número da opção desejada:\n"))
                            if not opcao in [0, 1, 2, 3]:
                                print(opcaoInvalida())
                            else:
                                resultado = opcoesSistema.get(opcao)()
                                print(resultado)
                                if opcao == 3:
                                    break
                    except ValueError:
                        print("Valor inválido")
    except ValueError:
        print("Valor inválido")
