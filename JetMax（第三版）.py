from flask import Flask, jsonify, request
import time
import hiwonder

app=Flask(__name__)

jetmax = hiwonder.JetMax()
sucker = hiwonder.Sucker()
hiwonder.pwm_servo1.set_position(90,0.1)

def arm_home():
    jetmax.go_home()
    time.sleep(2)

class JetMax:
    
    EQUIPMENT_ID = 'JetMax000001'

    # 设备的状态码
    STATUS_INIT: int = 0
    STATUS_IDLE: int = 1
    STATUS_BUSY: int = 2
    STATUS_WORKING: int = 3
    STATUS_FAULT: int = 4

    def __init__(self):
        self.status: int =self.STATUS_INIT
        self.head_pos: list[float] = []
        self.capture: bool = False
        arm_home()

    def get_status(self):
        return self.status

    def get_head_pos(self):
        return self.head_pos

    def get_capture(self):
        return self.capture

    def suck(self):
        sucker.set_state(True)
        time.sleep(1)

        is_ok = True
        return jsonify(is_ok=is_ok)

    def put(self):
        sucker.release(3)
        time.sleep(1)

        is_ok = True
        return jsonify(is_ok=is_ok)

    def move_head(self):
        my_json = request.get_json()
        pos = my_json.get('pos')

        x = pos[0]
        y = pos[1]
        z = pos[2]

        print(x, y, z)

        jetmax.set_position((x, y, z), 2)
        time.sleep(2)

        is_ok = True
        return jsonify(is_ok=is_ok)





if __name__ == '__main__':
    Jet_Max = JetMax()
