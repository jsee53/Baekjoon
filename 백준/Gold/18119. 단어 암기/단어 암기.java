import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] wordMasks = new int[N];
        
        for (int i = 0; i < N; i++) {
            String word = br.readLine().trim();
            int wordMask = 0;
            for (char ch : word.toCharArray()) {
                wordMask |= (1 << (ch - 'a'));
            }
            wordMasks[i] = wordMask;
        }

        // 초기 모든 알파벳을 기억한 상태
        int bitArray = (1 << 26) - 1;
        
        Set<Character> vowels = new HashSet<>(Arrays.asList('a', 'e', 'i', 'o', 'u'));
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int command = Integer.parseInt(st.nextToken());
            char ch = st.nextToken().charAt(0);

            if (!vowels.contains(ch)) { // 모음은 무시
                if (command == 1) { 
                    bitArray &= ~(1 << (ch - 'a')); // 알파벳 잊기
                } else if (command == 2) {
                    bitArray |= (1 << (ch - 'a')); // 알파벳 기억
                }
            }

            int count = 0;
            for (int wordMask : wordMasks) {
                if ((wordMask & bitArray) == wordMask) {
                    count++;
                }
            }
            sb.append(count).append("\n");
        }

        System.out.print(sb);
    }
}
