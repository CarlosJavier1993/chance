from pymongo import MongoClient

try:
    client = MongoClient("mongodb+srv://cjrcjrcc93:TestPassword123@clusterchance.fojllqs.mongodb.net/?retryWrites=true&w=majority")
    db = client['chance_db']
    print("Conexión exitosa")
except Exception as e:
    print("Error de conexión:", e)