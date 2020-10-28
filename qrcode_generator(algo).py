#pip install qrcode
import qrcode
img=qrcode.make("https://www.google.com/webhp?authuser=1") #it will make it
img
#for saving it
img.save("google.jpg")