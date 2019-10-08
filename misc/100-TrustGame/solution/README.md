# 100 - Trust Game (Solution)

## Visiting the Challenge
Being provided the url of the challenge, attempting to visit it in the browser will yield a gif about trust. Inspecting the source suggests that you try to use the command line.

## Curling the Challenge
While this was intended to be the right path to the solution, some changes to curl resulted in the flaw that the challenge relies on not being consistent. So instead, we use this opportunity to redirect the user towards wget. This can be seen by running `curl $URL`.

## Wgetting the Challenge
By running `wget $URL`, the server will send the `ping` command in `ticker.sh` to see if it's being piped anywhere. If it's not being piped anywhere, then we send the contents of `good.sh` which just taunts the user with `What, don't you trust us?`

### Wget | bash
By running `wget $URL | bash`, wget will simply save the contents of the previous section into a file called `index.html`, because wget doesn't print contents to stdout by default.

### Wget -O - | bash
By running `wget $URL -O - | bash`, the `ping` command in `ticker.sh` will run immediately when it's sent and this causes a timing variation for the rest of the script, allowing the malicious server to change the content that it's serving on the fly. So instead of the contents of `good.sh` we will send the contents of `flag.sh`.

### Wget -O - | sudo bash
Unfortunately, in this game of trust, we're expecting the user to trust in us completely. Just allowing us to run arbitrary code isn't good enough, we need to be privileged while we do it. So the very first section of `flag.sh` will check if the effective user ID (EUID) is 0 (root), and if it's not then print another comment about trusting us and a link to a youtube video suggesting that it's a permission error.


## Getting the Flag

The easiest way to get the flag is to trust the server: `wget $URL -O - | sudo bash`

But we also reward hackers who don't trust random CTF challenges, so an alternate solution can be achieved: `wget $URL -O - | (sleep 5; cat -)`. This works because we're still piping to something that sleeps, just like the server is expecting.