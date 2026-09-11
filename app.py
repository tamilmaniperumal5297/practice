from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "success",
        "message": "Welcome to the Jungle K8s App!",
        "version": "1.0.0",
        "environment": "Production-K8s"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)