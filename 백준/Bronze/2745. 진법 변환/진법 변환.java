import java.util.Scanner;

class Main {
	
	public static void main(String[] args) {
    	Scanner in = new Scanner(System.in);
    	
    	String N = in.next();
    	int B = in.nextInt();
    	
    	int result = 0;
    	
    	for(int i = 0; i < N.length(); i++) {
    		if(N.charAt(N.length()-i-1)>='A') {
    			result += (N.charAt(N.length()-i-1)-'A'+10) * Math.pow(B, i);
    		}
    		else {
    			result += (N.charAt(N.length()-i-1)-'0') * Math.pow(B, i);
    		}
    	}
    	
    	System.out.print(result);
    }
    
}
