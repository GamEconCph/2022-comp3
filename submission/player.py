import numpy as np
from game_tournament.game import Player 

class player(Player):

    name = 'xxx' # <--- set your name here 
    
    def play(self, f_profit_own, f_profit_opponent, pmin, pmax) -> float:
        '''
        INPUTS: 
            f_profit_own: function of two inputs, p1 and p2, that returns the profit for you: f_profit_own(p1, p2)
            f_profit_opponent: function that returns the profit for the opponent: f_profit_opponent(p2, p1) (Note the order!!)
            pmin: lowest permitted price 
            pmax: highest permitted price 

        OUTPUT: 
            p: your price (float)
        '''
        
        p = np.random.uniform(pmin, pmax)
        
        p = np.clip(p, pmin, pmax) # convenient way of ensuring that the price is within the bounds

        assert np.isfloat(p), f'the chosen price must be a float'
        assert pmin <= p <= pmax, f'the chosen price must be between {pmin} and {pmax}'

        return p 