from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.movies

def insert_movie():
    title = input("Ingrese el título de la película: ")
    year = input("Ingrese el año de lanzamiento: ")
    genre = input("Ingrese el género de la película: ")
    db.movies.insert_one({"title": title, "year": year, "genre": genre})
    print("Película insertada correctamente.")

def delete_movie():
    title = input("Ingrese el título de la película que desea eliminar: ")
    result = db.movies.delete_one({"title": title})
    if result.deleted_count == 1:
        print("Película eliminada correctamente.")
    else:
        print("No se encontró ninguna película con ese título.")

def update_movie():
    title = input("Ingrese el título de la película que desea actualizar: ")
    new_title = input("Ingrese el nuevo título de la película: ")
    new_year = input("Ingrese el nuevo año de lanzamiento: ")
    new_genre = input("Ingrese el nuevo género de la película: ")
    result = db.movies.update_one({"title": title}, {"$set": {"title": new_title, "year": new_year, "genre": new_genre}})
    if result.modified_count == 1:
        print("Película actualizada correctamente.")
    else:
        print("No se encontró ninguna película con ese título.")

def consultar_por_año():
    año = input("Introduce el año de la película que deseas consultar: ")
    peliculas = list(db.movies.find({"year": año}, {"_id": 0, "title": 1}))
    if not peliculas:
        print("No se encontraron películas para el año especificado.")
    else:
        print(f"Películas lanzadas en {año}:")
        for pelicula in peliculas:
            print(pelicula['title'])

while True:
    print("\nMenú:")
    print("1. Insertar película")
    print("2. Eliminar película")
    print("3. Actualizar película")
    print("4. Buscar película por año")
    print("5. Salir")

    choice = input("Seleccione una opción: ")

    if choice == "1":
        insert_movie()
    elif choice == "2":
        delete_movie()
    elif choice == "3":
        update_movie()
    elif choice == "4":
        consultar_por_año()
    elif choice == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
