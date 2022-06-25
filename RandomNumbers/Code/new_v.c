#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include "coeffs.h"

//Defining the function for generating new random variables 
void log_rv(char *str)
{
int i=0,c;
FILE *fp_uni, *fp_new;
double x, temp=0.0;

fp_uni = fopen("uni.dat","r");
fp_new = fopen(str, "w");

//get numbers from file
while(fscanf(fp_uni,"%lf",&x)!=EOF)
{
//Count numbers in file
i=i+1;
//Calculate new rv
temp = -2 * (log(1 - x));
//Put in new file
fprintf(fp_new, "%lf\n", temp);
}
fclose(fp_uni);
fclose(fp_new);

return;

}
//End function for generating new random variables

int main(){
	log_rv("log.dat");
	return(0);
}
