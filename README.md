# DIO | VirtualBank-Python
**Criando um sistema bancário em Python. Esta é a primeira etapa da construção de um sistema bancário completo, abordando funcionalidades como criação de contas, transações e segurança. É uma oportunidade para aprimorar habilidades de programação Python e compreender 
conceitos financeiros e de segurança.**  

✒️Para a primeira versão do sistema devemos implementar apenas 3 operações: **depósito, saque e extrato.**

- Para as operações de depósito deve ser possível apenas valores positivos. 
  A versâo 1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.
  
- Para as operações de saque o sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.
  
- A operação de extrato deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações. Os valores devem ser exibidos utilizando o formato R$ xxx.xx. Exemplo: 1500.45 = R$ 1500.45

✒️**Segunda Versão**

- Para a segunda versão, vamos otimizar o Sistema Bancário com o uso de **Funções Python.** O objetivo é aprimorar a estrutura e a eficiência do sistema, implementando as operações de depósito, saque e extrato em funções específicas.

- Foram adicionadas duas novas funções para o Sistema Bancário: Cadastrar usuário (cliente) e cadastrar conta bancária que deve ser vinculada com o usuário. Além disso devemos também criar uma função chamada de "Listar Contas" com o objetivo de listar as contas já cadastradas. **Duas observações importantes aqui:** O número da conta é sequencial, iniciando em "1" e o número da agência é fixo "001". O usuário pode ter mais de uma conta, mas uma conta pertence somente a um usuário.
- **DICA**
- Para vincular um usuário a uma conta, foi utilizado um filtro a lista de usuários, buscando o numero do CPF informado para casa usuário da lista.

- Vamos refatorar o código existente, dividindo-o em funções reutilizáveis, facilitando a manutenção e o entendimento do sistema como um todo. Vamos aplicar conceitos avançados de programação e criar soluções mais elegantes e eficientes utilizando Python.

### Minhas contribuições para o projeto V1
**Com o objetivo de me desafiar, busquei entregar um pouco mais do que foi pedido no projeto inicial.**

Além das operações de depósito, saque e extrato, adicionei ao MENU mais uma opção que chamei de RESUMO EXTRATO, dando ao correntista uma opção de extrato simplificado, apenas com as informações, Total depositado, Total Sacado e Saldo.

Adicionei também ao extrato DATA e HORA, deixando um pouco mais completa a experiência do usuário / correntista. Ainda no extrato, diferente do proposto no projeto inicial, detalhei de forma separada as operações de DEPÓSITO e SAQUE.

Espero que este repositório ajude a você que está iniciando sua jornada em Python.

Se precisar de ajuda, fique à vontade para entrar em contato comigo. Se estiver ao meu alcance, terei prazer em ajudar.

### Minhas contribuições para o projeto V2
**Assim como na primeira versão, busquei entregar um pouco mais do que foi pedido no projeto inicial.**

Além do que já havia entregado a mais na V1 do sistema, adicionei ao MENU mais uma opção que chamei de EXTRATO CONSOLIDADO, dando ao correntista uma opção de extrato simplificado, apenas com as informações, Total depositado, Total Sacado e Saldo. Agora como uma função, o EXTRATO CONSOLIDADO informa ao usuário caso não haja nenhuma movimentação financeira.

Segue o [Link da V2 do sistema](https://github.com/rflombardi/VirtualBank-Python/blob/main/Desafio_sistema_bancario_v2.py)




