# coding: utf-8


from random import random, choice

from Action import Action
from Commons import *


class Battle:

    @log
    def __init__(self, parties):
        self.parties = parties

    @log
    def print_status(self):
        print_line()
        print("|     NAME |   HP/ MAX |  MP/MAX | ATK | DEF | INT | AGI |")
        for party in self.parties:
            for c in party.members:
                print(
                    "| {0:>8} | {1:>4}/{2:>4} | {3:>3}/{4:>3} | {5:>3} | {6:>3} | {7:>3} | {8:>3} |".format(
                        c.name, c.hp, c.hp_max, c.mp, c.mp_max, c.atk, c.defe, c.int, c.agi
                    )
                )

    @log
    def run(self):

        while True:
            self.print_status()

            actors = []
            for party in self.parties:
                actors += party.get_survivors()
            actors = sorted(actors, reverse=True, key=lambda c: c.agi + 0.25 * c.agi * random())  # AGI順に並び替え

            for actor in actors:
                print_line()
                print("Turn of " + actor.name)

                if actor not in actor.friend.get_survivors():
                    print(actor.name + " is already dead...")
                    break

                try:
                    action_name, target = actor.friend.tactics(actor, actor.friend, actor.enemy)
                except Exception as error:
                    print("ERROR: " + str(error))
                    action_name, target = "attack", choice(actor.enemy.get_survivors())

                if action_name == "attack":
                    Action.attack(actor, target)

                if action_name == "heal":
                    Action.heal(actor, target)

                if target.hp <= 0:
                    print(target.name + " is Down!")
                    target.conditions_loop["dead"] = True

                if len(actor.enemy.get_survivors()) <= 0:
                    return actor.friend
