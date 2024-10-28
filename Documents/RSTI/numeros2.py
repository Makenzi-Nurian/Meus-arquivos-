def media(l):
    return sum(l) / len(l)

def main():
    lista = [15, 25, 10, 9]
    media_lista = media(lista)
    print(f"Média: {media_lista}")

    variancia = calcular_variancia(lista, media_lista)
    print(f"Variância: {variancia}")

def calcular_variancia(l, media):
    return sum((x - media) ** 2 for x in l) / len(l)

main()