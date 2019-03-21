# Text-Based-Python-Game
This program is a lord of the Rings text based adventure game.
It was written using python and was the final project in my python class.

My algorithm looked something like this:
- 1.Create a menu for the user to select from
	- Create a new character
	- Learn the rules of the game
	- Load a previous character
  - Quit
  - Check the user’s response nad make sure it doesn’t break the game
  
- 2.Rules
  - Your character starts out with 20 hp
  - Your character’s race is determined upon creation.  Racials modify the game.
  - You are surrounded by ORCS!  You will fight through the vast tide of orcs. 
  - You can run but you can’t hide.  IF you run you get healed by a healer.  Otherwise you fight.
  - If you need to quit, you can save your character and replay the game as this character
- 3.Load up a previous character
	- Load up the characters information in a particular and unaltered order.
	- E.g. character (name, hp, potion, race)
- 4.Check if the character file exists
  - If it does – start the game
  - If it doesn’t – tell user that the file wasn’t found and ask again. 
- 5.If the user wants to quit, exit the program successfully.
- 6.Create a new Character
  - Ask the User for a name for the character
	- Ask the user the race of the character
	  - Display the racials for the user to decide
	  - Save this choice / modify the user’s gameplay
  - Start the game
- 7.Playing the game
  - Some flavor text is shown then the user is given a battle menu.
- 8.Battle menu
  - Fight / Attack
	  - Base percentage for attacks is 65% hit, 35% chance miss. User tries to hit,Then the orc tries to hit
	  - Show the HP of the Hero
	  - Show battle menu
    
 - Use a potion
   - Check and see if the user has any potions
   - If they do they can use on
   - If not, give them a message saying they’re out of potions
   
 - Run away 
   - 20% chance to successfully run away.
   - If you run away, healer heals the player for 10 hp
   - If you fail, the orc gets an attack on you and you still fight the same orc
    - On a successful fight, we ask the user if they want to save
	   - If they don’t, they fight the next orc
  - Once the user has fought 4 orcs then he/she will fight an uruk-kai 



This project took me a week to complete and is one of my favorite progams I have written

    

