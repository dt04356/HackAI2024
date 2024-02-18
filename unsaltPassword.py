
from PIL import Image

def unsaltPassword():
    
    image = Image.open("/Users/jasonburghart87/HackAI2024/ChuckblastLOSS.png")


    pixelsArr = Image.Image.getdata(image)


    passwordBin = ''
    for pixel in pixelsArr:
        for i in range(3):
            passwordBin += str(pixel[i] & 1)

    password = ''.join(chr(int(passwordBin[i:i+8], 2)) for i in range(0, len(passwordBin), 8))

    print(password)