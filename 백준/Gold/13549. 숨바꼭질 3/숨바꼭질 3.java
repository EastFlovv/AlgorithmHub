import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;

import java.util.PriorityQueue;

public class Main {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String[] init = br.readLine().split(" ");
		int start = Integer.parseInt(init[0]);
		int end = Integer.parseInt(init[1]);
		
		int[] dist = new int[100001];
		Arrays.fill(dist, Integer.MAX_VALUE);
		dist[start] = 0;
		
		PriorityQueue<Integer> pq = new PriorityQueue<>(new Comparator<Integer>() {
			@Override
			public int compare(Integer o1, Integer o2) {
				return dist[o1] - dist[o2];
			}
		});
		
		pq.add(start);
		
		while (pq.size() > 0) {
			int cur = pq.poll();
			if(cur == end) {
				System.out.println(dist[cur]);
				break;
			}
			
			if(cur + 1 < dist.length && dist[cur + 1] > dist[cur]) {
				dist[cur + 1] = dist[cur] + 1;
				pq.add(cur + 1);
			}
			
			if(cur - 1 >= 0 && dist[cur - 1] > dist[cur]) {
				dist[cur - 1] = dist[cur] + 1;
				pq.add(cur - 1);
			}
			
			if(cur * 2 < dist.length && dist[cur * 2] > dist[cur]) {
				dist[cur * 2] = dist[cur];
				pq.add(cur * 2);
			}
		}
		
		
	}
}
