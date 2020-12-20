import requests
import os

s = requests.Session()
s.verify = '/home/naquib/Desktop/individualproject/cert.pem'
clear = lambda: os.system('clear')
       
class choice:
    def start(self):
        clear()
        print("Hello. What Are you trying to fetch? \n1. Response Code from Website\n 2.Download image from website\n\n0.Exit System ")        
        x = int(input("\nPlease Enter Your Input: "))

        if x==1:
            clear()
            y=input('Response Code Menu\n\nPlease enter the URL: ')
            r = requests.get(y
        , verify='/home/naquib/Desktop/cert/cert.pem')
            print(r)
            b=int(input("\nEnter 0 to return Main Menu\n"))
            if b==0:
                choice.start(com1)
            else:
                quit()

        if x==2:
            clear()
            y=input('Image Downloader Menu\n\nPlease enter the URL: ')
            r = requests.get(y
        , verify='/home/naquib/Desktop/cert/cert.pem')
            print('\nImage Data Recieved')
            z=input('\nPlesae enter the file name: ')
            with open(z, 'wb') as f:
                f.write(r.content)
            print("\nSaved as: ", z)   
            b=int(input("\nEnter 0 to return Main Menu\n"))
            if b==0:
                choice.start(com1)
            else:
                quit()


        if x==0:
            print('See you later')
            quit()
            
        else:
            clear()
            choice.start(com1) 
            
com1 = choice()
choice.start(com1)            