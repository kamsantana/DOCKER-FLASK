from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return {"status": "success", "message": "¡Hola Mundo desde Flask, Docker y GitHub Actions!"}

if __name__ == '__main__':
    # El host 0.0.0.0 es obligatorio para que Docker pueda redirigir el puerto
    app.run(host='0.0.0.0', port=5000)