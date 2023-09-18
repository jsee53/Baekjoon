import java.util.Scanner;

class Main {
	
	public static void main(String[] args) {
    	Scanner in = new Scanner(System.in);
    	
    	int N = in.nextInt();
    	int M = in.nextInt();
    	
    	int K = in.nextInt();
    	
    	String chess[][] = new String[N][M];
    	
    	for(int i=0; i<N; i++) {
    		String input = in.next();
    		chess[i] = input.split("");
    	}
    	
    	int chessBlack[][] = new int[N][M];
    	int chessWhite[][] = new int[N][M];
    	
    	for(int i=0; i<N; i++) {
    		for(int j=0; j<M; j++) {
    			if((i+j)%2==0) { // 검정색 판 -> 검정색 칸, 흰색 판 -> 흰색 칸
    				if(chess[i][j].compareTo("B")==0) { // 검정색 판 변화 o, 흰색 판 변화 x
    					chessBlack[i][j] = 0;
    					chessWhite[i][j] = 1;
    				}
    				else {
    					chessBlack[i][j] = 1;
    					chessWhite[i][j] = 0;
    				}
    			}
    			else { // 검정색 판 -> 흰색 칸, 흰색 판 -> 검정색 칸
    				if(chess[i][j].compareTo("W")==0) { // 검정색 판 변화 x, 흰색 판 변화 o
    					chessBlack[i][j] = 0;
    					chessWhite[i][j] = 1;
    				}
    				else {
    					chessBlack[i][j] = 1;
    					chessWhite[i][j] = 0;
    				}
    			}
    		}
    	}
    	
    	int sumChessBlack[][] = new int[N+1][M+1];
    	int sumChessWhite[][] = new int[N+1][M+1];
    	
    	// 누적 합 계산
    	for(int i=0; i<N; i++) {
    		sumChessBlack[i+1][1] = chessBlack[i][0];
    		sumChessWhite[i+1][1] = chessWhite[i][0];
    		for(int j=1; j<M; j++) {
    			sumChessBlack[i+1][j+1] = sumChessBlack[i+1][j] + chessBlack[i][j]; // 행 더하기
    			sumChessWhite[i+1][j+1] = sumChessWhite[i+1][j] + chessWhite[i][j]; // 행 더하기
    		}
    	}
    	
    	for(int i=0; i<M; i++) {
    		for(int j=1; j<N; j++) {
    			sumChessBlack[j+1][i+1] += sumChessBlack[j][i+1]; // 열 더하기
    			sumChessWhite[j+1][i+1] += sumChessWhite[j][i+1]; // 열 더하기
    		}
    	}
    	
    	int count = N * M;
    	for(int i=K; i<=N; i++) {
    		for(int j=K; j<=M; j++) {
    			count = Math.min(count, sumChessBlack[i][j] - sumChessBlack[i-K][j] - sumChessBlack[i][j-K] + sumChessBlack[i-K][j-K]);
    			count = Math.min(count, sumChessWhite[i][j] - sumChessWhite[i-K][j] - sumChessWhite[i][j-K] + sumChessWhite[i-K][j-K]);
    		}
    	}
    	
    	System.out.println(count);
    }
    
}
