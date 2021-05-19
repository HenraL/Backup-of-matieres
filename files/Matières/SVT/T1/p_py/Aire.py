from math import pi,sqrt
class aire:
    def _init_(self):
        self.PI=pi
    def carré(c=0):
        print(f"{c}*{c}={c*c}²")
        return c*c
    def cercle(self,R=0):
        print("pi*(R)²=r².pi")
        print(f"{self.pi}*({R})²={self.pi*(R)**2}")
        return self.pi*(R)**2
    def rectangle(L=0,l=0):
        """L = longeur, l= largeur"""
        print(f"{L}*{l}={L*l}")
        return L*l
    def triangle(B=0,H=0):
        print(f"({B}*{H})/2 = {(B*H/2)}")
        return (B*H)/2
    def triangle_rectangle(b=0,c=0):
        """C
            |\\
            | \\
            |  \\
            |   \\
           b|    \\a
            |     \\
            |_     \\
            |_|_____\\
            A   c    B"""
        print(f"C\n |\\\n | \\\n |  \\\n |   \\\nb|    \\a\n |     \\\n |_     \\\n |_|_____\\\n A   c    B\n\n({b}*{c})/2 = {(b*c)/2}")
        return (b*c)/2
    def triangle_equilateral(c=0):
        print(f"(sqrt(3)/4)*({c})²={(sqrt(3)/4)*(c)**2}")
        return (sqrt(3)/4)*(c)**2
    def losange(d1=0,d2=0):
        """       /|\\
                 / | \\
                /  |  \\
               /   |   \\
              /    |    \\
             /     |d1   \\
            /      |      \\
           /___d2__|_______\\
           \\       |_|     /
            \\      |      /
             \\     |     /
              \\    |    /
               \\   |   /
                \\  |  /
                 \\ | /
                  \\|/"""
        print(f"       /|\\\n      / | \\\n     /  |  \\\n    /   |   \\\n   /    |    \\\n  /     |d1   \\\n /      |      \\\n/___d2__|_______\\\n\\       |_|     /\n \\      |      /\n  \\     |     /\n   \\    |    /\n    \\   |   /\n     \\  |  /\n      \\ | /\n       \\|/\n\n({d1}*{d2})/2={(d1*d2)/2}")
        return (d1*d2)/2

    def parallelogramme(B=0,h=0):
        """B=base, h=hauteur"""
        print(f"{B}*{h}={B*h}")
        return B*h
    def trapese(Ba=0,Bb=0,h=0):
        """               A__________________________________B
               /                           /|\\    \\
              /              a              |      \\
             /<=============================+=====> \\
            /                               |        \\
           /                                |         \\
          /                                 |          \\
         /                                  |           \\
        /                                   |            \\
       /                                   h|             \\
      /                                     |              \\
     /                                      |               \\
    /                                       |                \\
   /                       b               \\|/                \\
  /<==========================================================>\\
D/______________________________________________________________\\C"""
        
        print(f"\n\n(({Ba}+{Bb})*{h})/2={((Ba+Bb)*h)/2}")
        return ((Ba+Bb)*h)/2
