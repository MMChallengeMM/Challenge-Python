from datetime import datetime


def create_failure(failures: list) -> None:
    """Gera uma falha (id, data, tipo, descrição) e adiciona no histórico de falhas adicionado como parâmetro na função."""

    def generate_failure_type() -> str:
        """Retorna um str com o o tipo de falha para colocar no sistema."""
        while True:
            try:
                print("1. MECANICA\n"
                      "2. ELETRICA\n"
                      "3. SOFTWARE\n"
                      "4. OUTRO\n")
                option = int(input("Digite a opção desejada:\n"))
                match option:
                    case 1:
                        return "Mecânica"
                    case 2:
                        return "Elétrica"
                    case 3:
                        return "Software"
                    case 4:
                        return "Outro"
                    case _:
                        print("ERRO 1")
            except ValueError:
                print("Valor inválido")

    falha = {
        "failure_id": len(failures) + 1,
        "date": datetime.today().strftime("%d/%m/%Y"),
        "type": generate_failure_type(),
        "description": input("Digite a descrição da falha:\n")
    }
    failures.append(falha)
    print(f"Falha #{falha["failure_id"]} adicionada ao sistema.")


def generate_report(failures_to_report: list) -> None:
    """Gera um relatório básico de falhas(Falha mais frequente, número total de falhas) recebendo uma lista de falhas."""
    if len(failures_to_report) == 0:
        print("Não há falhas para o relatório")
        return

    fail_types = [fail["type"] for fail in failures_to_report]

    print(f"Mais frequente: {max(fail_types, key=fail_types.count)}\n"
          f"N° falhas: {len(failures_to_report)}")


def start_system(failures: list, adm_permission: bool = False) -> int:
    """Inicia o sistema, recebe uma lista de falhas e a permissão de admin. Retorna um int para ser usado com o menu de login."""
    def show_history(failures_to_show: list) -> None:
        """Mostra o histórico de falhas formatado."""
        history = ""

        for fail in failures_to_show:
            fail_id = fail["failure_id"]
            fail_date = fail["date"]
            fail_type = fail["type"]
            fail_description = fail["description"]
            history += f"#{fail_id} ({fail_date}) | {fail_type} - {fail_description}\n"

        if history == "":
            history = "Não há registros"

        print(history)

    system_menu_adm = ("1. Registrar nova falha\n"
                       "2. Exibir histórico de falhas\n"
                       "3. Gerar relatório de falhas\n"
                       "4. Voltar para os logins\n"
                       "0. Sair\n")

    system_menu = ("1. Registrar nova falha\n"
                   "2. Exibir histórico de falhas\n"
                   "3. Voltar para os logins\n"
                   "0. Sair\n")

    menu = system_menu_adm if adm_permission else system_menu
    if adm_permission:
        while True:
            try:
                print(menu)
                option = int(input("Digite a opção desejada:\n"))

                match option:
                    case 0:
                        return 0
                    case 1:
                        create_failure(failures)
                    case 2:
                        show_history(failures)
                    case 3:
                        generate_report(failures)
                    case 4:
                        return -1
                    case _:
                        print("ERRO")
            except ValueError:
                print("LIXO")
    else:
        while True:
            try:
                print(menu)
                option = int(input("Digite a opção desejada:\n"))

                match option:
                    case 0:
                        return 0
                    case 1:
                        create_failure(failures)
                    case 2:
                        show_history(failures)
                    case 3:
                        return -1
                    case _:
                        print("ERRO")
            except ValueError:
                print("LIXO")


def start_login(failures: list) -> None:
    """Inicia o menu de login entre operadores e administradores."""
    option = -1
    login_menu = ("1. Operador\n"
                  "2. Administrador\n"
                  "0. Sair\n")
    while True:
        try:
            option = -1 if option != 0 else 0
            if option == 0:
                print("Saindo...")
                break

            print(login_menu)
            option = int(input("Digite a opção desejada:\n"))

            match option:
                case 0:
                    continue
                case 1:
                    option = start_system(failures)
                case 2:
                    option = start_system(failures, True)

        except ValueError:
            print("Valor inválido")


failures_list = []
start_login(failures_list)
