#include <iostream>
using namespace std;

void Merge(int *a, int l, int m, int r) {
	//merge two subarray(l,r) of arr[0,1,2,3,4,5]
	// 1st subarray is arr[l...m]
	// 2nd subarray is arr[l...m]

	int i, j, k, temp[r-l+1];
	i = l;
	k = 0;
	j = m + 1;

	//create temporary array
	//int L[] = n1; 
	//int R[] = n2;

	//copy data to temporary array L[] and R[]
	//for (int i = 0; i < n1; i++)
	//	L[i] = arr[l + i];
	//for (int j = 0; j < n2; j++)
	//	R[j] = arr[m + 1 + j];

	//// merge temp array back into arr[l...r]
	//i = 0; // initial index of first sub-array
	//j = 0; // initial index of second sub-array
	//k = l; // initial index of merged sub-array

	while (i <= m && j <= r) {
		if (a[i] <= a[j]) {
			temp[k] = a[i];
			i++;
		}
		else {
			temp[k] = a[j];
			j++;
		}
		k++;
	}

	//copy remaining elements of L[], if there are any
	while (i <= m) {
		temp[k] = a[i];
		i++;
		k++;
	}
	//copy remaining elements of R[], if there are any
	while (j <= r) {
		temp[k] = a[i];
		j++;
		k++;
	}
	//assign sorted data stored in temp[] to a[]
	for (i = l; i <= r; i++) {
		a[i] = temp[i - l];
	}
}

//fn to splot array into two parts
void MergeSort(int *a, int l, int r) {
	int m;
	if (l < r) {
		//same as (l+r)/2, but avoids overflow for large L&h
		int m = (l + r) / 2;
		//sort first & second half
		MergeSort(a, l, m);
		MergeSort(a, m + 1, r);
		//merge them to get sorted output
		Merge(a, l, m, r);
	}
}

void PrintArray(int A[], int size) {
	int i;
	for (i = 0; i < size; i++)
		cout << "" << A[i] << endl;
}

int main() {
	int n, i;
	
	cout << "Give array " << endl;
	cin >> n;

	int arr[n]; 
	for (i = 0; i < n; i++) {
		cout << "Enter element " << i + 1 << ": ";
		cin >> arr[i];
	}

	MergeSort(arr, 0, n-1);

	cout << "Sorted array is" << endl;
	for (i = 0; i < n; i++)
		cout << "->" << arr[i];

	return 0;
}

// Suffering from errors, 
// mostly because of my lack of knowledge in C++