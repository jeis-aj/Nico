#import necessary libraries
from gpiozero import LED, Button, MotionSensor, Buzzer 
import smtplib
from time import sleep
from email.mime.text import MIMEText

#create objects to refer to each LED, the button, and the PIR sensor
led = LED(17)
pir = MotionSensor(20)
button = Button(16)
buzzer = Buzzer(27)

#Create Alarm State by default it off.
Alarm_state = False

#replace the next three lines with your credentials
from_email_addr = 'piraspberry364@gmail.com'
from_email_password = 'Asqw@3254'
to_email_addr = 'pir55452@gmail.com'

#set your email message
body = 'Raspberry Pi Alert: Motion is detected in your room.'
msg = MIMEText(body)

#set sender and recipient
msg['From'] = from_email_addr
msg['To'] = to_email_addr

#set your email subject
msg['Subject'] = 'INTRUDER ALERT..!!'

while True:

    if button.is_pressed:
        Alarm_state = True
        print('Alarm ON')

    if Alarm_state == True:
        led.on()
        sleep(1)
        if pir.motion_detected == True:
            print('motion detected')
            buzzer.beep()
            sleep(1)
            buzzer.off()
            led.off()
            #connecting to server and sending email
            #edit the following line with your provider's SMTP server details
            server = smtplib.SMTP('smtp.gmail.com', 587)
            #comment out the next line if your email provider doesn't use TLS
            server.starttls()
            server.login(from_email_addr, from_email_password)
            server.sendmail(from_email_addr, to_email_addr, msg.as_string())
            server.quit()
            print('Email sent')
            Alarm_state = False
