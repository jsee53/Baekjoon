import java.util.Scanner;

class Main {
	
	public static void main(String[] args) {
    	Scanner in = new Scanner(System.in);
    	
    	int N = in.nextInt();
    	int M = in.nextInt();
    	
    	int salary[] = new int[N];
    	for(int i=0; i<N; i++) {
    		salary[i] = in.nextInt();
    	}
    	
    	long sumSalary[] = new long[N];
    	
    	// 1~M 번째 까지의 합을 M번째에 저장
    	for(int i=0; i<M; i++) {
    		sumSalary[M-1] += salary[i];
    	}
    	
    	// 누적합 계산
    	for(int i=M; i<N; i++) {
    		sumSalary[i] = sumSalary[i-1] + salary[i] - salary[i-M];
    	}
    	
    	long result = 0;
    	for(int i=M-1; i<N; i++) {
    		result = Math.max(result, sumSalary[i]);
    	}
    	System.out.print(result);
    }
    
}
