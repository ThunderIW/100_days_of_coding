print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇

choice_1 = str(input("You're at a cross road. Where do you want to go ?\n  'left' or 'right'?\n")).lower()

if choice_1 == 'right':
    print('You fell into a hole. Game Over')

if choice_1 == 'left':
    choice_2 = str(input("You've come to a lake. There is an island in the middle of the lake.\n Type 'wait' to wait "
                         "for a boat. Type 'swim' to swim across the lake\n")).lower()
    if choice_2 == 'wait':
        print('''
      ______________
    |\ ___________ /|
    | |  _ _ _ _  | |
    | | | | | | | | |   
    | | |-+-+-+-| | |
    | | |-+-+=+%| | |
    | | |_|_|_|_| | |
    | |    ___    | |
    | |   [___] ()| |
    | |           | |
    | |         ||| |
    | |         ()| |
    | |           | |
    | |           | |
    | |           | |
    |_|___________|_|  

        ''')
        choice_3 = str(input("you arrive at the island unharmed. There is a house with 3 doors.\n One red, one yellow, "
                             "and one blue. which colour door do you choose\n ")).lower()
        if choice_3 == 'blue':
            print('''
             ,                   \,       '-,-`,'-.' | ._
               /|           \    ,   |\         }  )/  / `-,',
               [ '          |\  /|   | |        /  \|  |/`  ,`
               | |       ,.`  `,` `, | |  _,...(   (      _',
                \  \_\,``,   ` , ,  /  |         )         _,/
                 \  '  `  ,_ _`_,-,<._.<        /         /
                  ', `>.,`  `  `   ,., |_      |         /
                    \/`  `,   `   ,`  | /__,.-`    _,   `\
                -,-..\  _  \  `  /  ,  / `._) _,-\`       \
                 \_,,.) /\    ` /  / ) (-,, ``    ,        |
                ,` )  | \_\       '-`  |  `(               \
               /  /```(   , --, ,' \   |`<`    ,            |
              /  /_,--`\   <\  V /> ,` )<_/)  | \      _____)
        ,-, ,`   `   (_,\ \    |   /) / __/  /   `----`
       (-, \           ) \ ('_.-._)/ /,`    /
       | /  `          `/ \\ V   V, /`     /
    ,--\(        ,     <_/`\\     ||      /
   (   ,``-     \/|         \-A.A-`|     /
  ,>,_ )_,..(    )\          -,,_-`  _--`
 (_ \|`   _,/_  /  \_            ,--`
  \( `   <.,../`     `-.._   _,-`
   `                      ```
            ''')
            print('As you open the Blue door you see a looming monster and he attacks who tearing you to shreds, '
                  'Game Over')
        elif choice_3 == 'yellow':
            print("As you open the door you see what seem to be chest as you approached it you see what looks to be a "
                  "pile of gold, you win")

        elif choice_3 == 'red':
            print('''
                       O 
                      /|  
                     / \  


               (  .      )
           )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
 jgs^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            ''')
            print("As you open door you fall downwards into a pit of fire leading to you being burnt alive")
        else:
            print('You stand there pounding to yourself why is there no door, Game Over')
    if choice_2 == 'swim':
        print('As you swimming across the water you attacked by a trout leading to your death, Game Over')
else:
    print('You fell into a hole. Game Over')





