# Short notes

**(28/04/22)**
• Key thing to focus on going forward is backwards compatability. What I'm finding is that i have to refactor large 
amounts of the codebase each time i make  a change. By moving certain functions to their original "parent class" so 
to speak, i should be able to reduce the amount of time I spend on this.
• Currently I have 3 seperate parts of the game I could work on. One, attacks for players and basic code for enemies.
Two, more console features, such as commands. Three, more text features - in-line formatting alongside symbols, different
font options, etc.
• I want to focus on attacks: to do this I need to create some dummy sprites, along with finalising my basic enemy code. 
Enemy spawning needs to be handled: probably in my json files for the maps, enemies need to have hit animations, to avoid 
having these for mult. directions i could just rotate them.
• Another task i forgot: finishing off healthbar, adding interactables, adding prompts.
• ANOTHER task I forgot, I need to change how inputs are handled: right now it's hard coded into the game which keys correspond to which actions: i'd like to make this more memorable/easy to customise. 

So, to summarise what I'm doing next.
1. I will create a basic attack and health system, along with some test enemies 
2. Once this is completed, I will focus on reworking parts of the codebase to help me ensure future smooth development. This will be noted elsewhere.
3. I will add some more map features, such as interactable signs, and rework the current test map to be more useful for testing AND more visually appealing. 
4. I will change how inputs are handled
