import pandas as pd
from mysql.connector import connect, Error



#a)Crear una función que permita guardar el contenido del archivo en una sola tabla de una Base de Datos.
#Debe asumir que existe una Base de Datos llamada Ventas Coches, la cual contiene una tabla llamada Ventas.
def cargar_cvs(ruta_csv): #clase
    try:
        conexion = connect(host="localhost",  # esta es la función que nos permite conectarnos a la base de datos
                            user="root",
                            password="12345678",
                            database="VentasCoche")
        cursor = conexion.cursor()

    #la ruta del archivo y usamos un separador para los datos
        df = pd.read_csv(ruta_csv,
                         sep=";")
        print(df.head())
        print(df.columns)  #se usan para saber el nombre de las columas y q tipo de datos hay

    #normmalizo las ccolumns ck ssale un error e intento asegurqar q solo existan estas
        df = df[["Marca", "Precio"]]

    #hacemos el insert de los datos en la tabla
    #%s -> lo utilizamos para que loss datos que se van insertar se remplazaran ahi
        query = "insert into ventas (marca, precio) values (%s, %s)"

        #lo convertimos a tuplita
        datos = [tuple(row) for row in df.to_numpy()]

        #hjecutamos tremendo insert (es q son muchos datos JDKJENCFKJD)
        cursor.executemany(query, datos)
        conexion.commit()

        print("se inserto todo bn yeiii (^^ゞ")

    except Error as e:  # para ver si tenemos error de conexión y saber cuál error es
        print("errorcin:", e)


    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()


#b) Crear una función que se conecte a la base de datos y retorna un DataFrame con el número de autos vendidos por Marca
#y el total de ganancia (suma de precios), ordenado por el número de autos vendidos. Debe recibir como parámetro la marca
#que se desea calcular, además de incluir un valor default por si se requiere que retorne la información de todas las marcas.
def ventas(marca = None):
    try:
        conexion = connect(host="localhost",  # esta es la función que nos permite conectarnos a la base de datos
                           user="root",
                           password="12345678",
                           database="VentasCoche")

        #select de toda la tabla
        query1 = "select * from ventas"
        df = pd.read_sql(query1, conexion)

        if marca:
            df = df[df["marca"] == marca]

        #número de autos vendidos x marca
        venta = df.groupby("marca").agg(
            autos_vendidos = ("marca", "count"),
            total = ("precio", "sum")
        ).sort_values("autos_vendidos", ascending=False)

        return venta
    except Error as e:
        print("error lol:", e)

    finally:
        if conexion.is_connected():
            conexion.close()

if __name__ == "__main__":
    cargar_cvs(r"C:\Users\eveli\Downloads\coches.csv")
    resultado = ventas() #todas las marcas
    print(resultado)
    resultado2 = ventas("Acura")
    print(resultado2) #filtrado por una marca