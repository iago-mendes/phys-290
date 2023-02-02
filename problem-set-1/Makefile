TARGETS = Fibonacci.out

CFLAGS=-g -pedantic -Wall -Wextra

all: $(TARGETS)

Fibonacci.out: Fibonacci.cpp
	g++ $(CFLAGS) -o $@ $^

clean:
	rm -f ${TARGETS} *.out
