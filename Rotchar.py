word = input("Quel mot voulez vous encoder ?")
rot = int(input("Quel est la méthode rotchar que vous voulez utiliser (1-26)"))
i = 0
letter_temp = ""
final_word = ""

letter = ["a", "b", "c", "d","e", "f", "g", "h","i", "j", "k", "l","m", "n", "o", "p","q", "r", "s", "t","u", "v", "w", "x","y", "z"]

#Pour trouver la position d'une lettre 
def position(letter_temp):
  return ord(letter_temp.lower()) - ord('a')


  
while i < len(word):
    letter_temp = word[i]
    pos = position(letter_temp)
    print(pos)
    nb_rot = pos + rot
    letter_rot = nb_rot % 26
    letter_rot_final = letter[letter_rot]
    final_word = str(final_word) + str(letter_rot_final)  
    i = i + 1
print(final_word)



