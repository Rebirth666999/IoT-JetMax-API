from flask import Flask, jsonify, request
import time
import hiwonder

app=Flask(__name__)

jetmax = hiwonder.JetMax()
sucker = hiwonder.Sucker()
hiwonder.pwm_servo1.set_position(90,0.1)

@app.route('/suck',methods=['GET'])
def suck():

    sucker.set_state(True)
    time.sleep(1)
    
    is_ok=True
    return jsonify(is_ok=is_ok)

@app.route('/put',methods=['GET'])
def put():

    sucker.release(3)
    time.sleep(1)

    is_ok=True
    return jsonify(is_ok=is_ok)

@app.route('/move_head',methods=['POST'])
def move_head():

    my_json=request.get_json()
    pos=my_json.get('pos')

    x=pos[0]
    y=pos[1]
    z=pos[2]

    print(x,y,z)
        
    jetmax.set_position((x,y,z),2)	
    time.sleep(2)

    is_ok=True
    return jsonify(is_ok=is_ok)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
