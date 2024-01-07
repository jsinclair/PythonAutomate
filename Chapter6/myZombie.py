import zombiedice, random

class MyZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']

            if brains < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

class RandomZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        zombiedice.roll()

        while random.randint(0, 1) == 0:
            zombiedice.roll() # roll again

class TwoBrainsZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll() # first roll
        
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']

            if brains < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

class TwoShotgunsZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll() # first roll
        
        shotguns = 0
        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']

            if shotguns < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

class CommitalZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll() # first roll
        rolls = 1

        target = random.randint(1, 4)
        
        shotguns = 0
        while diceRollResults is not None and rolls < target:
            shotguns += diceRollResults['shotgun']

            if shotguns < 2:
                rolls += 1
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

class ScaredZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll() # first roll
        
        shotguns = 0
        brains = 0
        while diceRollResults is not None:
            print(diceRollResults)
            shotguns += diceRollResults['shotgun']
            brains += diceRollResults['brains']

            if brains >= shotguns:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

zombies = (
    RandomZombie(name='Random'),
    TwoBrainsZombie(name='Two Brains'),
    TwoShotgunsZombie(name='Two Shotguns'),
    CommitalZombie(name='Commital'),
    ScaredZombie(name='Scared')
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
#zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)