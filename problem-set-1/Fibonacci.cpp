// Iago Braz Mendes (T01362926)

#include <bits/stdc++.h>
using namespace std;

int main() {
	printf("Number of elements: ");

	int n;
	cin >> n;

	vector<long int> fibonacci_list;
	fibonacci_list.push_back(1);
	fibonacci_list.push_back(1);

	for (int i = 0; i < n; i++) {
		if (i > 1)
			fibonacci_list.push_back(fibonacci_list[i-1] + fibonacci_list[i-2]);

		printf("%2d: %ld\n", i+1, fibonacci_list[i]);
	}
}
