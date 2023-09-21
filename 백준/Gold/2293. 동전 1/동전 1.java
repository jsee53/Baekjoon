import java.util.Scanner;

class Main {
	
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		
		int N = in.nextInt();
		int K = in.nextInt();
		
		int coin[] = new int[N];
		for(int i=0; i<N; i++) {
			coin[i] = in.nextInt();
		}
		
		int dp[] = new int[K+1];
		dp[0] = 1;
		
		for(int i=0; i<N; i++) {
			for(int j=coin[i]; j<=K; j++) {
				dp[j] = dp[j] + dp[j-coin[i]];
			}
		}
		
		System.out.print(dp[K]);
	}
	
}
