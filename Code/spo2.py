
import time
import max30100

def OBP():
    
    mx30 = max30100.MAX30100()
    mx30.enable_spo2()

    mx30.read_sensor()

    mx30.ir, mx30.red

    bp = int(mx30.ir / 100)

    spo2 = int(mx30.red / 100)
    
    if mx30.ir != mx30.buffer_ir :
        print("Blood Pressure: ",bp);
        
    if mx30.red != mx30.buffer_red:
        print("Oxygen: ",spo2);
    return bp, spo2
    




