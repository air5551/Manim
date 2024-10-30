from manim import * #type: ignore
from manim.utils.color.XKCD import BLUEBERRY, RASPBERRY #type: ignore


class Man(Scene):
    def construct(self):
        squ = Square()
        tri = Triangle()
        squ.set_fill(color=RASPBERRY, opacity=0.5)
        tri.set_fill(color=BLUEBERRY, opacity=0.5)
        tri.set_color(BLUEBERRY)
        squ.set_color(RASPBERRY)
        tri.next_to(squ, direction=UP, buff=0.5)
        self.play(Create(squ))
        self.play(Create(tri))
        self.play(squ.animate.match_y(mobject=tri))#type: ignore