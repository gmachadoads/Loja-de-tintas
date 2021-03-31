galao = lata = sobra = 0
area = float(input('Área a ser pintada: '))

print('-'*30)


if area % 21.6 == 0:
    galao = area / 21.6
    print(f'Opção apenas galão:\nNecessário(s) {galao:.0f} galão(ões).\nCusto: R$ {galao * 25:.2f}')
else:
    galao = area // 21.6 + 1
    print(f'Opção apenas galão:\nNecessário(s) {galao:.0f} galão(ões).\nCusto: R$ {galao * 25:.2f}')
print('-'*30)

if area % 108 == 0:
    lata = area / 108
    print(f'Opção apenas lata:\nNecessário(s) {lata:.0f} lata(s).\nCusto: R$ {lata * 80:.2f}')
else:
    lata = area // 108 + 1
    print(f'Opção apenas lata:\nNecessário(s) {lata:.0f} lata(s).\nCusto: R$ {lata * 80:.2f}')
print('-'*30)

if (area / 108) < 1:
    if area % 21.6 == 0:
        galao = area / 21.6
        print(f'Opção menos desperdício:\n{galao:.0f} galão(ões) de tinta.\nCusto: R$ {galao*25:.2f} ')
    else:
        galao = area // 21.6 + 1
        print(f'Opção menos desperdício:\n{galao:.0f} galão(ões) de tinta.\nCusto: R$ {galao*25:.2f} ')
elif (area / 108) > 1:
    if area % 108 == 0:
        lata = area / 108
        print(f'Opção menos desperdício:\n{lata:.0f} lata(s) de tinta.\nCusto: R$ {lata*80:.2f} ')
    elif area % 108 < 108:
        lata = area // 108
        sobra = area - lata * 108
        if sobra % 21.6 == 0:
            galao = sobra / 21.6
            print(f'Opção menos desperdício:\n{lata:.0f} lata(s) e {galao:.0f} galão(ões) de tinta.\nCusto: R$ {galao*25 + lata*80:.2f}')
        else:
            galao = sobra // 21.6 + 1
            print(f'Opção menos desperdício:\n{lata:.0f} lata(s) e {galao:.0f} galão(ões) de tinta.\nCusto: R$ {galao*25 + lata*80:.2f}')
