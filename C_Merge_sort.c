/* not in place sort
 * Better than bubble, selection and insertion as time complexity is (n logn)
 * Logic is, recursive, divide and sort
 */

#include <stdio.h>
#include <string.h>

int input_set[5];
int temp[5];


void PrintSet(int * arr, int len)
{
	int i;
	for(i=0 ; i<len; i++)
	{
		printf("%d\t",arr[i]);
	}
	printf("\n");
}

void merge(int arr[], int b, int m, int e)
{
	int i, j, k;
	
	for(i=b, j=m+1, k=b; i<=m && j<=e; k++)
	{
		if(arr[i] <= arr[j])
		{
			temp[k] = arr[i];
			i++;
		}
		else
		{
			temp[k] = arr[j];
			j++;
		}
	}
	
	while(i<=m)
	{
		temp[k]=arr[i];
		k++;
		i++; 
	}

	while(j<=e)
	{
		temp[k] = arr[j];
		k++;
		j++;
	}
	for(i=b; i<=e ; i++)
		arr[i] = temp[i];

	PrintSet(temp,5);
}

void mergesort(int * in_set, int begin_index, int end_index)
{
	if( begin_index < end_index )
	{
		int mid_index = (begin_index + end_index)/2;
		mergesort(in_set, begin_index, mid_index);
		mergesort(in_set, mid_index+1, end_index);

		merge(in_set, begin_index, mid_index, end_index);
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
	
	memset(temp,0,len);

	mergesort(input_set, 0, len-1);

	printf("Sorted Array : ");
	PrintSet(input_set, len);
	
	return 0;
}

