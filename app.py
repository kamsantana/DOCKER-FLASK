from flask import Flask, render_template_string
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Estructura HTML y CSS visual integrada
    html_template = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Servidor Flask Activo</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }
            body {
                background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                color: #fff;
            }
            .card {
                background: rgba(255, 255, 255, 0.1);
                backdrop-filter: blur(10px);
                border: 1px solid rgba(255, 255, 255, 0.2);
                padding: 3rem;
                border-radius: 20px;
                text-align: center;
                box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
                max-width: 450px;
                width: 90%;
            }
            .icon {
                font-size: 4rem;
                margin-bottom: 1rem;
                animation: pulse 2s infinite;
            }
            h1 {
                font-size: 1.8rem;
                margin-bottom: 0.5rem;
                font-weight: 600;
            }
            .status {
                display: inline-block;
                background: #2ec4b6;
                color: #fff;
                padding: 0.25rem 1rem;
                border-radius: 50px;
                font-size: 0.85rem;
                font-weight: bold;
                text-transform: uppercase;
                margin-bottom: 1.5rem;
                letter-spacing: 1px;
            }
            p {
                color: #e0e0e0;
                font-size: 1rem;
            }
            .time {
                margin-top: 1.5rem;
                font-size: 1.1rem;
                font-weight: bold;
                background: rgba(0, 0, 0, 0.2);
                padding: 0.75rem;
                border-radius: 10px;
                border: 1px solid rgba(255, 255, 255, 0.1);
            }
            @keyframes pulse {
                0% { transform: scale(1); }
                50% { transform: scale(1.05); }
                100% { transform: scale(1); }
            }
        </style>
    </head>
    <body>
        <div class="card">
            <div class="icon">🚀</div>
            <h1>{{ message }}</h1>
            <span class="status">{{ status }}</span>
            <p>Tu aplicación de Flask se encuentra corriendo de forma exitosa dentro de un contenedor Docker.</p>
            <div class="time">
                ⏰ Hora del servidor: <br> <span style="color: #ff9f1c;">{{ current_time }}</span>
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_template, message="Servidor Flask Activo", status="success", current_time=current_time)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)