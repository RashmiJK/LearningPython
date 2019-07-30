/* In place sort
 * Inefficient
 * Quadratic time complexity
 * Logic is, treat the part of aray as sorted and pick the element from the other part and insert it in the 
 * required order in the sorted part.
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
void InsertionSort(int * in_set, int len)
{
	int i, hole, value;
	/* Considering index 0 as sorted part of the array */
	for(i=1 ; i<len; i++)
	{
		value = in_set[i];
		hole = i;
		while(hole>0 && in_set[hole-1]>value)
		{
			in_set[hole] = in_set[hole-1];
			hole = hole-1;
		}
		in_set[hole] = value;
		PrintSet(input_set, len);
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
	InsertionSort(input_set, len);
	return 0;
}

