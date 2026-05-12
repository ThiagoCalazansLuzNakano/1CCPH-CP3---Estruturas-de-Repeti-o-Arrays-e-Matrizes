temperaturas_sala = [[28, 31, 34, 33],[25, 27, 29, 28],[32, 35, 36, 34],[24, 26, 25, 27]]

for sala in temperaturas_sala:
    soma = 0
    critico = 0
    for temperatura in sala:
        soma = soma + temperatura
        if temperatura >= 33:
            critico += 1

    print(f"Sala")
    print(soma / 4)
    print(critico)
    print()
    print(f"Sala")
    print(soma / 4)
    print(critico)
    print()
    print(f"Sala")
    print(soma / 4)
    print(critico)
    print()
    print(f"Sala")
    print(soma / 4)
    print(critico)


