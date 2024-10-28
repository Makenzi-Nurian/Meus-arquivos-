class Caneta:
    def  __init__(self,cor):
        self.cor = cor
        self.tampada = True
        
    def destampar(self):
        if self.tampada:
            self.tampada = False
            print("A caneta foi destampada")
            
        else:
            print("A caneta já esta destampada")
        
    def tampar (self):  
        if not self.tampada:
           self.tampada = False
           print("A caneta esta tampada ")            
        
        
        
caneta = Caneta("Azul")
print(caneta.cor) 
print(caneta.tampada)
caneta.destampar()
caneta.destampar()
print(caneta.tampada)
caneta.tampar()
print(caneta.tampada)
       