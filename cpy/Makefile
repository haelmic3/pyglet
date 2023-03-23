.PHONY:run
run:run.so
	./main.py
run.so:run.c
	cc -fPIC -shared -o $@ $<
