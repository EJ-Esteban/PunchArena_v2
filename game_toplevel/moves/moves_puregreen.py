from moves.move_resources import move_super


class feint(move_super):
    upgrade_max = 6
    cost_list = [0, 50, 200, 450, 800, 1250, 1800]
    spriteName = "speedicon.png"

    def description_long(self):
        return ["Feint",
                "The player may pay mana to do extra moves in a turn."
                "\nFor a feint lvl N, player may make up to N extra moves for an increasing amount of mana",
                "Equippable Passive"]

    def cc_prereq(self, n):
        if n > self.upgrade_max:
            return 0
        a = int(.5 * self.cost(n))
        return [0, 0, a, 0]

    def cc_n(self, n):
        if n > self.upgrade_max:
            return 0
        a = int(.3 * self.cost(n))
        return [0, 0, a, 0]


class tornadokick(move_super):
    upgrade_max = 1
    cost_list = [0, 75]
    spriteName = "speedicon.png"

    def description_long(self):
        return ["Echo Kick",
                "The user stops running and uses their remaining leg actions (move) to kick their opponent multiple times. Melee range. Will not destroy breakable tiles."
                "\nCosts 4 mana and all remaining move. Does 2x move expended as damage."
                "Equippable Skill"]

    def cc_prereq(self, n):
        if n > self.upgrade_max:
            return 0
        return [0, 0, 75, 0]

    def cc_n(self, n):
        if n > self.upgrade_max:
            return 0
        a = int(.3 * self.cost(n))
        return [0, 0, 55, 0]
