#include <bits/stdc++.h>
using namespace std;

int main() {
	printf("Number of elements: ");

	int n;
	cin >> n;

	for (int i = 1; i <= n; i++) {
		if (i % 3 == 0 && i % 5 == 0)
			printf("%d: Bizz Buzz\n", i);
		else if (i % 3 == 0)
			printf("%d: Bizz\n", i);
		else if (i % 5 == 0)
			printf("%d: Buzz\n", i);
		else
			printf("%d: %d\n", i, i);
	}
}
