import time
import hiwonder

jetmax = hiwonder.JetMax()
sucker = hiwonder.Sucker()
hiwonder.pwm_servo1.set_position(90,0.1)

STATUS_INIT= 0
STATUS_IDLE= 1
STATUS_BUSY= 2
STATUS_WORKING= 3
STATUS_FAULT= 4

status = STATUS_INIT
a=0
b=-163
c=213
capture = 0

class PArmSuck:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def ArmHome(self):
        global a,b,c,status,capture
        sucker.release(3)
        time.sleep(1)
        capture=0
        status = STATUS_INIT
        a=0
        b=-163
        c=213
        jetmax.set_position((a, b, c), 1)
        time.sleep(1)
        is_ok=True
        return is_ok

    def GetStatus(self):
        return status

    def GetHeadPos(self):
        global a,b,c
        return [a,b,c]

    def GetCapture(self):
        return capture

    def Suck(self):
        global status,capture
        status=STATUS_WORKING
        sucker.set_state(True)
        time.sleep(1)
        capture=1
        is_ok = True
        return is_ok

    def Put(self):
        global status,capture
        sucker.release(3)
        time.sleep(1)
        status=STATUS_IDLE
        capture=0
        is_ok = True
        return is_ok

    def MoveHead(self,x,y,z):
        global a,b,c,status
        a=x
        b=y
        c=z
        status=STATUS_WORKING
        jetmax.set_position((a, b, c), 2)
        time.sleep(2)
        status=STATUS_IDLE
        is_ok = True
        return is_ok

test=PArmSuck(a,b,c)
print('status =',status)
print('HeadPos =',test.GetHeadPos())
print('Capture =',test.GetCapture())
