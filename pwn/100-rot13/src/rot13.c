#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int input_length = 0;
int i = 0;
char ret;

void jmp_esp()
{
    asm (
        "jmp %esp\n\t"
    );
}

void main()
{
    char input[64];
    setbuf(stdout, NULL);
    printf("Enter the string you would like me to rot13!\n");
    while (true)
    {
        ret = getc(stdin);
        if (ret == '\n') {
            input[input_length] = '\x00';
            break;
        }
        input[input_length] = ret;
        input_length += 1;
    }

    for (i = 0; i<input_length; i++)
    {
        input[i] = input[i]+13;
    }
    
    puts(input);

    asm (
        "leave\n\t"
        "ret\n\t"
    );
}
