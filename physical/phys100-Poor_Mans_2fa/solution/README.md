# 100 - Poor Man's 2FA

## The locks
So just by observation, there are two types of locks. One is a push button style, while the other is a 4 combo wheel style. The nice thing about these locks is that neither of them require any tools to decode the combinations. You only need your hands.

###Push Button Lock Box
With the push button lock box, there are 10 digit buttons, a reset button, and an open button. There are multiple videos on YouTube showing how to decode them, like [this video here](https://www.youtube.com/watch?v=8bzolgrC6BA). 

The basic concept is pretty simple. While holding the open button down, press the digit buttons. Some of them should push in, while others do not. The ones that push in are part of the combination. If no buttons can be pushed in, ease up slightly on the open button and try again. You'll find a sweet spot where this is possible.

Once you find all the numbers (which, in this case, are **14670**), you should be able to open the box and get half of the flag.

### 4 Combo Wheel Lock Box
On this lock box, there are just 4 combo wheels. The vulnerability with this lock is very common for combo wheel style locks. 

By pulling up on the shackle and fiddling with the combo wheels, you will find one that is harder to turn than the others. For that wheel, wiggle it back and forth on the current number. Take note of how much play there is on this number. Then, rotate the wheel to the next digit and wiggle it again. Keep doing this. Eventually you will find one number where there is more play than other numbers. This will be the correct number.

Now, leave that wheel alone and find the next wheel that is hard to turn and repeat the process. Keep repeating this process, and eventually it will open. The combo on this should be **7452** and you will now have the other half of the flag.

[Here is a video showing the process](https://www.youtube.com/watch?v=n9Fqzq1yqbA).