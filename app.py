from flask import Flask, jsonify, render_template
import random
from database import get_db_connection
from datetime import datetime

app = Flask(__name__, static_folder='static')

# Generar resultados de un sorteo y actualizar MongoDB
def generar_resultado(sorteo, serie, premio):
    try:
        # Generar boletos y ganador
        boletos = [f"{random.randint(0, 9999):04d}" for _ in range(10)]
        ganador = random.choice(boletos)
        fecha_emision = datetime.now().strftime("%Y-%m-%d")  # Fecha de emisión actual
        valor_billete = 10000  # Valor estándar del billete

        # Actualizar los datos en MongoDB
        db = get_db_connection()
        db.boletos.update_one(
            {"sorteo": sorteo},  # Busca el sorteo en la colección
            {
                "$set": {
                    "boletos": boletos,       # Actualiza los boletos
                    "serie": serie,           # Actualiza la serie
                    "premio": premio,         # Actualiza el premio
                    "ganador": ganador,       # Agrega el ganador
                    "fecha_emision": fecha_emision,  # Agrega la fecha de emisión
                    "valor_billete": valor_billete   # Agrega el valor del billete
                }
            },
            upsert=True  # Crea el documento si no existe
        )

        # Depuración
        print(f"Sorteo {sorteo} actualizado en MongoDB con boletos y ganador.")

        # Retornar los resultados para mostrarlos en la página
        return {
            "sorteo": sorteo,
            "serie": serie,
            "premio": premio,
            "boletos": boletos,
            "ganador": ganador,
            "fecha_emision": fecha_emision,
            "valor_billete": valor_billete
        }
    except Exception as e:
        print(f"Error al generar resultados: {e}")
        return {"error": "Error al generar resultados."}

@app.route('/')
def index():
    return render_template('index.html')  # Carga la página principal

@app.route('/sorteo/<int:sorteo>')
def sorteo(sorteo):
    try:
        db = get_db_connection()
        sorteo_data = db.boletos.find_one({"sorteo": sorteo})  # Busca el sorteo en la base de datos

        if not sorteo_data:
            # Si no existen datos, generar resultados y guardarlos
            print(f"Generando resultados para el sorteo {sorteo}...")
            if sorteo == 2255:
                resultado = generar_resultado(2255, 1, 150000000)
            elif sorteo == 3748:
                resultado = generar_resultado(3748, 2, 150000000)
            elif sorteo == 4567:
                resultado = generar_resultado(4567, 3, 150000000)
            else:
                return jsonify({"error": "Sorteo no válido"}), 404
        else:
            # Usar los datos existentes en la base de datos
            resultado = {
                "sorteo": sorteo_data.get("sorteo", "No especificado"),
                "serie": sorteo_data.get("serie", "No especificado"),
                "premio": sorteo_data.get("premio", "No especificado"),
                "boletos": sorteo_data.get("boletos", []),
                "ganador": sorteo_data.get("ganador", "No disponible"),
                "fecha_emision": sorteo_data.get("fecha_emision", "No disponible"),
                "valor_billete": sorteo_data.get("valor_billete", "No disponible")
            }

        return jsonify(resultado)
    except Exception as e:
        print(f"Error al procesar sorteo {sorteo}: {e}")
        return jsonify({"error": "Error al procesar solicitud."})

if __name__ == '__main__':
    app.run(debug=True)