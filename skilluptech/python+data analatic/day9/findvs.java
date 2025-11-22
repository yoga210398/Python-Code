import java.util.*;
public class findvs {
// 123456
// 012345
	public static void main(String[] args) {
		Scanner scan =  new Scanner(System.in);
		System.out.println("enter ur str= ");
		String letter=scan.nextLine();// String letter= input();   kihg
		
		int store=0;
		for(int i=0;i<letter.length();i++)
		{
			// k==a,k==e,k==i,k==u,k==o
			//i==a,i==e,i==i
			if(letter.charAt(i)=='a' || letter.charAt(i)=='e' || letter.charAt(i)=='i' || letter.charAt(i)=='o'||letter.charAt(i)=='u')
			{
				System.out.println("vowel present");
				store=1;
				break;
				
			}
		}
		if(store==0)
		{
			System.out.println(":no vowel is present in ur input");
		}
		
		
		
		
		
		

	}

}