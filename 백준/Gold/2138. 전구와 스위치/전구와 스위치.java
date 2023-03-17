import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int size = Integer.parseInt(br.readLine());
		
		boolean[] origin = new boolean[size];
		boolean[] origin2 = new boolean[size];
		boolean[] target = new boolean[size];
		
		String ori = br.readLine();
		for (int i = 0; i < size; i++) {
			origin[i] = ori.charAt(i) == '0' ? false : true;
			origin2[i] = ori.charAt(i) == '0' ? false : true;
		}
		
		String tar = br.readLine();
		for (int i = 0; i < size; i++) {
			target[i] = tar.charAt(i) == '0' ? false : true;
		}
		
		int ans = 0;
		int ans2 = 1;
		
//		if(origin[0] != target[0] || target[1] != origin[1]) ans += pressBtn(origin, 0);
		origin2[0] = !origin2[0];
		origin2[1] = !origin2[1];
		
		for (int i = 1; i < size; i++) {
			if(isPress(origin, target, i)) ans += pressBtn(origin, i);
			if(isPress(origin2, target, i)) ans2 += pressBtn(origin2, i);
		}


		for (int i = 0; i < size; i++) {
			if(origin[i] ^ target[i]) {
				ans = -1;
			}
			if(origin2[i] ^ target[i]) {
				ans2 = -1;
			}
		}
		
		System.out.println(ans == ans2 && ans == -1 ? -1 : ans == -1 || ans2 == -1 ? Math.max(ans, ans2) : Math.min(ans, ans2));
	}
	
	static int pressBtn(boolean[] origin, int i) {
		int o1 = i-1;
		int o2 = i;
		int o3 = i+1;
		
		if(o1 >= 0) origin[o1] = !origin[o1];
		origin[o2] = !origin[o2];
		if(o3 < origin.length) origin[o3] = !origin[o3];
		return 1;
	}

	static boolean isPress(boolean[] origin, boolean[] target, int i) {
		int o1 = i-1;
//		int o2 = i;
//		int o3 = i+1;
		
		if(origin[o1] ^ target[o1]) return true;
//		if(origin[o2] ^ target[o2]) return true;
//		if(o3 < origin.length && origin[o3] ^ target[o3]) return true;
		return false;
	}
	
}