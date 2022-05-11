# Konkurrence 2: Bimatrixspil 

I denne konkurrence skal du skrive en spillerfunktion, der kan spille bimatrixspil. Når du er færdig, skal du navngive din fil `player.py`, og lægge den i mappen `./submission/` og committe. Husk at sætte dens property `name = 'xxx'`, hvor `xxx` skal være et navn, som du vil bruge i samtlige konkurrencer i kurset. 

Den medfølgende notebook, `comp3-short.ipynb` loader spillerfunktioner fra mappen `./players/` og opstiller en turnering, hvor de kan spille imod hinanden. I `comp3-long.ipynb` finder du mere inspiration til, hvordan du kan opstille din funktion. Se også youtube videoerne [del 1](https://youtu.be/cKznghgnqX8) og [del 2](https://youtu.be/Gob3BfJt3Fo). 

## Spillerfunktionen

Spillerfunktionen skal tage flg. inputs 
* `f_profit_own`: funktion af to inputs, som giver din profit, `f_profit_own(p1, p2)`, 
* `f_profit_opponent`: samme, men for modstanderen, dog med modsat rækkefølge af inputs: `f_profit_opponent(p2, p1)`, 
* `pmin`: float, mindste tilladte pris, 
* `pmax`: float, største tilladte pris. 

 Nedenfor ser du et eksempel på en spillerfunktion, som vælger en tilfældig handling. 

```Python 
def play(self, f_profit_own, f_profit_opponent, pmin, pmax) -> float:
    p = np.random.uniform(pmin, pmax)
    return p # must be a float in the interval [pmin; pmax]
```

**Tilfældighed:** Du må gerne bruge tilfældighed, fx `np.random.uniform()` (eller `.normal()`) til at vælge blandt flere kandidater. Turneringen vil blive gentaget 100 gange mellem dig og din modstander for at midle sådan tilfældighed ud. 

