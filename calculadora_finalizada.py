import os
# Funções
def titulo(txt):
    print ('-'*42)
    print (txt.center(42))
    print ('-'*42)

def escolha(lista):
    c = 1
    for item in lista:
        print(f'[{c}] {item}')
        c +=1
    print('[0] Sair')

def time():
    t = input('Pressione ENTER para voltar...')  


# Menu Principal
while True:
    os.system('cls' if os.name == 'nt' else 'clear' )

    titulo('MENU PRINCIPAL')    
    escolha(['Decimal para outras bases','Outras bases para decimal'])    
    opcao = int(input('Digite uma opção:'))
    if opcao == 0: break
# Menu decimal para outras bases
    if opcao == 1:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')

            titulo('Decimal para outras bases')
            escolha(['Decimal para binário','Decimal para octal','Decimal para hexadecimal'])
            opcao = int(input('Digite uma opção:'))
            if opcao == 0: break
            if opcao <0 or opcao >3:
                print('Opção inválida!')
                time()
# Dec2bin1
            if opcao == 1:
                binario = ''
                entrada = int(input('Digite um número decimal:'))
                decimal = entrada
                while decimal!=0:
                    resto = decimal%2
                    binario = str(resto) + binario
                    decimal = decimal//2
                print(f'Decimal para binário: \n({entrada})₁₀ = ({binario})₂')
                time()
# Dec2oct2
            if opcao == 2:
                octal = ''
                entrada = int(input('Digite um número decimal:'))
                decimal = entrada
                while decimal!=0:
                    resto = decimal%8
                    octal = str(resto) + octal
                    decimal = decimal//8
                print(f'Decimal para octal: \n({entrada})₁₀ = ({octal})₈')
                time()
# Dec2hex3
            if opcao == 3:
                hexadecimal = ''
                entrada = int(input('Digite um número decimal:'))
                decimal = entrada
                while decimal!=0:
                    resto = decimal%16
                    if resto == 10: resto = 'A'
                    elif resto == 11: resto = 'B'
                    elif resto == 12: resto = 'C'
                    elif resto == 13: resto = 'D'
                    elif resto == 14: resto = 'E'
                    elif resto == 15: resto = 'F'
                    else:''                    
                    hexadecimal = str(resto) + hexadecimal
                    decimal = decimal//16
                print(f'Decimal para hexadecimal: \n({entrada})₁₀ = ({hexadecimal})₁₆')
                time()
# Menu outras bases para decimal
    if opcao == 2:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            titulo('Outras bases para decimal')
            escolha(['Binário para decimal','Octal para decimal','Hexadecimal para decimal'])
            opcao = int(input('Digite uma opção:'))
            if opcao == 0: break
            if opcao <0 or opcao >3: 
                print('Opção inválida!')
                time()
# Bin2dec1
            if opcao == 1:
                decimal = 0
                binario = input('Digite um número binário:')
                n = len(binario) - 1
                for d in binario:
                    decimal = decimal + int(d)*2**n
                    n -= 1
                print(f'Binário para decimal: \n({binario})₂ = ({decimal})₁₀')
                time()
# Oct2dec2
            if opcao == 2:
                decimal = 0
                octal = input('Digite um número octal:')
                n = len(octal) - 1
                for d in octal:
                    decimal = decimal + int(d)*8**n
                    n -= 1
                print(f'Octal para decimal: \n({octal})₈ = ({decimal})₁₀')
                time()
# Hex2dec3
            if opcao == 3:
                decimal = 0
                hexadecimal = input('Digite um número hexadeximal:')
                n = len(hexadecimal) - 1
                for d in hexadecimal:
                    d = d.upper()                    
                    if d == 'A' : d = 10
                    elif d == 'B': d = 11
                    elif d == 'C': d = 12
                    elif d == 'D': d = 13
                    elif d == 'E': d = 14
                    elif d == 'F': d = 15    
                    else:''
                    decimal = decimal + int(d)*16**n
                    n -= 1
                    hexadecimal = str(hexadecimal).upper()
                print(f'Hexadeximal para decimal: \n({hexadecimal})₁₆ = ({decimal})₁₀')
                time()   