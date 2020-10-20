import os
from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/')
def ac4():  
    pro = 1 
    ant = 0 
    limite = 50
    f = 0   
    r = "0, "
    while (f < limite):
        x = pro 
        pro = pro + ant 
        ant = x 
        f = f + 1  
        r += str(pro) + ',' 
    
    return r 
if __name__ == "__main__":
    port = int(os.envinon.get("PORT", 5000))
    app.run(host"0.0.0.0", port=port)
