from manim import * #type: ignore
from manim.utils.color.X11 import LIGHTBLUE
from manim.utils.color.XKCD import LIGHTAQUA, PINKISH, PURPLEPINK, VERYLIGHTPINK
from manim.utils.color.core import RGB_Tuple_Float, RGB_Tuple_Int #type: ignore
# Global Variables
# the type: Ignores is because Pyright is dumb
tri = Triangle()
circle = Circle()
square = Square()
cone = Cone()
rectangle = Rectangle()
class CreateCircle(Scene):
    def construct(self):
        circle = Circle()
        # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen
        self.play(FadeOut(circle))

class Scene2(Scene):
    def construct(self):
         SquareArrow = ArrowSquareFilledTip()
         SquareArrow.set_fill(GREEN, opacity=0.5)
         SquareArrow.set_y(10)
         self.play(Create(SquareArrow))
class Transformations(Scene):
    def construct(self):
        square.set_fill(BLUE,opacity=0.5)
        square.rotate(PI / 4)
        cone.next_to(square, buff = 0.5)
        cone.set_fill(GREEN, opacity=0.4)
        self.play(Create(cone))
        self.play(FadeTransform(square,circle))
        self.play(Transform(circle,tri))
        self.play(FadeOut(tri))


class Rotation(Scene):
    def construct(self):
        deg = 1.570796327
        #This is 90 degress in Radians (and remember that radians are the devil)
        tricolor =  BLUE
        tri2 = Triangle()
        tri2color = tricolor
        tri3 = Triangle()
        tri3color = PINKISH
        tri4color = tri3color
        tri4 = Triangle()
        square.set_fill(BLACK, opacity=0.5)
        tri.set_fill(tricolor,opacity=0.5)
        tri2.set_fill(tri2color,opacity=0.5)
        tri3.set_fill(tri3color,opacity=0.5)
        tri4.set_fill(tri4color,opacity=0.5)
        #This sets the Lines Colors
        tri.set_color(tricolor)
        tri2.set_color(tri2color)
        tri3.set_color(tri3color)
        tri4.set_color(tri4color)
        tri2.next_to(square, direction=DOWN, buff=0.5)
        tri3.next_to(square, direction=UP, buff=0.5)
        tri4.next_to(square, direction=LEFT, buff=0.4)
        tri.next_to(square, buff=0.4)
        self.play(Create(square))
        self.play(Create(tri), Create(tri3))
        self.play(Create(tri4), Create(tri2))
        self.play(square.animate.rotate(PI/4)) #type: ignore
        self.play(tri.animate.rotate_about_origin(deg), #type: ignore
        tri2.animate.rotate_about_origin(deg), # type:ignore 
        tri3.animate.rotate_about_origin(deg), #type: ignore
        tri4.animate.rotate_about_origin(deg))#type: ignore
        self.play(tri.animate.rotate(deg), #type: ignore
            tri3.animate.rotate(PI), #type: ignore
            tri4.animate.rotate(-deg)) #type: ignore
        self.play(FadeToColor(square, color=WHITE))# type: ignore
        self.wait(duration=1)
        self.play(Unwrite(square))
        self.play(
            Unwrite(tri), 
            Unwrite(tri2), 
            Unwrite(tri3), 
            Unwrite(tri4))
        
class Align(Scene):
    def construct(self):
        tri2 = Triangle()
        tri3 = Triangle()
        tri4 = Triangle()
        tri.next_to(square,direction=RIGHT, buff=0.4)
        tri2.next_to(square,direction=UP, buff=0.6)
        tri3.next_to(square, direction=DOWN, buff=0.5)
        tri4.next_to(square, direction=LEFT, buff=0.4)
        square.set_fill(color=GREEN, opacity=0.4)
        self.play(Create(square),Create(tri),
            Create(tri2),
            Create(tri3),
            Create(tri4))
        self.play(square.animate.rotate(PI/4),#type: ignore
            tri.animate.rotate(1.5708),#type: ignore
            tri4.animate.rotate(-1.570796327), #type: ignore
            tri2.animate.rotate(PI)) #type: ignore


class Rect(Scene):
    def construct(self):
        rectangle.set_fill(color=GREEN, opacity=0.5)
        self.play(Create(rectangle))
        self.play(rectangle.animate.rotate(PI/4)) #type: ignore
        

class DarkThemeBanner(Scene):
    def construct(self):
        banner = ManimBanner()
        self.play(banner.create())
        self.play(banner.expand())
        self.wait()
        self.play(Unwrite(banner))
