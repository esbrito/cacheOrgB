#include <stdio.h>

int countTriplet(int ar[], int n, int i, int j, int k, int counter) {
  k++;

  if(k == n) {
    j++;
    k = j+1;
  }

  if(j == n - 1) {
    i++;
    j = i+1;
    k = j+1;
  }

  if(i == n - 2) return counter;

  int x = ar[i]*ar[i], y = ar[j]*ar[j], z = ar[k]*ar[k];
  if (x == y + z || y == x + z || z == x + y)
    return countTriplet(ar, n, i, j, k, counter + 1);
  }

  return countTriplet(ar, n, i, j, k, counter);
}

/* Driver program to test above function */
int main() {
    int ar[] = {31, 60, 100, 25, 60, 83, 63, 1, 54, 35, 14, 57, 72, 23, 11, 47, 42, 1, 13, 62, 87, 35, 44, 53, 71};

    int ar_size = sizeof(ar)/sizeof(ar[0]);

    printf("NUMBER OF TRIPLET WITH RECURSIVE %d\n", countTriplet(ar, ar_size, 0, 1, 1, 0));

    return 0;
}
