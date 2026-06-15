from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def get_time():
    # Obtenemos la fecha y hora actual del sistema
    now = datetime.now()
    
    return {
        "status": "success",
        "message": "Servidor Flask activo",
        "current_time": now.strftime("%Y-%m-%d %H:%M:%S")  # Formato: Año-Mes-Día Hora:Minutos:Segundos
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)