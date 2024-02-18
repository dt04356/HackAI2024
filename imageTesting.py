

from PIL import Image
import urllib.request

def saltedPassword(url,password): # (image_path, password) password instead of testpassword
    
    # takes the generated URL from OPENAI
    img_url = url
    urllib.request.urlretrieve(img_url,"new_image.png")


    # Open the image from file
    image = Image.open("new_image.png")
    # Create a listed formation of the image
    pixelarr = list(Image.Image.getdata(image))

    # Tested password
    testpassword = password
    # Adding a random character ~ to the password to designate an end password for unsalting
    testpassword = testpassword+"~"

    #convert password to binary
    passwordBin = ''.join(format(ord(i), '08b') for i in testpassword)

    #modify a bit of each pixel to encode the password
    newPixels = []
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
    newImage.putdata(newPixels)
    newImage.save("SaltedImage.png")




# Function to unsalt the password image we salted
def unsaltPassword():
    # Opening the salted image from the saltpassword function
    image = Image.open("SaltedImage.png")

    # Pulling the data
    pixelsArr = Image.Image.getdata(image)

    # Prepping the password bin for unsalting
    passwordBin = ''

    # Undoing the bitwise operation process from salting 
    for pixel in pixelsArr:
        for i in range(3):
            passwordBin += str(pixel[i] & 1)

    # Checking for the tilde operator to end str casting
    password = ''
    for i in range(0,len(passwordBin), 8):
        if chr(int(passwordBin[i:i+8], 2)) == '~':
            break
        else:
            password += "".join(chr(int(passwordBin[i:i+8], 2)))

    # Printing the original password
    print("Your Password: " + password)

   
# Calling the methods


