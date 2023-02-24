import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		
		int loop = Integer.parseInt(br.readLine());
		
		for (int i = 0; i < loop; i++) {
			st = new StringTokenizer(br.readLine());
			
			sb.append(st.nextToken()).append(" ");
			int cnt = 0;
			int[] arr = new int[20];
			
			for (int j = 0; j < 20; j++) {
				arr[j] = Integer.parseInt(st.nextToken());
				int cur = j;
				if(j == 0) continue;
				while(cur != 0 && arr[cur] < arr[cur-1]) {
					cnt += swap(cur, cur-1, arr);
					cur--;
				}
			}
			
			sb.append(cnt).append("\n");
		}
		
		System.out.println(sb);
	}

	static int swap(int x, int y, int[] arr) {
		
		int tmp = arr[x];
		arr[x] = arr[y];
		arr[y] = tmp;
		
		return 1;
	}
	
}
