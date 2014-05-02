#Python translation of Minesweeper by Zack Davis and Jeff Fiddler, App Academy Week 2
#Original at https://github.com/zackmdavis/App_Academy_Exercises/blob/master/Week_2/minesweeper.rb

#CURRENT STATUS: Unicode issues. Otherwise, seems to work.

import yaml

class Minesweeper:
    
    default_game_rows = 12
    default_game_cols = 12
    default_mines = 10
    save_file = 'saved_game.yaml'
    
    def __init__(self):
        self.__setup()
        self.__play()
        
    def __setup(self):
        self.quit_requested = False 
        
        rows = self.default_game_rows
        cols = self.default_game_cols
        mines = self.default_mines
        
        print "Welcome to Minesweeper"
        print "Current settings: size: {rows}, {cols}, mines: {mines}".format(rows = rows, cols = cols, mines = mines)
        print "enter 'n' to start a new game, 's' to change size/mine settings, 'l' to load a saved game"
        setup_input = self.__get_char()
        
        if setup_input == 'n':
            self.board = MineBoard(rows, cols, mines)
        elif setup_input == 's':
            rows, cols, mines, = self.__get_settings()
            self.board = MineBoard(rows, cols, mines)
        elif setup_input == 'l':
            self.board =  yaml.load(open(self.save_file, 'r'))
        else:
            self.__setup()             
        print "(note: you can save your game with 's' or quit with 'q')"
        
        
    def __get_char(self):    
        # Thanks to http://stackoverflow.com/questions/510357/python-read-a-single-character-from-the-user
        class _Getch:
            """Gets a single character from standard input.  Does not echo to the screen."""
            def __init__(self):
                try:
                    self.impl = _GetchWindows()
                except ImportError:
                    self.impl = _GetchUnix()

            def __call__(self): 
                char = self.impl()
                if char == '\x03':
                    raise KeyboardInterrupt
                elif char == '\x04':
                    raise EOFError
                return char

        class _GetchUnix:
            def __init__(self):
                import tty
                import sys

            def __call__(self):
                import sys
                import tty
                import termios
                fd = sys.stdin.fileno()
                old_settings = termios.tcgetattr(fd)
                try:
                    tty.setraw(sys.stdin.fileno())
                    ch = sys.stdin.read(1)
                finally:
                    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
                return ch


        class _GetchWindows:
            def __init__(self):
                import msvcrt

            def __call__(self):
                import msvcrt
                return msvcrt.getch()


        getch = _Getch()

        return getch()
    
        # return "__get_char will return something"
        # print "__get_char will do something"

    def __get_settings(self):
        settings_input = raw_input("enter new settings like 'rows,columns,number_of_mines'")
        return [int(x) for x in settings_input.split(',')]

    def __get_move(self):
        print "Use i,j,k,l to steer the cursor. Space to explore. 'f' to flag."
        command = self.__get_char()
        
        class OpenStruct:
            pass
        
        move = OpenStruct()
        move.flag = False
        if command == ' ':
            pass
        elif command == 'f':
            move.flag = True
        elif command == 's':
            open(self.save_file, 'w').write(yaml.dump(self.board))
            return None
        elif command == 'q':
            self.quit_requested = True
            return None
        else:
            self.board.move_cursor(command)
            return None
            
        move.coordinates = self.board.cursor_location
        return move

    def __play(self):
        while not (self.__game_over() or self.quit_requested):
            self.board.show()
            move = self.__get_move()
            if move:
                if move.flag:
                   self.board.flag(move.coordinates)
                else:
                    self.board.explore(move.coordinates)
        self.board.show()
        

    def __game_over(self):        
        if self.board.won():
            print "good job"
            return True
        elif self.board.boom():
            print "ouch"
            return True
        else:
            return False
    
    
    
class MineBoard:

    def __init__(self, height, width, mine_count):
        self.height = height
        self.width = width
        self.mine_count = mine_count
        self.minefield = []
        self.cursor_location = [0,0]
        self.__populate_minefield()
        
    # def show(self): # !
        # print "  "
        
        # print self.__col_indices()
        # for row_index, row, in enumerate(self.minefield):
            # index_string = str(row_index)
            # if len(index_string) == 1:
                # spacer = "  "
            # else:
                # spacer = " "
            # print spacer, row_index, " ",
            # for tile in row:
                # if tile.location == self.cursor_location:
                    # print u"\u2591 " #  light shaded block 
                # elif tile.flag:
                    # print u"\u2691 " # flag icon
                # elif tile.explored:
                    # if tile.boom():
                        # print u"\u2622 " #  radioactivity symbol 
                    # elif tile.number != 0:
                        # print tile.number,  " "
                    # elif tile.number == 0:
                        # print "  "
                # else:
                    # print u"\u25A0 " #  filled-in square                         
            # print "\n"

    def show(self): # !
        print "  "
        
        print self.__col_indices()
        for row_index, row, in enumerate(self.minefield):
            index_string = str(row_index)
            if len(index_string) == 1:
                spacer = "  "
            else:
                spacer = " "
            print spacer, row_index, " ",
            rowstring = u""
            for tile in row:
                if tile.location == self.cursor_location:
                    rowstring = rowstring + u"\u2591 " #  light shaded block
                elif tile.flag:
                    # rowstring = rowstring + u"\u2691 " # flag icon
                    rowstring = rowstring + u"f "
                # elif tile.mine:
                    # rowstring = rowstring + u"m "
                elif tile.explored:
                    if tile.boom():
                    # if tile.mine: # !
                        # rowstring = rowstring + u"\u2622 " #  radioactivity symbol
                        rowstring = rowstring + u"r "
                    elif tile.number != 0:
                        rowstring = rowstring + str(tile.number) + u" "
                    elif tile.number == 0:
                        rowstring = rowstring + u"  "
                else:
                    rowstring = rowstring + u"\u25A0 " #  filled-in square 
            print rowstring
            # print "\n"            
    
    
    def move_cursor(self, command_key):
        import copy
        new_location = copy.copy(self.cursor_location)
        if command_key == 'i':
            new_location[0] -= 1
        elif command_key == 'j':
            new_location[1] -= 1
        elif command_key == 'k':
            new_location[0] += 1
        elif command_key == 'l':
            new_location[1] += 1
        if self.in_bounds(new_location):
            self.cursor_location = new_location
       
        
    def explore(self, coordinates):
        self.minefield[coordinates[0]][coordinates[1]].explore()
    
    def flag(self, coordinates):
        self.minefield[coordinates[0]][coordinates[1]].flag =  not self.minefield[coordinates[0]][coordinates[1]].flag
    
    def find_tile(self, coordinates):
        return self.minefield[coordinates[0]][coordinates[1]]
    
    def in_bounds(self, coordinates):
        return (coordinates[0] in range(0, self.height) and coordinates[1] in range(0, self.width))
    
    def won(self):
        from flatten import flatten
        mines = [tile for tile in flatten(self.minefield) if tile.mine]
        if mines == [x for x in mines if x.flag]:
            mines_flagged = True
        else:
            mines_flagged = False
        non_mines = [x for x in flatten(self.minefield) if not x.mine]
        if non_mines == [x for x in non_mines if x.explored]:
            non_mines_explored = True
        else:
            non_mines_explored = False
        return mines_flagged and non_mines_explored
    
    def boom(self):
        from flatten import flatten
        mines = [tile for tile in flatten(self.minefield) if tile.mine]
        for x in mines:
            if x.explored:
                return True
        return False
    
    
    def __populate_minefield(self):
        from random import randrange
        mine_locations = []
        while not len(mine_locations) == self.mine_count:
            candidate_location = [randrange(0,self.width), randrange(0,self.height)]
            if not candidate_location in mine_locations:
                mine_locations.append(candidate_location)
                
        for row in range(self.height):
            self.minefield.append([])
            for col in range(self.width):
            #put in mines
                new_tile = Tile([row, col], self)
                if [row, col] in mine_locations:
                    new_tile.set_mine()
                self.minefield[row].append(new_tile)
            
    
    def __col_indices(self):
        top = "  "
        bottom = "    "  
        for col_index in range(self.width):
            if col_index < 10:
                top = top + "  "
                bottom = bottom + "{0} ".format(col_index)
            else:
                top = top + "{0} ".format(col_index / 10)
                bottom = bottom + "{0} ".format(col_index % 10)
        return "{0}\n{1}".format(top, bottom)
        
        
        
class Tile:

    def __init__(self, coordinates, board):
        self.location = coordinates
        self.board = board
        self.explored = False
        self.flag = False
        self.number = None
        self.mine = False # !
        
    def neighborhood(self):
        neighbors = []
        for row_offset in range(-1, 2):
            for col_offset in range(-1, 2):
                if row_offset == 0 and col_offset == 0:
                    continue
                neighbor_coordinates = [self.location[0]+row_offset, self.location[1]+col_offset]
                if not self.board.in_bounds(neighbor_coordinates):
                    continue
                neighbors.append(self.board.find_tile(neighbor_coordinates))        
        return [x for x in neighbors if x != None]
        
    def explore(self):
        self.explored = True
        if not self.boom():
            neighbors = self.neighborhood()
            self.number = len([tile for tile in neighbors if tile.mine])
            if self.number == 0:
                unexplored_neighbors = [tile for tile in neighbors if not tile.explored]
                for tile in unexplored_neighbors:
                    tile.explore()
        
    def set_mine(self):
        self.mine = True      
        
    def boom(self):
        # return (self.mine and self.explored)
        if self.explored:
            if self.mine:
                return True
            else:
                return False
        else:
            return False
        
             
        
        
Minesweeper()

    