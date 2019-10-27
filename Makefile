target: deploy

deploy: rot13deploy pwnchessdeploy

clean: rot13clean pwnchessclean

rot13deploy:
	cp pwn/100-rot13/distFiles/rot13 pwn/100-rot13/src/

rot13clean:
	rm pwn/100-rot13/src/rot13

pwnchessdeploy:
	cp pwn/300-pwnchess/distFiles/pwnchess pwn/300-pwnchess/src/

pwnchessclean:
	rm pwn/300-pwnchess/src/pwnchess
