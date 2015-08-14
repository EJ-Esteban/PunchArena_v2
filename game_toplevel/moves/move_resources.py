from operator import add


class move_super:
    """move super class"""
    cost_list = [0]
    spriteName = "errorBlock.gif"
    upgrade_max = 1
    ability_aliases = []  # useful for toggle moves, like grab/throw

    def __init__(self):
        pass

    def cc_prereq(self, n):
        """color credits required to purchase"""
        return [0, 0, 0, 0]

    def cc_n(self, n):
        """color credits granted from purchasing"""
        return [0, 0, 0, 0]

    def cc_cum(self, n):
        x = [0, 0, 0, 0]
        for k in range(1, n + 1):
            foo = self.cc_n(n)
            x = map(add, x, foo)
        return x

    def cost(self, n):
        if n >= len(self.cost_list):
            self.formulaPD(n)
        return self.cost_list[n]

    def description_long(self):
        return ["title", "Long description here AAAAAAA"]

    def description_brief(self, ):
        return ["short title", "longer text"]

    def passive_effects_pre(self):
        """passive effects applied before game"""
        pass
    def passive_effects_arena(self):
        """passive effects applied in the arena"""
        pass

    def arena_move(self, user=None, targets=None, misc1=None, misc2=None):
        """generic move skeleton"""
        pass

    def formulaPD(self, n):
        """grow cost list to size given"""
        formula = 0
        for x in range(len(self.cost_list), n + 1):
            self.cost_list.append(formula)
        return

    def formulaCC(self, n):
        """formula for CC, if necessary.
        Most of the time CC is proportional to cost"""
        return [0, 0, 0, 0]

MOVELIST = [
    "walk",
    "grab",
    "throw",
    "block",
    "punch",
    "speed",
    "tactics",
    "bulk",
    "brawler"
]
