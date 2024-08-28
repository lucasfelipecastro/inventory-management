def opcoes_gerais():
    print("""
1 - Listar produtos em estoque
2 - Adicionar produtos
3 - Remover produtos 
4 - Sair
""")

def pular_linha():
    print()

galvanotek = ['GA90', 'G695', 'G697', 'FPN250', 'G32MM']
hiperpack = ['H742', 'H10', 'H20', 'H50APR', 'H56MPR']
niagara = ['MUD1', 'MUD2', 'MUD3', 'MUD4', 'MUD5']

while True:
    opcoes_gerais()
    escolha_opcao_geral = str(input('> ')).strip()

    if escolha_opcao_geral == '1':
        print('Galvanotek:', galvanotek)
        print('HiperPack:', hiperpack)
        print('Niagara:', niagara)
        pular_linha()

    elif escolha_opcao_geral == '2':
        adicionar_produto_marca = input('Digite a marca do produto: ').upper().strip()
        adicionar_produto_codigo = input('Digite o código do produto: ').upper().strip()

        print(f'Marca digitada: {adicionar_produto_marca}')
        print(f'Código digitado: {adicionar_produto_codigo}')

        if adicionar_produto_marca == 'GALVANOTEK' or adicionar_produto_marca == 'G':
            galvanotek.append(adicionar_produto_codigo)
            print(f'Produto {adicionar_produto_codigo} adicionado à marca Galvanotek.')

        if adicionar_produto_marca == 'HIPERPACK' or adicionar_produto_marca == 'H':
            hiperpack.append(adicionar_produto_codigo)
            print(f'Produto {adicionar_produto_codigo} adicionado à marca HiperPack.')
        
        if adicionar_produto_marca == 'NIAGARA' or adicionar_produto_marca == 'N':
            hiperpack.append(adicionar_produto_codigo)
            print(f'Produto {adicionar_produto_codigo} adicionado à marca Niagara.')

    elif escolha_opcao_geral == '4':
        print('Saindo do programa.')
        break

    else:
        print('Opção inválida. Tente novamente.')
