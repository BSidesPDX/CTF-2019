# BSidesPDX CTF 2019

## BSidesPDX

BSidesPDX CTF 2019 is using the [bsides-ctf-framework](https://github.com/BSidesPDX/bsides-ctf-framework). See [TTimzen's blog post](https://www.tophertimzen.com/blog/BSidesPDXCTFFramework/) for a detailed explanation of the framework, motivations, and instructions for writing challenges.

## Challenges

| Challenge Name                                                 | Category | Points | Port(s)             |
| -------------------------------------------------------------- | -------- | ------ | ------------------- |
| [Gravedigger101](data%20recovery/100-Gravedigger101/)            | physical | 100    | N/A                 |
| N/A                                                            | physical | 200    | N/A                 |
| [OffWithYourHeads](data%20recovery/300-OffWithYourHeads!/)       | physical | 300    | N/A                 |
| [rot13](pwn/100-rot13/)                                        | pwn      | 100    | 1337                |
| [pwnchess](pwn/300-pwnchess/)                                  | pwn      | 300    | 31337               |
| [Magic Numbers](re/100-magicnumbers/)                          | re       | 100    | N/A                 |
| [Bad CryptXor](re/300-badcryptXor/)                            | re       | 300    | N/A                 |
| [Trust Game](misc/100-TrustGame/)                              | misc     | 100    | N/A                 |
| [Hacking_in_the_Clear](forensics/for100-Hacking_in_the_Clear/) | for      | 100    | N/A                 |
| [Polybius](forensics/for300-polybius/)                         | for      | 300    | N/A                 |
| [Signed, Sealed, Delivered, I'm Yours!](web/100-signedsealed/) | web      | 100    | 48323, 48324        |
| [Yours truly](web/200-yourstruly/)                             | web      | 200    | 8081, 9000, 8080    |
| [Hell.js](web/300-helljs/)                                     | web      | 300    | 27330, 27331, 27332 |

## Local Deployment

To locally test, deploy or play challenges with Docker, run the following (Ubuntu)

1. `sudo apt install gcc-multilib gcc-mipsel-linux-gnu gcc-arm-linux-gnueabi g++-multilib linux-libc-dev:i386`
2. `make`
3. `docker-compose build && docker-compose up -d`
4. Containers are viewable at localhost:PORT (view with docker-compose ps)
5. `docker-compose kill` to stop the containers
6. `make clean` to clean the source folders

## Cloud Deployment

How we deployed
