
public class Totality {
	public int sum(int[] a, String stype) {
		int osum = 0;
		int esum = 0;
		int allsum = 0;

		for(int k = 0; k < a.length; k+=1) {
			
			if (stype.equals("even")) {
				if (k % 2 == 0) {
					esum += a[k];
				}
			}
			else if (stype.equals("odd")){
				if (k % 2 != 0) {
					osum += a[k];
				}
				
			}
			else {
				allsum += a[k];
				
			}
		}
		if (stype.equals("odd")) {
			return osum;			
		}		
		else if (stype.equals("even")) {
			return esum;			
		}		
		return allsum; 
	}
	
	
}
