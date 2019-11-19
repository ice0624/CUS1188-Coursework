public class BinomialCoefficient {
	
	public static void main(String[] args) {
		
		System.out.println("Binomial Coefficient for n = 1, k = 1: " + binomialC(1,1));
		System.out.println("Binomial Coefficient for n = 5, k = 2: " + binomialC(5,2));
		System.out.println("Binomial Coefficient for n = 4, k = 3: " + binomialC(4,3));
		System.out.println("Binomial Coefficient for n = 10, k = 6: " + binomialC(10,6));
	}
	
	//returns how many ways you can select k from n
	//O(k) space complexity
	public static int binomialC(int n, int k) {
		
		//terminate program early if n = k or k = 0
		if (n == k || k == 0) {
			return 1;
		}
		
		else {
			
			//array to store previous row
			int[] prev = new int[k+1];
			//array to calculate current row
			int[] current = new int[k+1];
			//initialize prev so we can start calculating the row for n = 2
			for(int y = 0; y < prev.length; y++) {
				prev[y] = 1;
			}
			
			//outer loop for n
			for (int i = 1; i <= n; i++) {
				
				//update prev
				for (int x = 1; x <= min(i,k); x++) {
					prev[x] = current[x];
				}
				
				//inner loop for k
				for(int j = 1; j <= min(i, k); j++) {
					//calculate current row from previous row
					current[j] = prev[j-1] + prev[j];
				}
			}
			return current[k];
		}
	}
	
	//helper method, finds minimum of two integers
	public static int min(int a, int b) {
		if(a < b) {
			return a;
		}
		else {
			return b;
		}
	}

}
