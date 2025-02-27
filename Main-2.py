from datetime import datetime
import json


def load_json(json_name: str = "failures.json") -> list:
    def create_json(name: str = "failures.json"):
        with open(name, "w", encoding="utf-8") as f:
            json.dump([], f, indent=4)

    try:
        with open(json_name, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        create_json(json_name)
        return load_json(json_name)


def save_on_json(list_to_save: list, json_name: str = "failures.json"):
    load_json(json_name)
    with open(json_name, "w", encoding="utf-8") as file:
        json.dump(list_to_save, file, indent=4)


def create_failure() -> None:
    """Gera uma falha (id, data, tipo, descrição) e adiciona no histórico de falhas adicionado como parâmetro na
    função."""

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

    failures_list = load_json()
    falha = {
        "failure_id": len(failures_list) + 1,
        "date": datetime.today().strftime("%d/%m/%Y"),
        "type": generate_failure_type(),
        "description": input("Digite a descrição da falha:\n"),
        "on_report": False
    }
    failures_list.append(falha)
    save_on_json(failures_list)
    print(f"Falha #{falha["failure_id"]} adicionada ao sistema.")


def generate_report() -> None:
    """Gera um relatório básico de falhas(Falha mais frequente, número total de falhas) recebendo uma lista de
    falhas."""

    all_failures = load_json()

    failures_to_report = [failure for failure in all_failures if failure["on_report"] is False]
    failures_on_report = [failure for failure in all_failures if failure["on_report"] is True]
    if len(failures_to_report) == 0:
        print("Não há falhas")
        return

    report_list = load_json("reports.json")
    fail_types = [failure["type"] for failure in failures_to_report]
    report = {
        "id_report": len(report_list) + 1,
        "most_frequent_failure": max(fail_types, key=fail_types.count),
        "number_of_failures": len(failures_to_report)
    }
    report_list.append(report)

    for failure in failures_to_report:
        failure["on_report"] = True

    all_failures = failures_on_report + failures_to_report

    save_on_json(all_failures)
    save_on_json(report_list, "reports.json")

    print(f"Falha mais frequente: {report['most_frequent_failure']}\n"
          f"Número de falhas: {report["number_of_failures"]}")

    # all_failures = load_json()
    # failures_to_report = []
    # index = []
    # for i, v in enumerate([failure for failure in load_json() if failure["on_report"] is False]):
    #     index.append(i)
    #     failures_to_report.append(v)
    #
    # report_list = load_json("reports.json") if load_json("reports.json") else load_json("reports.json")
    #
    # if len(failures_to_report) == 0:
    #     print("Não há falhas para o relatório")
    #     return
    #
    # fail_types = [fail["type"] for fail in failures_to_report]
    #
    # report = {
    #     "id_report": len(report_list) + 1,
    #     "most_frequent_failure": max(fail_types, key=fail_types.count),
    #     "number_of_failures": len(failures_to_report)
    # }
    #
    # report_list.append(report)
    #
    # for failure in failures_to_report:
    #     failure["on_report"] = True
    #
    # for i, failure in enumerate(all_failures):
    #     if i in index:
    #         updated_failure = failures_to_report[index[i]]
    #         all_failures.remove(failure)
    #         all_failures.insert(i, updated_failure)
    #
    # save_on_json(all_failures)
    # save_on_json(report_list, "reports.json")
    #
    # print(f"Mais frequente: {max(fail_types, key=fail_types.count)}\n"
    #       f"N° falhas: {len(failures_to_report)}")


def start_system(adm_permission: bool = False) -> int:
    """Inicia o sistema, recebe uma lista de falhas e a permissão de admin. Retorna um int para ser usado com o menu
    de login."""

    def show_history() -> None:
        """Mostra o histórico de falhas formatado."""
        history = ""

        for fail in load_json():
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
                        create_failure()
                    case 2:
                        show_history()
                    case 3:
                        generate_report()
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
                        create_failure()
                    case 2:
                        show_history()
                    case 3:
                        return -1
                    case _:
                        print("ERRO")
            except ValueError:
                print("LIXO")


def start_login() -> None:
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
                    option = start_system()
                case 2:
                    option = start_system(True)

        except ValueError:
            print("Valor inválido")


start_login()
