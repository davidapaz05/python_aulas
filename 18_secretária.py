'''
descrição: faça um programa que adicione alunos ao sistema da escola
(array) ou remova um aluno especifico.
nesse sistema deve estar previsto um menu com tres opções
=================================================
sistema senai
1 - adicionar aluno
2 - remover aluno
3 - apresentar alunos
4 - sair
insira a opção desejada:
=================================================
adicionar aluno
insira o nome do aluno
=================================================
remover aluno
insira o nome do aluno para ser removido
==================================================
alunos no sistema
'joão', 'pedro',
'''

sistema = []

while True:
    print(':::::::1)Sistema Senai:::::::\n:::::::2)Remover Aluno:::::::\n:::::::3)Apresentar alunos:::::::\n:::::::4)Sair:::::::\n')
    opcao = int(input('insira a opção desejada: '))
    if opcao == 1:
       print('-='* 30)
       print('adicionar aluno')
       addaluno = input('Insira o nome do aluno para ser adicionado: ')
       sistema.append(addaluno)
    elif opcao == 2:
        print('-='* 30)
        print('remover aluno')
        remoaluno = input('Insira o nome do aluno para ser removido: ')
        sistema.remove(remoaluno)
    elif opcao == 3:
        print('-='* 30)
        print('alunos no sistema')     
        print(sistema)
    elif opcao == 4:
        print('-='* 30)   
        print('saindo....')
        break
    
    
    
