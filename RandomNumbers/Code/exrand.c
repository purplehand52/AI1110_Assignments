#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

int main(void) //main function begins
{
 
//Uniform random numbers
//uniform("uni.dat", 1000000);

//Gaussian random numbers
//gaussian("gau.dat", 1000000);

//Mean of uniform
//printf("%lf",mean("uni.dat"));

//Bernoulli
//bernoulli("ber.dat", 1000000);

//Triangular
//triangular("tri.dat", 1000000);

//Random Variable Y
//y_randvar("y.dat", 5.0);

//PE0, PE1
//printf("P (E|0): %lf\n", prob_err(1));
//printf("P (E|1): %lf\n", prob_err(-1));

//PE
//printf("P_E: %lf\n", prob_err_pe());

//Plot PE vs A
//prob_err_a("pe_a.dat", "y.dat");

//Chi Plot
//chi("chi.dat", 1000000);

//Rayleigh Plot
//rayleigh("ray.dat", 1000000, 2);

//New Rayleigh Plot
//rayleigh("a.dat", 1000000, 5);

//New Values of Y
//y_randvar_ray("newY.dat", 1.0);

//Plot PE vs A (for Rayleigh)
prob_err_sigma("peaRay_new.dat");

return 0;
}


