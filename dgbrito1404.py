# senha-e-jogo
# codigo de senha com joguinho dentro
def jogo ():
    import random
    var = random.randint(1,10)
    print("voce tera que acertar um numero aleatorio com a media de 3 valores")
    while True:
        n1 = int(input("digite o valor 1 : "))
        n2 = int(input("digite o valor 2 : "))
        n3 = int(input("digite o valor 3 : "))
        media = (n1+n2+n3) / 3
        if n1 == n2 or n2 == n3 or n3==n1:
            print("voce tem que chutar 3 numeros diferentes")
            print('perdeu a sua chance')
            break
        elif media > var:
            print(f"a media deu {media} e é maior que o valor misterioso")
            print()
        elif media < var:
            print(f"a media deu {media} e é menor que o valor misterioso")
            print()
        else:
            print("parabens voce acertou, o numero era: ", var)
            break
normal = 0
pref = 0
while True:
    print('Seja Bem Vindo(a) --dg--')
    
    n = input('qual seu nome: ')
    
    i = int(input('qual sua idade: '))
    print()
    if i > 59:
        pref += 1 
        senha = f'P{pref:04}'
        print(f"{n}, {i} anos, sua senha é: {senha}")
    else:
        normal += 1
        senha = f'N{normal:04}'
        print(f"{n}, {i} anos, sua senha é: {senha}")

    print()
    print("deseja uma nova senha? sim ou nao  ")
    rep = input().lower()
    if rep != 'sim':
        print('Ok, obrigado e tenha um bom dia!')
        print()
        print('Gostaria jogar um jogo enquanto aguarda? ')
    else:
        continue
    jg = input().lower().strip()
    if jg in 'Ssim':
        jogo()
    break
