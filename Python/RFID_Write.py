import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    text = input('New data:')
    print("Now place your tag onto the RFID RC522 reader")
    reader.write(text)
    print("Written")
    
finally:
        GPIO.cleanup()
        