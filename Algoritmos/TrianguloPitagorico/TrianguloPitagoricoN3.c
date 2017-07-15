// A C++ program that returns true if there is a Pythagorean
// Triplet in a given aray.
#include <stdio.h>



// Returns true if there is Pythagorean triplet in ar[0..n-1]
int isTriplet(int ar[], int n) {
    int counter = 0;

    for (int i=0; i<n; i++)
    {
       for (int j=i+1; j<n; j++)
       {
          for(int k=j+1; k<n; k++) {
            // Calculate square of array elements
            int x = ar[i]*ar[i], y = ar[j]*ar[j], z = ar[k]*ar[k];


            if (x == y + z || y == x + z || z == x + y) {
                counter++;           
            }
          }
       }
    }
    return counter;
}

/* Driver program to test above function */
int main() {
    int ar[] = {31, 60, 100, 25, 60, 83, 63, 1, 54, 35, 14, 57, 72, 23, 11, 47, 42, 1, 13, 62, 87, 35, 44, 53, 71};
    int ar_size = sizeof(ar)/sizeof(ar[0]);

    int triplet = isTriplet(ar, ar_size)/2; //Divide by 2, because will count x + y and y + x for example

    printf("TRIPLETS? %d\n", triplet);

    return 0;
}
