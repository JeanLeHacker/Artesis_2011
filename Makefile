#/******************************************************************************
# *
# * Filename: Makefile
# *
# * Jan Mennekens   18 nov 2009     jan@dcim.be
# * 
# ******************************************************************************
# 
#
# settings
#
SHELL = /bin/sh

CC = gcc
AS = gas
AR = ar
LD = gcc
SP = splint

LIBS     = 
INCPATH  = -I .
USRDEFS  = -DSIMULATOR -g -Wall -pedantic -std=c99
CFLAGS   = $(INCPATH) $(USRDEFS)

COBJS    = cconv.o

all:  _cconv.so

#
# C code
#

.c.o:
	$(CC) -S $(CFLAGS) $*.c
	$(CC) -c $(CFLAGS) -o $*.o $*.c

.s.o:
	${AS} -alh -o $*.o $*.s > $*.lst

#
# conv test code
#
_cconv.so: cconv.i cconv.c cconv.h
	swig -python cconv.i
	python setup_cconv.py build_ext --inplace    

#
# clean
#
clean:
	rm -rf build
	rm -f *.o
	rm -f *.s
	rm -f cconv.py
	rm -f *.pyc
	rm -f *_wrap.c
	rm -f _cconv.so
	rm -f main

#
# docs
#
docs: cconv.c cconv.h
	doxygen Doxyfile

