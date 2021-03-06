from manimlib.imports import *


class PlottingGraphs(GraphScene):
    CONFIG = {
        "x_min": -4,
        "x_max": 4,
        "y_min": 0,
        "y_max": 2,
        "graph_origin": ORIGIN + 2 * DOWN,
        "x_labeled_nums": range(-4, 5),
        "y_labeled_nums": None,
        "y_axis_label": " ",
        "x_axis_width": 12,
        "y_axis_height": 5,
        "rt": 2,
    }

    def construct(self):
        X = RIGHT * self.x_axis_width / (self.x_max - self.x_min)
        Y = UP * self.y_axis_height / (self.y_max - self.y_min)

        intro = TextMobject(
            r"The probability density function is -\\ \vspace{2ex}",
            r"$\rho(x,t)$",
            r"$=\dfrac{2}{\pi\hbar}\cos^2\left(\dfrac{Px-Et}{2\hbar}\right)$\\ \vspace{4ex}",
            r"Where,",
            " $P=p_2-p_1$",
            " and",
            "$E=E_2-E_1$",
        )

        intro[1:3].set_color(GREEN).set_stroke(width=1.4)
        intro[4].set_color(BLUE).set_stroke(width=1.2)
        intro[6].set_color(BLUE).set_stroke(width=1.2)

        rho = intro[1].copy()
        self.play(Write(intro), run_time=4)

        self.wait(5)

        self.add(rho)
        self.play(FadeOut(intro), run_time=self.rt)
        self.play(
            rho.next_to,
            self.graph_origin + 2 * Y,
            buff=0.1,
            run_time=self.rt,
        )

        self.setup_axes(animate=False)

        self.wait(1)

        t_tracker = ValueTracker(0)
        t = t_tracker.get_value

        rho_graph = always_redraw(
            lambda: self.get_graph(
                lambda x: np.cos(x - t()) ** 2,
                x_min=-4,
                x_max=4,
                color=GREEN,
            )
        )
        rho_graph.suspend_updating()

        t_label = TexMobject("t = ", color=RED).to_corner(
            UR, buff=1.4
        )
        t_text = always_redraw(
            lambda: DecimalNumber(
                t(),
                color=GOLD,
            ).next_to(t_label, RIGHT, MED_SMALL_BUFF)
        )
        t_text.suspend_updating()
        t_parameter = VGroup(t_label, t_text)

        self.play(
            FadeIn(rho_graph),
            Write(t_parameter),
            run_time=self.rt,
        )
        self.wait(3)
        rho_graph.resume_updating()
        t_text.resume_updating()
        self.play(
            ApplyMethod(
                t_tracker.set_value,
                2.5,
                rate_func=linear,
                run_time=10,
            )
        )

        self.wait(4)
