import RPi.GPIO as GPIO
from escpos import printer
import random
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 

p = printer.Dummy()
#p = printer.Usb(0x0416, 0x5011, 0, 0x81, 0x03)

COUPON_CHANCE = 0.01

print(f"Coupon chance: {COUPON_CHANCE}")

def button_callback(channel):
    #print('Button was pushed!')
    is_coupon = random.random() < COUPON_CHANCE
    if is_coupon:
        p.image(f'/home/pi/Documents/thermalprinter-pi/assets/BON_COUPON.jpg')
        print('Coupon printed!')
    else:
        random_draw = random.randint(1,10)
        p.image(f'/home/pi/Documents/thermalprinter-pi/assets/BON_THESE_{random_draw}.jpg')
        print(f'Thesis {random_draw} printed!')
    
    #print(p.output)


GPIO.add_event_detect(10,GPIO.RISING,callback=button_callback,bouncetime=2000)

def main():
    p.text("Start Machine\n")
    print(p.output)
    
    message = input("Press enter to quit\n\n")
    GPIO.cleanup()


if __name__ == "__main__":
    main()