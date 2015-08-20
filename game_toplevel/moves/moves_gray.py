from moves.move_resources import move_super


class tithe(move_super):
    upgrade_max = 5000
    cost_list = [0, 60]
    spriteName = "titheicon.png"

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


class bounty(move_super):
    upgrade_max = 1
    cost_list = [0, 100]
    spriteName = "blanktile.png"

    def description_long(self):
        return ["Bounty",
                "The player meditates on prizes to come. This increases their reward should they win a fight. Has a 2 turn cooldown. Bonus maxes after 5 uses. Bonus is dependant on the opponent beatn.",
                "Equippable Skill"]

    def cc_n(self, n):
        if n > self.upgrade_max:
            return 0
        return [5, 5, 5, 5]
