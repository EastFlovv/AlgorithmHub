import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		String[] board = br.readLine().split(" ");
		int y = Integer.parseInt(board[0]);
		int x = Integer.parseInt(board[1]);
		
		int[] nums = new int[x];
		
		st = new StringTokenizer(br.readLine());
		
		for (int i = 0; i < x; i++) {
			nums[i] = Integer.parseInt(st.nextToken());
		}
		
		int left = nums[0];
		int right = nums[x-1];
		int lidx = 0;
		int ridx = x-1;
		
		int ans = 0;
		
		while(lidx != ridx) {
			if(nums[lidx] <= nums[ridx]) {
				lidx++;
				if(left <= nums[lidx]) left = nums[lidx];
				else ans += left - nums[lidx];
			}else {
				ridx--;
				if(right <= nums[ridx]) right = nums[ridx];
				else ans += right - nums[ridx];
			}
		}
		
		System.out.println(ans);
		
	}
}