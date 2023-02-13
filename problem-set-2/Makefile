TARGETS = Pi.out

CFLAGS=-g -pedantic -Wall -Wextra

all: $(TARGETS)

Pi.out: Pi.cpp
	g++ $(CFLAGS) -o $@ $^

clean:
	rm -f ${TARGETS} *.out
