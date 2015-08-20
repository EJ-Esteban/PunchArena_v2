from moves.move_resources import move_super


class meditate(move_super):
    upgrade_max = 5
    cost_list = [0, 40, 100, 180, 280, 400]
    spriteName = "blankTile.png"

    def description_long(self):
        return ["Meditation",
                "the player conjures some relaxing tea, rests, and regains their mana.",
                "Equippable Skill"]

    def cc_prereq(self, n):
        if n > self.upgrade_max:
            return 0
        a = int(.25 * self.cost(n))
        return [0, 0, 0, a]

    def cc_n(self, n):
        if n > self.upgrade_max:
            return 0
        a = int(.5 * self.cost(n)) - 15
        return [0, 0, 0, a]


class laser(move_super):
    upgrade_max = 4
    cost_list = [0, 20, 40, 80, 160]
    spriteName = "blankTile.png"

    def description_long(self):
        return ["Laser eyes",
                "The user launches a mean look from their eyes that coalesces into an angry blue projectile. Hurts other players a lot, penetrates enemies, and will break breakable tiles. Cannot be evaded. Projectile will not wrap around the map.",
                "Equippable Skill"]

    def cc_prereq(self, n):
        if n > self.upgrade_max:
            return 0
        a = self.cost(n) - 10
        return [0, 0, 0, a]

    def cc_n(self, n):
        if n > self.upgrade_max:
            return 0
        a = int(.5 * self.cost(n)) - 5
        return [0, 0, 0, a]


class poison(move_super):
    upgrade_max = 2
    cost_list = [0, 50, 100]
    spriteName = "blankTile.png"

    def description_long(self):
        return ["Poisonous Blow",
                "The attacker hurls a dagger covered in their own saliva. will inflict small damage on the opponent and apply \"Ack, germs!\" on the opponent, dealing damage at the end of that player's turn",
                "Equippable Skill"]

    def cc_prereq(self, n):
        if n > self.upgrade_max:
            return 0
        a = int(6 / 5 * self.cost(n))
        return [0, 0, 0, a]

    def cc_n(self, n):
        if n > self.upgrade_max:
            return 0
        a = int(4 / 5 * self.cost(n))
        return [0, 0, 0, a]
