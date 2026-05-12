temperaturas_sala = [
    [28, 31, 34, 33],
    [25, 27, 29, 28],
    [32, 35, 36, 34],
    [24, 26, 25, 27]
]

numero_sala = 1

for sala in temperaturas_sala:
    soma = 0
    critico = 0

    for temperatura in sala:
        soma += temperatura

        if temperatura >= 33:
            critico += 1

    media = soma / len(sala)

    print(f"Sala {numero_sala}")
    print(f"Média: {media}")
    print(f"Registros críticos: {critico}")
    print()

    numero_sala += 1