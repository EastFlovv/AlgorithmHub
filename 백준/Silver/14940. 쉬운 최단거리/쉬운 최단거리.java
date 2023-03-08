import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	
	static int[] dx = {1, -1, 0, 0};
	static int[] dy = {0, 0 , 1, -1};
	
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		int[][] board = new int[n][m];
		int[][] distance = new int[n][m];
		
		int si = 0;
		int sj = 0;
		
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < m; j++) {
				int x = Integer.parseInt(st.nextToken());
				board[i][j] = x;
				distance[i][j] = Integer.MAX_VALUE;
				
				if(x == 2) {
					si = i;
					sj = j;
				}
			}
		}
		
//		init fin
		
		Queue<int[]> que = new LinkedList<>();
		
		int[] start = {si, sj, 0};
		
		que.add(start);
		
		
		while(que.size() > 0) {
			int[] cur = que.poll();
			int y = cur[0];
			int x = cur[1];
			
			if(distance[y][x] <= cur[2]) continue;
			if(board[y][x] == 0) continue;
			distance[y][x] = cur[2];
			
			for (int i = 0; i < 4; i++) {
				int nx = dx[i] + x;
				int ny = dy[i] + y;
				
				if(nx < 0 || ny < 0 || nx == m || ny == n) continue;
				int[] next = {ny, nx, cur[2] + 1};
				que.add(next);
			}
		}
		
		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				sb.append(board[i][j] == 0 ? 0 : distance[i][j] == Integer.MAX_VALUE ? -1 : distance[i][j]).append(" ");
			}
			sb.append("\n");
		}
		
		System.out.println(sb);
	}
}
