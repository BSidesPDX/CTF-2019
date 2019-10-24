#!/bin/bash

pico2wave -w intro.wav -l en-US "Welcome to the ellingson mineral automated IT help line. To create a new ticket, dial. 1. now. To check on the status of a current ticket, dial. 2. now. To speak to an operator, dial. 3. now. To reset your password, dial. 9. now." 

pico2wave -w new_ticket.wav -l en-US "You have selected. 1. We apologize, but at this time the ticket creation system is currently unavailable. Estimated time until return: 3. business days. Thank you for calling the ellingson mineral automated IT help line. Goodbye!"

pico2wave -w current_ticket.wav -l en-US "You have selected. 2. We apologize, but there was an error accessing the ticket status system. Please call back and file and create a new ticket to report this issue. Thank you for calling the ellingson mineral automated IT help line. Goodbye!"

pico2wave -w operator.wav -l en-US "You have selected. 3. Please hold. . . . . All of our operators are currently busy. Your call is very important to us. The next available operator will be with you shortly. Please stay on the line"

pico2wave -w bad_option.wav -l en-US "The number you have entered is an invalid option. Please hang up and try again. Goodbye!"

pico2wave -w continue_holding.wav -l en-US "Your call is very important to us, please stay on the line and the next available operator will be with you shortly."

pico2wave -w password_reset_1.wav -l en-US "You have selected. 9. Please hold. . . . . Please enter your 5 digit employee ID number."

pico2wave -w bad_eid.wav -l en-US "The employee ID number entered was not recognized. Unauthorized access attempt detected. Goodbye."

pico2wave -w timzen.wav -l en-US "You have entered the employee ID number for Mr. Timzen"

pico2wave -w carl.wav -l en-US "You have entered the employee ID number for Mr. Carl"

pico2wave -w harding.wav -l en-US "You have entered the employee ID number for Mr. Harding"

pico2wave -w gallagher.wav -l en-US "You have entered the employee ID number for Mr. Gallager"

pico2wave -w strange.wav -l en-US "You have entered the employee ID number for Mr. Strange"

pico2wave -w scan_badge.wav -l en-US "Please scan your employee badge to authorize the password reset"

pico2wave -w bad_scan_badge.wav -l en-US "The badge scanned does not match the employee ID number given. Unauthorized access attempt detected. Goodbye"

pico2wave -w good_scan_badge.wav -l en-US "Password reset authorized. Please hold while your password is reset."

pico2wave -w flag.wav -l en-US "Your password has been reset. Your new password is: Capital B..  Capital S..  i..  d..  e..  s.. Capital  P.. Capital D.. Capital X.. {.. Capital Y.. Zero.  u.. underscore..  g..  0.. 7.. underscore..  t..  h.. three.. underscore.. p.. a.. s.. s.. w.. 0.. r.. d.. underscore.. seven.. i.. m.. 3.. underscore.. capital T.. zero.. underscore.. h.. four.. c.. k.. underscore.. t.. h.. three.. underscore.. g.. i.. b.. s.. zero.. n.. }.."

