import random

#creates an altered print function that prints text letter by letter
import time
import sys
def delayed_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.03)
    time.sleep(0.50)

#creates type advantages, weaknesses, resistances, weak against, & immunities
offensive_advantages = {
    'grass':['water', 'ground', 'rock'],
    'water':['fire', 'ground', 'rock'],
    'fire':['grass', 'ice', 'bug', 'steel'],
    'electric':['flying', 'water'],
    'flying':['grass', 'fighting', 'bug'],
    'ground':['fire', 'electric', 'rock', 'poison', 'steel'],
    'ice':['flying', 'ground', 'grass', 'dragon'],
    'rock':['flying', 'fire', 'ice', 'bug'], 'normal':[],
    'fighting':['normal', 'rock', 'ice', 'steel', 'dark'],
    'steel':['rock', 'ice', 'fairy'],
    'psychic':['fighting', 'poison'],
    'poison':['grass', 'fairy'],
    'bug':['grass', 'psychic', 'dark'],
    'dragon':['dragon'],
    'dark':['ghost', 'psychic'],
    'fairy':['fighting', 'dragon', 'dark'],
    'ghost':['ghost', 'psychic'],
    '':['']
}
defensive_weaknesses = {
    'water':['grass', 'electric'],
    'fire':['water', 'ground', 'rock'],
    'grass':['fire', 'flying', 'ice', 'poison', 'bug'],
    'electric':['ground'],
    'flying':['electric', 'rock', 'ice'],
    'ground':['grass', 'water', 'ice'],
    'ice':['rock', 'fire', 'fighting', 'steel'],
    'rock':['ground', 'water', 'grass', 'fighting', 'steel'],
    'normal':['fighting'],
    'fighting':['flying', 'psychic', 'fairy'],
    'steel':['fighting', 'ground', 'fire'],
    'psychic':['dark', 'bug', 'ghost'],
    'poison':['ground', 'psychic'],
    'bug':['flying', 'rock', 'fire'],
    'dragon':['ice', 'dragon', 'fairy'],
    'dark':['fighting', 'bug', 'fairy'],
    'fairy':['poison', 'steel'],
    'ghost':['ghost', 'dark'],
    '':['']
}
resistances = {
    'grass':['electric', 'grass', 'ground', 'water'],
    'water':['fire', 'ice', 'steel', 'water'],
    'fire':['bug', 'fire', 'grass', 'ice', 'steel'],
    'electric':['electric', 'flying', 'steel'],
    'flying':['bug', 'fighting', 'grass'],
    'ground':['poison', 'rock'],
    'ice':['ice'],
    'rock':['fire', 'flying', 'normal', 'poison'],
    'fighting':['bug', 'dark', 'rock'],
    'steel':['bug', 'dragon', 'fairy', 'flying', 'grass', 'ice', 'normal', 'psychic', 'rock', 'steel'],
    'psychic':['fighting', 'psychic'],
    'poison':['fighting', 'poison', 'bug', 'grass', 'fairy'],
    'bug':['fighting', 'grass', 'ground'],
    'dragon':['electric', 'fire', 'grass', 'water'],
    'dark':['dark', 'ghost'],
    'fairy':['bug', 'dark', 'fighting'],
    'ghost':['bug', 'poison'],
    'normal':[''],
    '':['']
}
weak_against = {
    'grass':['grass', 'fire', 'flying', 'steel', 'poison', 'bug', 'dragon'],
    'water':['grass', 'water', 'dragon'],
    'fire':['water', 'fire', 'rock', 'dragon'],
    'electric':['grass', 'electric', 'dragon'],
    'flying':['electric', 'rock', 'steel'],
    'ground':['grass', 'bug'],
    'ice':['water', 'fire', 'ice', 'steel'],
    'rock':['ground', 'fighting', 'steel'],
    'fighting':['flying', 'psychic', 'poison', 'bug', 'fairy'],
    'steel':['water', 'fire', 'electric', 'steel'],
    'psychic':['steel', 'psychic'],
    'poison':['ground', 'rock', 'poison', 'ghost'],
    'bug':['fire', 'flying', 'fighting', 'steel', 'poison', 'fairy', 'ghost'],
    'dragon':['steel'],
    'dark':['fighting', 'dark', 'fairy'],
    'fairy':['steel', 'poison',],
    'ghost':['dark'],
    'normal':[''],
    '':['']
}
immunities = {
    'ghost':['normal', 'fighting'],
    'normal':['ghost'],
    'flying':['ground'],
    'steel':['poison'],
    'ground':['electric'],
    'dark':['psychic'],
    'fairy':['dragon']
}

#move category[0], name[1], type[2], power[3], accuracy[4]
flamethrower = [1, "Flamethrower", 'fire', 90, 100]
fire_punch = [0, "Fire Punch", 'fire', 75, 100]
giga_drain = [1, "Giga Drain", 'grass', 75, 100] #special
solar_beam = [1, "Solar Beam", 'grass', 120, 100] #special
energy_ball = [1, "Energy Ball", 'grass', 90, 100]
aqua_tail = [0, "Aqua Tail", 'water', 90, 90]
dive = [0, "Dive", 'water', 80, 100]
sky_attack = [0, "Sky Attack", 'flying', 120, 90]
fly = [0, "Fly", 'flying', 90, 95]
thunderbolt = [1, "Thunderbolt", 'electric', 90, 100]
earthquake = [0, "Earthquake", 'ground', 100, 100]
stone_edge = [0, "Stone Edge", 'rock', 100, 80]
ice_beam = [1, "Ice Beam", 'ice', 90, 100]
avalanche = [0, "Avalanche", 'ice', 60, 100]
body_slam = [0, "Body Slam", 'normal', 85, 100]
slash = [0, "Slash", 'normal', 70, 100]
strength = [0, "Strength", 'normal', 80, 100]
dragon_claw = [0, "Dragon Claw", 'dragon', 80, 100]
sludge_bomb = [1, "Sludge Bomb", 'poison', 90, 100]
poison_jab = [0, "Poison Jab", 'poison', 80, 100]
u_turn = [0, "U-Turn", 'bug', 70, 100]
shadow_ball = [1, "Shadow Ball", 'ghost', 80, 100]
steel_wing = [0, "Steel Wing", 'steel', 70, 90]
psychic = [1, "Psychic", 'psychic', 90, 100]
dazzling_gleam = [1, "Dazzling Gleam", 'fairy', 80, 100]
dynamic_punch = [0, "Dynamic Punch", 'fighting', 100, 50]
brick_break = [0, "Brick Break", 'fighting', 75, 100]
throat_chop = [0, "Throat Chop", 'dark', 80, 100]
bite = [0, "Bite", 'dark', 60, 100]

#protect = [3, "Protect", '', 0, 0, 2] #special
#recover = [3, "Recover", '', 0, 0, 2] #special
#rest = [3, "Rest", '', 0, 0, 2] #special

#move category[0], name[1], type[2], stage value[3], list of affected stats[4], either 0(affects self) or 1(affects opponent)[5]
calm_mind = [2, "Calm Mind", 'psychic', 1, ['special attack', 'special defense'], 0]
iron_defense = [2, "Iron Defense", 'steel', 2, ['defense'], 0]
leer = [2, "Leer", 'normal', -1, ['defense'], 1]


class Pokemon:
    def __init__(self, name, types, base_hp, base_attack, base_defense, base_spatk, base_spdef, base_speed, move_list, level=100):
        #initialize each pokemon class attribute
        self.name = name
        self.level = level
        self.types = types
        self.max_health = 110 + (2*base_hp)     #applys formula to base stats to find the max health of the current pokemon based on it's level
        self.current_health = self.max_health
        self.knocked_out = False
        self.weakness = defensive_weaknesses.get(types[0]) + defensive_weaknesses.get(types[1])     #takes pokemon's type(s) and finds it's defensive weaknesses
        self.resists = resistances.get(types[0]) + resistances.get(types[1])    #takes pokemon's type(s) and finds it's offensive resistances
        #applys formula to base stats to find stats for current pokemon level
        self.attackst = (2*base_attack) + 5
        self.defensest = (2*base_defense) + 5
        self.sp_attackst = (2*base_spatk) + 5
        self.sp_defensest = (2*base_spdef) + 5
        self.speedst = (2*base_speed) + 5
        self.move_list = move_list
        self.status_condition = None
        self.status_counter = 0

    def __repr__(self):
        #printing a pokemon displays its name, type, level, and its hit points
        return f"the {self.types[0]} type pokemon {self.name}, with {self.current_health} hp remaining"

    def gain_health(self, amount):
        #increases the health of a pokemon
        self.current_health += amount
        self.current_health = round(self.current_health)
        print(f"{self.name} now has {self.current_health} health!")
        return self.current_health

    def lose_health(self, amount):
        #takes an amount of damage and applies it to the pokemon
        self.current_health -= amount
        self.current_health = round(self.current_health)
        #checks to see if the pokemon faints if their health is zero
        if self.current_health <= 0:
            self.current_health = 0
            self.knock_out()
        else:
            print(f"{self.name} now has {self.current_health} health.")
            return self.current_health

    def knock_out(self):
        #if the pokemons health is less than or equal to zero, the pokemon is knocked out
        if self.current_health <= 0:
            self.status_condition = None
            self.status_counter = 0
            self.knocked_out = True
            print(f"\n{self.name} has fainted.")

    def revive(self):
        #checks to make sure that the pokemon is knocked out before reviving it
        if self.current_health <= 0 and self.knocked_out == True:
            self.knocked_out = False
            self.current_health += (self.max_health / 2)    #returns the pokemon's health to half
            print(f"\n{self.name} was revived!")

    def attack(self, opposing_pokemon, move):
        #checks to see if the pokemon is able to attack the opponent
        if self.knocked_out == True:
            print("\nThis pokemon has fainted and is unable to attack!")
        else:
            #sets each modifier at 1
            critical = 1
            stab = 1
            typeadv = 1
            sametype = 1
            crit_random = random.randint(1, 30)
            #finds the info about the move
            movecategory = move[0]
            movename = move[1]
            movetype = move[2]
            movepower = move[3]
            moveaccuracy = move[4]
            #changes the modifiers based on type mathcups, criticals, and stab
            if movetype in opposing_pokemon.types:
                sametype = 0.5
            if crit_random == 6:
                critical = 2
            if movetype in self.types:
                stab = 1.3
            #checks if opponent has an immunities
            immunity = []
            for type in immunities.keys():
                if type in opposing_pokemon.types:
                    immunity = immunities[type]
            #if the opponent is immune to the attack, the attack will have no effect
            if movetype in immunity:
                print(f"\n{movename} has no affect on {opposing_pokemon.name}!")
            else:            
                #cycles through opponent pokemon weakness' and advantages and creates a value depending on the frequency of the movetype
                type_counter = 0
                for type in opposing_pokemon.weakness:
                    if movetype == type:
                        type_counter += 1
                for type in opposing_pokemon.resists:
                    if movetype == type:
                        type_counter -= 1
                #changes the type dis/advantage multiplier depending on the type_counter value
                if type_counter == -2:
                    typeadv = 0.25
                elif type_counter == -1:
                    typeadv = 0.5
                elif type_counter == 0:
                    typeadv = 1
                elif type_counter == 1:
                    typeadv = 2
                else:
                    typeadv = 4
                #multiplies damage by the modifier and rounds the result           
                modifier = stab * critical * typeadv * sametype
                if movecategory == 0:   #physical move
                    unrounded_damage = (((((2 * self.level / 6) + 2) * movepower * self.attackst / opposing_pokemon.defensest) / 50) + 2) * modifier
                elif movecategory == 1: #special move
                    unrounded_damage = (((((2 * self.level / 6) + 2) * movepower * self.sp_attackst / opposing_pokemon.sp_defensest) / 50) + 2) * modifier
                damage = round(unrounded_damage, 0)
                print(f"\n{self.name} used {movename}!")
                #randomly finds a value between 1-100 and if its less than the accuracy value, the attack hits
                accuracy_of_attack = random.randint(1, 100)
                if accuracy_of_attack >= moveaccuracy:
                    print(f"{self.name}'s attack missed!")
                else:
                    print(f"-{damage} hp")
                    #prints the restult of the type matchup
                    if critical == 2:
                        print("Critical Hit!")
                    if typeadv == 2 or typeadv == 4:
                        print("It's Super Effective!")
                    elif typeadv == 0.5 or typeadv == 0.25:
                        print("It's Not Very Effective!")
                    opposing_pokemon.lose_health(damage)
    
    def stat_changing_move(self, move, opposing_pokemon=None):
        #sets up information about the move and stat stages
        stat_stage_multiplier = {-2:0.5, -1:0.66, 1:1.5, 2:2}
        message = {-2:"harshly fell", -1:"fell", 1:"rose", 2:"sharply rose"}
        #finds information about the move being used
        movename = move[1]
        stage_change = move[3]
        affected_stats = move[4]
        affected_pokemon = move[5]
        print(f"\n{self.name} used {movename}!")
        if 2 + 2 != 4:
            #plan to add a maximum amount of times able to use a stat changing move
            print("But it failed!")
        else:
            #takes the stat from the affected stat list of the move
            if 'attack' in affected_stats:
                #decides who is affected by the stat change
                if affected_pokemon == 0:
                    self.attackst = self.attackst * stat_stage_multiplier[stage_change]
                else:
                    opposing_pokemon.attackst = opposing_pokemon.attackst * stat_stage_multiplier[stage_change]
            if 'defense' in affected_stats:
                if affected_pokemon == 0:
                    self.defensest = self.defensest * stat_stage_multiplier[stage_change]
                else:
                    opposing_pokemon.defensest = opposing_pokemon.defensest * stat_stage_multiplier[stage_change]
            if 'special attack' in affected_stats:
                if affected_pokemon == 0:
                    self.sp_attackst = self.sp_attackst * stat_stage_multiplier[stage_change]
                else:
                    opposing_pokemon.sp_attackst = opposing_pokemon.sp_attackst * stat_stage_multiplier[stage_change]
            if 'special defense' in affected_stats:
                if affected_pokemon == 0:
                    self.sp_defensest = self.sp_defensest * stat_stage_multiplier[stage_change]
                else:
                    opposing_pokemon.sp_defensest = opposing_pokemon.sp_defensest * stat_stage_multiplier[stage_change]
            if 'speed' in affected_stats:
                if affected_pokemon == 0:
                    self.speedst = self.speedst * stat_stage_multiplier[stage_change]
                else:
                    opposing_pokemon.speedst = opposing_pokemon.speedst * stat_stage_multiplier[stage_change]
            #for each affected stat, a message is printed describing the stat change
            for stat in affected_stats:
                stage_change_message = message[stage_change]
                if affected_pokemon == 0:
                    affected_pokemon_name = self.name
                else:
                    affected_pokemon_name = opposing_pokemon.name
                print(f"{affected_pokemon_name}'s {stat.title()} {stage_change_message}!")


class Trainer:
    def __init__(self, pokemon_list, potions, max_potions, revives, trainer_name):
        #initializes each trainer attribute
        self.pokemon_list = pokemon_list
        self.potions = potions
        self.max_potions = max_potions
        self.revives = revives
        self.trainer_name = trainer_name
        self.current_pokemon = 0    #index of the current pokemon in the pokemon list
        self.lost_fight = False

    def __repr__(self):
        #lists off the trainers pokemon and shows which one is currently in battle
        print(f"{self.trainer_name} has the following pokemon:")
        for pokemon in self.pokemon_list:
            print(pokemon)
        print(f"{self.pokemon_list[self.current_pokemon].name} is currently in battle.")

    def find_bars(self, pokemon_index):
        #splits current pokemon's health into 20 increments
        #represents pokemons health with bars each round, and fills the damage taken with white spaces
        bar_increments = (self.pokemon_list[pokemon_index].max_health / 20)
        num_of_bars = round(int(self.pokemon_list[pokemon_index].current_health / bar_increments), 0)
        bars = ""
        for num in range(num_of_bars):
            bars += "="
        lenbars = len(bars)
        whitespace_bars = 20 - lenbars
        if lenbars < 20:
            for i in range(whitespace_bars):
                bars += " "
        return f"|{bars}|"

    def find_pokemon_remaining(self):
        #prints pokeball icons that show the status of both trainers' pokemon
        pokeball_icon = "("
        for index, pokemon in enumerate(self.pokemon_list):
            if pokemon.knocked_out == False:
                pokeball_icon += "o"    #non fainted pokemon icon
            else:
                pokeball_icon += "ø"    #fainted pokemon icon
            if index == (len(self.pokemon_list) - 1):
                break
            pokeball_icon += ":"
        #if the trainer has less than 6 pokemon, it prints empty space in place for the pokeballs
        empty_icons = 6 - len(self.pokemon_list)
        if empty_icons > 0:
            for num in range(empty_icons):
                pokeball_icon += ": "
        pokeball_icon += ")"
        return self.trainer_name + " - " + pokeball_icon

    def open_bag(self, choice_index, bag_decision):
        #makes sure that the trainer has enough potions before using them, then increases the health of the current pokemon
        potion = (2 * self.pokemon_list[choice_index].max_health) / 5   #potion recovers 40% of their max health
        if bag_decision == 3:
            #uses a revive only if the pokemon has already fainted
            if self.pokemon_list[choice_index].knocked_out == True:
                self.pokemon_list[choice_index].revive()
                self.revives -= 1
            else:
                print("\nYou are unable to use a revive on a pokemon that is still alive!")
        else:
            #makes sure that the current pokemon is alive with less than max health
            if self.pokemon_list[choice_index].current_health == self.pokemon_list[choice_index].max_health:
                print("\nYou are unable to use a potion on a pokemon with max health!")
            elif self.pokemon_list[choice_index].knocked_out == True:
                print("\nYou are unable to use a potion on a pokemon that has fainted!")
            else:
                #uses a potion -- cuts the potion size if it'd make the current health higher than the max health
                if bag_decision == 1 and self.potions > 0:
                    print(f"\n{self.trainer_name} used a potion on {self.pokemon_list[choice_index].name}.")
                    max_current_diff = (self.pokemon_list[choice_index].max_health - self.pokemon_list[choice_index].current_health)    #difference between the max and current health
                    if max_current_diff < potion:
                        self.pokemon_list[choice_index].gain_health(max_current_diff)
                    else:
                        self.pokemon_list[choice_index].gain_health(potion)
                    self.potions -= 1
                elif bag_decision == 1 and self.potions == 0:
                    print("\nYou don't have any potions left!")
                #takes the difference between the current and max health of the pokemon and adds it to the current health
                if bag_decision == 2 and self.max_potions > 0:
                    print(f"\n{self.trainer_name} used a max potion on {self.pokemon_list[choice_index].name}.")
                    max_current_diff = (self.pokemon_list[choice_index].max_health - self.pokemon_list[choice_index].current_health)    #difference between the max and current health
                    self.pokemon_list[choice_index].gain_health(max_current_diff)
                    self.max_potions -= 1
                elif bag_decision == 2 and self.max_potions == 0:
                    print("\nYou don't have any potions left!")

    def use_move(self, opponent, move):
        #makes sure the active pokemon has the move in its list, and attacks with it
        if move in self.pokemon_list[self.current_pokemon].move_list:
            if move[0] == 2:    #checks if the move is a stat changing move
                self.pokemon_list[self.current_pokemon].stat_changing_move(move, opponent.pokemon_list[opponent.current_pokemon])
            elif move[0] == 0 or move[0] == 1:  #attacks if it's a physical or special move 
                self.pokemon_list[self.current_pokemon].attack(opponent.pokemon_list[opponent.current_pokemon], move)
            else:
                pass    #plan to add moves with extra functionality (i.e. protect, recover, giga drain, solar beam)
        else:
            print("\nThis pokemon doesn't have that move!")

    def switch_active_pokemon(self, new_active):
        #checks to make sure that the new_active value can be applied to the pokemon_list
        if new_active < len(self.pokemon_list) and new_active >= 0:
            #checks if the new pokemon is knocked out
            if self.pokemon_list[new_active].knocked_out:
                print(f"\n{self.pokemon_list[new_active].name} is knocked out! It is unable to enter the battle!")
            #checks whether the new pokemon is already in battle
            elif self.current_pokemon == new_active:
                print(f"\n{self.pokemon_list[new_active].name} is already in battle!")
            #switches to the new pokemon
            else:
                print(f"\n{self.pokemon_list[self.current_pokemon].name} was switched out.")
                print(f"{self.pokemon_list[new_active].name} has entered the battle!")
                self.current_pokemon = new_active

    def check_for_new_status(self, other, other_move_decision):
        #FUNCTION DECIDES WHETHER OR NOT TO GIVE THE CURRENT POKEMON A STATUS CONDITION 
        if self.pokemon_list[self.current_pokemon].knocked_out == False and self.pokemon_list[self.current_pokemon].status_condition == None:
            #assigns a status condition based on the move type
            conditions_by_type = {'fire':'burn', 'poison':'poison', 'ghost':'confused', 'electric':'paralyzed', 'ice':'frozen', 'psychic':'asleep'}
            #only assigns a pokemon a status condition after the opposing pokemon attacks with non-stat-changing move
            if other.pokemon_list[other.current_pokemon].move_list[other_move_decision][0] != 2 and other.pokemon_list[other.current_pokemon].move_list[other_move_decision][2] in conditions_by_type:
                obtain_status_condition_chances = random.randint(1, 9)     #1 in 9 chance that a status condition is given
                if obtain_status_condition_chances == 2:    #gives a status condition if the random number = 2
                    #obtains status condition depending on the type of the opposing pokemon's attack
                    self_status_condition = conditions_by_type.get(other.pokemon_list[other.current_pokemon].move_list[other_move_decision][2])
                    #prints out the message detailing the new status condition
                    if self_status_condition == 'poison' or self_status_condition == 'burn':
                        print(f"{self.pokemon_list[self.current_pokemon].name} was {self_status_condition}ed!")
                    elif self_status_condition == 'frozen':
                        print(f"{self.pokemon_list[self.current_pokemon].name} was frozen solid!")
                    elif self_status_condition == 'asleep':
                        print(f"{self.pokemon_list[self.current_pokemon].name} fell asleep!")
                    elif self_status_condition == 'paralyzed':
                        print(f"{self.pokemon_list[self.current_pokemon].name} was paralyzed! It may be unable to move!")
                    elif self_status_condition == 'confused':
                        print(f"{self.pokemon_list[self.current_pokemon].name} is now confused.")
                    self.pokemon_list[self.current_pokemon].status_condition = self_status_condition    #assigns the status condition to a pokemon attribute

    def pre_move_status_check(self, other, self_use_move):
        #FUNCTION DECIDES WHETHER TO REMOVE STATUS CONDITION - IF NOT, APPLIES AFFECTS OF THE STATUS CONDITION
        if self.pokemon_list[self.current_pokemon].knocked_out == False:
            if self.pokemon_list[self.current_pokemon].status_condition != None:
                if self.pokemon_list[self.current_pokemon].status_counter > 0:
                    random_remove_status = random.randint(1, 100)   #finds a random number between 1-100 
                    chance_of_removing_status = 20 * self.pokemon_list[self.current_pokemon].status_counter     #finds a number depending on the number of turns the pokemon has had a status condition
                    #determines whether the random number is less than the turn based number
                    #if so, the status condition is removed
                    if random_remove_status <= chance_of_removing_status:
                        status_condition_removal_message = {'burn':"'s burn wore off.", 'poison':"'s poison wore off.", 'confused':" snapped out of confusion!", 'paralyzed':" is no longer paralyzed.", 'frozen':" thawed out!", 'asleep':" woke up!"}
                        print(f"\n{self.pokemon_list[self.current_pokemon].name}{status_condition_removal_message.get(self.pokemon_list[self.current_pokemon].status_condition)}")
                        #resets class attributes
                        self.pokemon_list[self.current_pokemon].status_condition = None
                        self.pokemon_list[self.current_pokemon].status_counter = 0

                #a frozen or sleeping pokemon is unable to attack during their turn
                if self.pokemon_list[self.current_pokemon].status_condition == 'frozen' or self.pokemon_list[self.current_pokemon].status_condition == 'asleep':
                    print(f"\n{self.pokemon_list[self.current_pokemon].name} is {self.pokemon_list[self.current_pokemon].status_condition.title()}! \nIt's unable to attack!")
                    self_use_move = False
                    self.pokemon_list[self.current_pokemon].status_counter += 1

                #flips a coin to decide whether to prevent an attack and do damage from confusion
                elif self.pokemon_list[self.current_pokemon].status_condition == 'confused':
                    print(f"\n{self.pokemon_list[self.current_pokemon].name} is confused.")
                    coin_flip = random.randint(1, 2)
                    if coin_flip == 2:
                        print("It hurt itself in its confusion!")
                        self.pokemon_list[self.current_pokemon].lose_health(self.pokemon_list[self.current_pokemon].max_health / 8)
                        self_use_move = False
                    self.pokemon_list[self.current_pokemon].status_counter += 1

                #1 in 3 chance that the paralysis prevents the pokemon from attacking
                elif self.pokemon_list[self.current_pokemon].status_condition == 'paralyzed':
                    coin_flip = random.randint(1, 3)
                    if coin_flip == 2:
                        print(f"\n{self.pokemon_list[self.current_pokemon].name} is paralyzed. \nIt can't to move!")
                        self_use_move = False
                    self.pokemon_list[self.current_pokemon].status_counter += 1


#instantiates each pokemon with stats, moves, types, and name
#stats: name, types, base_hp, base_attack, base_defense, base_spatk, base_spdef, base_speed,
charizard = Pokemon("Charizard", ['fire', 'flying'], 78, 84, 78, 109, 85, 100, [flamethrower, fly, steel_wing, calm_mind])
venusaur = Pokemon("Venusaur", ['grass', 'poison'], 80, 82, 83, 100, 100, 80, [giga_drain, solar_beam, sludge_bomb, leer])
blastoise = Pokemon("Blastoise", ['water', ''], 79, 83, 100, 85, 105, 78, [aqua_tail, ice_beam, bite])
pidgeot = Pokemon("Pidgeot", ['flying', 'normal'], 83, 80, 75, 70, 70, 101, [sky_attack, slash, u_turn])
jolteon = Pokemon("Jolteon", ['electric', ''], 65, 65, 60, 110, 95, 130, [thunderbolt, body_slam, shadow_ball])
nidoking = Pokemon("Nidoking", ['ground', 'poison'], 81, 102, 77, 85, 75, 85, [earthquake, stone_edge, poison_jab])
dragonite = Pokemon("Dragonite", ['dragon', 'flying'], 91, 134, 95, 100, 100, 80, [dragon_claw, sky_attack, fire_punch])
gengar = Pokemon("Gengar", ['ghost', 'poison'], 60, 65, 60, 130, 75, 110, [sludge_bomb, shadow_ball, giga_drain])
alakazam = Pokemon("Alakazam", ['psychic', ''], 55, 50, 45, 135, 95, 120, [psychic, dazzling_gleam, calm_mind])
machamp = Pokemon("Machamp", ['fighting', ''], 90, 130, 80, 65, 85, 55, [dynamic_punch, strength, throat_chop])
snorlax = Pokemon("Snorlax", ['normal', ''], 160, 110, 65, 65, 110, 30, [body_slam, brick_break])
cloyster = Pokemon("Cloyster", ['water', 'ice'], 50, 95, 180, 85, 45, 70, [avalanche, dive])
#instantiates both trainers with pokemon lists, and potion counts
player1 = Trainer([nidoking, venusaur, blastoise, pidgeot, machamp, charizard], 2, 1, 1, "Red")
cpu = Trainer([gengar, cloyster, alakazam, snorlax, jolteon, dragonite], 0, 3, 0, "Blue")


def start_fight(user, opponent):
    #introduces the battle and the current pokemon
    print(f"\n{opponent.trainer_name} would like to battle! \n{opponent.trainer_name} sent out {opponent.pokemon_list[opponent.current_pokemon]}. \nYou sent {user.pokemon_list[user.current_pokemon]}.")
    back_input = 0
    end_fight = False
    while end_fight == False:
        #saves list of pokemon to a variable to be used multiple times
        current_list_pokemon = "\nList of Pokemon: "
        for pokemon_index, pokemon in enumerate(user.pokemon_list):
            current_list_pokemon += f"\n{pokemon_index + 1}. {pokemon.name} \t{pokemon.current_health}/{pokemon.max_health}"


        #CPU AND USER PRE-ROUND SWITCHES IF POKEMON HAVE FAINTED:
        if opponent.pokemon_list[opponent.current_pokemon].knocked_out == True or user.pokemon_list[user.current_pokemon].knocked_out == True:
            
            user_already_switched = False
            #checks to see if the user's current pokemon has fainted - if so, forces you to switch pokemon
            if user.pokemon_list[user.current_pokemon].knocked_out == True:
                #makes sure that the user makes a valid decision
                options = range(1, len(user.pokemon_list) + 1)
                while user.pokemon_list[user.current_pokemon].knocked_out == True:
                    #if user input is not in a list of options, they are given the option to redo their input until it's valid
                    print("\nCurrent Pokemon has fainted. Must be switched out.")
                    print(current_list_pokemon)
                    try:
                        switch_decision = int(input("Switch to: "))
                    except:
                        print("\n*Decision must be an integer!")
                        continue
                    if switch_decision not in options:
                        print("\n*Not a valid option! Try again!")
                        continue
                    user.switch_active_pokemon(switch_decision - 1)
                user_already_switched = True

            #sets up a switch if the opponent pokemon has fainted
            if opponent.pokemon_list[opponent.current_pokemon].knocked_out == True:
                #selects a pokemon but doesn't switch to it
                valid_option = False
                while valid_option == False:
                    for pokemon_index, pokemon in enumerate(opponent.pokemon_list):
                        if opponent.pokemon_list[pokemon_index].knocked_out == False:
                            opponent_switch = pokemon_index
                            valid_option = True

                #if the opponent pokemon has fainted, the user is allowed to make a switch
                if user.pokemon_list[user.current_pokemon].knocked_out == False and user_already_switched == False:
                    valid_option = False
                    options = (0, 1)
                    while valid_option == False:
                        print(f"{opponent.trainer_name} is about to send in {opponent.pokemon_list[opponent_switch].name}. \n\n1. Yes \t 0. No")
                        #makes sure input is an integer and prevents a ValueError
                        try:
                            opponent_fainted_switch = int(input("Would you like to switch Pokemon? "))
                        except:
                            print("\n*Decision must be an Integer!")
                            continue
                        #checks to see if input value is an option
                        if opponent_fainted_switch in options:
                            valid_option = True
                        else:
                            print("\n*Not a valid option! Try Again!")
                            continue
                    if opponent_fainted_switch == 1:
                        options = range(1, len(user.pokemon_list) + 1)
                        valid_option = False
                        while valid_option == False:
                            #if user input is not in a list of options, they are given the option to redo their input until it's valid
                            print(current_list_pokemon)
                            try:
                                switch_input = int(input("Switch pokemon: "))
                            except:
                                print("\n*Decision must be an Integer!")
                                continue
                            if switch_input == back_input:
                                break
                            #checks to see if input value is an option
                            if switch_input in options:
                                user.switch_active_pokemon(switch_input - 1)
                                valid_option = True
                            else:
                                print("\n*Not a valid option! Try Again!")
                                continue
                    opponent.switch_active_pokemon(opponent_switch)
                
                #makes switch if both opponent and user pokemon have fainted
                else:
                    opponent.switch_active_pokemon(opponent_switch)


        #BEGINNING OF TURN:
        print("\n----------POKEMON BATTLE----------")
        print(f"{user.find_pokemon_remaining()} \t {opponent.find_pokemon_remaining()}\n")


        #CPU DECISION MAKING PROCESS:
        opponent_use_item = False
        opponent_use_move = False
        #if cpu current pokemon's health is below 1/4 of the max, theres a 1 in 3 chance the cpu will use a potion
        potion_or_attack = random.randint(1, 3)
        if (opponent.pokemon_list[opponent.current_pokemon].current_health <= (opponent.pokemon_list[opponent.current_pokemon].max_health / 4)) and potion_or_attack == 2:
            if opponent.max_potions > 0:
                opponent_use_item = True
        else:
            #takes the cpu's current pokemon's moves and tries to find one that has an advantage against the user's current pokemon
            opponent_use_move = True
            find_supereffective_move = False
            for move_index, move in enumerate(opponent.pokemon_list[opponent.current_pokemon].move_list):
                if move[2] in user.pokemon_list[user.current_pokemon].weakness and move[2] not in user.pokemon_list[user.current_pokemon].resists:
                    opponent_move_decision = move_index
                    find_supereffective_move = True
                    break
            if find_supereffective_move == False:
                #if no supereffective move is found, there will be a 1 and 3 chance that the user's pokemon will use a status move if it has one
                opponent_has_statchange_move = False
                for move in opponent.pokemon_list[opponent.current_pokemon].move_list:
                    if move[0] == 2:
                        opponent_has_statchange_move = True
                        break
                #if the opponents current pokemon has a status move and the random number == 2, the pokemon uses the move
                opponent_use_statchange_move = random.randint(1, 3)
                if opponent_use_statchange_move == 2 and opponent_has_statchange_move == True:
                    for move_index, move in enumerate(opponent.pokemon_list[opponent.current_pokemon].move_list):
                        if move[0] == 2:
                            opponent_move_decision = move_index
                            break
                #if the cpu doesn't use a status move, a random move in the current pokemon's list is chosen
                else:
                    confirmed_non_status = False
                    while confirmed_non_status == False:
                        opponent_move_decision = random.randint(1, len(opponent.pokemon_list[opponent.current_pokemon].move_list)) - 1
                        if opponent.pokemon_list[opponent.current_pokemon].move_list[opponent_move_decision][0] != 2:
                            confirmed_non_status = True


        #USER DECISION MAKING PROCESS:
        #starts by creating a loop that allows a back button to function
        #if the user inputs '0', it will restart the loop allowing the user to redo their decisions
        confirmed_option = False
        first_back = True
        while confirmed_option == False:
            user_use_move = False
            user_use_item = False
            user_make_switch = False
            back_button_pressed = False
            if first_back == False:
                print("<<< Back")
                print("----------------------------------")
            print(f"{user.pokemon_list[user.current_pokemon].name} \t {user.find_bars(user.current_pokemon)}")
            print(f"{opponent.pokemon_list[opponent.current_pokemon].name} \t {opponent.find_bars(opponent.current_pokemon)}")
            print("----------------------------------")
            #gives you an attack, open bag, or switch pokemon option
            valid_option = False
            basic_options = (1, 2, 3)   #1 - attack; 2 - open bag; 3 - pokemon options
            while valid_option == False:
                print("\n1. Attack \n2. Bag \n3. Pokemon")
                #makes sure input is an integer and prevents a ValueError
                try:
                    user_decision = int(input("What will you do: "))
                except:
                    print("\n*Decision must be an Integer!")
                    continue
                #checks to see if input value is an option
                if user_decision in basic_options:
                    valid_option = True
                else:
                    print("\n*Not a valid option! Try Again!")
                    continue
            #gives you the attack options and executes them
            if user_decision == 1:
                print("")
                move_options = range(1, len(user.pokemon_list[user.current_pokemon].move_list) + 1)
                valid_option = False
                while valid_option == False:
                    #prints out each move for current pokemon
                    for move_index, move in enumerate(user.pokemon_list[user.current_pokemon].move_list):
                        print(f"{move_index + 1}. {move[1]}")
                    try:
                        user_move_decision = int(input("Which attack will you use: "))
                    except:
                        print("\n*Decision must be an Integer!")
                        continue
                    if user_move_decision in move_options:
                        valid_option = True
                    #if input is equal to 0, it breaks the loop and returns to the basic options
                    elif user_move_decision == back_input:
                        back_button_pressed = True
                        break
                    else:
                        print("\n*Not a valid option! Try Again!")
                        continue
                #changes the input back into an index for the move list
                user_move_decision = user_move_decision - 1
                user_use_move = True

            #opens bag to choose between potions and revives
            if user_decision == 2:
                bag_options = (1, 2, 3) #1 - potion; 2 - max potion; 3 - revive
                valid_option = False
                while valid_option == False:
                    print(f"\n1. Potion \t {user.potions} \n2. Max Potion \t {user.max_potions} \n3. Revive \t {user.revives}")
                    try:
                        bag_decision = int(input("What item will you use: "))
                    except:
                        print("\n*Decision must be an Integer!")
                        continue
                    #checks to see if the input is an option that works
                    #then makes sure the input will work when executed during the turn
                    if bag_decision in bag_options:
                        if bag_decision == 1 and user.potions > 0:
                            valid_option = True
                        elif bag_decision == 2 and user.max_potions > 0:
                            valid_option = True
                        elif bag_decision == 3 and user.revives > 0:
                            valid_option = True
                        else:
                            if bag_decision == 1:
                                print("\n*You don't have any potions left!")
                                break
                            elif bag_decision == 2:
                                print("\n*You don't have any max potions left!")
                                continue
                            elif bag_decision == 3:
                                print("\n*You don't have any revives left!")
                                continue
                    elif bag_decision == back_input:
                        back_button_pressed = True
                        break
                    else:
                        print("\n*Not a valid option! Try Again!")
                        continue
                #if they press the back button, the confirmed options loop restarts
                if back_button_pressed == True:
                    first_back = False
                    continue
                pokeitem_options = range(1, len(user.pokemon_list) + 1) #makes a list of options depending on the number of pokemon the trainer has
                valid_option = False
                #ensure the user chooses a valid option
                while valid_option == False:
                    print(current_list_pokemon)
                    try:
                        user_pokemon_choice = int(input("Use item on which pokemon: "))
                    except:
                        print("\n*Decision must be an Integer!")
                        continue
                    #makes sure that the input will work when executed during the turn
                    #if it doesn't, the user is forced to redo the input
                    if user_pokemon_choice in pokeitem_options:
                        if (bag_decision == 1 or bag_decision == 2) and (user.pokemon_list[user_pokemon_choice - 1].current_health == user.pokemon_list[user_pokemon_choice - 1].max_health):
                            print("\nYou are unable to use a potion on a pokemon with max health!")
                            continue
                        elif (bag_decision == 1 or bag_decision == 2) and user.pokemon_list[user_pokemon_choice - 1].knocked_out == True:
                            print("\nYou are unable to use a potion on a pokemon that has fainted!")
                            continue
                        elif bag_decision == 3 and user.pokemon_list[user_pokemon_choice - 1].knocked_out == False:
                            print("\nYou are unable to use a revive on a pokemon that is still alive!")
                            continue
                        else:
                            valid_option = True
                    elif user_pokemon_choice == back_input:
                        back_button_pressed = True
                        break
                    else:
                        print("\n*Not a valid option! Try Again!")
                        continue
                user_bag_pokedecision_index = user_pokemon_choice - 1
                user_use_item = True
            
            #gives you the switch pokemon option
            elif user_decision == 3:
                pokemon_options = range(1, len(user.pokemon_list) + 1)  #pokemon options depends on the number of pokemon the trainer has
                valid_option = False
                #ensure the user chooses a valid option
                while valid_option == False:
                    print(current_list_pokemon)
                    try:
                        pokemon_decision = int(input("Pokemon: "))
                    except:
                        print("\n*Decision must be an Integer!")
                        continue
                    if pokemon_decision in pokemon_options:
                        valid_option = True
                    elif pokemon_decision == back_input:
                        back_button_pressed = True
                        break
                    else:
                        print("\n*Not a valid option! Try Again!")
                        continue
                if back_button_pressed == True:
                    first_back = False
                    continue
                pokemon_decision_index = pokemon_decision - 1
                #prints out the summary of the selected pokemon
                valid_option = False
                while valid_option == False:
                    #prints out the health, type, and stats of the selected pokemon
                    chosen_user_pokemon = user.pokemon_list[pokemon_decision - 1]
                    user.find_bars(pokemon_decision - 1)
                    print(f"\n{chosen_user_pokemon.name} Summary: \nHealth: {user.find_bars(pokemon_decision - 1)} {chosen_user_pokemon.current_health} / {chosen_user_pokemon.max_health}")
                    print(f"Status Condition: {chosen_user_pokemon.status_condition}")
                    pokemon_types_summary = "Type: "
                    for type in chosen_user_pokemon.types:
                        if type != None:
                            pokemon_types_summary += type.title() + " "
                    print(pokemon_types_summary)
                    print(f"Stats: {chosen_user_pokemon.max_health} / {chosen_user_pokemon.attackst} / {chosen_user_pokemon.defensest} / {chosen_user_pokemon.sp_attackst} / {chosen_user_pokemon.sp_defensest} / {chosen_user_pokemon.speedst}")
                    #each move is printed as either a physical/special attack, or a status move
                    print("Moves:")
                    for move in chosen_user_pokemon.move_list:
                        move_category = move[0]
                        if move_category == 0:
                            category_text = "Physical"
                        elif move_category == 1:
                            category_text = "Special"
                        else:
                            category_text = "Status"
                        #if it's a status move:
                        if move_category == 2:
                            increase_or_decrease = ""
                            if move[3] > 0:
                                increase_or_decrease = "Increases"
                            else:
                                increase_or_decrease = "Decreases"
                            if move[-1] == 1:
                                move_target = "Opponent"
                            else:
                                move_target = user.pokemon_list[pokemon_decision - 1].name
                            affected_stats = ""
                            for index, stat in enumerate(move[4]):
                                affected_stats += stat.title()
                                #if the iterated stat isn't the last one in the list and the list has more than 2 stats, add a comma after the stat
                                if stat != move[4][-1] and len(move[4]) > 2:
                                    affected_stats += ", "
                                #if the list only contains one stat, and the stat is the second to last one in the list, add "and "
                                #converts the length of the list into a base zero index value, and subtracts one to find the second to last element in the list
                                if len(move[4]) != 1 and index == (len(move[4]) - 1) - 1:
                                    affected_stats += " and "
                            stat_or_stats = "stat"
                            if len(move[4]) > 1:
                                stat_or_stats = "stats"
                            stage_value_string = ""
                            stage_value_string += str(move[3])[-1]
                            stage_or_stages = "stage"
                            if move[3] > 1 or move[3] < -1:
                                stage_or_stages = "stages"
                            #prints a status move description depending on the move information
                            print(f"    {move[1]}: \n\t{move[2].title()} - {category_text} \n\t{increase_or_decrease} {move_target}'s {affected_stats} {stat_or_stats} by {stage_value_string} {stage_or_stages}.")
                        else:
                            #prints an attack move desription with move information
                            print(f"    {move[1]}: \n\t{move[2].title()} - {category_text} \n\tpower: {move[3]} - accuracy: {move[4]}")
                    print("\n1. Shift Pokemon --- 0. Cancel")
                    try:
                        switch_or_cancel = int(input("Would you like to switch to this pokemon? "))
                    except:
                        print("\n*Decision must be an Integer!")
                        continue
                    if switch_or_cancel == 1:   #user decides to make the switch
                        #makes sure that the input will work when executed during the turn
                        #if it doesn't, the user is forced to redo the input
                        if pokemon_decision in pokemon_options:
                            if (pokemon_decision - 1) == user.current_pokemon:
                                print(f"\n{chosen_user_pokemon.name} is already in battle!")
                                continue
                            elif chosen_user_pokemon.knocked_out == True:
                                print(f"\n{chosen_user_pokemon.name} is knocked out! It's unable to enter the battle!")
                                continue
                            else:
                                user_use_move = False
                                user_make_switch = True
                                valid_option = True
                    elif switch_or_cancel == back_input:
                        back_button_pressed = True
                        break
                    else:
                        print("\n*Not a valid option! Try Again!")
                        continue
            if back_button_pressed == True:
                first_back = False
                continue
            confirmed_option = True
            

        #TURN EXECUTION IF ONE OR BOTH TRAINERS DECIDE NOT TO ATTACK
        if user_use_move == False or opponent_use_move == False:
            #user doesn't use move -- opponent uses move
            if user_use_move == False and opponent_use_move == True:
                #decides what function the user will execute
                if user_use_item == True:
                    user.open_bag(user_bag_pokedecision_index, bag_decision)
                elif user_make_switch == True:
                    user.switch_active_pokemon(pokemon_decision_index)
                
                #opponent uses move
                #checks for a status condition
                opponent.pre_move_status_check(user, opponent_use_move)
                #checks to see if status condition from previous function either knocks pokemon out or prevents it from attacking
                if opponent.pokemon_list[opponent.current_pokemon].knocked_out == False:
                    #perform opponent move
                    opponent.use_move(user, opponent.pokemon_list[opponent.current_pokemon].move_list[(opponent_move_decision)])
                    if user.pokemon_list[user.current_pokemon].knocked_out == False and user.pokemon_list[user.current_pokemon].status_condition == None:
                        user.check_for_new_status(opponent, opponent_move_decision)

            #user uses move -- opponent doesn't use move
            elif user_use_move == True and opponent_use_move == False:
                #decides what function the opponent will execute
                if opponent_use_item == True:
                    opponent.open_bag(opponent.current_pokemon, 2)
                #change here if ability for opponent to make their own switches is added
                else:
                    #opponent.switch_active_pokemon(pokemon_decision - 1)
                    pass
                
                #user uses move
                #checks for a status condition
                user.pre_move_status_check(opponent, user_use_move)
                #checks to see if status condition from previous function either knocks pokemon out or prevents it from attacking
                if user_use_move == True and user.pokemon_list[user.current_pokemon].knocked_out == False:
                    #perform user move
                    user.use_move(opponent, user.pokemon_list[user.current_pokemon].move_list[(user_move_decision)])
                    if opponent.pokemon_list[opponent.current_pokemon].knocked_out == False and opponent.pokemon_list[opponent.current_pokemon].status_condition == None:
                        opponent.check_for_new_status(user, user_move_decision) 

            #both user and opponent are not using a move
            else:
                #user is faster
                if user.pokemon_list[user.current_pokemon].speedst >= opponent.pokemon_list[opponent.current_pokemon].speedst:
                    #decides what function the user will execute
                    if user_use_item == True:
                        user.open_bag(user_bag_pokedecision_index, bag_decision)
                    elif user_make_switch == True:
                        user.switch_active_pokemon(pokemon_decision_index)
                    #decides what function the opponent will execute
                    if opponent_use_item == True:
                        opponent.open_bag(opponent.current_pokemon, 2)
                    #change here if ability for opponent to make their own switches is added
                    else:
                        #opponent.switch_active_pokemon(pokemon_decision - 1)
                        pass
                #opponent is faster
                else:
                    #decides what function the opponent will execute
                    if opponent_use_item == True:
                        opponent.open_bag(opponent.current_pokemon, 2)
                    #change here if ability for opponent to make their own switches is added
                    else:
                        #opponent.switch_active_pokemon(pokemon_decision - 1)
                        pass
                    #decides what function the user will execute
                    if user_use_item == True:
                        user.open_bag(user_bag_pokedecision_index, bag_decision)
                    elif user_make_switch == True:
                        user.switch_active_pokemon(pokemon_decision - 1)


        #TURN EXECUTION IF BOTH TRAINERS DECIDE TO ATTACK
        else:
            #user is faster
            if user.pokemon_list[user.current_pokemon].speedst >= opponent.pokemon_list[opponent.current_pokemon].speedst:
                #checks for a status condition
                user.pre_move_status_check(opponent, user_use_move)
                #checks to see if status condition from previous function either knocks pokemon out or prevents it from attacking
                if user_use_move == True and user.pokemon_list[user.current_pokemon].knocked_out == False:
                    #perform user move
                    user.use_move(opponent, user.pokemon_list[user.current_pokemon].move_list[(user_move_decision)])
                    #after the users move, decides whether to give the opponent a status condition if they're still alive
                    if opponent.pokemon_list[opponent.current_pokemon].knocked_out == False and opponent.pokemon_list[opponent.current_pokemon].status_condition == None:
                        opponent.check_for_new_status(user, user_move_decision) 
                #checks to see if opponent survives the attack
                if opponent.pokemon_list[opponent.current_pokemon].knocked_out == False:
                    #checks for a status condition
                    opponent.pre_move_status_check(user, opponent_use_move)
                    #checks to see if status condition from previous function either knocks pokemon out or prevents it from attacking
                    if opponent_use_move == True and opponent.pokemon_list[opponent.current_pokemon].knocked_out == False:
                        #perform opponent move
                        opponent.use_move(user, opponent.pokemon_list[opponent.current_pokemon].move_list[(opponent_move_decision)])
                        #after the opponents move, decides whether to give the user a status condition if they're still alive
                        if user.pokemon_list[user.current_pokemon].knocked_out == False and user.pokemon_list[user.current_pokemon].status_condition == None:
                            user.check_for_new_status(opponent, opponent_move_decision)

            #opponent is faster
            else:
                #checks for a status condition
                opponent.pre_move_status_check(user, opponent_use_move)
                #checks to see if status condition from previous function either knocks pokemon out or prevents it from attacking
                if opponent_use_move == True and opponent.pokemon_list[opponent.current_pokemon].knocked_out == False:
                    #perform opponent move
                    opponent.use_move(user, opponent.pokemon_list[opponent.current_pokemon].move_list[(opponent_move_decision)])
                    #after the opponents move, decides whether to give the user a status condition if they're still alive
                    if user.pokemon_list[user.current_pokemon].knocked_out == False and user.pokemon_list[user.current_pokemon].status_condition == None:
                        user.check_for_new_status(opponent, opponent_move_decision)
                #checks to see if user survives the attack
                if user.pokemon_list[user.current_pokemon].knocked_out == False:
                    #checks for a status condition
                    user.pre_move_status_check(opponent, user_use_move)
                    #checks to see if status condition from previous function either knocks pokemon out or prevents it from attacking
                    if user_use_move == True and user.pokemon_list[user.current_pokemon].knocked_out == False:
                        #perform user move
                        user.use_move(opponent, user.pokemon_list[user.current_pokemon].move_list[(user_move_decision)])
                        #after the users move, decides whether to give the opponent a status condition if they're still alive
                        if opponent.pokemon_list[opponent.current_pokemon].knocked_out == False and opponent.pokemon_list[opponent.current_pokemon].status_condition == None:
                            opponent.check_for_new_status(user, user_move_decision) 

            
        #CHECKS WHETHER THE GAME SHOULD END:
        #if all pokemon have fainted on either side, the fight ends
        faint_counter = 0
        for pokemon in user.pokemon_list:
            if pokemon.knocked_out == True:
                faint_counter += 1
        if faint_counter == len(user.pokemon_list):
            user.lost_fight = True
            end_fight = True
        faint_counter = 0
        for pokemon in opponent.pokemon_list:
            if pokemon.knocked_out == True:
                faint_counter += 1
        if faint_counter == len(opponent.pokemon_list):
            opponent.lost_fight = True
            end_fight = True


        #gives post turn status affects - poison, burn
        if user.pokemon_list[user.current_pokemon].status_condition != None or opponent.pokemon_list[opponent.current_pokemon].status_condition != None:
            #checks which pokemon is slower, the slower of which will be affected by any status affects first
            if user.pokemon_list[user.current_pokemon].speedst < opponent.pokemon_list[opponent.current_pokemon].speedst:
                user_slower = True
            else:
                user_slower = False
            if user_slower == True:
                first, second = user, opponent
            else:
                first, second = opponent, user

            if first.pokemon_list[first.current_pokemon].knocked_out == False:
                if first.pokemon_list[first.current_pokemon].status_condition == 'burn' or first.pokemon_list[first.current_pokemon].status_condition == 'poison':
                    print(f"\n{first.pokemon_list[first.current_pokemon].name} was hurt by its {first.pokemon_list[first.current_pokemon].status_condition.title()}!")
                    first.pokemon_list[first.current_pokemon].lose_health(first.pokemon_list[first.current_pokemon].max_health / 8)
                    first.pokemon_list[first.current_pokemon].status_counter += 1             

            if second.pokemon_list[second.current_pokemon].knocked_out == False:
                if second.pokemon_list[second.current_pokemon].status_condition == 'burn' or second.pokemon_list[second.current_pokemon].status_condition == 'poison':
                    print(f"\n{second.pokemon_list[second.current_pokemon].name} was hurt by its {second.pokemon_list[second.current_pokemon].status_condition.title()}!")
                    second.pokemon_list[second.current_pokemon].lose_health(second.pokemon_list[second.current_pokemon].max_health / 8)
                    second.pokemon_list[second.current_pokemon].status_counter += 1   


    #END OF BATTLE MESSAGES:
    #displays winning or losing messages at the end of a battle, and randomly decides the prize money
    earnings = random.randint(200, 1000)
    if user.lost_fight == True:
        print(f"\nYou blacked out and paid your opponent ${earnings}....")
    if opponent.lost_fight == True:
        print(f"\n{user.user_name} has defeated {opponent.user_name}! \n{user.user_name} got ${earnings} for winning!")
    return "Thanks for Playing!"


print(start_fight(player1, cpu))
