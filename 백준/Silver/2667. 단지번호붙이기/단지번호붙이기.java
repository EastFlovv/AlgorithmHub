
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
public class Main {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int size = Integer.parseInt(br.readLine());
		boolean[][] visited = new boolean[size][size];
		
		String[][] apart = new String[size][size];
		
		for (int i = 0; i < size; i++) {
			String[] line = br.readLine().split("");
			apart[i] = line;
		}
		
		List<Integer> list = new ArrayList<>();
		
		for (int i = 0; i < apart.length; i++) {
			for (int j = 0; j < apart.length; j++) {
				if(apart[i][j].equals("1") && !visited[i][j]) list.add(dfs(i, j, visited, apart));
			}
		}
		
		list.sort(Comparator.naturalOrder());
		
		for (int i = 0; i < list.size(); i++) {
			if(i == 0) System.out.println(list.size());
			System.out.println(list.get(i));
		}
		
	}
	
	static int[] dx = {1, -1, 0, 0};
	static int[] dy = {0, 0, 1, -1};
	
	public static int dfs(int x, int y, boolean[][] visited, String[][] apart) {
		visited[x][y] = true;
		
		int maxHouses = 1;
		
		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			
			if(nx < 0 || nx == visited.length || ny < 0 || ny == visited.length) continue;
			if(visited[nx][ny] || apart[nx][ny].equals("0")) continue;
			maxHouses += dfs(nx, ny, visited, apart);
		}
		return maxHouses;
	}
	
	
}
