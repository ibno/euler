all: problem013 problem012 problem016

clean: 
	rm problem012 problem013 problem016

problem012: problem012.c
	cc -O3 -Wall problem012.c -o problem012 -lm

problem013: problem013.c
	cc -O3 -Wall problem013.c -o problem013 

problem016: problem016.c
	cc -O3 -Wall problem016.c -o problem016
