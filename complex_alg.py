from manimlib.imports import *


class PlottingGraphs(GraphScene):
    CONFIG = {
        "x_min": -2,
        "x_max": 10,
        "y_min": -2,
        "y_max": 10,
        "graph_origin": ORIGIN + 2 * (2 * LEFT + DOWN),
        "x_axis_label": "$Re(z)$",
        "y_axis_label": "$Im(z)$",
        "x_labeled_nums": list(np.arange(-2, 11, 2)),
        "y_labeled_nums": list(np.arange(-2, 11, 2)),
        "x_axis_width": 10,
        "y_axis_height": 6,
    }

    def construct(self):
        XD = self.x_axis_width / (self.x_max - self.x_min)
        YD = self.y_axis_height / (self.y_max - self.y_min)

        title = TextMobject(
            r"Seeing the Addition of two Complex Numbers \\ in Complex Plane"
        )

        X = XD * RIGHT
        Y = YD * UP

        a1 = 4 * X + 4 * Y
        a2 = 2 * X + 5 * Y
        a = a1 + a2

        v1 = Vector(direction=a1).set_color(BLUE)
        v1.shift(self.graph_origin)
        v2 = Vector(direction=a2).set_color(YELLOW)
        v2.shift(self.graph_origin)
        v = Vector(direction=a).set_color(GREEN)
        v.shift(self.graph_origin)

        v1_lx = (DashedLine(ORIGIN, 4 * X)).set_color(BLUE)
        v1_ly = (DashedLine(ORIGIN, 4 * Y)).set_color(BLUE)
        v1_lx.shift(v1.get_corner(LEFT + UP))
        v1_ly.shift(v1.get_corner(RIGHT + DOWN))

        v2_lx = (DashedLine(ORIGIN, 2 * X)).set_color(YELLOW)
        v2_ly = (DashedLine(ORIGIN, 5 * Y)).set_color(YELLOW)
        v2_lx.shift(v2.get_corner(LEFT + UP))
        v2_ly.shift(v2.get_corner(RIGHT + DOWN))

        v_lx = (DashedLine(ORIGIN, 6 * X)).set_color(GREEN)
        v_ly = (DashedLine(ORIGIN, 9 * Y)).set_color(GREEN)
        v_lx.shift(v.get_corner(LEFT + UP))
        v_ly.shift(v.get_corner(RIGHT + DOWN))

        v1_text = TextMobject(r"$z_1=4+4i$")
        v2_text = TextMobject(r"$z_2=2+5i$")
        v_text = TextMobject(r"$z=z_1+z_2$")
        v_text1 = TextMobject(r"$=6+9i$").scale(0.8)
        v1_text = (v1_text.next_to(v1)).scale(0.8)
        v2_text = (v2_text.next_to(v2)).scale(0.8)
        v_text = v_text.shift(
            1.3 * v.get_corner(UP + RIGHT)
        ).scale(0.8)
        v_text1 = v_text1.next_to(v_text, DOWN)

        z_2 = VGroup(*[v2, v2_text, v2_lx, v2_ly])

        self.play(ShowCreation(title))
        self.wait(2)
        self.play(FadeOut(title))

        self.setup_axes(animate=True)
        self.wait(0.5)

        self.play(ShowCreation(v1))
        self.play(
            ShowCreation(v1_text),
            ShowCreation(v1_lx),
            ShowCreation(v1_ly),
        )
        self.wait(0.5)

        self.play(ShowCreation(v2))
        self.play(
            ShowCreation(v2_text),
            ShowCreation(v2_lx),
            ShowCreation(v2_ly),
        )
        self.wait(0.5)

        self.play(ApplyMethod(z_2.shift, a1))
        self.play(
            ApplyMethod(v1_lx.shift, 5 * Y),
            ApplyMethod(v1_ly.shift, 2 * X),
            ApplyMethod(v1_text.shift, 2 * X),
        )
        self.wait(1)

        self.play(ShowCreation(v))
        self.play(ShowCreation(v_text))
        self.play(
            ShowCreation(v_text1),
            Transform(VGroup(v1_lx, v2_lx), v_lx),
            Transform(VGroup(v1_ly, v2_ly), v_ly),
        )
        self.wait(3)
