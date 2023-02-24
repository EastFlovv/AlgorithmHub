import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException {
		
		boolean[] firstWin = new boolean[1001];
		
		for (int i = 1; i < firstWin.length; i++) {
			if(i < 4)
				firstWin[i] = !firstWin[i-1];
			else
				firstWin[i] = !(firstWin[i-1] && firstWin[i-3]);
		}
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		System.out.println(firstWin[Integer.parseInt(br.readLine())] ? "SK" : "CY");
		
		
		
	}
}
