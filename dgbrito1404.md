# senha-e-jogo
codigo de senha com joguinho dentro
def jogo ():
    import random
    var = random.randint(1,10)
    print("voce tera que acertar um numero aleatorio com a media de 3 valores")
    while True:
        n1 = int(input("digite o valor1 : "))
        n2 = int(input("digite um valor2 : "))
        n3 = int(input("digite um valor3 : "))
        if n1 == n2 or n2 == n3 or n3 == n1:
            print("voce tem que chutar 3 numeros diferentes")
        elif ((n1+n2+n3) / 3) > var:
            print("essa media é maior que o valor misterioso")
        elif ((n1+n2+n3) / 3) < var:
            print("essa media é menor que o valor misterioso")
        else:
            print("parabens voce acertou, o numero era: ", var)
            break

normal = 0
pref = 0
while True:
    n = input('qual seu nome: ')
    i = int(input('qual sua idade: '))
    if i > 59:
        pref += 1 
        senha = f'P{pref:04}'
        print(f"{n}, {i} anos, sua senha é: {senha}")
    else:
        normal += 1
        senha = f'N{normal:04}'
        print(f"{n}, {i} anos, sua senha é: {senha}")
    
    print("deseja uma nova senha? sim ou nao  ")
    rep = input().lower()
    if rep != 'sim':
        print('OK, obrigada e tenha um bom dia!')
        print('deseja jogar um jogo enquanto espera? ')
    jg = input()
    if jg == 'sim':
        jogo()
    break
