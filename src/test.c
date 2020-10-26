int main() {
	int a, b, c;
	a = 0;
	b = 1;
	c = 0;
	while (1) {
		c = a + b;
		a = b;
		b = c;
	}
	return 0;
}
