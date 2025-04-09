def calculate_prizes(ganadores):
    total_premio = 150000000
    premios_por_sorteo = [total_premio / len(ganadores)]
    return premios_por_sorteo
def get_db_connection():
    client = MongoClient("mongodb+srv://cjrcjrcc93:TestPassword123@clusterchance.fojllqs.mongodb.net/?retryWrites=true&w=majority")
    db = client['chance_db']
    return db