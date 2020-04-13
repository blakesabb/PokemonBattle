"""
    imports classes from pokemon.py file
    reads the following csv files: pokemon.csv, moves.csv
    uses pokemon and move class to simulate a 1 on 1 pokemon battle using only gen 1 pokemon
"""
import csv
from random import randint
from random import seed
from copy import deepcopy

from pokemon import Pokemon
from pokemon import Move

seed(1) #Set the seed so that the same events always happen


#DO NOT CHANGE THIS!!!
# =============================================================================
element_id_list = [None, "normal", "fighting", "flying", "poison", "ground", "rock", 
                   "bug", "ghost", "steel", "fire", "water", "grass", "electric", 
                   "psychic", "ice", "dragon", "dark", "fairy"]

#Element list to work specifically with the moves.csv file.
#   The element column from the moves.csv files gives the elements as integers.
#   This list returns the actual element when given an index
# =============================================================================
    
def read_file_moves(fp):  
    '''
        open file putting fp in csv reader
        grab move name, element index, attack type, and pokemon generation number
        if generation number isn't gen 1 don't use those moves
        find element using element index
        skip move if damage classification isn't 1
        skip if power, or accuracy is empty string
        create move using these variables
        append move to move list
        return move list
    '''
    fp = csv.reader(fp) 
    next(fp, None) # skip first line
    move_list = list()
    # loop here
    for row in fp:
        movename = row[1]
        element_index = row[3]
        attack_type = row[9]
        generationID = row[2]
        if int(generationID) != 1: # generation_id column does not equal 1.   
            continue
        element = element_id_list[int(element_index)]
        damage_classification = row[9]
        if int(damage_classification) == 1: # damage_classification_id does equal 1. 
            continue
        power = row[4]
        if power == "":
            continue
        accuracy = row[6]
        if accuracy == "":
            continue
        
        
        #(self, name = "", element = "normal", power = 20, accuracy = 80, attack_type = 2)
        move = Move(movename, element, int(power), int(accuracy), int(attack_type))
        move_list.append(move)
    return move_list

#fp = open('moves_tiny.csv', encoding="utf-8")
#print(read_file_moves(fp))

def read_file_pokemon(fp):
    '''
        put fp in csv reader and skip first line
        grab the elements, hp, patt, pdef, satt, sdef, and id from file reader
        moves = none
        set each pokemon using these variables and put in pokemon list
        return pokemon list
    '''
    #### when reading pokemon, remember to use a deep copy so you dont change the original list - from prof
    fp = csv.reader(fp) 
    next(fp, None) # skip first line
    pokemon_list = list()
    IDlist = list()
    # loop here
    for row in fp:
        generation_collumn = row[11]
        #print(generation_collumn)
        name = row[1].lower()
        element1 = row[2].lower()
        element2 = row[3].lower()
        hp = int(row[5])
        patt = int(row[6])
        pdef = int(row[7])
        satt = int(row[8])
        sdef = int(row[9])
        moves = None
        ID = row[0]
        if ID in IDlist:
            continue
        IDlist.append(ID)
        if int(generation_collumn) != 1:
            continue
        pokemon = Pokemon(name, element1, element2, moves, hp, patt, pdef, satt, sdef)
        #(self, name = "", element1 = "normal", element2 = "", moves = None, hp = 100, patt = 10, pdef = 10, satt = 10, sdef = 10)
        pokemon_list.append(pokemon)
    return pokemon_list

#fp = open('pokemon_tiny.csv', encoding="utf-8")
#print(read_file_pokemon(fp))

def choose_pokemon(choice,pokemon_list):
    '''
        if choice is a digit find pokemon based on index and return deepcopy
        else if choice is found in pokemon list, set pokemon to that choice and return deepcopy
        if none of those happen, return None
    '''
    if choice.isdigit():
        index = int(choice) - 1
        return deepcopy(pokemon_list[index])
    else:
        for line in pokemon_list:
            newline = str(line).split(" ")
            if choice == newline[0]:
                return deepcopy(line)
    return None # return none to check if pokemon choice is valid

        

#choice = input("choose a pokemon")
#fp = open('pokemon_tiny.csv', encoding="utf-8")
#print(choose_pokemon(choice, read_file_pokemon(fp)))

def add_moves(pokemon,moves_list):
    '''
        add first random move found (ignore element)
        loop up to 200 times to find moves that have the same element as the pokemon
        if element is the same add that move to pokemon moves
        if moves list contains less than 4 moves return False
        if list contains 4 moves return True
    '''
    #print(moves_list)
    #print(pokemon.element1, pokemon.element2)

    element1 = pokemon.element1
    element2 = pokemon.element2
    count = 0

    random = randint(0, len(moves_list)-1)
    move = moves_list[random]
    pokemon.add_move(move)
    while count <= 200:

        random = randint(0, len(moves_list)-1)
        move = moves_list[random]
        if move.get_element() == element1 or move.get_element() == element2:
            if move not in pokemon.moves:
                pokemon.add_move(move)
        count += 1
        if pokemon.get_number_moves() == 4:
            break
    if pokemon.get_number_moves() < 4:
        return False
    else:
        return True

    #pokemon.add_move()


#pokemon = Pokemon()
#fp = open('moves.csv', encoding="utf-8") # if i make this 'moves_tiny.csv' I don't get the index error
#moves_list = read_file_moves(fp)
#print(add_moves(pokemon, moves_list))

def turn (player_num, player_pokemon, opponent_pokemon):
    '''
        Player_num is an int for printing which player: 1 or 2
        Player_pokemon, the attacker, and opponent_pokemon are of type Pokemon
        Player Turn steps
    '''
    if player_num == 1:
        opponent_num = 2
    else:
        opponent_num = 1
    print("Player {}'s turn".format(player_num))
    print(player_pokemon)
    while True:
        print("Show options: 'show ele', 'show pow', 'show acc'")
        attack_choice = input("Select an attack between 1 and {} or show option or 'q': ".format(len(player_pokemon.get_moves()))).lower()
        if attack_choice == 'show ele':
            player_pokemon.show_move_elements()
            continue
        elif attack_choice == 'show pow':
            player_pokemon.show_move_power()
            continue
        elif attack_choice == 'show acc':
            player_pokemon.show_move_accuracy()
            continue
        elif attack_choice.isdigit():
            break
        elif attack_choice == 'q':
            print("Player {} quits, Player {} has won the pokemon battle!".format(player_num, opponent_num))
            return False
    if attack_choice.isdigit():
        moves = player_pokemon.get_moves()
        move = moves[int(attack_choice)-1]
        print('selected move: {}\n'.format(move))
        print('{} hp before:{}'.format(opponent_pokemon.get_name(), opponent_pokemon.get_hp()))
        player_pokemon.attack(move, opponent_pokemon)
        print('{} hp after:{}\n'.format(opponent_pokemon.get_name(), opponent_pokemon.get_hp()))
    if opponent_pokemon.get_hp() <= 0:
        print("Player {}'s pokemon fainted, Player {} has won the pokemon battle!".format(opponent_num, player_num))
        return False
    return True


#print(turn())

def main():
    '''
        This function simulates a 1-on-1 pokemon battle between Player 1 and Player 2.  
    '''
    moveslist = read_file_moves(open('moves.csv', encoding="utf-8"))
    pokemonlist = read_file_pokemon(open('pokemon.csv', encoding="utf-8"))
    #move =Move('rock-throw','rock',50,90,2)
    #print(move.__str__())
    #print(move.__repr__())
    #print(move.attack_type)
        #########
    usr_inp = input("Would you like to have a pokemon battle? ").lower()
    while usr_inp != 'n' and usr_inp != 'q' and usr_inp != 'y':
        usr_inp = input("Invalid option! Please enter a valid choice: Y/y, N/n or Q/q: ").lower()
        
    if usr_inp != 'y':
        print("Well that's a shame, goodbye")
        return
    restart = 'y'
    while restart == 'y':
        choice1 = input("Player {}, choose a pokemon by name or index: ".format(1)).lower()
        pokemon_1 = choose_pokemon(choice1, pokemonlist)
        while pokemon_1 is None:
            choice1 = input("Invalid option, choose a pokemon by name or index: ").lower()
            pokemon_1 = choose_pokemon(choice1, pokemonlist)
        print('pokemon1:\n{}'.format(pokemon_1))
        choice2 = input("Player {}, choose a pokemon by name or index: ".format(2)).lower()
        pokemon_2 = choose_pokemon(choice2, pokemonlist)
        while pokemon_2 is None:
            choice2 = input("Invalid option, choose a pokemon by name or index: ").lower()
            pokemon_2 = choose_pokemon(choice2, pokemonlist)
        print('pokemon2:\n{}'.format(pokemon_2))
        add_moves(pokemon_1, moveslist)
        add_moves(pokemon_2, moveslist)
        while True:
            turncheck = turn(1, pokemon_1, pokemon_2)
            if turncheck is False:
                break
            turncheck = turn(2, pokemon_2, pokemon_1)
            if turncheck is False:
                break
            print('Player 1 hp after: {}'.format(pokemon_1.hp))
            print('Player 2 hp after: {}'.format(pokemon_2.hp))
        restartcheck = input("Battle over, would you like to have another? ")
        while str(restartcheck).lower() != 'y' and restartcheck.lower() != 'n' and restartcheck.lower() != 'q':
            restartcheck = input("Invalid option! Please enter a valid choice: Y/y, N/n or Q/q: ")
        restart = restartcheck.lower()

    print("Well that's a shame, goodbye")



if __name__ == "__main__":
    main()
