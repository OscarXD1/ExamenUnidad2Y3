#Melendez Cruz Evelyn
#Juarez Potenciano Joselin
#Salazar Alvarez Oscar Gael
#951

import pandas as pd
#Se crea el df inicial
def crear():
    d = {"Departamento" : ["Ventas", "Ventas", "HR", "HR", "IT", "IT"],
         "ID" : [1001, 1002, 2001, 2002, 3001, 3002],
         "Nombre" : ["Juan", "Ana", "Luis", "Maria", "Pedro", "Sofia"],
         "Edad" : [30, 24, 29, 25, 32, 28],
         "Salario" : [40000, 42000, 38000, 39000, 50000, 52000]
         }
    df = pd.DataFrame(data=d)
    return df
#AQUI SOLO METI LOS DFS QUE OCUPARE PARA NO METERLOS AL MAIN
def dfsExtra():
    d2 = {"Departamento" : ["Ventas", "HR", "IT"],
         "ID" : [1003, 2003, 3003],
         "Nombre" : ["Oscar", "Joselin", "Evelyn"],
         "Edad" : [21, 20, 21],
         "Salario" : [40000, 42000, 38000]
         }

    dExtra ={"ID" : [1001, 1002, 1003, 2001, 2002, 2003, 3001, 3002, 3003],
            "dirección":["alpes", "Cerro", "Urbi", "Otay", "Playas", "Xoxo", "Calle", "Blvd", "Benton" ],
             "teléfono":["123456789","123456789","123456789","123456789","123456789","123456789","123456789","123456789","123456789"],
             "estado civil":["Soltero","Soltero","Casado","Soltero", "Viudo", "Soltero", "Casado", "Soltero", "Casado"],
             "correo":["c1@gmail.com","c2@gmail.com","c3@gmail.com","c4@gmail.com","c5@gmail.com","c6@gmail.com","c7@gmail.com","c8@gmail.com","c9@gmail.com"],
             "años de experiencia":[1, 2, 3, 4, 5, 6, 7, 8, 9]

    }
    df2 = pd.DataFrame(data=d2)
    dfExtra = pd.DataFrame(data=dExtra)

    return df2, dfExtra

#Funcion para realizar estadistica del departamento seleccionado
def estadisticasDepto(depto, df):
    df_depto = df[df["Departamento"] == depto]
    #DataFrame que mostrara tres columnas: El calculo que se realiza, el calculo de la edad, el calculo del salario
    estadisticas = {"Estadisticas" : ["Media", "Desviacion Estandar", "VMinimo", "VMax"],
                    "Edad":
                        [
                        df_depto["Edad"].mean(),
                        df_depto["Edad"].std(),
                        df_depto["Edad"].min(),
                        df_depto["Edad"].max()
                         ],
                    "Salario":
                        [
                        df_depto["Salario"].mean(),
                        df_depto["Salario"].std(),
                        df_depto["Salario"].min(),
                        df_depto["Salario"].max()
                        ]
                    }
    df_estadisticas = pd.DataFrame(estadisticas)
    #Se retorna el resultado
    return df_estadisticas

#Funcion para unir dos csv
def unirdfs(df1, df2):
    # convertir csv individuales
    df1.to_csv("empleados1.csv", index=False)
    df2.to_csv("empleados2.csv", index=False)

    # Unir los dfs
    dfUnido = pd.concat([df1, df2], ignore_index=True)

    #Convertir a csv el nuevo df
    dfUnido.to_csv("dfUnido.csv", index=False)

    # Retornar el DataFrame unido
    return dfUnido

#Agrega los datos basandose en el id del trabajador
def agregarDatos(dfUnido, rutaCsvExtra):
    # Leer archivo extra
    dfExtra = pd.read_csv(rutaCsvExtra)


    # Unir con la columna de ID
    dfCompleto = pd.merge(dfUnido, dfExtra, on="ID", how="left")

    # Retornar el df
    return dfCompleto

if __name__ == "__main__":
    df = crear()
    print(df)
    print ("===================================")
    print(estadisticasDepto("Ventas", df))
    print("===================================")
    df2, dfExtra = dfsExtra()
    # Guardar dfExtra como CSV
    dfExtra.to_csv("extraInfo.csv", index=False)
    dfUnido = unirdfs(df, df2)
    print(dfUnido)
    print("====================================")
    dfFinal = agregarDatos(dfUnido, "extraInfo.csv")
    print(dfFinal)
