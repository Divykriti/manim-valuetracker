from manim import*
import math

class ArithValueTracker(ValueTracker):
    def __add__(self, other):
        if hasattr(other, 'get_value'):
            return self.get_value() + other.get_value()
        return self.get_value() + other
    
    def __mul__(self, other):
        if hasattr(other, 'get_value'):
            return self.get_value() * other.get_value()
        return self.get_value() * other
    
class HingedSquares(Scene):
    def construct(self):

        #initial values
        a = ArithValueTracker(0)        #angle
        r = 2                           #radius
        h = 0                           #center of main circle x-coord
        k = 0                           #center of main circle y-coord

        #returns point on circle with given radius r and center (h,k)
        def circ(x):
            return [r*math.cos(x)+h, r*math.sin(x)+k, 0]
        
        #main circle and moving dot on it
        c = Circle(radius = r).move_to([h,k,0])            
        d = Dot(circ(a))

        self.add(c,d)
        self.play(a.animate.set_value(PI))
