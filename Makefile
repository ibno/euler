SRCS_C = $(wildcard *.c)
SRCS_CPP = $(wildcard *.cc)
CFLAGS = -O3 -Wall
CPPFLAGS = -O3
LDFLAGS = -lm

all: $(SRCS_C:.c=) $(SRCS_CPP:.cc=)

.c: $<
	cc $(CFLAGS) $< -o $@ $(LDFLAGS)

.PHONY: clean
clean: 
	rm -f $(SRCS_C:.c=) $(SRCS_C:.c=.o) $(SRCS_CPP:.cc=)

.cc: $<
	g++ $(CPPFLAGS) $< -o $@ $(LDFLAGS)


