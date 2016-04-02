from flask import Flask,request,abort
from models import model
import json
from flask_socketio import SocketIO,send,emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

@app.route('/api/dustbin',methods=['POST'])
def dustbin():
    try:
        import pdb;pdb.set_trace()
        id = request.args.get('id',None)
        completeness = request.args.get('per')
        dustbin_object = model.dustbin_data.objects(id=id)
        if len(dustbin_object) < 0:
            abort(400)
        dustbin_object = dustbin_object[0]
        dustbin_object.completeness = completeness
        dustbin_object.save()
        send("hello",namespace='/chat')
        return "success"
    except:
        abort(400)

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

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
