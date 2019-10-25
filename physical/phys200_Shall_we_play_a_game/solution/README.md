# 200 - Shall we play a game?

As part of the challenge description, the player is given a partially redacted document describing how to solve the challenge.

## Selector switches #1
These are just meant to be brute force options. In fact, the middle switch, due to an accident the night before the CTF, is non functoinal anyway so there are only four actual switches.

In this case, the pattern was ON, OFF, DON'T CARE, ON, OFF

##Authentication code
Here the player needs to put in an 8 digit authentication code. However, after a few attempts it should be obvious that the authentication code fails immediately when the wrong digit is entered. By iteratively attempting the code, it can be cracked. The code is 37234596.

## Selector switches #2
More switch fun, this time the pattern is OFF, ON, DON'T CARE, OFF, ON.

## Shutdown sequence
This is where things get a bit trickier. Now, the code will not tell you it is incorrect until after the entire code is input. 

However, in the partially redacted document, each color is redacted individually and the text is a monospace font. Using this information, the player should be able to figure out the length of each word. The lengths are 3, 4, 6, 5, 5, and 3. 

3 can only be red
4 can only be blue
5 can either be green or white
6 can only be yellow

This reduces the possible combinations to two:
- Red, blue yellow, white, green, red
- Red, blue, yellow, green, white, red

In this case, the 2nd possibility is the correct sequence.

##Activtation keys
The final, and most difficult, step of this challenge. Two keys must be turned simultaneously. One key is given, but no second key can be found. Interestingly enough, the one key turns both locks, meaning they are they same key. However, trying to turn one lock then the other doesn't work.

This is where the specialized piece of equipment provided by the challenge creator comes into play. A manual tubular key cutter. Using this, and the blank tubular keys provided, the player has to duplicate the existing key. 

When the key is duplicated, and both keys are turned simultaneously, the challenge is complete and a flag is displayed.