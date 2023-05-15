import mysql.connector
import easygui as eg

# Pedir datos para la configuracion de la conexion
usuario = eg.enterbox("Ingrese el usuario", title="MySQL")
password = eg.passwordbox("Ingrese la contraseña", title="MySQL")
host = eg.enterbox("Ingrese el host", title="MySQL")
database = eg.enterbox("Ingrese el nombre de la base de datos", title="MySQL")

# Configuración de la conexión
config = {
    'user': usuario,
    'password': password,
    'host': host,
    'database': database
}

try:
    # Conexión a la base de datos
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    # Contar cuantas tablas hay en la base de datos
    cursor.execute("SHOW TABLES;")
    results = cursor.fetchall()
    lista = []
    for row in results:
        lista.append("\n")
        lista.append(row)
        
    lista = str(lista)
    lista = lista.replace("[", "")
    lista = lista.replace("]", "")
    lista = lista.replace("'", "")
    lista = lista.replace(",", "")
    lista = lista.replace(" ", " ")
    lista = lista.replace("{", " ")
    lista = lista.replace("}", " ")
    lista = lista.replace("\\n", " ")

    # Menu
    menu = ["Insertar", "Consultar", "Eliminar tabla","Eliminar datos de una tabla", "Actualizar datos", "Salir"]
    choice = eg.buttonbox("Bienvenido a la base de datos del MySQL", title="MySQL", choices=menu)
    while choice != "Salir":
        if choice == "Insertar":
            # Mostar las tablas de la base de datos
            eg.msgbox(lista, title="Tablas", ok_button="Aceptar")

            # Pedir al usuario que tabla quiere insertar
            tabla = eg.enterbox("Ingrese la tabla a la que quiere insertar", title="MySQL")

            # Mostrar estructura de la tabla
            cursor.execute(f"DESCRIBE {tabla};")

            # Recuperación de los resultados
            results = cursor.fetchall()

            # Mostrar los resultados
            resultado = []
            for row in results:
                resultado.append("\n")
                resultado.append(row)
            resultado = str(resultado)
            resultado = resultado.replace("[", "")
            resultado = resultado.replace("]", "")
            resultado = resultado.replace("'", "")
            resultado = resultado.replace(",", "")
            resultado = resultado.replace(" ", " ")
            resultado = resultado.replace("{", " ")
            resultado = resultado.replace("}", " ")
            resultado = resultado.replace("\\n", " ")

            # Preguntar que datos quiere insertar
            insertar = eg.enterbox(f"{resultado}\nIngrese los datos a insertar\nEjem: 123,abc,zxy098\nEl ""create table ya existe, solo es poner lo que vaya dentro de la estructura del comando""", title="MySQL")

            # Insertar un registro
            cursor.execute(f"INSERT INTO {tabla} VALUES ({insertar});")
            break
        
        elif choice == "Consultar":
            # Mostar las tablas de la base de datos
            eg.msgbox(lista, title="Tablas", ok_button="Aceptar")

            # Pedir al usuario que tabla quiere consultar
            tabla = eg.enterbox("Ingrese la tabla a la que quiere consultar", title="MySQL")

            # Mostrar estructura de la tabla
            cursor.execute(f"DESCRIBE {tabla};")

            # Recuperación de los resultados
            results = cursor.fetchall()

            # Mostrar los resultados
            consulta = []
            for row in results:
                consulta.append("\n")
                consulta.append(row)
            consulta = str(consulta)
            consulta = consulta.replace("[", "")
            consulta = consulta.replace("]", "")
            consulta = consulta.replace("'", "")
            consulta = consulta.replace(",", "")
            consulta = consulta.replace(" ", " ")
            consulta = consulta.replace("{", " ")
            consulta = consulta.replace("}", " ")
            consulta = consulta.replace("\\n", " ")

            # Preguntar que datos quiere consultar
            consultar = eg.enterbox(f"{consulta}\nIngrese los datos a consultar (pueden ser varios datos)\nEjem: nombre==""Amanda""", title="MySQL")

            # Consultar un registro
            cursor.execute(f"SELECT * FROM {tabla} WHERE {consultar};")

            # Recuperación de los resultados
            results = cursor.fetchall()

            # Mostrar los resultados
            selectLista = []
            for row in results:
                selectLista.append("\n")
                selectLista.append(row)
            selectLista = str(selectLista)
            selectLista = selectLista.replace("[", "")
            selectLista = selectLista.replace("]", "")
            selectLista = selectLista.replace("'", "")
            selectLista = selectLista.replace(",", "")
            selectLista = selectLista.replace(" ", " ")
            selectLista = selectLista.replace("{", " ")
            selectLista = selectLista.replace("}", " ")
            selectLista = selectLista.replace("\\n", " ")
        
            # Mostrar los resultados
            eg.msgbox(selectLista, title="Resultados", ok_button="Aceptar")
            break
        
        elif choice == "Eliminar tabla":
            # Mostar las tablas de la base de datos
            eg.msgbox(lista, title="Tablas", ok_button="Aceptar")

            # Pedir al usuario que tabla quiere eliminar
            tabla = eg.enterbox("Ingrese la tabla a la que quiere eliminar", title="MySQL")

            # Eliminar una tabla
            cursor.execute(f"DROP TABLE {tabla};")

            # Mostrar las tablas de la base de datos actualizadas
            cursor.execute("SHOW TABLES;")
            results = cursor.fetchall()

            # Mostrar los resultados
            dbActualizada = []
            for row in results:
                dbActualizada.append("\n")
                dbActualizada.append(row)
            dbActualizada = str(dbActualizada)
            dbActualizada = dbActualizada.replace("[", "")
            dbActualizada = dbActualizada.replace("]", "")
            dbActualizada = dbActualizada.replace("'", "")
            dbActualizada = dbActualizada.replace(",", "")
            dbActualizada = dbActualizada.replace(" ", " ")
            dbActualizada = dbActualizada.replace("{", " ")
            dbActualizada = dbActualizada.replace("}", " ")

            # Mostrar los resultados
            eg.msgbox(dbActualizada, title="Base de datos actualizada", ok_button="Aceptar")
            break

        elif choice == "Eliminar datos de una tabla":
            # Mostar las tablas de la base de datos
            eg.msgbox(lista, title="Tablas", ok_button="Aceptar")

            # Pedir al usuario que tabla quiere eliminar
            tabla = eg.enterbox("Ingrese la tabla a la que quiere eliminar datos", title="MySQL")

            # Mostrar estructura de la tabla
            cursor.execute(f"DESCRIBE {tabla};")

            # Recuperación de los resultados
            results = cursor.fetchall()

            # Mostrar los resultados
            resultadoElim = []
            for row in results:
                resultadoElim.append("\n")
                resultadoElim.append(row)
            resultadoElim = str(resultadoElim)
            resultadoElim = resultadoElim.replace("[", "")
            resultadoElim = resultadoElim.replace("]", "")
            resultadoElim = resultadoElim.replace("'", "")
            resultadoElim = resultadoElim.replace(",", "")
            resultadoElim = resultadoElim.replace(" ", " ")
            resultadoElim = resultadoElim.replace("{", " ")
            resultadoElim = resultadoElim.replace("}", " ")
            resultadoElim = resultadoElim.replace("\\n", " ")

            # Preguntar que datos quiere eliminar
            eliminar = eg.enterbox(f"{resultadoElim}\nIngrese los datos a eliminar\nEjem: nombre==""Amanda""", title="MySQL")

            # Eliminar un registro
            cursor.execute(f"DELETE FROM {tabla} WHERE {eliminar};")

            # Mostrar las tablas de la base de datos actualizadas
            cursor.execute("SHOW TABLES;")
            results = cursor.fetchall()

            # Mostrar los resultados
            dbActualizada = []
            for row in results:
                dbActualizada.append("\n")
                dbActualizada.append(row)
            dbActualizada = str(dbActualizada)
            dbActualizada = dbActualizada.replace("[", "")
            dbActualizada = dbActualizada.replace("]", "")
            dbActualizada = dbActualizada.replace("'", "")
            dbActualizada = dbActualizada.replace(",", "")
            dbActualizada = dbActualizada.replace(" ", " ")
            dbActualizada = dbActualizada.replace("{", " ")
            dbActualizada = dbActualizada.replace("}", " ")
            dbActualizada = dbActualizada.replace("\\n", " ")

            # Mostrar los resultados
            eg.msgbox(dbActualizada, title="Base de datos actualizada", ok_button="Aceptar")
            break

        elif choice == "Actualizar datos de una tabla":
            # Mostar las tablas de la base de datos
            eg.msgbox(lista, title="Tablas", ok_button="Aceptar")

            # Pedir al usuario que tabla quiere actualizar
            tabla = eg.enterbox("Ingrese la tabla a la que quiere actualizar datos", title="MySQL")

            # Mostrar estructura de la tabla
            cursor.execute(f"DESCRIBE {tabla};")
            results = cursor.fetchall()

            # Mostrar los resultados
            resultadoAct = []
            for row in results:
                resultadoAct.append("\n")
                resultadoAct.append(row)
            resultadoAct = str(resultadoAct)
            resultadoAct = resultadoAct.replace("[", "")
            resultadoAct = resultadoAct.replace("]", "")
            resultadoAct = resultadoAct.replace("'", "")
            resultadoAct = resultadoAct.replace(",", "")
            resultadoAct = resultadoAct.replace(" ", " ")
            resultadoAct = resultadoAct.replace("{", " ")
            resultadoAct = resultadoAct.replace("}", " ")
            resultadoAct = resultadoAct.replace("\\n", " ")

            # Preguntar que datos quiere actualizar
            actualizar = eg.enterbox(f"{resultadoAct}\nIngrese los datos a actualizar\nEjem: nombre==""Amanda""", title="MySQL")

            # Actualizar un registro
            cursor.execute(f"UPDATE {tabla} SET {actualizar};")

            # Mostrar las tablas de la base de datos actualizadas
            cursor.execute("SHOW TABLES;")
            results = cursor.fetchall()

            # Mostrar los resultados
            dbActualizada = []
            for row in results:
                dbActualizada.append("\n")
                dbActualizada.append(row)
            dbActualizada = str(dbActualizada)
            dbActualizada = dbActualizada.replace("[", "")
            dbActualizada = dbActualizada.replace("]", "")
            dbActualizada = dbActualizada.replace("'", "")
            dbActualizada = dbActualizada.replace(",", "")
            dbActualizada = dbActualizada.replace(" ", " ")
            dbActualizada = dbActualizada.replace("{", " ")
            dbActualizada = dbActualizada.replace("}", " ")
            dbActualizada = dbActualizada.replace("\\n", " ")

            # Mostrar los resultados
            eg.msgbox(dbActualizada, title="Base de datos actualizada", ok_button="Aceptar")
            break
            
        elif choice == "Salir":
            eg.msgbox("Gracias por usar el programa", title="MySQL", ok_button="Aceptar")
            break


except mysql.connector.Error as e:
    print(f"Error de conexión a la base de datos: {e}")


finally:
    # Cierre del cursor y la conexión
    if cursor:
        cursor.close()
    if conn:
        conn.close()
