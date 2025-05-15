# Snek-in-Python
a snake game (that can be run in console) implemented in python



Controll using WASD.
Start game by pressing any of these keys.



Game has 3 levels with custom maps, where:  
green 'o' - is your snek  
red 'o' - is an apple  
inverted 'o' - is an enemy snake  
gold 'o' - golden apple (restores health)  
'#' - are walls  
'+' - are portals to next level  
'.' - are background tiles.  


Collisions with any other objects than apples resoults in decrease in hp. You loose when you run out of it.


Reach each point goal to advance to the next level. Gain 100 points to win.


-- KEEP THE MAP TXT FILE IN THE SAME DIRECTORY OR THE GAME WON'T RUN --

You can edit every map by replacing characters corresponding to walls, background and portals in the text file.
The map loops, so crossing border without walls means teleporting to the other side.
Keep in mind that if the number of tiles is mismatched - the game won't run.


-- it's an upload of one of my college projects --
