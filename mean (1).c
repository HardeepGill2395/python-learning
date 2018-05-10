#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<time.h>
int randm[10000];
float noise(float sig);
int gen(int n);
int main()
{
    float a[10000],x[10000],sig,p,r,d,da,far,mean,sum;
    int i,j,n,F,ifs[10000],ufs[10000],ffs[10000],k,count1=0,count2=0,temp;
    printf("Enter the number of nodes:\n");
    scanf("%d",&n);
    printf("\n");
    for(i=0;i<n;i++)
    {
        a[i]=35;
    }
    sig=sqrt(0.1);
    printf("Initial data of the sensor nodes:\n");
    for(i=0;i<n;i++)
    {
        r=noise(sig);
        x[i]=a[i]+r;
        printf("%f\n",x[i]);

    }
    printf("\n");
    for(i=0;i<n;i++)
    {
        ifs[i]=ufs[i]=0;
    }
    printf("Enter the probability of faulty nodes(The range should be within 0.05 to 0.5):\n");
    scanf("%f",&p);
    printf("\n");
    F=p*n;
    printf("Number of faulty nodes= %d\n",F);
    gen(n);
    for(i=0;i<F;i++)
    {
        for(j=0;j<F-i;j++)
        {
            if(randm[j]>randm[j+1])
            {
                temp=randm[j];
                randm[j]=randm[j+1];
                randm[j+1]=temp;

            }
        }
    }
    printf("Position of faulty nodes are:\n");
    for(i=0;i<F;i++)
    {
        printf("%d\t",randm[i]);
        ufs[randm[i]]=1;
    }
    printf("\n");
    printf("Updated fault status of the entered number of nodes:\n");
    for(i=0;i<n;i++)
    {
        printf("%d\t",ufs[i]);
    }
    printf("\n");
    k=0;
    sig=sqrt(10);
    for(i=0;i<n;i++)
    {
        r=noise(sig);
        if(i==randm[k])
        {
            x[i]=x[i]+r;
            k++;
        }
        else
        x[i]=x[i];
//        printf("%f\t",x[i]);
//        printf("\n");
    }


/*    
    for(i=0;i<n;i++)
    {
        sum=sum+x[i];
    }
*/

    int temprorary = 0;
    for(i=0;i<n;i++)
    {
    	for(j=i+1;j<n;j++)
    	{
    		if(x[i]>x[j])
    		{
    			temprorary = x[i];
    			x[i] = x[j];
    			x[j] = temprorary;
    		}
    	}
    }

    float median = 0;
    median = (n%2)?x[n/2]:(x[n/2]+x[(n/2)+1])/2.0;
    median = median*median;

    //mean=sum/n;
    printf("Median= %f\t",median);
    printf("\n");
    for(i=0;i<n;i++)
    {
        d=x[i]-median;
        if(d<0)
        d=d*(-1);
        sig=0.1;
        if(d<3.0*sig)
        ffs[i]=0;
        else
        ffs[i]=1;
    }
  //  printf("\n \n");
    printf("final fault status of the entered number of nodes:\n");
    for (i=0;i<n;i++)
    {
        printf("%d\t",ffs[i]);

    }
    printf("\n");
    for(i=0;i<n;i++)
    {
        if (ffs[i]==1 && ufs[i]==1)
        {
            count1++;
        }
        if(ffs[i]==1 && ufs[i]==0)
        {
            count2++;
        }
    }
    printf("count1=%d count2=%d\n",count1,count2);
    da=((float)count1/F)*100;
    printf("data accuracy=%f\t",da);
    printf("\n \n");
    far=((float)count2/(n-F))*100;
    printf("Fault alarm ratio=%f\t",far);
    printf("\n \n");
    return 0;
}
float noise(float sig)
{
    float t1,t2,R,mean=0.0,a,b,r,c;
    t1=((float)rand())/RAND_MAX;
    t2=((float)rand())/RAND_MAX;
    a=logf((1)/(1-t1));
    R=sqrt(2*(sig*sig)*a);
    b=(2*3.141*t2);
    c=cosf(b);
    r=mean+R*c;
    return r;
}
int gen(int n)
{
    int i,a,x,xn,c;
    c=3;
    a=1;
    srand(time(NULL));
    x=rand()%n+1;
    for(i=0;i<n;i++)
    {
        xn=(a*x+c)%n;
        x=xn;
        randm[i]=xn;
    }
}