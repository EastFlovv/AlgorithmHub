import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		st = new StringTokenizer(br.readLine());
		
		int words = Integer.parseInt(st.nextToken());
		int post = Integer.parseInt(st.nextToken());
		
		Set<String> set = new HashSet<>();
		
		for (int i = 0; i < words; i++) {
			set.add(br.readLine());
		}
		
		for (int i = 0; i < post; i++) {
			set.removeAll(Arrays.asList(br.readLine().split(",")));
			sb.append(set.size()).append("\n");
		}
		
		System.out.println(sb);
		
	}
}