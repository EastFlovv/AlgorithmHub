import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		
		int tcs = Integer.parseInt(br.readLine());
		
		for (int tc = 1; tc <= tcs; tc++) {
			sb.append("#").append(tc).append(" ");
			
			st = new StringTokenizer(br.readLine());
			int n = Integer.parseInt(st.nextToken());
			int k = Integer.parseInt(st.nextToken());
			
			int[] flash = new int[n];
			int[] blocks = new int[k];
			
			int mx = 0;
			int lx = 0;
			
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < n; i++) {
				int x= Integer.parseInt(st.nextToken());
				flash[i] = x;
				mx = Math.max(mx, x);
				
			}
			
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < k; i++) {
				blocks[i] = Integer.parseInt(st.nextToken());
			}
			
			
			int nx = 0;
			
			while (lx + 1 != mx) {
				nx = (lx + mx) / 2;
				
				boolean isUp = false;
				
				int curCon = 0;
				int kpos = 0;
				
				for (int i = 0; i < n; i++) {
					if(flash[i] <= nx) curCon++;
					else curCon = 0;
					if(curCon == blocks[kpos]) {
						curCon = 0;
						kpos++;
					}
					if(kpos == k) {
						isUp = true;
						break;
					}
				}
				
				if(isUp) mx = nx;
				else lx = nx;
			}
			sb.append(mx).append("\n");
		}
		
		
		
		System.out.println(sb);
		
	}
}
