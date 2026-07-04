#include <stdio.h>

int removeDuplicates(int *nums, int numsSize)
{
    int *writer = nums;
    int *reader = writer + 1;
    for (int i = 1; i < numsSize; i++)
    {
        if (*reader != *(reader - 1))
        {
            writer++;
            *writer = *reader;
        }
        reader++;
    }
    return (writer - nums) + 1;
}