#include <stdio.h>
#include <stdbool.h>
#include <string.h>
# define BUFFER_SIZE 64

void check_passed()
{
	puts("check passed!");
	puts("the secret is 'PABE is fun'");
}

void check_failed()
{
	puts("check failed!");
	puts("try again ;)");
}

void (*check_functions[2]) () = {check_passed, check_failed};

bool check_input(char *input)
{
	if (!strncmp(input, "PABE", strlen("PABE")))
	{
		check_functions[0]();
		return true;
	}
	else
	{
		check_functions[1]();
		return false;
	}
}

int main(int argc, char *argv[])
{
	if (argc != 2)
	{
		puts("Please provide an argument!");
		return 1;
	}

	char buffer[BUFFER_SIZE] = {0};

	strncpy(buffer, argv[1], BUFFER_SIZE - 1);

	printf("your input: %s\n", buffer);

	if (check_input(buffer))
	{
		return 1;
	}
	else
	{
		return 0;
	}
}
