print('Exercício de simulador de caixa eletrônico\n')

saque = int(input('Digite o valor do saque: R$ '))
saldo = saque

print('----' * 7)
print('Calculando notas...')
print('----' * 7)


while True:
    if saldo >= 100:
        modulo_100 = int(saldo / 100)
        troco_100 = saldo % 100
        saldo = saldo - (modulo_100 * 100)
        print(f'{modulo_100} nota(s) de R$ 100,00.')
        if saldo == 0:
            break
    elif saldo >= 50:
        modulo_50 = int(saldo / 50)
        troco_50 = saldo % 50
        saldo = saldo - (modulo_50 * 50)
        print(f'{modulo_50} nota(s) de R$ 50,00.')
        if saldo == 0:
            break
    elif saldo >= 20:
        modulo_20 = int(saldo / 20)
        troco_20 = saldo % 20
        saldo = saldo - (modulo_20 * 20)
        print(f'{modulo_20} nota(s) de R$ 20,00.')
        if saldo == 0:
            break
    elif saldo >= 10:
        modulo_10 = int(saldo / 10)
        troco_10 = saldo % 10
        saldo = saldo - (modulo_10 * 10)
        print(f'{modulo_10} nota(s) de R$ 10,00.')
        if saldo == 0:
            break
    elif saldo >= 5:
        modulo_5 = int(saldo / 5)
        troco_5 = saldo % 5
        saldo = saldo - (modulo_5 * 5)
        print(f'{modulo_5} nota(s) de R$ 5,00.')
        if saldo == 0:
            break
    elif saldo >= 2:
        modulo_2 = int(saldo / 2)
        troco_2 = saldo % 5
        saldo = saldo - (modulo_2 * 2)
        print(f'{modulo_2} nota(s) de R$ 2,00.')
        if saldo == 0:
            break
    elif saldo >= 1:
        modulo_1 = int(saldo / 1)
        troco_1 = saldo % 1
        saldo = saldo - (modulo_1 * 1)
        print(f'{modulo_1} nota(s) de R$ 1,00.')
        if saldo == 0:
            break
print('----' * 7)
print('\nVolte sempre!')