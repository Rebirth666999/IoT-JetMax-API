import time
#import hiwonder

#jetmax = hiwonder.JetMax()
#sucker = hiwonder.Sucker()
#hiwonder.pwm_servo1.set_position(90,0.1)

STATUS_INIT= 0
STATUS_IDLE= 1
STATUS_BUSY= 2
STATUS_WORKING= 3
STATUS_FAULT= 4

status = STATUS_INIT
a=0
b=-163
c=213
capture = False

class control:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def arm_home(self):
        global a,b,c
        a=0
        b=-163
        c=213
        #jetmax.set_position((a, b, c), 2)
        time.sleep(2)
        is_ok=True
        return is_ok

    def get_status(self):
        return status

    def get_head_pos(self):
        global a,b,c
        return [a,b,c]

    def get_capture(self):
        return capture

    def suck(self):
        global status,capture
        status=STATUS_WORKING
        #sucker.set_state(True)
        time.sleep(1)
        status=STATUS_IDLE
        capture=True
        is_ok = True
        return is_ok

    def put(self):
        global status,capture
        status=STATUS_WORKING
        #sucker.release(3)
        time.sleep(1)
        status=STATUS_IDLE
        capture=False
        is_ok = True
        return is_ok

    def move_head(self,x,y,z):
        global a,b,c,status
        a=x
        b=y
        c=z
        status=STATUS_WORKING
        #jetmax.set_position((a, b, c), 2)
        time.sleep(2)
        status=STATUS_IDLE
        is_ok = True
        return is_ok

test=control(a,b,c)
print('status =',status)
print('head_pos =',test.get_head_pos())
print('capture =',test.get_capture())