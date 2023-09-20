import java.util.Scanner;

class Main {
	static StringBuilder sb;
	
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		
		while (in.hasNext()) {
			int N = in.nextInt();
			sb = new StringBuilder();
			
			fibo(1, (int)Math.pow(3, N));
			System.out.println(sb);
		}
	}
	
	static void fibo(int start, int length) {
		if(length==1) {
			sb.append("-");
			return;
		}
		
		// 첫번째 - 재귀로 다시 공백 탐색
		fibo(start, length/3);
		
		// 두번째 공백
		for(int i=start+length/3; i<start+length*2/3; i++) {
			sb.append(" ");
		}
		
		// 세번째 - 재귀로 다시 공백 탐색
		fibo(start, length/3);
	}
    
}
