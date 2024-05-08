from datetime import datetime
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.fut1


jugadores = [
    {"DNI": "12334978A", "Nombre": "Lionel", "Apellidos": "Messi", "Fecha_Nacimiento": datetime(1987, 6, 24), "Direccion": "Barcelona", "Telefono": "1234567890", "Nacionalidad": "Argentina", "Talla": "M", "Peso": "68", "Clubes": ["FC Barcelona", "Paris Saint-Germain"]},
    {"DNI": "87654321B", "Nombre": "Cristiano", "Apellidos": "Ronaldo", "Fecha_Nacimiento": datetime(1985, 2, 5), "Direccion": "Turin", "Telefono": "9876543210", "Nacionalidad": "Portugal", "Talla": "L", "Peso": "83", "Clubes": ["Juventus"]},
    {"DNI": "45678901C", "Nombre": "Neymar", "Apellidos": "Jr.", "Fecha_Nacimiento": datetime(1992, 2, 5), "Direccion": "Paris", "Telefono": "5678901234", "Nacionalidad": "Brasil", "Talla": "L", "Peso": "68", "Clubes": ["FC Barcelona", "Paris Saint-Germain"]}
]
db.Jugadores.insert_many(jugadores)


clubes = [
    {"Nombre": "FC Barcelona", "Palmares": "25", "Ciudad": "Barcelona", "Division": 1, "Internacionalidad": 1, "Entrenadores": ["12315278A", "45678901C"]},
    {"Nombre": "Juventus", "Palmares": "37", "Ciudad": "Turin", "Division": 1, "Internacionalidad": 1, "Entrenadores": ["87654321B"]}
]


entrenadores = [
    {"DNI": "12315278A", "Nombre": "Pep Guardiola"},
    {"DNI": "87654321B", "Nombre": "Zinedine Zidane"},
    {"DNI": "45678901C", "Nombre": "Jurgen Klopp"}
]
db.Entrenador.insert_many(entrenadores)


contratos = [
    {"Fecha": datetime(2024, 1, 15), "Duracion": datetime(2029, 1, 15), "Salario": 1200000, "Clausula": 1000, "DNI_Jugador": "12334978A", "Nombre_Club": "FC Barcelona"},
    {"Fecha": datetime(2024, 1, 15), "Duracion": datetime(2028, 1, 15), "Salario": 800000, "Clausula": 8000, "DNI_Jugador": "87654321B", "Nombre_Club": "Juventus"}
]
db.Contrato.insert_many(contratos)
