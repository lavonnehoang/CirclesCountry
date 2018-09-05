public class Gravity {
      public double falling(double time, double velo){
        // fill in code here
    	  double distance;
    	  final double GRAVITY = 9.8;
    	  
    	  distance = (velo * time) + (0.5 * GRAVITY * (time*time));
    	  
    	  return distance;
    	  
    	  
      }
  }