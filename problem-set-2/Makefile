TARGETS = Pi.out SquareRoot.out

CFLAGS=-g -pedantic -Wall -Wextra

all: $(TARGETS)

Pi.out: Pi.cpp
	g++ $(CFLAGS) -o $@ $^

SquareRoot.out: SquareRoot.cpp
	g++ $(CFLAGS) -o $@ $^

clean:
	rm -f ${TARGETS} *.out
