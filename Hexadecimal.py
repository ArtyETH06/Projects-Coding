#Hexa converter (encode/decode)
letter_temp = ""
number = ["61", "62", "63", "64","65", "66", "67", "68","69", "6a", "6b", "6c", "6d", "6e", "6f", "70","71", "72", "73", "74","75", "76", "77", "78","79", "7a"]
#------------------------------------------------------------------------------On définit les fonctions-----------------------------------------------------------------------------------
#Pour trouver la position d'une lettre 
def position(letter_temp):
  return ord(letter_temp.lower()) - ord('a')


def pos(letter_temp):
    number.index(letter_temp)


def encodeHexa(word):  
    number = ["61", "62", "63", "64","65", "66", "67", "68","69", "6a", "6b", "6c", "6d", "6e", "6f", "70","71", "72", "73", "74","75", "76", "77", "78","79", "7a"]
    final_number = ""
    final_word = ""
    i = 0
    for letter in word:
        letter_temp = word[i]
        #Va cherhcer la position de cette lettre dans le tableau "letter"
        pos = position(letter_temp)
        final_number = number[pos]
        final_word = str(final_word) + str(" ") + str(final_number)  
        i = i + 1

    print(final_word)


def decodeHex(word):
    hexadecimal = {
        "61" : "A",
        "62" : "B",
        "63" : "C",
        "64" : "D",
        "65" : "E",
        "66" : "F",
        "67" : "G",
        "68" : "H",
        "69" : "I",
        "6a" : "J",
        "6b" : "K",
        "6c" : "L",
        "6d" : "M",
        "6e" : "N",
        "6f" : "O",
        "70" : "P",
        "71" : "Q",
        "72" : "R",
        "73" : "S",
        "74" : "T",
        "75" : "U",
        "76" : "V",
        "77" : "W",
        "78" : "X",
        "79" : "Y",
        "7a" : "Z",

    }

    result = ""
    for i, j in zip(word[0::2], word[1::2]):
        result += hexadecimal[i + j]

    return result



#------------------------------------------------------------------------------Utilisation des fonctions-----------------------------------------------------------------------------------

choice = int(input("1--> Encode in hexadécimal| 2--> decode hexadécimal"))

if choice == 1:
    word = input("Quel mot voulez vous encoder ?")
    encodeHexa(word)

elif choice == 2:

    word = input("Quel mot voulez vous décoder ?")
    word = word.replace(" ", "")
    result = decodeHex(word)
    print(result)


else:
    print("Wrong Match Impossible to execute 404")






