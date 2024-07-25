class Solution {
    public int search(int[] arr, int k) {
        int l=0;

int N = arr.length;

int h= N-1;

int max_index = -1;

while(l<=h) {

int m= l+(h-l)/2;
    System.out.print("value of m is :"+m);

if( (m>0 && arr[m]>arr[m-1]) && (m<N-1 && arr[m]>arr[m+1])) {

max_index = m;

break;

}else if(arr[l]<=arr[m]) {

l=m+1;

}else {

h=m-1;

}

}
        System.out.print(max_index);

if(N==1) {
    if(arr[0]==k)
        return 0;
    else
        return -1;
}

if(N>1 && arr[0]>arr[1]) max_index =0;

if(k<=arr[N-1]) { // Target in 2nd part

l=max_index+1;

h=N-1;

}else { // Target in 1st part

l=0;

h=max_index;

}

// Apply Binary search in that half

while(l<=h) {

int m=l+(h-l)/2;

if(arr[m]==k) return m;

else if(arr[m]<k) l = m+1;

else h=m-1;

}

return -1;


    }
}