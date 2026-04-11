from flask import Flask, jsonify, request
import JetMax

app=Flask(__name__)

@app.route('/init',methods=['GET'])
def init():
    return jsonify(is_ok=JetMax.test.arm_home())

@app.route('/suck', methods=['GET'])
def suck():
    return jsonify(is_ok=JetMax.test.suck())

@app.route('/put', methods=['GET'])
def put():
    return jsonify(is_ok=JetMax.test.put())

@app.route('/move_head', methods=['POST'])
def move_head():
    myjson = request.get_json()
    pos=myjson.get('pos')
    x=pos[0]
    y=pos[1]
    z=pos[2]
    return jsonify(is_ok=JetMax.test.move_head(x,y,z))

@app.route('/get_status', methods=['GET'])
def get_status():
    return jsonify(JetMax.test.get_status())

@app.route('/get_head_pos', methods=['GET'])
def get_head_pos():
    return jsonify(pos=JetMax.test.get_head_pos())

@app.route('/get_capture', methods=['GET'])
def get_capture():
    return jsonify(JetMax.test.get_capture())

if __name__ == '__main__':
    app.run(host='0.0.0.0')
