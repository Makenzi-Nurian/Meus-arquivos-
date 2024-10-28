
def media (l):
    return sum(l) / len (l)
    
def variancia(l):
    somatorio = 0
    for i in l:
        somatorio += (i - media(l))**2
    return somatorio / len(l)     

def desvio_padrao (l):
    return variancia (l)**(0.5)  
    
    
def main () :
    lista = [15,25,10,9]
    valor_media = media (lista)
    valor_variancia = variancia (lista)
    valor_desvio_padrao = desvio_padrao (lista)
    
    print(f"Média: {valor_media}")
    print(f"Variância: {valor_variancia}")
    print(f"Odesvio padrão é: {round(valor_desvio_padrao)}")
    
main()       
   
   