## Description

  For this hardware focused challenge you will receive a spinning disk storage device- a 3.5in form factor HDD with SATA connector.  You will also receive the materials necessary to complete the challenge and find the flag should Off With Your Heads! be successful.
In order to find the flag you have to perform a task very similar to the data recovery procedure known as a head swap.  In a normal
headswap for data recovery, the technician first has to remove the bad heads from the "patient" drive, very carefully remove the 
functional heads from a "donor" drive, then place the donor heads into the patient.  Since matching donors with patients can be a 
challenge unto itself and would require more HDDs and more space, this challenge only requires you to completely remove heads from 
the hard drive provided to you then place them back into the same drive.  What is meant by completely is that simply sliding them 
off the heads ramp that's inside the drive doesn't count.  The heads have to get "air time".  Someone will be supervising you 
during your attempt to make sure the removal is complete.

  In addition to the procedure itself you must fashion your own head combs (these keep the hard drive heads, which are magnetically 
attracted to each other, from touching and rendering them incapaple of reading data ever again).  The DIY head comb materials 
typically used by old school data recovery gurus will be given to you, but you do not have to use them.  If you think something 
better will work, do it.  Just keep in mind that hard drive heads are extremely fragile.  If they touch anything, they are toast.

  Once you have fashioned your own head combs and think you are ready- go forth and swap.  In the CTF room you will find a table 
that has everything you need to make the attempt including a glove box style clean hood which will help keep major debris from 
destroying the hard drive's platters (disks) and heads.  Someone will be at the table to assist you with using the equipment and 
equipment only- they will not help you with the actual procedure.

  When you are done with the head swap you can test to see if it was successful on your own machine.  If it was successful, you 
should be able to find the flag; the hard drive model ID (and the capacity, just for fun) has been altered and houses the flag rather than the manufacturer issued information.  If it was not successful, the flag is nevermore.  Signs that it wasn't a success are clicking, 
beeping, scratching, gurgling, moaning, and/or absolute silence (as in the drive doesn't boot).

Here is a full list of what is provided to you:
*  A ruler*
*  DIY head comb materials
   *  plastic and/or foil packaging from first aid kits or OTC medicine (without the meds)
   *  tape
*  Scissors*
*  SATA & power adapter*
*  A hard drive**
*  DIY head comb "schematics"
*  Nitrile gloves
*  Tweezers*
*  Torque set* 

*This item must be returned to us as soon as you are done using it.

**Return the hard drive to us once you have found the flag- please do not take it outside the CTF room. 

Important things to remember:
1.  The heads can't touch ANYTHING.
2.  The heads are magnetic and if not properly separated by head combs they WILL touch, they WILL die, and the flag WILL be lost.
3.  The platters are also very fragile.  Do NOT touch them.  If they are damaged you will have a significantly lower chance of getting the flag.

A video of Scott Moulton from MyHardDriveDied performing this type of "DIY" head swap with similar tools can be found on YouTube here:
<a href="http://www.youtube.com/watch?feature=player_embedded&v=uIPZtJyrVPw
" target="_blank"><img src="http://img.youtube.com/vi/uIPZtJyrVPw.jpg" 
alt="Scott Moulton's 50 cent head combs" width="240" height="180" border="10" /></a>


## Deploy

Physical deployment; no infrastructure.

## Challenge

An online aqcuaintance claims to have lead the 2019 raid on the main Area 51  top secret medical research facility.   The things they saw were horrifying..ghastly..unbelievable.  Forunately they were able to bring back proof- an older hard drive they found while exploring what seemed to be an exam room.  Unfortunately, they dropped it when trying to escape the clutches of Area 51 guards.  

You may not be a data recovery expert but you don't need a PhD to know when a hard drive has read its last sector and clicked its last click. 
What you do need are steady hands, patience, and maybe a touch of madness to bring it back from the dead.  Push your fine motor skills and ingenuity to their limit and head over to the data recovery station in the CTF room.  Who knows?  You could be the Herbert West of head swaps..

flag:```BSidesPDX{ITs_AL1v3!}```
