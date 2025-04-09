from pymongo import MongoClient
import random
from datetime import datetime

def get_db_connection():
    client = MongoClient("mongodb+srv://cjrcjrcc93:TestPassword123@clusterchance.fojllqs.mongodb.net/?retryWrites=true&w=majority")
    db = client['chance_db']
    return db

def initialize_db():
    db = get_db_connection()
    
    # Verificar si la colección está vacía
    if db.boletos.count_documents({}) == 0:
        sorteos = [
            {
                "sorteo": 2255,
                "serie": 1,
                "premio": 150000000,
                "fecha_emision": "2025-06-12",
                "valor_billete": 10000,
                "boletos": generate_boletos(),
            },
            {
                "sorteo": 3748,
                "serie": 2,
                "premio": 150000000,
                "fecha_emision": "2025-06-12",
                "valor_billete": 10000,
                "boletos": generate_boletos(),
            },
            {
                "sorteo": 4567,
                "serie": 3,
                "premio": 150000000,
                "fecha_emision": "2025-06-12",
                "valor_billete": 10000,
                "boletos": generate_boletos(),
            },
        ]
        db.boletos.insert_many(sorteos)  # Inserta los sorteos iniciales
        print("Sorteos iniciales insertados correctamente.")
    else:
        print("Los sorteos ya estaban insertados.")


def generate_boletos():
    import random
    # Generar una lista de 10 números aleatorios de 4 dígitos
    return [f"{random.randint(0, 9999):04d}" for _ in range(10)]


def get_boletos():
    db = get_db_connection()
    return list(db.boletos.find())