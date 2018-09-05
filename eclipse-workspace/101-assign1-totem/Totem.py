"Lavonne Hoang"
'''
Created on Jan 28, 2018

@author: lavonnehoang
'''
import random

if __name__ == '__main__':  
    
#head part functions

    def hair_buzz():
        a1 = r"012345678901234567"
        a2 = r" |||||||||||||||| "
        return a2
    
    def hair_spiky():
        a1 = r"012345678901234567"
        a2 = r" /\/\/\/\/\/\/\/\ "
        return a2 
    
    def hair_longer():
        a1 = r"012345678901234567"
        a2 = r" |||||||||||||||| "
        a3 = r" |||||||||||||||| "
        a4 = r" |||||||||||||||| "
        return a2 + "\n" + a3 + "\n" + a4
    
    def nose_triangle():
        a1 = r"012345678901234567"
        a2 = r" |       /\     | "
        a3 = r" |      /  \    | "
        a4 = r" |     /    \   | "
        return a2 + "\n" +a3 + "\n" +a4
    
    def nose_rightwards():
        a1 = r"012345678901234567"
        a2 = r" |        |\    | "
        a3 = r" |        | \   | "
        a4 = r" |        |  \  | "
        return a2 + "\n" +a3 + "\n" +a4
        
    def nose_leftwards():
        a1 = r"012345678901234567"
        a2 = r" |       /|     | "
        a3 = r" |      / |     | "
        a4 = r" |     /  |     | "
        return a2 + "\n" +a3 + "\n" +a4
    
    def eye_wide():
        a1 = r"012345678901234567"
        a2 = r"   _____  _____   "
        a3 = r"  /     \/     \  "
        a4 = r" |  ()  /   ()  | "
        a5 = r" \____/ \______/  "
        return a2 + "\n" +a3 + "\n" +a4 + "\n" +a5
    
    def eye_narrow():
        a1 = r"012345678901234567"
        a2 = r" |  /\        /\| "
        a3 = r" | |()|      |()| "
        a4 = r" | \_/       \_/| "
        return a2 + "\n" +a3 + "\n" +a4 
    
    def eye_heart():
        a1 = r"012345678901234567"
        a2 = r"  __  __  __  __  "
        a3 = r" /  \/  \/  \/  \ "
        a4 = r" \     / \     /  "
        a5 = r"  \   /   \   /   "
        a6 = r"   \ /     \/     "
        return a2 + "\n" +a3 + "\n" +a4 + "\n" +a5 +"\n" + a6
    
    def mouth_smile():
        a1 = r"012345678901234567"
        a2 = r" ________________ "
        a3 = r" \              / "
        a4 = r"  \____________/  "
        return a2 + "\n" +a3 + "\n" +a4
    
    def mouth_tongue():
        a1 = r"012345678901234567"
        a2 = r" ________________ "
        a3 = r" \   \     /    / "
        a4 = r"  \___\___/____/  "
        return a2 + "\n" +a3 + "\n" +a4
    
    def mouth_open():
        a1 = r"012345678901234567"
        a2 = r" |      ___     | "
        a3 = r" |     |   |    | " 
        a4 = r" |    |    |    | "
        return a2 + "\n" +a3 + "\n" +a4 
    
    def chin_plain():
        a1 = r"012345678901234567"
        a2 = r" |||||||||||||||| "
        a3 = r" |||||||||||||||| "
        return a2 + "\n" +a3
        
    def chin_curvy():
        a1 = r"012345678901234567"
        a2 = r" {{{{{{{{}}}}}}}} "
        a3 = r" {{{{{{{{}}}}}}}} "
        return a2 + "\n" +a3
    
    def chin_combo():
        a1 = r"012345678901234567"
        a2 = r" |||||||||||||||| "
        a3 = r" {{{{{{{{}}}}}}}} "
        return a2 + "\n" +a3
    
    #whole head functions
    
    def head_plain():
        """
        Print a head that looks fairly normal with narrow eyes, 
        a triangle nose, a buzz cut, a smile, and a plain chin. 
        """
        print (hair_buzz())
        print (eye_narrow())
        print (nose_triangle())
        print (mouth_smile())
        print (chin_plain())
        
    def head_hearteyes():
        """
        Print a head that looks like it's in love with heart eyes,
        a rightward facing nose, longer hair, a smile, and a curvy
        chin.
        """
        print (hair_longer())
        print (eye_heart())
        print (nose_rightwards())
        print (mouth_smile())
        print (chin_curvy())
        
    def head_surprised():
        """
        Print a surprised-looking head with big eyes, a leftward facing nose,
        spiky hair, an open mouth, and a curvy and plain chin.
        """
        print (hair_spiky())
        print (eye_wide())
        print (nose_leftwards())
        print (mouth_open())
        print (chin_combo())
        
    #fixed totem function    
    
    def totem_fixed():
        """
        Print the same totem pole with three heads: one surprised,
        one plain, and one in love. 
        """
        head_surprised()
        head_plain()
        head_hearteyes()
        
    def head_with_hair(hairfunc):
        """
        Print a head with big narrow eyes, a triangle nose, a smile,
        a plain chin, but with hair specified by hairfunc.
        """
        print (hairfunc())
        print (eye_narrow())
        print (nose_triangle())
        print (mouth_smile())
        print (chin_plain())
        
    def head_with_eyes_and_mouth(eyefunc, mouthfunc):
        """
        Print a head with longer hair, a leftwards nose, and a curvy chin
        but with eyes and a mouth specified by eyefunc and mouthfunc. 
        """
        print (hair_longer())
        print (eyefunc())
        print (nose_leftwards())
        print (mouthfunc())
        print (chin_curvy())
        
    def head_with_chin(chinfunc):
        """
        Print a head with spiky hair, a rightwards nose, a combo of plain and
        curvy chin, wide eyes, an open mouth, but with a chin specified
        by chinfunc.
        """
        print (hair_spiky())
        print (eye_wide())
        print (nose_rightwards())
        print (mouth_open())
        print (chinfunc())
        
    def selfie_band():
        a1 = r"012345678901234567"
        a2 = r" ++++----++++---- "   
        a3 = r" |lh260    lh260| "
        a4 = r" ++++----++++---- "
        return a2 + "\n" +a3 + "\n" +a4 
    
    def selfie(eyefunc, nosefunc, mouthfunc):
        """
        prints a whole head with a selfie band, buzzed hair, a curvy
        chin, and eyes, nose, and mouth specified by eyefunc, nosefunc,
        and mouthfunc respectively.
        """
        print (hair_buzz())
        print (selfie_band())
        print (eyefunc())
        print (nosefunc())
        print (mouthfunc())
        print (chin_curvy())
        
    def totem_selfie():
        """
        prints three different totem heads from the selfie function
        specified above.
        """
        selfie(eye_heart, nose_leftwards, mouth_open)
        selfie(eye_wide, nose_triangle, mouth_tongue)
        selfie(eye_heart, nose_rightwards, mouth_smile)
        
    def totem_random():
        """
        prints three random totem heads from the random head function 
        created below.
        """
        random_head()
        random_head()
        random_head()
        
    def random_head():
        """
        creates a random totem head using a random number generator
        that chooses from the three whole head functions created
        earlier in the program.
        """
        x = random.randint(1,3)
        if x==1: 
            head_hearteyes()
        elif x==2:
            head_surprised()
        else:
            head_plain()
        
    print("\nfixed totem\n")
    totem_fixed()
    
    print("\nself totem\n")
    totem_selfie()
    
    print("\nrandom totem\n")
    totem_random()

    
    