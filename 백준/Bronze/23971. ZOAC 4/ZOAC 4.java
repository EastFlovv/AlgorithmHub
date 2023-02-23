import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String[] data = br.readLine().split(" ");
		
		double h = Integer.parseInt(data[0]);
		double w = Integer.parseInt(data[1]);
		double hn = Integer.parseInt(data[2]);
		double wm = Integer.parseInt(data[3]);
		
		int x = (int) Math.ceil(h / (hn + 1));
		int y = (int) Math.ceil(w / (wm + 1));
		System.out.println(x*y);
		
		
		
	}
}
