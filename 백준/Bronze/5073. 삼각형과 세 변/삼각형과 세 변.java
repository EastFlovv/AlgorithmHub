import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;


public class Main {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		while (true) {
			String s = br.readLine();
			if(s.equals("0 0 0")) break;
			
			StringTokenizer st = new StringTokenizer(s);
			
			int[] triangle = new int[3];
			int t = 0;
			while (st.hasMoreTokens()) {
				triangle[t++] = Integer.parseInt(st.nextToken());
			}
			
			Arrays.sort(triangle);
			
			if(triangle[0] + triangle[1] <= triangle[2]) {
				sb.append("Invalid").append("\n");
			}else {
				
				String shape = "Equilateral";
				
				for (int i = 0; i < triangle.length - 1; i++) {
					if(triangle[i] != triangle[i+1]) {
						switch (shape) {
						case "Equilateral":
							shape = "Isosceles";
							break;
						case "Isosceles":
							shape = "Scalene";
						}
					}
				}
				
				sb.append(shape).append("\n");
			}
		}
		System.out.println(sb);
	}
}
