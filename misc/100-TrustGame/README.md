# 100 - Trust Game

## Description

This challenge aims to hand out free flags to anyone who is trusting enough to run pipe content directly from the internet into their bash shell or alternatively figures out how to bypass the pipe check in the server. Details about this "attack" can be found here: https://www.idontplaydarts.com/2016/04/detecting-curl-pipe-bash-server-side/

## Deploy

Depends on:

- python2.7
- numpy (pip install numpy)

`server.py` exposes one port, 5555, which needs to be exposed to the participant. 

## Challenge

Do you want to play a game?

Do you trust me?

How far will you go?

misc100-trustgame.bsidespdxctf.party:5555

Flag: `BSidesPDX{n3v3r_$ud0_(ur1_b4$h_1t5_r3411y_b4d}`