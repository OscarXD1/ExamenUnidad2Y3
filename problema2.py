#Joselin Juarez Potenciano 2211684
#Evelyn Anelis Melendez Cruz
#Oscar Gael Salazar Alvarez
#Examen Unidad 2 y 3

""""
Se tiene un archivo llamado bank-loans.csv, el cual contiene información sobre los préstamos de los clientes de un banco.
Utilizando la librería Pandas se pide, las siguientes funciones una por cada inciso, debe probar su funcionamiento en un main:

a. Realizar una función que reciba como parámetro una edad mínima y una edad máxima. Retorna un DataFrame con la información de los clientes entre dicho rango. (15%)

b. Mostrar por pantalla las edades medias según el nivel de estudios. (15%)

"""
import pandas as pd

#leo el archivo para converitlo a un df y poder usarlo
ruta= "bank-loans.csv"
df=pd.read_csv(ruta)
#print(df)

#print(df.min()) #la minima es 20 y la maxima es 61 solo los puse para saber
#print(df.max())

def rangoEdades(df:pd.DataFrame, edadMin, edadMax):
    #if age >= edadMin and age <= edadMax puse ese if para guiarme
    #aqui lo que hare es que a la columna de edad le voy a poner la condcion de si es igual o mayor a la edad minima lo dejen
    # y si la columna edad es menor o igual a la edad maxima tambien se deje  y al final solo imprimo para que pueda ver el resultado
    dfEdades=df[(df["age"]>= edadMin) & (df["age"]<= edadMax)]

    return dfEdades


def edadesEducacion(df:pd.DataFrame):
    #aqui solo agrupare la columna de educacion con edades y sacare el promedio o la media d la columna de edad
    promedioEstudios=df.groupby("education")["age"].mean()
    print(promedioEstudios)

if __name__ == "__main__":
    print(rangoEdades(df, 20,25))
    print("==========================================================")
    print(rangoEdades(df,18,20))
    print("===========================================================")
    edadesEducacion(df)

