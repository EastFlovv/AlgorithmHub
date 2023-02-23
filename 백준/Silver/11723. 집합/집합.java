import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int orders = Integer.parseInt(br.readLine());
		boolean[] set = new boolean[21];
		
		for (int i = 0; i < orders; i++) {
			
			String[] order = br.readLine().split(" ");

			switch (order[0]) {
			case "add":
				set[Integer.parseInt(order[1])] = true;
				break;
				
			case "remove":
				set[Integer.parseInt(order[1])] = false;
				break;
				
			case "check":
				sb.append(set[Integer.parseInt(order[1])] ? 1 : 0).append("\n");
				break;
				
			case "toggle":
				set[Integer.parseInt(order[1])] = !set[Integer.parseInt(order[1])];
				break;
				
			case "all":
				for (int j = 0; j < set.length; j++) {
					set[j] = true;
				}
				break;
				
			case "empty":
				for (int j = 0; j < set.length; j++) {
					set[j] = false;
				}
				break;
			}
		}
		
		System.out.println(sb);
		
		
		
	}
}
