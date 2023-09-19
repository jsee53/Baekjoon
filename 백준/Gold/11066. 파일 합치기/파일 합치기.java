import java.util.Scanner;

class Main {
	
	public static void main(String[] args) {
    	Scanner in = new Scanner(System.in);
    	
    	StringBuilder sb = new StringBuilder();
    	
    	int T = in.nextInt();
    	for(int i=0; i<T; i++) {
    		int K = in.nextInt();
    		int file[] = new int[K];
    		for(int j=0; j<K; j++) {
    			file[j] = in.nextInt();
    		}
    		
    		
    		int dp[][] = new int[K+1][K+1];
    		int sum[] = new int[K+1];
    		
    		for(int j=1; j<=K; j++) {
    			sum[j] = sum[j-1] + file[j-1];
    		}
    		
    		for(int end=1; end<=K; end++) {
    			for(int start=end-1; start>=1; start--) {
    				dp[start][end] = Integer.MAX_VALUE;
    				for(int mid=start; mid<end; mid++) {
    					dp[start][end] = Math.min(dp[start][end], dp[start][mid]+dp[mid+1][end]);
    				}
    				dp[start][end] += sum[end] - sum[start-1];
    			}
    		}
    		
    		sb.append(dp[1][K]+"\n");
    	}
    	
    	System.out.print(sb);
    }
    
}
