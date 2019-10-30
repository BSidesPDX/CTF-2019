## How To Get the Flag for OffWithYourHeads! Data Recovery Challenge

This challenge is not meant to be difficult as far as finding the flag itself.  It was created to offer CTF partipants a chance to
work on an almost strictly physical challenge that is a very common procedure in data recovery and give them a window into other 
aspects of information security or data security.  
If you are curious about how the hard drive ID and capacity were "permanently" altered (and the security implications involved) I
suggest checking out data recovery forums and researching hard disk firmware modules.  The forums at [HDDOracle](http://www.hddoracle.com/index.php),
[HDDGuru](https://forum.hddguru.com/) and [Data Medics](https://www.data-medics.com/forum/) are great places to start.

* **Step 0:** Probably a great idea to watch some YouTube videos on how to swap hard drive heads, and even how to make your own head
combs.  Scott Moulton does a great job of both here <a href="http://www.youtube.com/watch?feature=player_embedded&v=uIPZtJyrVPw
" target="_blank"><img src="http://img.youtube.com/vi/uIPZtJyrVPw.jpg" 
alt="Scott Moulton's 50 cent head combs" width="240" height="180" border="10" /></a>.

* **Step 1:** Remove the PCB!  It is much easier to remove the head stack connector by pushing it up from the bottom.  That can't
be done if the PCB is still attached.

* **Step 2:** Carefully unscrew the top lid of the HDD making sure to keep the torx screws in order since the head screw can be 
a different size than the others.

* **Step 3:** Examine the internals of the hard drive, paying special attention to the heads parked on the ramp (if outter parked
heads- for inner parked heads you would want to roughly base the distance on the platter height) noting how many there are and make
as precise a guess as you can as to the distance between each head.  You may even attempt measuring with a ruler.
![heads distance parked on ramp- demo](https://user-images.githubusercontent.com/53837252/67820000-b917b600-fa74-11e9-8adb-58ad88054068.jpeg)

* **Step 4:** Make your head combs using the knowledge you have from the internal exam regarding the distance between the heads.
It is important to keep in mind that the heads are magnetically attracted to each other.  You want to make sure the combs you craft
have enough "springy" tension to keep the heads from touching.
![DIY head comb scale](https://user-images.githubusercontent.com/53837252/67820109-29263c00-fa75-11e9-8be6-49290b6b5be9.jpeg)
**AAA battery for scale**
![initial tool- too springy](https://user-images.githubusercontent.com/53837252/67820069-03009c00-fa75-11e9-8bb8-68e0354830b7.jpeg)
**the initial tool didn't provide enough tension**
![final head swap tool- demo](https://user-images.githubusercontent.com/53837252/67819910-5de5c380-fa74-11e9-8f76-80615a38a7cf.jpeg)
**the final tool had twice the wall tape as the inital tool**
* **Step 5:** Using either static-guard tweezers or your fingers, gently place the head combs between each set of heads (there can
be multiple, depending on the HDD capacity).  Be sure they are as secure as possible while not at risk for touching the very tips
of the heads where the sliders (actual read and write elements) are located.  It is better to avoid the head combs sliding over the
platters but not absolutely necessary as the combs made from OTC medicine foil packets or gum tend to be smooth enough and safe for
minimal contact with the platters (in fact Scott Moulton uses the same tools for inner parked heads which means they are in fact
sliding over the platters).  You may have to unscrew the head stack connector and set it aside prior to the combs placement.  This
will depend on the HDD manufacturer, form factor, and other anatomical features of the disk drive.
![head comb placement with tweezers](https://user-images.githubusercontent.com/53837252/67820092-1ad82000-fa75-11e9-85ef-230acb062d89.jpeg)
**as you can see here, I didn't remove the PCB for the demo pics- don't be like me!**
![head comb placed and in action](https://user-images.githubusercontent.com/53837252/67820025-d3519400-fa74-11e9-9e00-496c6327e7c6.jpeg)

* **Step 6:** Once the head combs are securely in place and if you didn't have to unscrew the head stack connector prior to
placement, do so now.

* **Step 7:** Unscrew the top magnet above the base of the head stack assembly (HSA).  Using either a magnetic hammer or needle nose pliers,
remove the top magnet in a steady upward motion away from the platters.  Be careful to avoid knocking into the platters or scraping
across the voice coil that is at the base of the HSA.

* **Step 8:** Remove the rubber stopper that prevents the heads from swinging off the ramp.  It is usually located where the top
left corner of the magnet was prior to removal.  You won't be able to clear the platters if the stopper is not removed first.

* **Step 9:** Using curved tweezers (or whatever you are comfortable with using), pinch the hole in the center of the head stack and
the hole to the right of that.
![tweezer placement for head stack grab](https://user-images.githubusercontent.com/53837252/67821689-16166a80-fa7b-11e9-9610-ea3b2b6f56cc.jpeg)
Be careful not to stick the tweezers very far into the HSA or you won't gain any pull because you will be grabbing the stationary
cylinder that holds the stack in place.  Do not touch the connector ribbon that is on the outter edge of the stack.  It is *very*
fragile, flimsy, and susceptible to permanent damage from scratches.

* **Step 10:** Remove the head stack being sure not to let the heads touch anything (like knocking into the ramp, connector, or the
sides of the drive case) and pay close attention to the head combs, making sure they don't fall out or get pushed out between the
head spaces.  You have to *gently* jiggle the head stack to allow for a smoother removal from the center head screw cylinder.

* **Step 11:** Once you have a good grip bring the heads off the center cylinder and raise the assembly off the base.  For this
challenge, 3-6 inches constitutes as acceptable "air time".

* **Step 12:** Gently place the HSA back onto the center cylinder.  Once they are flush with their original position, carefully
swing the heads back onto the ramp.  Using your free hand put the rubber stopper securely back in position so the heads won't fly
off the ramp.

* **Step 13:** Reassemble the HDD internals: screw the top magnet back on, place the head stack connector back in its original 
position and secure its screws, remove the head combs, and finally cover with the lid and tighten the screws.

* **Step 14:** Test your procedure by connecting the drive via SATA to USB power adapter to your machine and listen for any signs
of head failure such as clicking, beeping, or buzzing.  If using Linux, open a terminal and with dmesg or similar, find the device.
The hard drive's ID has been altered and will always show the flag along with a modified capacity of 6.66GB (sometimes rounded to 
7GB, the true capacity of the hard drives used in the BSidesPDX CTF were 320GB to 500GB).  
![bsidespdxFLAG](https://user-images.githubusercontent.com/53837252/67822536-ec127780-fa7d-11e9-97c2-475e337fd2fd.png)
In Windows you can check disk management, and with Mac you will have to open disk utility first then check disk properties.














