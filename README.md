# Sistema de Histórico de Falhas do CCO

>Challenge FIAP X CCR

---

# Sumário
1. #### [Descrição](#descrição-do-projeto)
2. #### [Funcionalidades](#funcionalidades-principais)
3. #### [Tecnologias](#tecnologias-utilizadas)
4. #### [Como executar](#como-executar-o-projeto)
5. #### [Diferenças entre sprints](#diferenças-entre-a-sprints)
6. #### [Autores](#autores)
---

## Descrição do Projeto
Este projeto tem como objetivo automatizar o monitoramento e o registro de falhas no Centro de Controle de Operações (CCO) utilizado pela CCR para gerenciar o tráfego ferroviário. O sistema permite o registro de falhas, a consulta de históricos e a geração de relatórios, aumentando a eficiência operacional e reduzindo a necessidade de intervenções manuais.

## Funcionalidades Principais
1. **Login e Controle de Acesso**: Usuários podem acessar o sistema com diferentes permissões:
   - Administradores: controle total sobre os dados.
   - Operadores: acesso limitado a consultas.
2. **Registro de Falhas**: Administradores podem cadastrar novas falhas no sistema.
3. **Consulta ao Histórico de Falhas**: Listagem de falhas com filtros específicos.
4. **Geração de Relatórios**: Criação de relatórios baseados no histórico de falhas.

## Tecnologias Utilizadas
- Python
- JSON (para armazenamento de dados)

## Como Executar o Projeto
1. Certifique-se de ter o Python instalado.
2. Clone o repositório:
   ```sh
   git clone https://github.com/MMChallengeMM/Challenge-Python
   ```
3. Navegue até a pasta do projeto:
   ```sh
   cd Challenge-Python
   ```
4. Execute o script principal:
   ```sh
   python main.py
   ```

## Diferenças entre a Sprints
### Sprint 1 > 2
- Refatoração do código: alteração de nomeações de variáveis e funções para o padrão `snake_case`.
- Atualização na formatação dos menus.

### Sprint 2 > 3
- Implementação da persistência de dados utilizando arquivos JSON.
- Introdução da funcionalidade de relatórios com identificação da falha mais frequente.
- Melhorias na interface de linha de comando para facilitar a interação do usuário.

## Autores
- **João Vinicius Alves - 559369**
- **Juan Pablo Coelho - 560445**
- **Matheu Marotto - 560447**

