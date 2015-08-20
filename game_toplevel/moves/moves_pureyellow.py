from moves.move_resources import move_super


class bknux(move_super):
    upgrade_max = 3
    cost_list = [0, 10, 40, 90]
    spriteName = "blankTile.png"

    def description_long(self):
        return ["Brass Knuckles",
                "The player is wielding a bunch of brass tacks! While this makes their punches hurt more, the user also occasionally pokes themselves when they punch.",
                "Equippable Passive"]

    def cc_prereq(self, n):
        if n > self.upgrade_max:
            return 0
        a = self.cost(n) + 5
        return [0, a, 0, 0]

    def cc_n(self, n):
        if n > self.upgrade_max:
            return 0
        a = self.cost(n) - 5
        return [0, a, 0, 0]


class bblow(move_super):
    upgrade_max = 3
    cost_list = [0, 20, 40, 80]
    spriteName = "blankTile.png"

    def description_long(self):
        return ["Breaking Blow",
                "The user yells menacingly while punching. This results in a devastating blow that ignores blocks and does extra damage. At higher levels deals extra damage to blocking enemies.",
                "Equippable Skill"]

    def cc_prereq(self, n):
        if n > self.upgrade_max:
            return 0
        a = self.cost(n) - 5
        return [0, a, 0, 0]

    def cc_n(self, n):
        if n > self.upgrade_max:
            return 0
        a = int(.5 * self.cost(n))
        return [0, a, 0, 0]
