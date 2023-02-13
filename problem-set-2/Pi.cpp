/**
 * This program calculates the value of pi by bisection.
*/

#include <bits/stdc++.h>
using namespace std;

void Bicsection(double (*f)(double x), double xL, double xR, double accuracy) {
	for (int i = 1; i <= 100; i++) {
		double xC = .5 * (xL + xR);

		if (f(xL) * f(xC) < 0)
			xR = xC;
		else if (f(xC) * f(xR) < 0)
			xL = xC;

		double guess = .5 * (xL + xR);
		double error = .5 * (xR - xL);

		printf("%3d) %.16f +/- %.4e\n", i, guess, error);

		if (error < accuracy)
			break;
	}
}

int main() {
	Bicsection(sin, 3, 4, 1e-15);

	printf("Ref: %.16f\n", M_PI);
}