// #include <stdio.h>

int main(int argc, char const *argv[]) {
	// a > b
	int a = 96;
	int b = 36;

	while (a - b != 0)
	{
		// printf("a = %d, b = %d\n", a, b);
		a = a-b;

		if (b > a)
		{
			int c = a;
			a = b;
			b = c;

		}
	}
	// printf("PGCD = %d\n", b);
	return 0;
}
