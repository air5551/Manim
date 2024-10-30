from manim import * #type: ignore
from manim.utils.color.XKCD import BLUEBERRY, RASPBERRY #type: ignore


class Man(Scene):
    def construct(self):
        squ = Square()
        tri = Triangle()
        tri2 = Triangle()
        squ.set_fill(color=RASPBERRY, opacity=0.5)
        tri.set_fill(color=BLUEBERRY, opacity=0.5)
        tri2.set_fill(color=PURE_BLUE, opacity=0.5)
        tri.set_color(BLUEBERRY)
        squ.set_color(RASPBERRY)
        tri2.set_color(PURE_BLUE)
        tri.next_to(squ, direction=UP, buff=0.8)
        tri2.next_to(tri2, direction=LEFT)
        self.play(Create(squ))
        self.play(Create(tri))
        self.play(Create(tri2))
        self.play(squ.animate.match_y(mobject=tri)) #type: ignore
        self.play(tri2.animate.match_y(mobject=squ)) #type: ignore