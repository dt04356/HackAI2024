import application
import GUI
import imageTesting

def main():
    s=input('Enter parts of an image: ')
    pas = input('Enter your password to be encrypted: ')
    url = application.pullImage(s)
    imageTesting.saltedPassword(url,pas)
    imageTesting.unsaltPassword()

GUI.GUI()
main()
    