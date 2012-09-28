SRCS_C = $(wildcard *.c)
CFLAGS = -O3 -Wall
LDFLAGS = -lm

all: $(SRCS_C:.c=)

.c: $<
	cc $(CFLAGS) $< -o $@ $(LDFLAGS)

.PHONY: clean
clean: 
	rm -f $(SRCS_C:.c=) $(SRCS_C:.c=.o)
