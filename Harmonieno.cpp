#include"iostream"
#include"math.h"
 using namespace std;
int fact(int f)
{
int s=1;
  for(int i=0;i<=f;i++)
      s*=i;
  return s;
}
int main()
{
int i,j,n,r,l,q,a[100],h=1;
  long int mod=1000000007;
  long int har[100];
  cin>>n;
  for(i=1;i<=n;i++)
    {
    cin>>a[i];
    }
  cin>>q;
  for(i=0;i<q;i++)
    {
    cin>>l;
      cin>>r;
      for(j=l;j<r;j++)
        {
        h*=fact(a[j]);
        }
      h%=mod;
      h=pow(h,r-l);
      har[i]=h;
      h=1;
    }
    for(int z=0;z<q;z++)
    {
        cout<<har[i]<<endl;
    }
  return 0;
}
