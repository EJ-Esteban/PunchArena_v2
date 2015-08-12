from moves.move_resources import move_super


class speed(move_super):
    cost_list = [10, 20, 30, 50, 80, 120, 180, 270, 400]
    spriteName = "walkButton"

    def cc_n(self, n):
        return int(.5 * self.cost_list[n - 1])

    def description_long(self):
        return "speed"

    def description_long(self):
        return ["short title", "longer text"]
