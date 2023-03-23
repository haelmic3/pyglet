#!/usr/local/bin/python3
import ctypes as ct
def main():
	m = ct.CDLL("run.so")
	s = b"Hello, World!"
	m.run(len(s),s)
if(__name__=="__main__"):main()
