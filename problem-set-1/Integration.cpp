#include <bits/stdc++.h>
using namespace std;

// limits of x in radians
double x_min = 0;
double x_max = M_PI / 2;

// function to be integrated
double f(double x) {
	return sin(x);
}

double RectangleRule(int N) {
	double df = (x_max - x_min) / N;
	double integral = 0;

	for (int i = 0; i < N-1; i++) {
		double x = x_min + i * df;
		integral += f(x) * df;
	}

	return integral;
}

double TrapezoidalRule(int N) {
	double df = (x_max - x_min) / N;
	double integral = 0;

	for (int i = 0; i <= N; i++) {
		double x = x_min + i * df;

		if (i == 0 || i == N)
			integral += f(x) * df / 2;
		else
			integral += f(x) * df;
	}

	return integral;
}

int main() {
	double R1, R2;

	printf("Using Rectangle Rule\n");
	R1 = abs(RectangleRule(100) - 1);
	R2 = abs(RectangleRule(200) - 1);
	printf("\tError with N = 100 (R1): %f\n", R1);
	printf("\tError with N = 200 (R2): %f\n", R2);
	printf("\tR1 / R2: %f\n", R1 / R2);

	printf("\nUsing Trapezoidal Rule\n");
	R1 = abs(TrapezoidalRule(100) - 1);
	R2 = abs(TrapezoidalRule(200) - 1);
	printf("\tError with N = 100 (R1): %f\n", R1);
	printf("\tError with N = 200 (R2): %f\n", R2);
	printf("\tR1 / R2: %f\n", R1 / R2);
}
