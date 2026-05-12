temperaturas_sala = [[28, 31, 34, 33],[25, 27, 29, 28],[32, 35, 36, 34],[24, 26, 25, 27]]

for sala in temperaturas_sala:
    soma = 0
    critico = 0
    Sala =0
    for temperatura in sala:
        soma = soma + temperatura
        if temperatura >= 33:
            critico += 1

    print(f"Sala {Sala + 1}")
    print(soma / 4)
    print(critico)
    print(f"Sala {Sala + 2}")
    print(soma / 4)
    print(critico)
    print(f"Sala {Sala +3}")
    print(soma / 4)
    print(critico)
    print(f"Sala {Sala +4}")
    print(soma / 4)
    print(critico)


