class HanoiGame:
    
    @classmethod
    def play(cls, num_discs):
        
        discs = [list(range(1, num_discs+1))[::-1],[],[]]
        
        while discs[2] != list(range(1, num_discs+1))[::-1]:
            print discs
            to_and_from = raw_input(
                "Write the index of the pile you want to move from "
                + "(pile 1, 2, or 3) and to in the form 'from,to' \n"
                )
            index_from, index_to = [int(char)-1 for char in to_and_from.split(",")]
            print "index_from: " + str(index_from)
            print "index_fo: " + str(index_to)
            if not discs[index_from]:
                print "Cannot move from an empty pile!"
                continue 
            if discs[index_to]:
                print "discs[index_from]: " + str(discs[index_from])
                if (discs[index_from][-1] > discs[index_to][-1]):
                    print "You can't put a larger disc on a smaller one, dummy"
                    continue
            discs[index_to].append(discs[index_from].pop())
        print "You win!"
                
HanoiGame.play(3)            