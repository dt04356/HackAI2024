

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
                newPixel[i] = newPixel[i] & -1 | int(passwordBin[passIndex])
                passIndex += 1
            newPixels.append(tuple(newPixel))

    

    #changes the image to the new image with password incoded
    newImage = Image.new(image.mode, image.size)
    print(newImage == pixelarr)
    
    newImage.save("ChuckblastLOSS.png")

    


saltedPassword()
