from manimlib.imports import *


class PlottingGraphs(GraphScene):
    CONFIG = {
        "x_min": -4,
        "x_max": 4,
        "y_min": -2,
        "y_max": 2,
        "graph_origin": ORIGIN,
        "x_labeled_nums": list(range(-4, 5)),
        "y_labeled_nums": list(range(-2, 3)),
        "x_axis_width": 12,
        "y_axis_height": 4,
        "total_fourier_terms": 21,
    }

    def construct(self):
        XTD = self.x_axis_width / (self.x_max - self.x_min)
        YTD = self.y_axis_height / (self.y_max - self.y_min)

        # 		sq_wave=self.get_graph(self.sqwave)
        title1 = TextMobject(
            r"Any Periodic function ($f(x)$) with period L obeying Dirichlet's \\ Condition can be represented by Fourier Series $--$"
        ).to_edge(2 * UP)
        title2 = (
            TextMobject(
                r" $f(x)=\sum_{n=0}^{\infty}(a_n Cos(\frac{2\pi nx}{L})+b_n Sin(\frac{2\pi nx}{L}))$ "
            )
            .set_color(GOLD)
            .next_to(title1, 2 * DOWN)
        )
        title3 = TextMobject(
            r"Let's see how increasing number of terms in Fourier Series \\ can approximate a Square Wave function "
        ).next_to(title2, 4 * DOWN)
        self.play(ShowCreation(title1))
        self.wait(3)
        self.play(ShowCreation(title2))
        self.wait(2)
        self.play(ShowCreation(title3))
        self.wait(5)
        self.play(FadeOut(title1), FadeOut(title2))

        term_text = (
            TextMobject(r"No of fourier Terms \large{n} $=$")
        ).to_corner(UL)
        self.play(ReplacementTransform(title3, term_text))

        self.setup_axes(animate=True)

        # Plotting the fourier terms using loop
        # 		self.bn=np.array([ 0, 0.63661977, -0.31830989,  0.21220659 ,-0.15915494 , 0.12732395, -0.1061033, 0.09094568 ,-0.07957747,  0.07073553 ,-0.06366198 , 0.05787452, -0.05305165,0.04897075 ,-0.04547284 , 0.04244132, -0.03978874 , 0.03744822,-0.03536777,0.0335063  ,-0.03183099]) #Data for sawtooth wave
        # coefficients collected form a separete fourier program for square wave
        self.bn = np.loadtxt("fourier_coeff.txt", unpack=True)  

        for N in range(self.total_fourier_terms):
            if (
                self.bn[N] > 1e-5 or N == 0
            ):  # excluding terms having small coefficient value
                self.fourier_term_no = N
                term_num = TextMobject("$%d$" % N).next_to(
                    term_text, RIGHT
                )
                get_func = self.get_graph(
                    self.sin_terms
                ).set_color(BLUE)

                if N > 0:
                    self.play(
                        ReplacementTransform(
                            previous_func, get_func
                        ),
                        ReplacementTransform(
                            previous_term, term_num
                        ),
                    )
                else:
                    self.play(
                        ShowCreation(get_func),
                        ShowCreation(term_num),
                    )
                print(N)
                previous_func = get_func
                previous_term = term_num
                self.wait(1.4)

    # 	def sqwave(self,x):
    # 		period =8.0
    # 		if ((self.x_max - x)%(period/2.0))<1:
    # 			return 1
    # 		else :
    # 			return -1

    def sin_terms(self, x):
        l = 4  # periodicity of the function
        func = 0.0  # a0 term
        for n in range(1, 1 + self.fourier_term_no):
            func = func + (
                self.bn[n] * np.sin(2 * PI * n * x / l)
            )
        return func
