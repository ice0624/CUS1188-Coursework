
public class Test {
	
	public static void main(String[] args) {
		
		int[] test1 = {100, 300, 50, 2, 99, 32};
		int[] test2 = {100, 300, 50, 2, 99, 32};
		
		System.out.print("Original array: ");
		print(test1);
		System.out.println();
		
		int start1 = (int) System.nanoTime();
		selectionsort(test1);
		int end1 = (int) System.nanoTime();
		int time1 = end1-start1;
		print(test1);
		System.out.println("Selection sort runtime: " + time1);
		
		int start2 = (int) System.nanoTime();
		insertionsort(test2);
		int end2 = (int) System.nanoTime();
		int time2 = end2-start2;
		
		print(test2);
		System.out.println("Insertion sort runtime: " + time2);
		
	}
	
	public static void selectionsort(int[] list) {
		for(int i = 0; i < list.length; i++) {
			int minindex = i;
			for(int j = i+1; j<list.length; j++) {
				if(list[j] < list[minindex]) {
					minindex = j;
				}
			}
			int temp = list[i];
			list[i] = list[minindex];
			list[minindex] = temp;
		}
	}
	
	public static void insertionsort(int[] list) {
		for(int i = 1; i < list.length; i++) {
			int current = i;
			while(current > 0 && (list[current] < list[current-1])) {
				int temp = list[current-1];
				list[current-1] = list[current];
				list[current] = temp;
				current--;
			}
		}
	}
	
	public static void print(int[] list) {
		for(int i = 0; i < list.length; i++) {
			System.out.print(list[i] + " ~ ");
		}
	}
}
