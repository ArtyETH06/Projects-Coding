#Les imports
import urllib.request
import pandas as pd
from bs4 import BeautifulSoup as bs
from PIL import Image
from pytesseract import pytesseract
from PIL import Image
from operator import itemgetter
import requests
import os


#-------------------------------------------------------------------------------------------Début-------------------------------------------------------------------------------
#Clear auto du terminal (trop usefull)
os.system('cls||clear')
#-------------------------------------------------------------------------------------------Fonctions-------------------------------------------------------------------------------

#Pour passer de l'URL à une image
def url_to_image(prod_final2):
    urllib.request.urlretrieve(
    prod_final2,
    "test.gif")
    img = Image.open("test.gif")
    img.save("test.gif")
    #img.show()



#Pour avoir une image plus lisible par Tesseract
def img_clear():
    #Conversion pour que ce soit +lisible
    im = Image.open("test.gif")
    im = im.convert("P")
    im2 = Image.new("P",im.size,255)
    im = im.convert("P")

    temp = {}

    for x in range(im.size[1]):
        for y in range(im.size[0]):
            pix = im.getpixel((y,x))
            temp[pix] = pix
            
            if pix != 0 or pix !=255:
                im2.putpixel((y,x),1)
            if pix > 1:
                im2.putpixel((y,x),255)
            if  130 < pix < 255:
                im2.putpixel((y,x),0)


    im2.save("test.gif")




#Affiche l'histogramme
def img_hist():
    im = Image.open("test.gif")
    im = im.convert("P")
    print (im.histogram())



#Voir les couleurs les plus fréquentes
def img_color():
    im = Image.open("test.gif")
    im = im.convert("P")
    his = im.histogram()

    values = {}

    for i in range(256):
        values[i] = his[i]

    for j,k in sorted(values.items(), key=itemgetter(1), reverse=True)[:10]:
        print (j,k)



#Pour passer de l'image à une 'string' pour pouvoir exploiter la donnée
def image_to_text():
    #Define path to tessaract.exe
    path_to_tesseract = r'C:\Program Files\Tessercat-OCR\tesseract.exe'
    #Define path to image
    path_to_image = 'test.gif'
    #Point tessaract_cmd to tessaract.exe
    pytesseract.tesseract_cmd = path_to_tesseract
    #Open image with PIL
    img = Image.open(path_to_image)
    #Extract text from image
    text = pytesseract.image_to_string(img)
    text = text.replace(" ","")
    #print("Captcha:\n", text)
    return text





def get_contenu():
    cookie = requests.Session()
    url = "The link where the Cpatcha is"
    page = cookie.get(url)
    soup = bs(page.text, features="html.parser")
    soup
    prod= soup.find_all('img')
    prod
    #On "convertit" prod en str
    prodStr = str(prod)
    #Enlever la balise <img>
    prod_final = prodStr.replace('[<img src="', "")
    prod_final2 = prod_final.replace('"/>]', "")
    url_to_image(prod_final2)
    img_clear()
    text = image_to_text()
    text2 = text.replace('\n', '')
    text_final = text2.replace(' ', '')
    cametu = text_final
    response2 = cookie.post(url, data = {"The name of the placeholder": cametu})

    print("----------------------------------------------------------------------------------Data-------------------------------------------------------------------------------")
    print("Captcha:\n --> ", cametu,"\nStatut:\n --> ", response2)

    print("---------------------------------------------------------------------------Contenu de la page------------------------------------------------------------------------\n", response2.text )


    
#-------------------------------------------------------------------------------------------Call des fonctions-------------------------------------------------------------------------------

get_contenu()

#-------------------------------------------------------------------------------------------Données des pixels-------------------------------------------------------------------------------

# Blanc (0) -> 11147
# Vert (127) -> 399 ?
# Noir (140) -> 216 ?