import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine());
		
		int size = Integer.parseInt(st.nextToken());
		
		int target = Integer.parseInt(st.nextToken());
		
		PriorityQueue<Integer> pq = new PriorityQueue<>(
//				new Comparator<Integer>() {
//			public int compare(Integer o1, Integer o2) {
//				return o1-o2;
//			};
//		}
		);
		
		st = new StringTokenizer(br.readLine());
		
		for (int i = 0; i < size; i++) {
			int k = Integer.parseInt(st.nextToken()); 
			pq.add(k);
		}
		
		for (int i = 0; i < target - 1; i++) {
			pq.remove();
		}
		System.out.println(pq.remove());
	}
}