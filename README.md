Messing around with saving and game states - menu, in game, etc.~~ 

To Do:
* Player UI, such as health bar and weapon showcase on main screen
* Basic animations 
* Linked to this, AI
* Need to move some spritesheet loading to the main game.py file in order to help with performance later.
* Need to fix spritesheet divisors to be of their own list. 
* I NEED player UI to be done sooner rather than later. Order of priority is spritesheet -> attack -> UI -> console.  
* Rewrite widgets to no longer be image based. 
* Actually new priority list - rewrite/rework most sprites to have a render function and add this into the game. fix any sort of issues where old code is still lurking for no reason, general cleanup. Move files into one another, cut down on unnecessary variables, etc. Make sure names are as short as possible and understandable. Redraw the mainmap, I dislike this current one. Once I feel that I've slimmed down the code as best as I can, I'm going to work on some more stuff. Oh, and fix the bug where the collision hitbox for the exit is too low. 
* General timeline for these changes is - by weekend finish all code cleanup. Monday is UI, Tuesday/Wednesday is attacks. Thursday/Firday is art + map making. Saturday/Sunday, get some enemies in, get the tests working. 
* note, change how keybinds work in game.py, decently high priority i'll do it after console. also rework the world.py code for the uhh states it's getting long
