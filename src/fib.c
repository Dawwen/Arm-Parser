int main() {
	int tmp = 0;
	int first = 0;
	int second = 1;

	while (1) {
		tmp = first + second;
		first = second;
		second = tmp;
	}
	return 0;
}
