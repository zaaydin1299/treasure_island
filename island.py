print("Welcome to Treasure Island , you/n're mission is find the treasure.")
choice1 = input('You are at a crossroads, which way do you want to go, "left" or "right"?').lower()
if choice1 == "left":

   choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.' ).lower()
   if choice2 == "wait": 

    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure island! YOU WİN!")
    elif choice3 == "blue":
      print("It's a room full of water. Game over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
   else:
    print("You get attacked by an angry trout. Game Over.") 
else:
 print("You fell into a hole. Game Over.")             

