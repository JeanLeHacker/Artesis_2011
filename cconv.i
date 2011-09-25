// cconv.i : convolution function
%module cconv
%include "typemaps.i"
%include "cpointer.i"
%include "carrays.i"

%{
#include "cconv.h"
%}

%array_class(float, float_arr);
    
void conv (float_arr *x, int P,
           float_arr *y, int Q,
           float_arr *z, int N);
