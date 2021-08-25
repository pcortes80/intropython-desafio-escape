# Importa librería sys
import sys

# Lee el largo del script, para asegurarse de ingresar la cantidad de argumentos correctos
largo = len(sys.argv)

# Solo si la cantidad de argumentos ingresados es correcta se realizan los calculos
if largo > 2:
    g = float(sys.argv[1]) # lee el primer argumento del script : gravedad "g"
    r = float(sys.argv[2]) # lee el segundo argumento del script : radio "r"

    # Pasa el radio "r" a Kms
    r = r*1000

    # Calcula el valor de Ue (velocidad de escape)
    # Usa round() para redondear hacia arriba con 2 decimales
    Ue = round(((2*g*r)**0.5),2)
    
    # Imprime en pantalla la velocidad de escape
    print("La velocidad de escape es " + str(Ue) + " m/s.")
    
else:
    # Mensaje al usuario
    print("Hay argumentos que faltan. Por favor intente de nuevo.")

# Fin del programa