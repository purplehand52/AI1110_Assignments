#include<math.h>

//Function declaration
double **createMat(int m,int n);
void readMat(double **p, int m,int n);
void print(double **p,int m,int n);
double **loadtxt(char *str,int m,int n);
double linalg_norm(double **a, int m);
double **linalg_sub(double **a, double **b, int m, int n);
double **linalg_inv(double **mat, int m);
double **matmul(double **a, double **b, int m, int n, int p);
double **transpose(double **a,  int m, int n);
void uniform(char *str, int len);
void gaussian(char *str, int len);
double mean(char *str);
//End function declaration


//Defining the function for matrix creation
double **createMat(int m,int n)
{
 int i;
 double **a;
 
 //Allocate memory to the pointer
a = (double **)malloc(m * sizeof( *a));
    for (i=0; i<m; i++)
         a[i] = (double *)malloc(n * sizeof( *a[i]));

 return a;
}
//End function for matrix creation


//Defining the function for reading matrix 
void readMat(double **p, int m,int n)
{
 int i,j;
 for(i=0;i<m;i++)
 {
  for(j=0;j<n;j++)
  {
   scanf("%lf",&p[i][j]);
  }
 }
}
//End function for reading matrix

//Read  matrix from file
double **loadtxt(char *str,int m,int n)
{
FILE *fp;
double **a;
int i,j;


a = createMat(m,n);
fp = fopen(str, "r");

 for(i=0;i<m;i++)
 {
  for(j=0;j<n;j++)
  {
   fscanf(fp,"%lf",&a[i][j]);
  }
 }
//End function for reading matrix from file

fclose(fp);
 return a;

}


//Defining the function for printing
void print(double **p, int m,int n)
{
 int i,j;

 for(i=0;i<m;i++)
 {
  for(j=0;j<n;j++)
  printf("%lf ",p[i][j]);
 printf("\n");
 }
}
//End function for printing

//Defining the function for norm

double linalg_norm(double **a, int m)
{
int i;
double norm=0.0;

 for(i=0;i<m;i++)
 {
norm = norm + a[i][0]*a[i][0];
}
return sqrt(norm);

}
//End function for norm

//Defining the function for difference of matrices

double **linalg_sub(double **a, double **b, int m, int n)
{
int i, j;
double **c;
c = createMat(m,n);

 for(i=0;i<m;i++)
 {
  for(j=0;j<n;j++)
  {
c[i][j]= a[i][j]-b[i][j];
  }
 }
return c;

}
//End function for difference of matrices

//Defining the function for inverse of 2x2 matrix


double **linalg_inv(double **mat, int m)
{
double **c, det;
c = createMat(m,m);

det = mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0];

c[0][0] = mat[1][1]/det;
c[0][1] = -mat[1][0]/det;
c[1][0] = -mat[0][1]/det;
c[1][1] = mat[0][0]/det;

return c;

}
// End  function for inverse of 2x2 matrix


//Defining the function for difference of matrices

double **matmul(double **a, double **b, int m, int n, int p)
{
int i, j, k;
double **c, temp =0;
c = createMat(m,p);

 for(i=0;i<m;i++)
 {
  for(k=0;k<p;k++)
  {
    for(j=0;j<n;j++)
    {
	temp= temp+a[i][j]*b[j][k];
    }
	c[i][k]=temp;
	temp = 0;
  }
 }
return c;

}
//End function for difference of matrices

//Defining the function for transpose of matrix

double **transpose(double **a,  int m, int n)
{
int i, j;
double **c;
//printf("I am here");
c = createMat(n,m);

 for(i=0;i<n;i++)
 {
  for(j=0;j<m;j++)
  {
c[i][j]= a[j][i];
//  printf("%lf ",c[i][j]);
  }
 }
return c;

}
//End function for transpose of matrix

//Defining the function for generating uniform random numbers
void uniform(char *str, int len)
{
int i;
FILE *fp;

fp = fopen(str,"w");
//Generate numbers
for (i = 0; i < len; i++)
{
fprintf(fp,"%lf\n",(double)rand()/RAND_MAX);
}
fclose(fp);

}
//End function for generating uniform random numbers

//Defining the function for calculating the mean of random numbers
double mean(char *str)
{
int i=0,c;
FILE *fp;
double x, temp=0.0;

fp = fopen(str,"r");
//get numbers from file
while(fscanf(fp,"%lf",&x)!=EOF)
{
//Count numbers in file
i=i+1;
//Add all numbers in file
temp = temp+x;
}
fclose(fp);
temp = temp/(i);
return temp;

}
//End function for calculating the mean of random numbers

//Defining function for mean of RV**2
double mean_sec(char *str)
{
int i=0,c;
FILE *fp;
double x, temp=0.0;

fp = fopen(str, "r");
//get numbers
while(fscanf(fp, "%lf", &x) != EOF)
{
//Count numbers in life
i=i+1;
//Add squares
temp=temp+(x*x);
}
fclose(fp);
temp = temp/(i);
return(temp);
}
//Ending function for mean of RV**2
//Defining the function for generating Gaussian random numbers
void gaussian(char *str, int len)
{
int i,j;
double temp;
FILE *fp;

fp = fopen(str,"w");
//Generate numbers
for (i = 0; i < len; i++)
{
temp = 0;
for (j = 0; j < 12; j++)
{
temp += (double)rand()/RAND_MAX;
}
temp-=6;
fprintf(fp,"%lf\n",temp);
}
fclose(fp);

}
//End function for generating Gaussian random numbers

//Defining function to generate Bernoulli distribution {-1, 1}
void bernoulli(char *str, int len)
{
int i;
FILE *fp;
double temp = 0;

fp = fopen(str,"w");
//Generate numbers
for (i = 0; i < len; i++)
{
if((double)rand()/RAND_MAX < 0.5){
	temp = -1;
}
else{
	temp = 1;
}
fprintf(fp, "%lf\n", temp);
}

fclose(fp);
}
//End function to generate Bernoulli distribution {-1, 1}

//Defining Random Variable Y
void y_randvar(char *str, double a){
int i;
double x, n, y;

//Files
FILE *fp_ber, *fp_gau, *fp_new;
fp_ber = fopen("ber.dat", "r");
fp_gau = fopen("gau.dat", "r");
fp_new = fopen(str, "w");

//Generate numbers
while ((fscanf(fp_ber, "%lf", &x) != EOF) && (fscanf(fp_gau, "%lf", &n) != EOF)){
	y = a*x + n;
	fprintf(fp_new, "%lf\n", y);
}

//Close
fclose(fp_ber);
fclose(fp_gau);
fclose(fp_new);
}
//Ending definition of random variable Y

//Define Probability error
double prob_err(int i){
	//Values
	double x;
	double y;
	
	//Load files
	FILE *fp1, *fp2;
	fp1 = fopen("ber.dat", "r");
	fp2 = fopen("y.dat", "r");
	
	//Counting
	double ber_pos = 0;
	double ber_neg = 0;
	double xy_0 = 0;
	double xy_1 = 0;
	
	//Iterate through Bernoulli values
	while(fscanf(fp1, "%lf", &x) != EOF){
		fscanf(fp2, "%lf", &y);
		
		//Go through cases
		//P e|0
		if((x == 1) && (i == 1)){
			if(y < 0) xy_0++;
			ber_pos++;
		}
		
		//P e|1
		else if((x == -1) && (i == -1)){
			if(y > 0) xy_1++;
			ber_neg++;
		}
		
		//If x = 1, general
		else if(x == 1){
			ber_pos++;
			continue;
		}
		
		//If x = -1, general
		else{
			ber_neg++;
			continue;
		}
	}
	
	fclose(fp1);
	fclose(fp2);
		
	//Return
	if(i == 1) return xy_0/ber_pos;
	else return xy_1/ber_neg;
}

//P_e value
double prob_err_pe(){
	double pe0, pe1;
	pe0 = prob_err(1);
	pe1 = prob_err(-1);
	
	return((pe0 + pe1)/2);
}

//P_e vs a
void prob_err_a(char *str){
	FILE *fp;
	fp = fopen(str, "w");
	
	//Iterate through 20 values of a
	double step_inc = 0.5;
	double temp;
	
	for(int i = 1; i <= 20; i++){
		y_randvar("y.dat", step_inc*i);
		temp = prob_err_pe();
		fprintf(fp, "%lf\n", temp);
	}
	
	fclose(fp);
	return;
}

//Chi_Generator
void chi(char *str, int len)
{
int i,j,k;
double temp1, temp2, chi_val;
FILE *fp;

fp = fopen(str,"w");
//Generate numbers
for (i = 0; i < len; i++)
{
	temp1 = 0;
	temp2 = 0;
	for (j = 0; j < 12; j++)
	{
		temp1 += (double)rand()/RAND_MAX;
	}

	for (k = 0; k < 12; k++){
		temp2 += (double)rand()/RAND_MAX;
	}
	
	temp1-=6;
	temp2-=6;
	
	chi_val = temp1*temp1 + temp2*temp2;

	fprintf(fp,"%lf\n",chi_val);
}
fclose(fp);
}

//Rayleigh_Generator
void rayleigh(char *str, int len)
{
int i,j,k;
double temp1, temp2, ray_val;
FILE *fp;

fp = fopen(str,"w");
//Generate numbers
for (i = 0; i < len; i++)
{
	temp1 = 0;
	temp2 = 0;
	for (j = 0; j < 12; j++)
	{
		temp1 += (double)rand()/RAND_MAX;
	}

	for (k = 0; k < 12; k++){
		temp2 += (double)rand()/RAND_MAX;
	}
	
	temp1-=6;
	temp2-=6;
	
	ray_val = sqrt(temp1*temp1 + temp2*temp2);

	fprintf(fp,"%lf\n",ray_val);
}
fclose(fp);
}


