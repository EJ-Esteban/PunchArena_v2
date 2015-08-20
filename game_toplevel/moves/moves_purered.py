from moves.move_resources import move_super


class heal(move_super):
    upgrade_max = 5
    cost_list = [0, 40, 100, 180, 280, 400]
    spriteName = "blankTile.png"

    def description_long(self):
        return ["Band Aids",
                "the player conjures some bandages, rests, and regains their health.",
                "Equippable Skill"]

    def cc_prereq(self, n):
        if n > self.upgrade_max:
            return 0
        a = int(.25 * self.cost(n))
        return [a, 0, 0, 0]

    def cc_n(self, n):
        if n > self.upgrade_max:
            return 0
        a = int(.5 * self.cost(n)) - 15
        return [a, 0, 0, 0]


class slam(move_super):
    upgrade_max = 1
    cost_list = [0, 75]
    spriteName = "blankTile.png"

    def description_long(self):
        return ["Body Slam",
                "A rather conservative wrestling move. Deals moderate damage based on players current HP..",
                "Equippable Skill"]

    def cc_prereq(self, n):
        if n > self.upgrade_max:
            return 0
        return [75, 0, 0, 0]

    def cc_n(self, n):
        if n > self.upgrade_max:
            return 0
        return [55, 0, 0, 0]
