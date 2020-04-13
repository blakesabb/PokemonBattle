"""
    Class file containing pokemon and move classes for use in pokemon game (project 11)
"""

from random import randint


#DO NOT CHANGE THIS!!!
# =============================================================================
is_effective_dictionary = {'bug': {'dark', 'grass', 'psychic'}, 
                           'dark': {'ghost', 'psychic'},
                           'dragon': {'dragon'}, 
                           'electric': {'water', 'flying'}, 
                           'fairy': {'dark', 'dragon', 'fighting'},
                           'fighting': {'dark', 'ice', 'normal', 'rock', 'steel'}, 
                           'fire': {'bug', 'grass', 'ice', 'steel'}, 
                           'flying': {'bug', 'fighting', 'grass'}, 
                           'ghost': {'ghost', 'psychic'}, 
                           'grass': {'water', 'ground', 'rock'}, 
                           'ground': {'electric', 'fire', 'poison', 'rock', 'steel'}, 
                           'ice': {'dragon', 'flying', 'grass', 'ground'}, 
                           'normal': set(), 
                           'poison': {'fairy', 'grass'}, 
                           'psychic': {'fighting', 'poison'}, 
                           'rock': {'bug', 'fire', 'flying', 'ice'},
                           'steel': {'fairy', 'ice', 'rock'},
                           'water': {'fire', 'ground', 'rock'}
                           }

not_effective_dictionary = {'bug': {'fairy', 'flying', 'fighting', 'fire', 'ghost','poison','steel'}, 
                            'dragon': {'steel'}, 
                            'dark': {'dark', 'fairy', 'fighting'},
                            'electric': {'dragon', 'electric', 'grass'},
                            'fairy': {'fire', 'poison', 'steel'},
                            'fighting': {'bug', 'fairy', 'flying', 'poison', 'psychic'}, 
                            'fire': {'dragon', 'fire', 'rock', 'water'}, 
                            'flying': {'electric', 'rock', 'steel'}, 
                            'ghost': {'dark'}, 
                            'grass': {'bug', 'dragon', 'grass', 'fire', 'flying', 'poison', 'steel'}, 
                            'ground': {'bug','grass'}, 
                            'ice': {'fire', 'ice', 'steel', 'water'}, 
                            'normal': {'rock', 'steel'}, 
                            'poison': {'ghost', 'ground', 'poison', 'rock'}, 
                            'psychic': {'psychic', 'steel'}, 
                            'rock': {'fighting', 'ground', 'steel'}, 
                            'steel': {'electric', 'fire', 'steel', 'water'},
                            'water': {'dragon','grass', 'ice'}
                            }

no_effect_dictionary = {'electric': {'ground'}, 
                        'dragon': {'fairy'},
                        'fighting': {'ghost'}, 
                        'ghost': {'normal', 'psychic'}, 
                        'ground': {'flying'}, 
                        'normal': {'ghost'}, 
                        'poison': {'steel'},
                        'psychic': {'dark'}, 
                        
                        'bug': set(), 'dark': set(), 'fairy': set(),'fire': set(), 
                        'flying': set(), 'grass': set(), 'ice': set(), 
                        'rock': set(), 'steel': set(), 'water': set()
                        }

#Dictionaries that determine element advantages and disadvantages
# =============================================================================

class Move(object):
    def __init__(self, name = "", element = "normal", power = 20, accuracy = 80,
                 attack_type = 2):
        """ Initialize attributes of the Move object """
        
        self.name = name
        self.element = element
        self.power = power
        
        self.accuracy = accuracy
        self.attack_type = attack_type  #attack_type is 1, 2 or 3 
        # 1 - status moves, 2 - physical attacks, 3 - special attacks
        
    def __str__(self):
            
        '''
            Returns just the name of the move (used for printing).
            for printing. Takes 1 arg: self. Returns a string.
        '''
        name = str(self.name)
        return name

    def __repr__(self):
        '''
            Returns just the name of the move (can utilize the __str__() method here).
            for displaying in the shell. Takes 1 arg: self. Returns a string.
        '''

        return self.__str__()

    def get_name(self):
        '''
            Returns the name attribute.
        '''
        return self.name
    
    def get_element(self):
        '''
            return element attribute
        '''
        return self.element
    
    def get_power(self):
        '''
            return power
        '''
        return self.power
    
    def get_accuracy(self):
        '''
            return accuracy
        '''
        return self.accuracy
    
    def get_attack_type(self):
        '''
            return attack type
        '''
        # this is the "interesting/confusing" function in class
        return self.attack_type


    def __eq__(self,m):
        '''return True if all attributes are equal; False otherwise'''
        return self.name == m.get_name() and self.element == m.get_element() and\
                self.power == m.get_power() and self.accuracy == m.get_accuracy() and\
                self.attack_type == m.get_attack_type()
        
        
class Pokemon(object):
    def __init__(self, name = "", element1 = "normal", element2 = "", moves = None,
                 hp = 100, patt = 10, pdef = 10, satt = 10, sdef = 10):
        ''' initializes attributes of the Pokemon object '''
        
        self.name = name
        self.element1 = element1
        self.element2 = element2
        
        self.hp = hp
        self.patt = patt
        self.pdef = pdef
        self.satt = satt
        self.sdef = sdef
        
        self.moves = moves
        
        try:
            if len(moves) > 4:
                self.moves = moves[:4]
                
        except TypeError: #For Nonetype
            self.moves = list()

    def __eq__(self,p):
        '''return True if all attributes are equal; False otherwise'''
        return self.name == p.name and \
            self.element1 == p.element1 and \
            self.element2 == p.element2 and \
            self.hp == p.hp and \
            self.patt == p.patt and \
            self.pdef == p.pdef and \
            self.satt == p.satt and \
            self.sdef == p.sdef and \
            self.moves == p.moves

    def __str__(self):
        '''
            formats everything and returns it as a string
        '''
        hpstring = 'Health: ' + str(self.hp)
        pattstring = 'patt: ' + str(self.patt)
        pdefstring = 'pdef: ' + str(self.pdef)
        sattstring = 'satt: ' + str(self.satt)
        sdefstring = 'sdef: ' + str(self.sdef)

        s = "{:<15s}{:<20s}{:<15s}{:<15s}{:<15s}{:<15s}".format(self.name ,hpstring, pattstring, pdefstring, sattstring, sdefstring)
        s += "\nElement:     {:<15s}{:<5s}\n\n".format(self.element1,self.element2)
        for m in self.moves:
            s += "{:<15s}".format(str(m))
        return s


    def __repr__(self):
        '''
            Returns the same value as the __str__() method to.
            for displaying in the shell. Takes 1 arg: self. Returns a string.
        '''
        return self.__str__()


    def get_name(self):
        '''
            Returns the name attribute.
        '''
        return self.name
    
    def get_element1(self):
        '''
            Returns the element1 attribute
        '''
        return self.element1
    
    def get_element2(self):
        '''
            Returns the element2 attribute.
        '''
        return self.element2
    
    def get_hp(self):
        '''
            Returns the hp attribute.
        '''
        return self.hp
    
    def get_patt(self):
        '''
            Returns the patt attribute.
        '''
        return self.patt

    def get_pdef(self):
        '''
            Returns the pdef attribute.
        '''
        return self.pdef

    def get_satt(self):
        '''
            Returns the satt attribute.
        '''
        return self.satt

    def get_sdef(self):
        '''
            Returns the sdef attribute.
        '''
        return self.sdef
    
    def get_moves(self):
        '''
            Returns the moves attribute.
        '''
        return self.moves

    def get_number_moves(self):
        '''
            counts moves in get_moves
            return count
        '''
        count = 0
        for moves in self.get_moves():
            count += 1
        return count

    def choose(self,index):
        '''
            Takes an index and returns the corresponding move from the moves list.
            If there is an IndexError returns None.
        '''
        try:
            move_choice = self.moves[index]
            return move_choice
        except IndexError:
            return None
    

    def show_move_elements(self):
        '''
            Displays the elements of the pokemon’s moves (each in a 15-space field, left justified).
            This function does not return anything.
        '''
        moves = self.get_moves()
        elementlist = list()
        for move in moves:
            element = move.get_element()
            elementlist.append(element)
        elementstring = ""
        for element in elementlist:
            elementstring += "{:<15}".format(element)

        print(elementstring)
        #print('{:<15}, {:<15}'.format(self.element1, self.element2)) # this doesn't get the move element, it gets the pokemon element instead

    def show_move_power(self):
        '''
            Displays the power of the pokemon’s moves (each in a 15-space field, left justified).
            This function does not return anything.
        '''
        
        powerstr = ""
        for index in self.moves:
            powerstr += "{:<15}".format(index.get_power())
            
        print(powerstr)
        #move = Move()
        #print('{:<15}'.format(move.get_power()))

    def show_move_accuracy(self):
        '''
            Displays the accuracy of the pokemon’s moves (each in a 15-space field, left justified).
            This function does not return anything.
        '''
        accuracystr = ""
        for index in self.moves:
            accuracystr += "{:<15}".format(index.get_accuracy())
        print(accuracystr)
        #move = Move()
        #print("{:<15}".format(move.get_accuracy()))

    def add_move(self, move):
        '''
            Adds the move parameter to the list of moves for this pokemon if this pokemon has three or less moves.
            This function does not return anything.
        '''
        if len(self.moves) <= 3:
            self.moves.append(move)
        
    def attack(self, move, opponent):
        '''
            mp: the power of the move
            A: The patt or satt of the attacking Pokemon
            D: The pdef or sdef of the defending Pokemon
            modifier: takes into effect same-type attack bonus (STAB) if move is super effective or not effective.
        '''

        power = move.get_power()
        
        if move.get_attack_type() == 2:
            A = self.get_patt()
            D = opponent.get_pdef()
        elif move.get_attack_type() == 3:
            A = self.get_satt()
            D = opponent.get_sdef()
        else:
            print("Invalid attack_type, turn skipped.")
            return
        rand = randint(1, 100)

        accuracy = move.get_accuracy()
        if accuracy < rand:
            print("Move missed!")
            return


        modifier = 1
        # element 1 effective check
        opponent_element = opponent.get_element1()
        #print(opponent_element)
        #move_element = move.get_element
        if opponent_element in is_effective_dictionary[move.get_element()]:
            modifier = modifier * 2
        elif opponent_element in not_effective_dictionary[move.get_element()]:
            modifier = modifier/2
        elif opponent_element in no_effect_dictionary[move.get_element()]:
            print('No effect!')
            return
        
        #element 2 effective check
        opponent_element2 = opponent.get_element2()
#        if opponent_element2 == '':
#            pass

        if opponent_element2 in is_effective_dictionary[move.get_element()]:
            modifier = modifier * 2
        elif opponent_element2 in not_effective_dictionary[move.get_element()]:
            modifier = modifier/2
        elif opponent_element2 in no_effect_dictionary[move.get_element()]:
            print('No effect!')
            return
        
        if modifier > 1:
            print("It's super effective!!!!")
        elif modifier < 1:
            print("Not very effective...")
            
        # (STAB) bonus
        if move.get_element() == self.get_element1() or move.get_element == self.get_element2():
            modifier = modifier * 1.5
        #if move_element == self.element1 or move_element == self.element2:
        #    modifier = modifier*1.5

        #damage calculator
        
#        AoverD = A/D
#        numerator = power*AoverD*20
#        numOver = numerator/50
#        damage = numOver + 2
#        damage = damage * modifier
        damage = (((power*(A/D)*20)/50)+2)*modifier
        damage = int(damage)
        #print(damage)
        #print(self.hp)
        
        # modifier check

            
        #opponent.subtract_hp(damage)
        
        if opponent.hp <= damage:
            opponent.hp = 0
            return
        else: 
            opponent.hp = opponent.hp-damage
        
        
    def subtract_hp(self, damage): # currently doesn't subtract opponents hp idk how to find opponent hp variable
        '''
        subtract damage from opponents hp
        '''
        
        if self.hp <= damage:
            self.hp = 0
            return
        else:
            self.hp = self.hp - damage
        #print(self.hp)


        
        
#key = 'ice'
#print(is_effective_dictionary[key])
#if 'dragon' in is_effective_dictionary[key]:
#
#P = Pokemon()
#M = Move()
#Opponent = Pokemon()
##print(P)
##print(Opponent)
#P.attack(M, Opponent)
#print(P.__str__())
