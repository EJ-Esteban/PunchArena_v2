from moves.move_resources import move_super


class tithe(move_super):
    upgrade_max = 3000
    cost_list = [60]
    spriteName = "errorBlock.gif"

    def description_long(self):
        return ["Tithe",
                "Convert money into color credits"
                "\nDoes nothing, but gives you color credits",
                "True Passive"]

    def cc_n(self, n):
        if n > self.upgrade_max:
            return 0
        return [5, 5, 5, 5]

    def formulaPD(self, n):
        """grow cost list to size given"""
        formula = 60
        for x in range(len(self.cost_list), n + 1):
            self.cost_list.append(formula)
        return
