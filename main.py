
from os import system, name 

import random
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def replay():
   rejouer = input('Vous voulez rejouer O/N :')
   if rejouer == "o" or rejouer == "O":
         hangman()
   elif rejouer == "n" or rejouer == "N":
         exit()
         clear()
   else:
      print('Veuillez recommencer entrer O ou N')
      replay()

def hangman():
   clear()
   with open('liste_francais.txt', 'r') as f:
      words = f.readlines()
   w = random.choice(words)[:-1]
   i =0
   g = 1
   word = ''
   list = []
   mainlist = []
   guessed = False
   letter = []
   print (f"Le mot est composé de {len (w)} lettres")
   while guessed == False and g <= 10:      
      l = input('Veuillez entrer une lettre : ')
      mainlist.append (l.upper ())
      listLetter = "-".join(mainlist)
      print(listLetter)
      if l not in w:
      
         if g == 1 :
                                          print(f""" 
                                                      
                                             ______   
                                                            """)
         elif g == 2 :
                                          print ("""
                                                |
                                                |
                                                |
                                                |
                                                |
                                                |
                                                |
                                                |
                                             ___|___""")
         elif g == 3:
               print ("""
                                                +++++++
                                                |     
                                                |         
                                                |        
                                                |
                                                |
                                                |
                                                |
                                             ___|___""")
         elif g == 4:
                  print ("""
                                                +++++++
                                                |     |
                                                |         
                                                |        
                                                |
                                                |
                                                |
                                                |
                                             ___|___""")

         elif g == 5:
                  print ("""
                                                +++++++
                                                |     |
                                                |     O      
                                                |        
                                                |
                                                |
                                                |
                                                |
                                             ___|___""")
         elif g == 6:
                  print ("""
                                                +++++++
                                                |     |
                                                |    \\O      
                                                |        
                                                |
                                                |
                                                |
                                                |
                                             ___|___""")

         elif g == 7:
                  print ("""
                                                +++++++
                                                |     |
                                                |    \\O/      
                                                |        
                                                |
                                                |
                                                |
                                                |
                                             ___|___""")
         elif g == 8:
                  print ("""
                                                +++++++
                                                |     |
                                                |    \\O/      
                                                |     |       
                                                |     |
                                                |
                                                |
                                                |
                                             ___|___""")
         elif g == 9:
                  print ("""
                                                +++++++
                                                |     |
                                                |    \\O/      
                                                |     |       
                                                |     |
                                                |    /
                                                |
                                                |
                                             ___|___""")
         elif g == 10:
                  print ("""
                                                +++++++
                                                |     |
                                                |    \\O/      
                                                |     |       
                                                |     |
                                                |    / \\
                                                |
                                                |
                                             ___|___
                                       Vous avez perdu le mot est """+w)
         g += 1
         if g > 10:
           replay()

      else:            
            list.append(l.lower())
               # list.sort()
            word = ''   
            if guessed == False: 
               for l in w.lower():                        
                  if l in list:                  
                     word += l                                 
                  else:
                     word +=' _'
               print(word)
            if word == w:
               print (' ')
               print (f"Bravo vous avez trouver le mot {w} !")
               print (' ')
               replay()
                     
hangman() 


