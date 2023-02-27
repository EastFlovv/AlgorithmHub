import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		while (true) {
			String str = br.readLine();
			if(str.equals("end")) break;
//			모음이 없으면 패스워드 불통
//			if(!vowel(str)) {
//				sb.append("<").append(str).append("> is not acceptable").append("\n");
//				continue;
//			}
			
			int vow = 0;
			int con = 0;
			char beforeChar = ' ';
			boolean doubleChar = false;
			boolean isFail = false;
			boolean hasVowel = false;
			
			
			
			for (int i = 0; i < str.length(); i++) {
//								
				char cur = str.charAt(i);
//				1번 조건
				if(!hasVowel && isVowel(cur)) hasVowel = true;
				
//				3번 조건
//				같은글자가 연속으로 오면... fail e나 i가 오면 3번에서 fail
				if(cur == beforeChar) {
//					isEo가 true이면서 세번째 이면
					if(isEo(cur) && doubleChar)  {
//						fail처리
						isFail = true;
						break;
					}else if(isEo(cur)){
//						그렇지 않고 E나 O면 2번 되었음을 처리
						doubleChar = true;
					}else {
//						그냥 두번이면 fail
						isFail = true;
						break;
					}
				}else {
//					연속되지 않으면 doubleChar를 false로 되돌림
					doubleChar = false;
				}
				
//				2번조건
				if(isVowel(cur)) {
					vow++;
					con = 0;
				}else {
					vow = 0;
					con++;
				}
				
//				3번 연속된 con, vow가 나타나면 fail
				if(con == 3 || vow == 3) {
					isFail = true;
					break;
				}
//				현재 글자를 이전 글자로 세팅
				beforeChar = cur;
			}
			
//			실패하지 않았으면 acceptable 처리
			if(!isFail && hasVowel) sb.append("<").append(str).append("> is acceptable.").append("\n");
			else sb.append("<").append(str).append("> is not acceptable.").append("\n");
		}
		
		
		System.out.println(sb);
	}
	
	
	
//	모음이 하나 이상 있는가
	static boolean vowel(String str) {
		if(str.split("a").length > 1) return false;
		if(str.split("e").length > 1) return false;
		if(str.split("i").length > 1) return false;
		if(str.split("o").length > 1) return false;
		if(str.split("u").length > 1) return false;
		return true;
	}
	
	static boolean isVowel(char c) {
		if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') return true;
		return false;
	}
	
	static boolean isEo(char c) {
		if((c == 'e' || c == 'o')) return true;
		return false;
	}
	
}
