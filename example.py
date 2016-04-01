from flask import Flask, render_template,send_from_directory
from flask_socketio import SocketIO, emit
from flask import Flask,request,abort
from models import model
import json
from flask_socketio import SocketIO,send,emit
from qrcode import *
import os
import string
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
app.config['UPLOAD_FOLDER'] = 'uploads/'

@app.route('/api/get_dustbins')
def get_dustbins():
    dustbins = model.dustbin_data.objects()
    dict = []
    for d in dustbins:
        data = {}
        for key in d:
           data[key] = str(d[key])
        dict.append(data)
    return json.dumps(dict)

@app.route('/api/getQRCODE')
def getQR():
    rand = id_generator()
    qr = QRCode(version=20, error_correction=ERROR_CORRECT_L)
    qr.add_data(rand)
    qr.make()
    im = qr.make_image()
    im.save(os.path.join(app.config['UPLOAD_FOLDER'],rand+'.jpg'))
    return send_from_directory(app.config['UPLOAD_FOLDER'],rand+'.jpg')


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

@socketio.on('update trash')
def update_trash(id,completeness):
    response = dustbin(id,completeness)
    import pdb; pdb.set_trace()
    emit('update trash', str(response), broadcast=True)

def dustbin(id,completeness):
    try:
        import pdb;pdb.set_trace()
        dustbin_object = model.dustbin_data.objects(id=id)
        if len(dustbin_object) < 0:
            abort(400)
        dustbin_object = dustbin_object[0]
        dustbin_object.completeness = completeness
        dustbin_object.save()
        send("hello",namespace='/chat')
        data = {}
        for key in dustbin_object:
           data[key] = str(d[key])
        return data
    except Exception as e:
        return e

if __name__ == '__main__':
    app.host = "0.0.0.0"
    app.debug = True
    socketio.run(app,host="0.0.0.0")
