import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;

public class Main {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String[] initData = br.readLine().split(" ");
		
		int invited = Integer.parseInt(initData[0]);
		int game = initData[1].equals("Y") ? 1 : initData[1].equals("F") ? 2 : 3;
		
		Set<String> set = new HashSet<>();
		
		for (int i = 0; i < invited; i++) {
			set.add(br.readLine());
		}
		
		System.out.println((int)set.size() / game);
		
		
	}
}