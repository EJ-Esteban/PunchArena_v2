from operator import add


class move_super:
    """move super class"""
    cost_list = [0]
    spriteName = "errorBlock"
    ability_aliases = []  # useful for toggle moves, like grab/throw

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
        return 0

    def description_long(self):
        return "Long description here AAAAAAA"

    def description_long(self):
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


MOVELIST = [
    "speed",
    "bulk",
    "tactics",
    "brawler"
]
