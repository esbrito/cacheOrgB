#include <stdio.h>

int max (int *a, int n, int i, int j, int k) {
    int m = i;
    if (j < n && a[j] > a[m]) {
        m = j;
    }
    if (k < n && a[k] > a[m]) {
        m = k;
    }
    return m;
}
 
void downheap (int *a, int n, int i) {
    while (1) {
        int j = max(a, n, i, 2 * i + 1, 2 * i + 2);
        if (j == i) {
            break;
        }
        int t = a[i];
        a[i] = a[j];
        a[j] = t;
        i = j;
    }
}
 
void heapsort (int *a, int n) {
    int i;
    for (i = (n - 2) / 2; i >= 0; i--) {
        downheap(a, n, i);
    }
    for (i = 0; i < n; i++) {
        int t = a[n - i - 1];
        a[n - i - 1] = a[0];
        a[0] = t;
        downheap(a, n - i - 1, 0);
    }
}
 


int isTriplet(int arr[], int n)
{
    int counter = 0;
    // Square array elements
    // Square array elements
    for (int i=0; i<n; i++)
        arr[i] = arr[i]*arr[i];
 
 
    // Now fix one element one by one and find the other two
    // elements
    for (int i = n-1; i >= 2; i--)
    {
        // To find the other two elements, start two index
        // variables from two corners of the array and move
        // them toward each other
        int l = 0; // index of the first element in arr[0..i-1]
        int r = i-1; // index of the last element in arr[0..i-1]
        while (l < r)
        {
            counter++;

            // A triplet found
            if (arr[l] + arr[r] == arr[i]){
                printf("Counter: %d\n", counter);
                return 1;  
            }
            // Else either move 'l' or 'r'
            (arr[l] + arr[r] < arr[i])?  l++: r--;
        }
    }
 
    printf("Counter: %d\n", counter);
    return 0;
}
 
/* Driver program to test above function */
int main() {
    //int ar[] = {31, 60, 100, 25, 60, 83, 63, 1, 54, 35, 14, 57, 72, 23, 11, 47, 42, 1, 13, 62, 87, 35, 44, 53, 71};
    //int ar[] = {31, 60, 100, 25, 60, 83, 63, 1, 54, 35, 14, 57, 72, 23, 11, 47, 42, 1, 13, 62, 87, 35, 44, 53, 71, 49, 17, 44, 87, 41, 1, 70, 97, 27, 11, 47, 65, 20, 92, 86, 51, 37, 45, 74, 73, 14, 9, 39, 98, 72, 48, 10, 37, 4, 28, 13, 29, 2, 97, 37, 42, 70, 11, 19, 67, 70, 64, 95, 41, 65, 31, 91, 46, 84, 29, 52, 41, 88, 59, 62, 23, 67, 43, 84, 72, 93, 12, 21, 57, 92, 79, 30, 79, 52, 7, 51, 38, 44, 6};
    int ar[] = {8691,994,3578,8964,4858,1703,4826,1035,7357,6647,2267,2050,4375,9799,5331,4832,2185,5213,1959,5734,5090,9760,6805,7058,7482};
    // int ar[] = {3, 1, 4, 6, 5};
    int ar_size = sizeof(ar)/sizeof(ar[0]);
    heapsort(ar, ar_size);
    int triplet = isTriplet(ar, ar_size);
    
    printf("IS TRIPLET? %d\n", triplet);

    return 0;
}
