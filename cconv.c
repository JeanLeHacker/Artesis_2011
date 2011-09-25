#include <assert.h>
#include "cconv.h"

void conv (float *x, int P,
           float *y, int Q,
           float *z, int N)
{
    int k;      /* outer loop counter       */
    int i;      /* inner loop counter       */
    float t;    /* temporary sum            */
    int lower;  /* lower inner loop bound   */
    int upper;  /* upper inner loop bound   */

    /* sanity check */
    assert (N == (P + Q - 1));

    /* calculate */
    for (k = 0; k < N; k++) {
        t = 0.0;
        lower = MAX(0,   k-(Q-1));
        upper = MIN(P-1, k      );

        for (i = lower; i <= upper; i++) {
            t = t + x[i] * y[k-i];
        }

        z[k] = t;
    }
}
