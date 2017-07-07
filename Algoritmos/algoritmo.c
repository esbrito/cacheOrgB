#include <stdlib.h>

int main(int argc, char const *argv[])
{
    int counter = 0;
    int i = 0;
    for(i = 0; i < 100000; i++)
    {
        counter++;
        counter = counter * 35;
        counter = counter / 7;
        counter = counter - (counter/2);
    }
    
    float counter2 = 0;
    int i2 = 0;
    for(i2 = 0; i2 < 100000; i2++)
    {
        counter2++;
        counter2 = counter2 * 35;
        counter2 = counter2 / 7;
        counter2 = counter2 - (counter2/2);
    }

    double counter3 = 0;
    int i3 = 0;
    for(i3 = 0; i3 < 100000; i3++)
    {
        counter3++;
        counter3 = counter3 * 35;
        counter3 = counter3 / 7;
        counter3 = counter3 - (counter3/2);
    }
    
}
