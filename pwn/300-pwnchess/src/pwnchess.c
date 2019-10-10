#include <stdio.h>
#include <stdlib.h>

int moves = 2;

char read_byte()
{
	printf("Enter byte in decimal format (e.g. 255): ");
	unsigned int value = 0;
	scanf("%u", &value);
	if (value > 255)
	{
		printf("Value too large, exiting...");
		exit(2);
	}

	printf("You entered: 0x%x\n", value);
	return (char)value;
}

unsigned long long read_address()
{
	unsigned long long u;
	printf("Enter address in decimal format (e.g. 12345): ");
	scanf("%llu", &u);
	printf("You entered: 0x%llx\n", u);
	return u;
}

void move_read()
{
	unsigned long long addr = read_address();
	char *p = (char*)addr;
	printf("%llx : %02hhx\n", addr, p[0]);
}

void move_write()
{
	unsigned long long addr = read_address();
	char *p = (char*)addr;
	char value = read_byte();
	p[0] = value;
	printf("Value(0x%02x) written to 0x%llx\n", value, addr);
}

void move_exit()
{
	exit(1);
}

void print_menu()
{
	printf("1) Perform a read\n");
	printf("2) Perform a write\n");
	printf("3) Exit\n");
}

void print_remaining_moves()
{
	printf("Remaining moves: %d\n", moves);
}

void loop()
{
	while (moves > 0)
	{
		print_menu();
		print_remaining_moves();
		moves = moves - 1;

		char input = 0;
		while (input > '3' || input < '1')
		{
			input = getchar();
		}
		// read newline character
		getchar();

		if (input == '1')
			move_read();
		else if (input == '2')
			move_write();
		else
			move_exit();
	}
}

void main()
{
	int leak = 0x0;
	setbuf(stdout, NULL);
	printf("Welcome to pwnchess!\n");
	printf("The rules are simple:\n");
	printf("1) You get %d moves\n", moves);
	printf("2) For each move, you are allowed to read 1 byte or write 1 byte\n");
	printf("3) Oh yeah, and the only way to win is to pop a shell!\n\n");
	printf("Here is a stack address to get you started: %p\n\n", &leak);
	printf("Good luck!\n\n");
	return loop();
}
