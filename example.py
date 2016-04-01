from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask import Flask,request,abort
from models import model
import json
from flask_socketio import SocketIO,send,emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

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

@socketio.on('my update')
def test_message(message):
    response = dustbin()
    emit('update', response)

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
    socketio.run(app,host="0.0.0.0",port=5000)
