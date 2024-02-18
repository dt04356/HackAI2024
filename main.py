import application
import imageTesting

def main():
    s=input('Enter parts of an image: ')
    pas = input('Enter your password to be encrypted: ')
    url = application.pullImage(s)
    imageTesting.saltedPassword(url,pas)
    imageTesting.unsaltPassword()

main()
    