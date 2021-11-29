This is my arkanoid project, run main.py to run it all. Assets holds all of the necessary assets for this to work. See bottom of page for known bugs. 

## TO DO:  

• Revamp end screen - right now it just shows your score, and the highscore - not very nice.  

• BETTER COLLISIONS - Right now, if the ball collides in a particular manner, it can just absolutely tear its way through the center of the block clump. THIS IS NOT INTENTIONAL. However, due the simplicity of the collisions, it was inevitable. As of 29/11/21 this has been mildly fixed, but the ball can still have some strange collisions with the bricks.

• ~~Tweak ball respawning - it can be a little fast at the moment for the user. Maybe make it remain on the paddle untill the user hits space?~~ Completed (29/11/2021)

## **FAQS:**

### *Why did I use so many files?*  

Made debugging easier + I liked the organisation.

### *Why is the code messy in some areas?*  

I got more tired as I continued working on it, so you can see the quality decrease over time. Maybe I'll come back to it. 

### *How do I test specific levels?*  

Change the roundNumber variable in main.py to the level number you want to test. The game will then start on that level. 

### *How do I test powerups?*  

- Go to baseround.py (which is just the round framework) and go to the randomSpawn function.   
- Change the randint(2,10) to randint(7,7) to get a 100% spawn rate when a brick is destroyed.   
- If you want a specific powerup, comment out the " powerup = Powerup(validPowerups[randint(0,len(validPowerups)-1)]) " line   
- Instead, write powerup = Powerup(insert-powerup-name-here), putting the powerup name in the brackets. See notes section below for valid powerup names. 
- You're done! Now your chosen powerup will spawn whenever you break a brick.  

### *How do I adjust enemy spawn rate?*
Head to the bottom of baseround.py. Find the line that says if (time.time() - roundStartTime) >= 25:  - this controls enemy spawn rate. The 25 is how many seconds there are between enemy spawns, and by editing it you can change this. 

### *How do I make my own round?*  

- Create a new text file in textfiles, and name it following the format: round_i.txt , with i being a number. (NOTE: number cannot be greater than the maxRounds variable in main.py. Number can also not match an already existing file )    
- The first row should have 1 number in it - this represents the Y co-ordinate for the first row of bricks.    
- The next rows should each have 13 characters in them. These can be 0 to 9, representing a brick colour (see bottom of this readme for which are which) or "-" , which represents a brick wide gap. If a row isnt 13 characters, it can cause issues in the code - so if you want a gap, you'll have to use "-" to represent it.    
- Once you've completed the file, make sure to save it. Then, go to the notes section below, and check what index (yourRoundNumber-1)%4 is equal to, to see what colour you round background will be, and what enemy will spawn.    
- You're done!     

### *Why the lack of comments in certain areas?*

A lot of parts of my code flow fairly well I feel, and repeat the same logic. There are a lot of areas I should have commented, but I just didn't have the time. 

### *What is loop control? (referenced in comments)*

So, I wanted most of my animations to run at a different FPS to the main game, as I just didnt have the images for it, so I only wanted it to update at a suitable number of frames. To achieve this, I used loop control - a variable that iterates untill it reaches a particular value - this value would be 60 divided by the number of frames i wanted the animation to be. When it hit this value, the next image in the animation list would be loaded, and loopcontrol would be reset.  



## **NOTES:**

### *Brick colour to numbers:*  

0 - BLUE  
1 - CYAN  
2 - GOLD  
3 - GREEN  
4 - ORANGE  
5 - PINK  
6 - RED  
7 - SILVER  
8 - WHITE  
9 - YELLOW  
"-" - NONE

### *Round Colours:*  

0 - DARKBLUE  
1 - DARKGREEN  
2 - LIGHTBLUE  
3 - LIGHTRED  

### *Round Enemies:*  

0 - Cone  
1 - Pyramid  
2 - Molecule  
3 - Cube  

### *Powerup Names:*  
1 - Catch  
2 - Laser  
3 - Duplicate  
4 - Extra life  
5 - Expand  
6 - SLOW




## **KNOWN BUGS**  

[1] ~~For some reason, collecting the duplicate powerup while having the catch powerup active will not cause the catcch powerup to properly stop working.~~ (29/11/21) FIXED - RAN THE CHECK FOR IF ITS CATCH BEFORE I CHANGED POWERUP.  

[2] ~~Ball tends to glitch through gold bricks. Enemy collisions with gold brick don't seem to work properly. Second one seems easily fixable, not sure about first.~~ (28/11/21) FIXED - EDITED BRICK.PY BRICKHIT FUNCTION TO WORK FOR GOLD BRICKS + ADDED ENEMY COLLISION CODE FOR GOLD BRICKS. LET ME KNOW IF YOU SEE MORE GOLD BRICK ISSUES. 
