from tema7-LeerDatos import num2

class OperasBas:
    #declaracion de propiedades de clase
    num1=0
    num2=0
    res=0
    
    #declaracion de constructo
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
    
    #declaracion de métodos de clase
    
    def suma(self):
        self.res=self.num1+self.num2
        print("La suma es {}".format(res))
        
#Por indentacion se queda afuera de la clase
def main():
    obj=OperasBas(3,4)
    obj.suma()
    
if __name__ == "__main__":
    main()