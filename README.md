# Sistema de Histórico de Falhas

Este é um sistema simples de histórico de falhas desenvolvido como parte do trabalho da disciplina 'Computational Thinking Using Python'. O programa apresenta menus para diferentes tipos de usuários e funcionalidades para gerenciar falhas no sistema.

## Funcionalidades

- **Login:**
  - **Administrador**: Pode registrar novas falhas, exibir o histórico de falhas, gerar relatórios de falhas, e voltar para a tela de login.
  - **Operador Geral**: Pode exibir o histórico de falhas, gerar relatórios de falhas, e voltar para a tela de login.

- **Sistema de Histórico:**
  - **Registrar Falha**: Adiciona uma nova falha ao sistema.
  - **Exibir Histórico de Falhas**: Mostra o histórico de falhas registradas.
  - **Gerar Relatório de Falhas**: Mostra o número total de falhas e o tipo de falha mais frequente.

## Como Usar

1. Execute o programa em um ambiente Python:
    ```bash
    Main.py
    ```

2. O programa exibirá um menu de login. Escolha a opção desejada:
    - `1` para logar como Administrador
    - `2` para logar como Operador Geral
    - `0` para sair do programa

3. Dependendo do tipo de usuário selecionado, um novo menu será exibido com opções específicas para realizar tarefas de acordo com o nível de acesso.

4. Siga as instruções na tela para registrar falhas, exibir o histórico, gerar relatórios, ou retornar ao menu de login.

## Estrutura do Código

- **Menus:**
  - `menuLogin`: Tela de login com opções para Administrador, Operador Geral e sair.
  - `menuSistemaAdm`: Menu para Administrador com opções de gerenciamento de falhas.
  - `menuSistemaGeral`: Menu para Operador Geral com opções limitadas.

- **Funções:**
  - `opcaoPadrao()`: Retorna uma mensagem de opção inválida.
  - `opcaoSair()`: Finaliza o programa.
  - `logarAdm()`: Loga como Administrador.
  - `logarGeral()`: Loga como Operador Geral.
  - `voltarLogin()`: Retorna à tela de login.
  - `registrarFalha()`: Adiciona uma falha ao sistema.
  - `exibeHistorico()`: Exibe o histórico de falhas.
  - `exibeRelatorio()`: Exibe o relatório de falhas.

- **Lógica do Menu:**
  - A lógica do menu é implementada utilizando um loop `while` que permite ao usuário navegar pelos menus e realizar ações conforme a sua permissão.

## Requisitos

- Python 3.x

## Observações

- O código utiliza códigos de formatação ANSI para colorir a saída no terminal.
- As funcionalidades de adicionar falhas, exibir histórico e gerar relatórios são placeholders e devem ser implementadas conforme necessário.

## Contribuições

Contribuições para melhorar ou expandir o sistema são bem-vindas. Sinta-se à vontade para fazer um fork do repositório e enviar pull requests com melhorias ou correções.

---

**Data:** Setembro de 2024
