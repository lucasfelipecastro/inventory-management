def opcoes():
   print("""
1 - Listar produtos em estoque
2 - Adicionar produtos
3 - Remover produtos 
""")
opcoes()

escolha_opcao_geral = str(input('> ')).strip()

if escolha_opcao_geral == '1':
   galvanotek = ['GA90', 'G695', 'G697', 'FPN250', 'G32MM']
   hiperpack = ['H742', 'H10', 'H20', 'H50APR', 'H56MPR']
   niagara = ['MUD1', 'MUD2', 'MUD3', 'MUD4', 'MUD5']
   print('Galvanotek:', galvanotek)
   print('Hiperpack:', hiperpack)
   print('Niagara:', niagara)