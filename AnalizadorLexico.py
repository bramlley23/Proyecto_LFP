
contenido_archivo=""
estado=0
char_actual=""
lexema=""
lexemas=[]
numeros=[]
tokens=[]
tokenError=[]
columna=0
fila=1
with open('p.txt','r',encoding='UTF-8')as f:
	contenido_archivo=f.read()

contenido_archivo= contenido_archivo+" "


#metodo para comparar si es una letra
def esletra(caracter):
	letras =["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	if caracter.upper() in letras:
		return True
	else:
		return False

#metodo para comprobar si es digito
def esnumero(caracter):
	digitos=["0","1","2","3","4","5","6","7","8","9"]
	if caracter in digitos:
		return True
	else:
		False

x=0

while x<len(contenido_archivo):
	char_actual=contenido_archivo[x]


#<--------------------Estado Cero ---------------->
	if estado==0:
		if esletra(char_actual):
			estado=3 #si es una letra nos movemos al estado 3 y concatenamos la letra a la subcadena lexema
			lexema=lexema+char_actual

		elif esnumero(char_actual):
			estado=1#si es un numero nos movemos al estado 1 y concatenamos el numero a la subcadena lexema
			lexema=lexema+char_actual

#<-----------aqui estamos reconociendo los meta-simbolos----------|#
		elif char_actual==",":
			print("se reconocio espacio ", fila)
#|                                                                |#
		elif char_actual=="\n":
			print("se reconocio salto de linea ", fila)
#|                                                                |#
		elif char_actual=="[":
			print("se reconocio corchete abierto ", fila)

#|                                                                |#
		elif char_actual=="]":
			print("se reconocio corcheta cerrada ", fila)

#|                                                                |#
		elif char_actual=="\'":
			print("se reconocio comilla ", fila)
#|                                                                |#
		else:
			print("se encontro un error en :"+char_actual , " columnita ", columna)

#|---------------------------------------------------------------|#

	#<---------------- Estado uno ----------------->

	elif estado==1:
		if esnumero(char_actual):
			lexema=lexema+char_actual
			estado=1
		elif char_actual==".":
			lexema=lexema+char_actual
			estado=2
		else:
			#print("se encontro un error en " + char_actual , " y columna ", columna,)
			lexema=""
			estado=0


#<---------------------estado dos-------------------------->
	elif estado==2:
		if esnumero(char_actual):
			lexema=lexema+char_actual
			estado=2
		else:
			estado=0
			x=x-1
			print("se reconocio " + lexema , " numero ", fila)
			numeros.append("numeros")
			numeros.append(lexema)
			numeros.append("fila")

			lexema=""

	#<------------------estado 3 se reconoce letras--------------->
	elif estado==3:
		if esletra(char_actual):
			estado=3
			lexema=lexema+char_actual
		else:
			estado=0
			x=x-1
			print("se reconocio " +lexema , "fila ", fila)
			tokens.append(lexema)
			tokens.append(fila)


			lexema=""
	columna = columna+1
	fila = fila+1

	x=x+1
concatenacion=[tokens,'\n',numeros]

print(concatenacion)
print()
