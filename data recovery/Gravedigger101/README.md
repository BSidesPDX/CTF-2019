## Description  

So, the head swap challenge was too difficult for you.  Fear not!  And want not and waste not etc etc.  No reason to immediately 
discard an entire hard drive just becuase of a few bad heads.  Data recovery requires the use of all the components of a
hard drive, and we tend to recycle our donors only after we have harvested all the good parts so we can use them later.

Along with head swaps, PCB swaps are another common procedure in this field.  Without the ROM which is housed on the PCB we couldn't access the hard drive's Service Area thus
allowing it to boot and spin, let alone allow access to user data.  And ROM capacity is *just* large enough to store a CTF flag..so that's
what we did!    

Gravedigger101 will require challengers to first figure out that they aren't quite done with the HDDs post-head swap.
They will be prompted to visit the "data recovery graveyard" where they can dig through the dead HDDs from OffWithYourHeads! as 
well as an assortment of other PCBs and HDDs from various manufacturers.  Though the graveyard will contain many different 
brands/families of non-functional HDDs as well as functional/non-functional PCBs they will all share something in common- the ROM 
chip can be desoldered.  Once desoldered, challengers will have to figure out a way to dump the ROM.  We will have 
USB MiniPRO TL866CS Programmers (x2) as well as USB to TTL CH341A EEPROM BIOS programmers (x2)* available for use to create a 
ROM dump and find the flag**.  While we are offering equipment for use in creating a ROM dump, challengers are of course not 
required to use any of it in order to find the flag.  

The programmers will be labeled with "Gravedigger101" in an effort to keep challengers from being totally lost as to what to do next.

We will also be there to assist in steering them in the right direction, without giving obvious clues.

In total, participants will be provided with the following:

* access to a rework station
* programmers/readers for ROM chips
* target PCB


*Both the MiniPRO and the TTL programmer will require challengers to download drivers.  

**Due to the variance in ROM size of each HDD, the flag will not be hidden at the same offset.  It will likely be 
different for each drive, though it will be located toward the end of the ROM data, inserted just before the "empty" space 
begins with FF FF FF FF. 

## Deployment

--- Hardware Deployment Notes:

-- Windows:

Xgecu Drivers and Software
http://www.autoelectric.cn/MiniPro/XgproV900_Setup.rar

Minipro Drivers and Software - Depreciated Hardware:
http://www.autoelectric.cn/MiniPro/minipro_setup685.rar

CH341A Programmer:
http://www.mediafire.com/file/v7yp367795dz877/CH341A-programmer-software-1.29.zip/file

-- Linux:

IT JUST WORKS!

Use flashrom
https://www.flashrom.org/Flashrom


## Challenge

You know the old adage "kill the brain and you kill the ghoul"?  That may apply to undead that are bound by flesh but it doesn't 
apply to data storage devices... If you or someone you know attempted OffWithYourHeads! and failed (or even if you want to skip that 
challenge altogether), head to the data recovery graveyard and start digging...


Flag: BSidesPDX{inR0M_n0_ON3_C4N_He@R_YOu$cR34M}

