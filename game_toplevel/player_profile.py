"""
player profiles are what is traded at the top level of the game.

the Armory and Move shop affect the player's moves, net worth, color credits, etc,
and players are loaded into the arena based on their profiles

"""
from operator import add


class Profile:
    def __init__(self, name="Aria"):
        self.name = name

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
