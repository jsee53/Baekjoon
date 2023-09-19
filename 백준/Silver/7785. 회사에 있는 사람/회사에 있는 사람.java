import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;

class Main {
	
	public static void main(String[] args) {
    	Scanner in = new Scanner(System.in);
    	
    	HashMap<String, String> map = new HashMap<String, String>();
    	
    	int N = in.nextInt();
    	for(int i=0; i<N; i++) {
    		String name = in.next();
    		String check = in.next();
    		if(map.containsKey(name)) {
    			map.remove(name);
    		}
    		else {
    			map.put(name, check);
    		}
    	}
    	
    	List<String> result = new ArrayList<>(map.keySet());
    	// ArrayList를 사전순으로 정렬
        Collections.sort(result);

        // 역순으로 뒤집기
        Collections.reverse(result);
    	
    	for (String re : result) {
            System.out.println(re);
        }
    }
    
}
