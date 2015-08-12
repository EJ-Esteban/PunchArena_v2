"""
player profiles are what is traded at the top level of the game.

the Armory and Move shop affect the player's moves, net worth, color credits, etc,
and players are loaded into the arena based on their profiles

"""
from operator import add
import ast


class Profile:
    def __init__(self, name="Aria"):
        name = name.replace('_', ' ')
        s = ""
        for x in name.split():
            s += x.capitalize() + " "
        self.name = s[:-1]

        # basic, unskilled stats
        self.max_hp = 10
        self.max_mp = 10
        self.max_move = 3
        self.base_damage = 3
        self.blood_in = 6
        self.blood_out = 4  # 6 turns to gain bloodlust, 4 to bleed out

        # moves
        self.abilities = dict()
        self.abilities['none'] = 0
        self.abilities['walk'] = 1
        self.abilities['punch'] = 1
        self.abilities['block'] = 1
        self.abilities['grab'] = 1
        self.abilities['throw'] = 1

        self.equipped_abilties = ['walk', 'punch', 'block', 'grab',
                                  'none', 'none', 'none', 'none']

        # money and equiipment stuff
        self.punch_dollars = 100
        self.net_worth = 100
        self.effective_net_worth = 0
        self.color_credits = [0, 0, 0, 0]

        # options
        self.sprite = 'bob'
        self.purchased_sprites = ['bob']
        self.text_speed = 'normal'
        self.battle_speed = 'normal'

    def build_player(self, player):
        """builds player for arena match"""
        player.name = self.name
        player.max_hp = self.max_hp
        player.max_mp = self.max_mp
        player.max_move = self.max_move
        player.base_damage = self.base_damage
        player.blood_in = self.blood_in
        player.blood_out = self.blood_out

        player.abilities = self.equipped_abilties

    def punchdollar_dx(self, amount):
        self.punch_dollars += amount

    def tally_color_credits(self):
        total_color_credits = [0, 0, 0, 0]
        for move in self.abilities.keys():
            # get the cumulative cc for a given move
            # move_credits = move.get_cum_cc(move)
            map(add, total_color_credits, move)

        self.color_credits = total_color_credits
        return total_color_credits

    def equip_ability(self, move, slot):
        if slot == 0:
            # cannot overwrite walk slot
            return False
        if move not in self.abilities:
            # cannot equip unowned moves
            return False
        if move in self.equipped_abilties:
            # cannot equip moves twice
            return False
        self.equipped_abilties[slot] = move
        return True

    def save_player(self):
        name = self.name.replace(' ', '_')

        filename = "save/%s.txt" % name
        f = open(filename, 'w')

        print(self.name, file=f)
        print(str(self.max_hp), file=f)
        print(str(self.max_mp), file=f)
        print(str(self.max_move), file=f)
        print(str(self.base_damage), file=f)
        print(str(self.blood_in), file=f)
        print(str(self.blood_out), file=f)

        print(str(self.punch_dollars), file=f)
        print(str(self.net_worth), file=f)
        print(str(self.effective_net_worth), file=f)
        print(str(self.color_credits), file=f)

        print(str(self.equipped_abilties), file=f)
        print(str(self.abilities), file=f)

        # options
        print(str(self.sprite), file=f)
        print(str(self.purchased_sprites), file=f)
        print(str(self.text_speed), file=f)
        print(str(self.battle_speed), file=f)

    def load_player(self, name):
        name = name.replace(' ', '_')
        s = ""
        for x in name.split():
            s += x.capitalize() + " "
        name = s[:-1]
        filename = "save/%s.txt" % name
        with open(filename, "r") as ins:
            array = []
            for line in ins:
                array.append(line)
        self.name = array[0].rstrip()
        self.max_hp = int(array[1])
        self.max_mp = int(array[2])
        self.max_move = int(array[3])
        self.base_damage = int(array[4])
        self.blood_in = int(array[5])
        self.blood_out = int(array[6])

        self.punch_dollars = int(array[7])
        self.net_worth = int(array[8])
        self.effective_net_worth = int(array[9])
        self.color_credits = ast.literal_eval(array[10])

        self.equipped_abilties = ast.literal_eval(array[11])
        self.abilities = ast.literal_eval(array[12])

        self.sprite = array[13].rstrip()
        self.purchased_sprites = ast.literal_eval(array[14])
