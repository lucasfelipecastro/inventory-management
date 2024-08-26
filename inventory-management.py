def opcoes_gerais():
   print("""
1 - Listar produtos em estoque
2 - Adicionar produtos
3 - Remover produtos 
""")

def pular_linha():
   print()

opcoes_gerais()

galvanotek = ['GA90', 'G695', 'G697', 'FPN250', 'G32MM']
hiperpack = ['H742', 'H10', 'H20', 'H50APR', 'H56MPR']
niagara = ['MUD1', 'MUD2', 'MUD3', 'MUD4', 'MUD5']

escolha_opcao_geral = str(input('> ')).strip()

if escolha_opcao_geral == '1':
    print('Galvanotek:', galvanotek)
    print('Hiperpack:', hiperpack)
    print('Niagara:', niagara)
    pular_linha()

elif escolha_opcao_geral == '2':
    adicionar_produto_marca = input('Digite a marca do produto: ').upper().strip()
    adicionar_produto_codigo = input('Digite o código do produto: ').upper().strip()

    if adicionar_produto_marca == 'GALVANOTEK' or adicionar_produto_marca == 'G':
        galvanotek.append(adicionar_produto_codigo)
        print(f'Produto {adicionar_produto_codigo} adicionado à marca Galvanotek.')