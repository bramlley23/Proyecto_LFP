from tkinter import *
from tkinter import filedialog


class ArchivoEntrada:
    raiz=Tk()
    archivo = " "
    x=0

    def __init__(self,archivo):
         self.archivo = archivo
         self.x=0 #variable para obtener el primer char
         self.estado=0
         self.columna=0
         self.fila=1
         self.char_actual=""
         self.lexema=""
         self.numeros=[]
         self.tokens=[]

#<--------------- VENTANA EMERGENTE ------------------------------------------->
    def ventanaEmergente(self):
        self.archivo = filedialog.askopenfilename(title="Archivos", initialdir="C:/")
        self.archivo = self.archivo + " "

        with open(self.archivo)as f_obj:
            lineas = f_obj.readlines()

        for line in lineas:
            print(line.rstrip())

#<--------------- METODO PARA COMPARAR CARACTERES DE LETRAS ------------------->

    def esletra(self,caracter):
    	letras =["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    	if caracter.upper() in letras:
    		return True
    	else:
    		return False

#<--------------- METODO PARA COMPARAR CARACTERES DE NUMEROS ------------------>

    def esnumero(self,caracter):
    	digitos=["0","1","2","3","4","5","6","7","8","9"]
    	if caracter in digitos:
    		return True
    	else:
    		False
#<--------------- METODO AUTOMATA FINITO DETERMINISTA ------------------------->

    def automata(self):

        while self.x<len(self.archivo):
            self.char_actual=self.archivo[self.x]
#<--------------------------------- Estado Cero ------------------------------->
            if self.estado == 0:
                if self.esletra(self.char_actual):
                    self.estado=3 #si es una letra nos movemos al estado 3 y concatenamos la letra a la subcadena lexema
                    self.lexema=self.lexema+self.char_actual
                elif self.esnumero(self.char_actual):
                    self.estado=1#si es un numero nos movemos al estado 1 y concatenamos el numero a la subcadena lexema
                    self.lexema=self.lexema+self.char_actual
                elif self.char_actual==",":
                    print("se reconocio espacio ", self.fila)
                elif self.char_actual=="\n":
                    print("se reconocio salto de linea ", self.fila)
                elif self.char_actual=="[":
                    print("se reconocio corchete abierto ", self.fila)
                elif self.char_actual=="]":
                    print("se reconocio corcheta cerrada ", self.fila)
                elif self.char_actual=="\'":
                    print("se reconocio comilla ", self.fila)
                else:
                    print("se encontro un error en :"+self.char_actual , " columnita ", self.columna)
#<--------------------------------- Estado Uno ------------------------------->
            elif self.estado==1:
                if self.esnumero(self.char_actual):
                    self.lexema=self.lexema+self.char_actual
                    self.estado=1
                elif self.char_actual==".":
                    self.lexema=self.lexema+self.char_actual
                    self.estado=2
                else:
                    print("se encontro un error en " + self.char_actual , " y columna ", self.columna,)
                    self.lexema=""
                    self.estado=0
#<--------------------------------- Estado Dos ------------------------------->
            elif self.estado==2:
                if self.esnumero(self.char_actual):
                    self.lexema=self.lexema+self.char_actual
                    self.estado=2
                else:
                    self.estado=0
                    self.x=self.x-1
                    print("se reconocio " + self.lexema , " numero ", self.fila)
                    numeros.append("numeros")
                    numeros.append(self.lexema)
                    numeros.append("fila")
                    self.lexema=""
#<--------------------------------- Estado Tres ------------------------------->
            elif self.estado==3:
                if self.esletra(self.char_actual):
                    self.estado=3
                    self.lexema=self.lexema+self.char_actual
                else:
                    self.estado=0
                    self.x=self.x-1
                    print("se reconocio " +self.lexema , "fila ", self.fila)
                    self.tokens.append(self.lexema)
                    self.tokens.append(self.fila)
                    self.lexema=""
            self.columna = self.columna+1
            self.fila = self.fila+1
            self.x=self.x+1


invocar = ArchivoEntrada("Hola mundo")
invocar.ventanaEmergente()
invocar.automata()
