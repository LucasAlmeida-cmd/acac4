import os
from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/')
def fibonaci():
    resposta = '0,1,'
    indice1 = 0
    indice2 = 1
    x = [0, 1]
    y = None
    inicio = 0
    resposta1 = 1
    while resposta1 <= 48:
        resposta1 += 1
        y = x[indice1] + x[indice2]
        x.append(y)
        resposta += str(y) + ','
        indice1 += 1
        indice2 += 1

    print(resposta)


fibonaci()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
