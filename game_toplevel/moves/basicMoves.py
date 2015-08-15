from moves.move_resources import move_super


class walk(move_super):
    spriteName = "walkButton.gif"

    def cost(self, n):
        return 0

    def description_long(self, ):
        return ["walk",
                "Arrow keys: move yourself around the arena."
            , "Basic Move"]


class grab(move_super):
    spriteName = "grabButton.gif"

    def cost(self, n):
        return 0

    def description_long(self):
        return ["grab",
                "space: pick any objects on the floor up"
                "\narrow keys: grab opponent and wrestle with them"
            , "Basic Move"]


class throw(move_super):
    spriteName = "throwButton.gif"

    def cost(self, n):
        return 0

    def description_long(self):
        return ["throw",
                "space: drop any held objects"
                "\narrow keys: attempt to throw a held oppponent"
            , "Basic Move"]


class block(move_super):
    spriteName = "blockButton.gif"

    def cost(self, n):
        return 0

    def description_long(self):
        return ["block",
                "\nhurt less in a direction"
            , "Basic Move"]


class punch(move_super):
    spriteName = "punchbutton.gif"

    def cost(self, n):
        return 0

    def description_long(self):
        return ["punch",
                "hit crap"
                "\n(basic attack for your base damage)"
            , "Basic Move"]
