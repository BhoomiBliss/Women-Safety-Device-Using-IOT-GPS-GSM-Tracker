import RPi.GPIO as GPIO
import time
import cv2
from gsm import SendMessage

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

SW = 26
HR_SENSOR = 12
tempFlag = 0
bpFlag = 0
hrFlag = 0
GPIO.setup(HR_SENSOR,GPIO.IN)
GPIO.setup(SW,GPIO.IN)

def HEART_BEAT():
     global tempFlag
     global bpFlag
     global hrFlag
     tempFlag = 0
     bpFlag   = 0
     hrFlag   = 1
     if hrFlag == 1 :
      print('Hold The finger On sensor')
      #time.sleep(1) 
      sensorCounter = 0
      startTime     = 0
      endTime       = 0
      rateTime      = 0
      while sensorCounter < 1 and  hrFlag == 1:
        if (GPIO.input(HR_SENSOR)):
          if sensorCounter == 0:
            startTime = int(round(time.time()*1000))
            #print startTime
          sensorCounter = sensorCounter + 1
          #print sensorCounter
          while(GPIO.input(HR_SENSOR)):
            if hrFlag == 0:
              break
            pass

      time.sleep(1)      
      endTime  = int(round(time.time()*1000))
      #print endTime
      rateTime = endTime - startTime
      #print rateTime
      rateTime = rateTime / sensorCounter
      heartRate = (60000 / rateTime) #/ 3 
      heartRate = abs(heartRate)
      heartRate=int(heartRate+20)
      print ('heartRate : ', heartRate)
      return heartRate

import smtplib
from email.message import EmailMessage
def send_email_attach(from_email_addr, from_email_pass, to_email_addr, subject, body, attachment_path):
    # Create an EmailMessage object
    msg = EmailMessage()
    msg.set_content(body)
    msg['From'] = from_email_addr
    msg['To'] = to_email_addr
    msg['Subject'] = subject

    # Add attachment if provided
    if attachment_path:
        with open(attachment_path, 'rb') as attachment:
            # Read the attachment and add it to the message
            msg.add_attachment(attachment.read(), maintype='image', subtype='octet-stream', filename=attachment_path.split('/')[-1])
    
    # Connect to the SMTP server and send the email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email_addr, from_email_pass)
    server.send_message(msg)
    server.quit()

def Capture():
    vs = cv2.VideoCapture(0)
    counts = 0
    counter = 0
    while True:
        ret, img = vs.read()
        if not ret:
            print('camera not recognised')
        counter += 1
        if counter > 5:
            counts += 1
            cv2.imwrite('frame'+str(counts)+'.png', img)
        cv2.imshow('streaming', img)
        if cv2.waitKey(1000) & 0xFF == ord('q'):
            break
        if counts > 4:
            break
    vs.release()
    cv2.destroyAllWindows()
    
    f = open('location.txt', 'r')
    loc = f.read()
    f.close()
    lat, long = loc.split(',')
    print('lat : ', lat, 'long : ', long)
    
    msg = f"Emergency at https://www.google.com/maps/search/?api=1&query={lat},{long}"
    SendMessage(8951298296, msg)
    SendMessage(9535435250, msg)
    SendMessage(7483678483, msg)
    SendMessage(8073632100, msg)
    for counts in range(1, 6):
        send_email_attach('sinchanaka269@gmail.com', 'ompm swmh xmom uutc', 'thanmayigowda174@gmail.com', 'Alert', f'Emergency at https://www.google.com/maps/search/?api=1&query={lat},{long}, check below attachment', 'frame'+str(counts)+'.png')
        send_email_attach('sinchanaka269@gmail.com', 'ompm swmh xmom uutc', 'Yashudevadiga2003@gmail.com', 'Alert', f'Emergency at https://www.google.com/maps/search/?api=1&query={lat},{long}, check below attachment', 'frame'+str(counts)+'.png')
        send_email_attach('sinchanaka269@gmail.com', 'ompm swmh xmom uutc', 'bhoomikasshetty2020@gmail.com',  'Alert', f'Emergency at https://www.google.com/maps/search/?api=1&query={lat},{long}, check below attachment', 'frame'+str(counts)+'.png')
    
def Emergency():
    if GPIO.input(SW) == False:
        print('Emergency')
        Capture()
        


