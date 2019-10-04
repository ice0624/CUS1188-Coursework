//Answer for problem set 4, exercise 2 

public class Mergesort3 {
	public static void main(String args[]) {
		int[] test = {99, 88, 77, 33, 11, 22, 55, 44, 66, 100, 200, 999, 7};
		System.out.print("Original list: ");
		print(test);
		System.out.println();
		
		mergeSort(test);
		System.out.print("Sorted list: ");
		print(test);
	}
	
	public static void mergeSort(int[] array) {
		if(array.length <= 1) {
			return;
		}
		
		int[] first = new int[array.length/3];
		int[] second = new int[(array.length-first.length)/2];
		int[] third= new int[array.length-(first.length+second.length)];
		
		for(int a = 0; a < first.length; a++) {
			first[a] = array[a];
		}
		
		for(int b = 0; b < second.length; b++) {
			second[b] = array[first.length+b];
		}
		
		for(int c = 0; c < third.length; c++) {
			third[c] = array[(first.length+second.length)+c];
		}
		
		mergeSort(first);
		mergeSort(second);
		mergeSort(third);
		
		int x = 0;
		int i1 = 0;
		int i2 = 0;
		int i3 = 0;
		
		while((i1 < first.length) && (i2 < second.length) && (i3 < third.length)) {
			if((first[i1] < second[i2]) && (first[i1] < third[i3])) {
				array[x] = first[i1];
				i1++;
			}
			else if((second[i2] < first[i1]) && (second[i2] < third[i3])) {
				array[x] = second[i2];
				i2++;
			}
			else {
				array[x] = third[i3];
				i3++;
			}
			x++;
		}
		
		if(i1 == first.length) {
			while((i2 < second.length) && (i3 < third.length)) {
				if(second[i2] < third[i3]) {
					array[x] = second[i2];
					i2++;
				}
				else {
					array[x] = third[i3];
					i3++;
				}
				x++;
			}
			
			if(i2 == second.length) {
				for(int i = i3; i < third.length; i++) {
					array[x] = third[i3];
					i3++;
					x++;
				}
			}
			else {
				for(int i = i2; i < second.length; i++) {
					array[x] = second[i2];
					i2++;
					x++;
				}
			}
		}
		else if(i2 == second.length) {
			while((i1 < first.length) && (i3 < third.length)) {
				if(first[i1] < third[i3]) {
					array[x] = first[i1];
					i1++;
				}
				else {
					array[x] = third[i3];
					i3++;
				}
				x++;
			}
			
			if(i1 == first.length) {
				for(int i = i3; i < third.length; i++) {
					array[x] = third[i3];
					i3++;
					x++;
				}
			}
			else {
				for(int i = i1; i < first.length; i++) {
					array[x] = first[i1];
					i1++;
					x++;
				}
			}
		}
		else {
			while((i1 < first.length) && (i2 < second.length)) {
				if(first[i1] < second[i2]) {
					array[x] = first[i1];
					i1++;
				}
				else {
					array[x] = second[i2];
					i2++;
				}
				x++;
			}
			
			if(i1 == first.length) {
				for(int i = i2; i < second.length; i++) {
					array[x] = second[i2];
					i2++;
					x++;
				}
			}
			else {
				for(int i = i1; i < first.length; i++) {
					array[x] = first[i1];
					i1++;
					x++;
				}
			}
		}	
	}
	public static void print(int[] list) {
		for(int i = 0; i < list.length; i++) {
			System.out.print(list[i] + " ~ ");
		}
	}
}
