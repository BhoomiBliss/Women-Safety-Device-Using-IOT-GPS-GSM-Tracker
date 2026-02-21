import serial
import time 
ser = serial.Serial(
   port='/dev/ttyUSB0',  #ttyAMA0 ttyS0 ttyUSB0
   baudrate = 9600,
   parity=serial.PARITY_NONE,
   stopbits=serial.STOPBITS_ONE,
   bytesize=serial.EIGHTBITS,
   timeout=1
)
def getResponse(cmd,reply,timeout):    
    cmd = cmd + '\r'
    print('CPU'+':'+cmd)
    ser.write(bytes(cmd,'utf-8'))
    time.sleep(0.01)
    for i in range (0,timeout):
        in_msg=ser.readline()
        in_msg = in_msg.decode('utf-8').strip()
        time.sleep(0.01)
        ans=in_msg.find(reply)
        if(ans!=-1):
            i=timeout             
    print('GSM'+':'+in_msg)       
    time.sleep(0.5)
    
def gsmPrint(cmd,timeout):
    cmd = cmd + '\r'
    print('CPU'+':'+cmd)
    ser.write(bytes(cmd,'utf-8'))
    time.sleep(0.01)
    for i in range (0,timeout):
        in_msg=ser.readline()
        in_msg = in_msg.decode('utf-8').strip()
        time.sleep(0.01)        
        if(len(in_msg)>0): #someting on reply
            i=timeout
    print('GSM'+':'+in_msg)       
    time.sleep(0.5)
    
def gsmEndcommand():
    ser.write(bytes(chr(26),'utf-8'))
    time.sleep(1)
    in_msg=ser.readline()
    in_msg = in_msg.decode('utf-8').strip()
    print('GSM'+':'+in_msg)
    time.sleep(1)
      

def SendMessage(Num, msg):
#     getResponse(f'ATD{Num};','OK',2)    
    getResponse('AT','OK',2)
    getResponse('AT+CMGF=1','OK',2)
    getResponse(f'AT+CMGS=\"{Num}\"','OK',2)#put your number replacing 'xxxxxxxxxxxxx'
    gsmPrint(msg,2)
    gsmEndcommand()

