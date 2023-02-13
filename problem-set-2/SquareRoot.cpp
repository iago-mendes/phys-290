// Iago Braz Mendes (T01362926)

#include <bits/stdc++.h>
using namespace std;

#define ACCURACY 1e-12

double n = 2;

double FA(double x) {
	return .2 * x + .8 * n / x;
}

double FB(double x) {
	return .5 * (x + n / x);
}

double FC(double x) {
	double num = x * (pow(x, 2) + 3 * n);
	double den = 3 * pow(x, 2) + n;
	return num / den;
}

// iterates function F, N times, starting from x
void iterate(double (*F)(double x), double x, int N) {
	double error;

	int i;
	for (i = 1; i <= N; i++) {
		double x_prev = x;
		x = F(x);

		error = abs(x - x_prev);
		if (error < ACCURACY) {
			break;
		}
	}

	printf("%.16f +/- %.4e (%d iterations)\n", x, error, i);
}

int main() {
	printf("FA:  ");
	iterate(FA, .1, 100);

	printf("FB:  ");
	iterate(FB, .1, 100);

	printf("FC:  ");
	iterate(FC, .1, 100);

	printf("Ref: %.16f\n", sqrt(2));
}
