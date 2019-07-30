/* In place sort
 * Inefficient
 * Quadratic time complexity
 * Logic is, pick the smallest number from input list, put in the lowest possible index
 */

#include <stdio.h>

int input_set[5];


void PrintSet(int * arr, int len)
{
	int i;
	for(i=0 ; i<len; i++)
	{
		printf("%d\t",arr[i]);
	}
	printf("\n");
}
void SelectionSort(int * in_set, int len)
{
	int i, j, temp, iMin;
	for(i=0 ; i<(len-1); i++)
	{
		iMin = i;
		for(j=i+1; j<len ; j++)
		{
			if(in_set[j] < in_set[iMin])
			{
				iMin = j;
			}
		}
		if (i != iMin)
		{
			temp = in_set[i];
			in_set[i] = in_set[iMin];	
			in_set[iMin] = temp;
			printf("i=%d iMin=%d :", i,iMin);
			PrintSet(in_set, len);
		}
	}
}

int main()
{
	int i, len;

	printf("Input numbers: \n");
	len = sizeof(input_set)/sizeof(int);

	for(i=0; i<len; i++)
	{
		scanf("%d",&input_set[i]);
	}
	
	printf("Unsorted Array : ");
	PrintSet(input_set, len);
	SelectionSort(input_set, len);
	return 0;
}

