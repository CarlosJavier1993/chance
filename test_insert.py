from pymongo import MongoClient

try:
    client = MongoClient("mongodb+srv://cjrcjrcc93:TestPassword123@clusterchance.fojllqs.mongodb.net/?retryWrites=true&w=majority")
    db = client['chance_db']
    db.boletos.insert_one({"sorteo": 9999, "serie": 1, "premio": 500000, "boletos": [1234, 5678]})
    print("Documento insertado correctamente.")
except Exception as e:
    print("Error:", e)