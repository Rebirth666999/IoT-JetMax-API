from flask import Flask, jsonify, request
import JetMax

app=Flask(__name__)

@app.route('/Init',methods=['GET'])
def Init():
    return jsonify(is_ok=JetMax.test.ArmHome())

@app.route('/Suck', methods=['GET'])
def Suck():
    return jsonify(is_ok=JetMax.test.Suck())

@app.route('/Put', methods=['GET'])
def Put():
    return jsonify(is_ok=JetMax.test.Put())

@app.route('/MoveHead', methods=['POST'])
def MoveHead():
    myjson = request.get_json()
    pos=myjson.get('pos')
    x=pos[0]
    y=pos[1]
    z=pos[2]
    return jsonify(is_ok=JetMax.test.MoveHead(x,y,z))

@app.route('/GetStatus', methods=['GET'])
def GetStatus():
    return jsonify(JetMax.test.GetStatus())

@app.route('/GetHeadPos', methods=['GET'])
def GetHeadPos():
    return jsonify(pos=JetMax.test.GetHeadPos())

@app.route('/GetCapture', methods=['GET'])
def GetCapture():
    return jsonify(JetMax.test.GetCapture())

if __name__ == '__main__':
    app.run(host='0.0.0.0')
