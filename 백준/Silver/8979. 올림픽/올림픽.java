import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;

public class Main {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String[] init = br.readLine().split(" ");
		
		int allCountries = Integer.parseInt(init[0]);
		int target = Integer.parseInt(init[1]);
		
		Country[] rank = new Country[allCountries];
		
		for (int i = 0; i < allCountries; i++) {
			String[] data = br.readLine().split(" ");
			
			int c = Integer.parseInt(data[0]);
			int g = Integer.parseInt(data[1]);
			int s = Integer.parseInt(data[2]);
			int b = Integer.parseInt(data[3]);
			
			Country country = new Country(c, g, s, b);
			rank[i] = country;
		}
		
		
		Arrays.sort(rank,new Comparator<Country>() {
			@Override
			public int compare(Country o1, Country o2) {
				return o2.gold - o1.gold != 0 ?
						o2.gold - o1.gold : o2.silver - o1.silver != 0 ?
						o2.silver - o1.silver : o2.bronze - o1.bronze;
			}
		});
		
		int ans = 0;
		
		for (int i = 0; i < allCountries; i++) {
			if(rank[i].country == target) ans = i; 
		}
		
		for (int i = ans; i >= 0 ; i--) {
			if(
					rank[i].gold == rank[i-1].gold &&
					rank[i].silver == rank[i-1].silver &&
					rank[i].bronze == rank[i-1].bronze
					) ans--;
			else break;
		}
		System.out.println(ans + 1);
	}
	
	static class Country{
		int country;
		int gold;
		int silver;
		int bronze;

		public Country(int c, int g, int s, int b) {
			this.country = c;
			this.gold = g;
			this.silver = s;
			this.bronze = b;
		}
	}
	
	
}
