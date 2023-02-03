TARGETS = Fibonacci.out BizzBuzz.out Integration.out

CFLAGS=-g -pedantic -Wall -Wextra

all: $(TARGETS)

Fibonacci.out: Fibonacci.cpp
	g++ $(CFLAGS) -o $@ $^

BizzBuzz.out: BizzBuzz.cpp
	g++ $(CFLAGS) -o $@ $^

Integration.out: Integration.cpp
	g++ $(CFLAGS) -o $@ $^

clean:
	rm -f ${TARGETS} *.out
