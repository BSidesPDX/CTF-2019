# 300 - Forgot My Password

## What's this strange device?
For all you dirty millennials, this weird device is what's called a rotary phone. Back in the day, phone's didn't have screens, and you were tethered to a wall via a wire...

But seriously, it's just a rotary phone. In this case, it's a rotary phone with a RFID reader attached to it and a lock on the dial. The lock is on the number 8 and prevents at least the 9 and 0 from being dialed. Normally, the lock is terrible and could easily be picked. However, since the challenge creator is a jerk, he squirted a bunch of super glue in the lock so it can't be removed.

## Calling the automated help line
On the dial of the phone there's a label with a number (6463725, which spells out mineral). Calling this number you're greeted with an automated voice welcoming you to Ellingson Mineral's automated IT help line. There are a few options in the phone tree, but the last one is interesting. You can reset your password by dialing 9. 

## How do I dial 9?
With the lock on the dial, dialing 9 using the rotary dial is not possible. Fortunately, back in the day with pulse dialing phones like this, there was something called "switch-hook dialing". Essentially, by tapping the switch hook (the little plastic button(s) that hang up the phone), you can dial numbers. So what do you have to do? Just tap the switch hook 9 times.

## Password reset authorization
So now that you're in the password reset menu, the system asks for your 5 digit employee ID number. Well, you don't have one, you're not an employee. However, in the special rules it was noted that at some point you have to interact with some of the CTF organizers. If you spot one, you might notice they've got Ellingson Mineral badges. On their badge, there's a barcode. If you can get a photo of this barcode and decode it, you'll get their 5 digit employee ID number.

Enter the employee ID number, and then the system asks to confirm your identity by scanning your badge. Ok, so the employee ID isn't enough. It was also noted that the challenge creator provided a specialized piece of equipment. There should be some RFID badge reader/writers and a number of blank badges around. The speakers on the RFID reader/writers have been disabled, because it's hard to sneakily clone a badge when it's making loud screeching noises.

So, using the badge reader/writer, you have to covertly use it to read the employee badge. The unfortunate thing about these devices is the extremely limited range. You pretty much have to be touching the reader to the badge. Once you are able to successfully read the badge, you can write it to one of the blank badges.

## Last step
Now that you have a cloned badge, just scan it when the system asks for it. If everything is good, it'll start spelling out the flag for you.