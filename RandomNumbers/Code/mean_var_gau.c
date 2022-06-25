#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include "coeffs.h"

int main(){
	//Find Mean
	double u_mean = mean("gau.dat");

	//Find Variance
	double u_mean_sec = mean_sec("gau.dat");	
	double u_var = -(u_mean * u_mean) + u_mean_sec;

	//Print
	printf("Mean: %lf\n", u_mean);
	printf("Variance: %lf\n", u_var);
	return(0);
}
