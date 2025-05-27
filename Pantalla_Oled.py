#Actividad I2C
from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import time

i2c = busio.I2C(SCL, SDA)
disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
disp.fill(0)
disp.show()
width = disp.width
height = disp.height

def mensajes():
    image = Image.new('1', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    draw.rectangle((1, 1, width-1, height-1), outline=255, fill=0)

    inicio_X = 5
    inicio_Y = 2
    draw.text((inicio_X, inicio_Y+3), 'Integrantes:', font=font, fill=255)
    draw.text((inicio_X, inicio_Y+13), 'Javier Rosas', font=font, fill=255)
    draw.text((inicio_X, inicio_Y+23), 'A01738607', font=font, fill=255)
    draw.text((inicio_X, inicio_Y+33), 'Elian Cantalapiedra', font=font, fill=255)
    draw.text((inicio_X, inicio_Y+43), 'A01738462', font=font, fill=255)

    disp.image(image)
    disp.show()
    time.sleep(5)

    disp.fill(0)
    disp.show()

    image = Image.new('1', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    mensaje = ""
    while True:
        mensaje = str(input("Escribe un mensaje para mostrar en la Raspberry:" ))
        if len(mensaje) <= 50:
            break
    draw.text((inicio_X, inicio_Y+1), mensaje, font=font, fill=255)
    disp.image(image)
    disp.show()

mensajes()
