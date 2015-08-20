from moves.move_resources import move_super


class fflurry(move_super):
    upgrade_max = 1
    cost_list = [0, 70]
    spriteName = "blankTile.png"

    def description_long(self):
        return ["Fist Flurry",
                "Attacks using the player's basic punch three times in rapid succession. Any punch bonuses are applied to each attack. Any special or random effects (e.g., miss, poison...) may be applied at each punch independently of the other two."
                "Equippable Skill"]

    def cc_prereq(self, n):
        if n > self.upgrade_max:
            return 0
        return [0, 20, 60, 0]

    def cc_n(self, n):
        if n > self.upgrade_max:
            return 0
        return [0, 10, 30, 0]


class bigslam(move_super):
    upgrade_max = 2
    cost_list = [0, 100, 300]
    spriteName = "blankTile.png"

    def description_long(self):
        return ["Reckless Slam",
                "The player recklessly throws themselves at their opponent. They hit for high damage proportional to their remaining health. User then take damage proportional to their max health. If the enemy can be pushed, they will be pushed in a direction. If not, they will take a small amount of extra damage. Damage will still be taken if blow is evaded.",
                "Equippable Skill"]

    def cc_prereq(self, n):
        if n > self.upgrade_max:
            return 0
        a = b = 0
        if n == 1:
            a = 50
            b = 100
        elif n == 2:
            a = 150
            b = 300
        return [a, b, 0, 0]

    def cc_n(self, n):
        if n > self.upgrade_max:
            return 0
        a = b = 0
        if n == 1:
            a = 30
            b = 60
        elif n == 2:
            a = 100
            b = 200
        return [a, b, 0, 0]


class pdriver(move_super):
    upgrade_max = 1
    cost_list = [0, 200, 400, 600]
    spriteName = "blankTile.png"

    def description_long(self):
        return ["Pile Driver",
                "Deals massive damage to grappled opponents. Leaves opponents confused. Releases grapple.",
                "Equippable Skill"]

    def cc_prereq(self, n):
        if n > self.upgrade_max:
            return 0
        a = int(.4 * self.cost(n))
        return [0, a, 0, a]

    def cc_n(self, n):
        if n > self.upgrade_max:
            return 0
        a = int(.1 * self.cost(n))
        return [0, a, 0, a]
