# from @鹤翔万里
# 使用-st导出带alpha通道的png图片

from manimlib.imports import *

class Nameplate4K_white(Scene):
    CONFIG = {
        "text_color": WHITE,
        "sheen_fac": -0.4,
        "sheen_dir": LEFT,
        "text_sheen_dir": RIGHT,
    }
    def construct(self):
        k = Text("4K", font="Orbitron").scale(2.6).shift(UP*0.6).set_color(self.text_color).set_sheen_direction(self.text_sheen_dir)
        rec1 = RoundedRectangle(height=4, width=7, color=GOLD, fill_opacity=0, stroke_width=30)
        rec2 = Rectangle(height=1.3, width=6.8, color=GOLD, fill_opacity=1).next_to(rec1.get_bottom(), UP, buff=0.1)
        recs = VGroup(rec1, rec2)
        rec1.set_sheen(self.sheen_fac, self.sheen_dir)
        rec2.set_sheen(self.sheen_fac, self.sheen_dir)
        ultraHD = VGroup(
            Text("ULTRA", font="Source Han Sans CN Light", color=BLACK).scale(1.2),
            Text("HD", font="Source Han Sans CN Bold", color=BLACK).scale(1.2)
        ).arrange(RIGHT, buff=0.5).move_to(rec2).shift(DOWN*0.1)

        self.add(recs, k, ultraHD)


class Nameplate4K_black(Nameplate4K_white):
    CONFIG = {
        "text_color": BLACK,
        "sheen_fac": -0.4,
        "sheen_dir": LEFT,
    }


# 这个比较好看
class Nameplate4K_gold(Nameplate4K_white):
    CONFIG = {
        "text_color": [GOLD_E, GOLD_A],
        "sheen_fac": -0.3,
        "sheen_dir": LEFT,
        "text_sheen_dir": UR,
    }