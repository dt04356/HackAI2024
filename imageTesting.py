

from PIL import Image

def saltedPassword(): # (image_path, password) password instead of testpassword
    #open the image and get its data
    image = Image.open("/Users/jasonburghart87/Downloads/Chuckblast.png")
    pixelarr = list(Image.Image.getdata(image))

    testpassword = "campustheboulderderek"

    #convert password to binary
    passwordBin = ''.join(format(ord(i), '08b') for i in testpassword)

    #modify a bit of each pixel to encode the password
    newPixels= []
    passIndex = 0
    for pixel in pixelarr:
        newPixel = list(pixel)
        for i in range(3): #for RGB channel
            if passIndex < len(passwordBin):
                newPixel[i] = newPixel[i] & ~1 | int(passwordBin[passIndex])
                passIndex += 1
        newPixels.append(tuple(newPixel))

    

    #changes the image to the new image with password incoded
    newImage = Image.new(image.mode, image.size)
    newImage.save("ChuckblastLOSS.png")

    # for i in range(100):
    #     #print("pixelArr: " + str(pixelarr[i]) + "         newPixels: " + str(newPixels[i]))




def unsaltPassword():

    image = Image.open("/Users/jasonburghart87/HackAI2024/ChuckblastLOSS.png")


    pixelsArr = Image.Image.getdata(image)


    passwordBin = ''
    for pixel in pixelsArr:
        for i in range(3):
            passwordBin += str(pixel[i] & 1)

    password = ''.join(chr(int(passwordBin[i:i+8], 2)) for i in range(0, len(passwordBin), 8))

    print(password)








saltedPassword()
unsaltPassword()
