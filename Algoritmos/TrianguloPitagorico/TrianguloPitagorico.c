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



            if (x == y + z || y == x + z || z == x + y) counter++;
          }
       }
    }

    // If we reach here, no triplet found
    return counter;
}

/* Driver program to test above function */
int main() {
    int ar[] = {31, 60, 100, 25, 60, 83, 63, 1, 54, 35, 14, 57, 72, 23, 11, 47, 42, 1, 13, 62, 87, 35, 44, 53, 71};
    // int ar[] = {31, 60, 100, 25, 60, 83, 63, 1, 54, 35, 14, 57, 72, 23, 11, 47, 42, 1, 13, 62, 87, 35, 44, 53, 71, 49, 17, 44, 87, 41, 1, 70, 97, 27, 11, 47, 65, 20, 92, 86, 51, 37, 45, 74, 73, 14, 9, 39, 98, 72, 48, 10, 37, 4, 28, 13, 29, 2, 97, 37, 42, 70, 11, 19, 67, 70, 64, 95, 41, 65, 31, 91, 46, 84, 29, 52, 41, 88, 59, 62, 23, 67, 43, 84, 72, 93, 12, 21, 57, 92, 79, 30, 79, 52, 7, 51, 38, 44, 6};
    // int ar[] = {3, 1, 4, 6, 5};
    int ar_size = sizeof(ar)/sizeof(ar[0]);

    int triplet = isTriplet(ar, ar_size);

    printf("NUMBER OF TRIPLET %d\n", triplet);

    return 0;
}
