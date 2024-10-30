from manim import * #type: ignore
from manim.utils.color.XKCD import RASPBERRY #type: ignore


class Man(Scene):
    def construct(self):
        squ = Square()
        squ.set_fill(color=RASPBERRY, opacity=0.5)
        squ.set_color(RASPBERRY)
        self.play(Create(squ))