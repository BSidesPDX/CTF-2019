# 300 - Forgot my password

##Description
You're presented with a rotary telephone. Attached to this rotary telephone is an RFID reader and a lock on the 8 digit of the dial. On the face of the dial there is a 5 digit number with the note "IT Help Desk". When this number is dialed, an automated IT help desk system answers. There are multiple options in the phone tree, but option 9 leads to a password reset menu. However, due to the lock, the 9 cannot be dialed. On old rotary phones, there is a dialing technique called switch hook dialing where the button normally used to hang up the phone can be tapped to dial numbers. By using switch hook dialing, the password reset menu can be accessed. You are then required to input "your" employee ID number. Some of the CTF organizers will have custom RFID badges with their picture and a barcode printed on the front. The barcode, when decoded, is the employee ID. RFID cloners and blank cards will be provided, and users will have to covertly clone a badge as well as capture/decode the barcode. Once a correct employee ID is entered, the system requests the user to scan their badge on the RFID reader attached to the phone. If the badge associated with the previously entered employee ID is scanned, the password reset will be succesful and the flag will be spelled out over the phone.

The challenger will be provided with the rotary phone, RFID cloner, and blank  RFID cards.
##Challenge
You've made it into an Ellingson Mineral Company branch office. You found this phone, tucked away in a corner and it's got the number for IT on it. Maybe give it a call?

Flag: `BSidesPDX{Y0u_go7_th3_passw04d_7im3_T0_h4ck_th3_gibs0n}`

##Reset instructions
1. Hang up the phone
2. If something is wrong with the challenge, hang up the phone and turn off the power switch. Turn it back on and wait 30 seconds before picking up the phone. You should hear a dial tone.
