#ifndef __CCONV_H__
#define __CCONV_H__


#include <assert.h>
#include "cconv.h"

#define MIN(a,b)    (((a) < (b)) ? (a) : (b))
#define MAX(a,b)    (((a) > (b)) ? (a) : (b))

/* conv 
 *
 * brief
 *      calculate convulution of two floating point arrays
 *
 * inputs
 *      x   first array
 *      P   length of first array
 *      y   second array
 *      Q   length of second array
 *  outputs
 *      z   resulting convolution
 *      N   length of resulting convolution
 *
 *  remark
 *      N == P + Q - 1, or an error will result
 *
 *  preconditons
 *      x, y, z pre-allocated
 *      P, Q, N indicate correct array size
 *
 */
void conv (float *x, int P,
           float *y, int Q,
           float *z, int N);

#endif /* __CCONV_H__ */
