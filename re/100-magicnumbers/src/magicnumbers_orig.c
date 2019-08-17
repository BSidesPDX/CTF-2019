#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>

#define INPUT_LENGTH 255

#define X 1
#define Y 1
#define FLAG_LENGTH 1
#define FLAG ""

#define MAGIC1 1337
#define MAGIC2 31337
#define MAGIC3 314159265

void decrypt(char* plaintxt, int plaintxt_len)
{
    for (int i=0; i<plaintxt_len; i++)
    {
        if (i%2 == 0)
            plaintxt[i] = plaintxt[i]-X;
        else
            plaintxt[i] = plaintxt[i]+Y;
    }
}

int main()
{
    char flag_decrypted[FLAG_LENGTH];
    int in1, in2, in3;

    // Welcome message
    printf("Welcome to Magic Numbers!\n");
    printf("You will be prompted for 3 magic numbers.\n");
    printf("After you enter each magic numbers, I will let you know if it's correct or not!\n");
    printf("ProTip: Be sure you enter the numbers in decimal format (not hex!)\n");
    printf("In other words, if the magic number is 0x539, you should enter 1337 into the program.\n");

    // Magic #1
    printf("Enter Magic Number 1/3: ");
    if (scanf("%d", &in1) != 1) {
        printf("Did you enter a number?\n");
        return 1;
    }
    if (in1 != MAGIC1) {
        printf("Sorry, that is not the correct number.  You entered: %d\n", in1);
        return 1;
    }
    printf("Ok, I gave you that one free, let's make it a little harder now\n");

    // Magic #2
    printf("Enter Magic Number 2/3: ");
    if (scanf("%d", &in2) != 1) {
        printf("Did you enter a number?\n");
        return 1;
    }
    if (in2 != MAGIC2) {
        printf("Sorry, that is not the correct number.  You entered: %d\n", in2);
        return 1;
    }

    // Magic #3
    printf("Enter Magic Number 3/3: ");
    if (scanf("%d", &in3) != 1) {
        printf("Did you enter a number?\n");
        return 1;
    }
    if (in3 != MAGIC3) {
        printf("Sorry, that is not the correct number.  You entered: %d\n", in3);
        return 1;
    }

    // Print flag
    printf("Good job!! -- 1 second while I decrypt your flag for you!\n");
    memcpy(flag_decrypted, FLAG, FLAG_LENGTH);
    decrypt(flag_decrypted, FLAG_LENGTH);
    printf("%s\n", flag_decrypted);
    return 0;
}
