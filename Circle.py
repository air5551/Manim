from manim import * #type: ignore


# class CreateCircle(Scene):
#     def construct(self):
#         circle = Circle()
#         # create a circle
#         circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
#         self.play(Create(circle))  # show the circle on screen
#         self.play(FadeOut(circle))

class Scene2(Scene):
    def construct(self):
         SquareArrow = ArrowSquareFilledTip()
         SquareArrow.set_fill(GREEN, opacity=0.5)
         SquareArrow.set_y(10)
         self.play(Create(SquareArrow))
class Transformations(Scene):
    def construct(self):
        tri = Triangle()
        circle = Circle()
        square = Square()
        square.set_fill(BLUE,opacity=0.5)
        cone = Cone()
        square.rotate(PI / 4)
        cone.next_to(square, buff = 0.5)
        cone.set_fill(GREEN, opacity=0.4)
        self.play(Create(cone))
        self.play(FadeTransform(square,circle))
        self.play(Transform(circle,tri))
        self.play(FadeOut(tri))
