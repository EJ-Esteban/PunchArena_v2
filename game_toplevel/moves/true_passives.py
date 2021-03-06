from moves.move_resources import move_super


class sturdy(move_super):
    upgrade_max = 1000
    cost_list = [0, 10, 10, 10, 20, 30, 40, 60, 90, 130]
    spriteName = "sturdyicon.png"

    def description_long(self):
        return ["Sturdy",
                "BE STRONG LIKE MOUNTAIN."
                "\n(+5 HP per level)",
                "True Passive"]

    def cc_n(self, n):
        a = self.cost(n)
        return [int(.5 * a), 0, 0, 0]

    def formulaPD(self, n):
        """grow cost list to size given"""
        formula = 0
        for x in range(len(self.cost_list), n + 1):
            a = self.cost_list[x - 1]
            b = self.cost_list[x - 3]
            self.cost_list.append(a + b)
        return


class tactics(move_super):
    upgrade_max = 1000
    cost_list = [0, 10, 10, 10, 20, 30, 40, 60, 90, 130]
    spriteName = "tacticsicon.png"

    def description_long(self):
        return ["tactics",
                "BE SMART LIKE SUN TZU"
                "\n(+5 MP per level)",
                "True Passive"]

    def cc_n(self, n):
        a = self.cost(n)
        return [0, int(.5 * a), 0, 0]

    def formulaPD(self, n):
        formula = 0
        for x in range(len(self.cost_list), n + 1):
            a = self.cost_list[x - 1]
            b = self.cost_list[x - 3]
            self.cost_list.append(a + b)
        return


class speed(move_super):
    upgrade_max = 1000
    cost_list = [0, 10, 20, 30, 50, 80, 120, 180, 270, 400]
    spriteName = "speedicon.png"

    def description_long(self):
        return ["speed",
                "GO FAST LIKE SANIC"
                "\n(+1 move per level)",
                "True Passive"]

    def cc_n(self, n):
        a = self.cost(n)
        return [0, 0, int(.5 * a), 0]

    def formulaPD(self, n):
        """grow cost list to size given"""
        formula = 0
        for x in range(len(self.cost_list), n + 1):
            a = self.cost_list[x - 1]
            b = self.cost_list[x - 3]
            self.cost_list.append(a + b + 10)
        return


class brawler(move_super):
    upgrade_max = 1000
    cost_list = [0, 10, 10, 20, 30, 50, 80, 130, 210, 340]
    spriteName = "brawlericon.png"

    def description_long(self):
        return ["brawler",
                "GO HARD LIKE PINOCCHIO"
                "\n(+1 dmg per level)",
                "True Passive"]

    def cc_n(self, n):
        a = self.cost(n)
        return [0, 0, 0, int(.5 * a)]

    def formulaPD(self, n):
        """grow cost list to size given"""
        formula = 0
        for x in range(len(self.cost_list), n + 1):
            a = self.cost_list[x - 1]
            b = self.cost_list[x - 2]
            self.cost_list.append(a + b)
        return
