
class GameCharacter:
    
    hp_cap = 100
    mp_cap = 50
        
    def __init__(self, name):
        self._name = name
        self._level = 1
        self._health = GameCharacter.hp_cap
        self._mana = GameCharacter.mp_cap
        
    
    @property
    def name(self):
        return self._name
    
    @property
    def health(self):
        return self._health
    
    @health.setter
    def health(self, new_value):
        if(new_value < 0):
            self._health = 0
        elif(new_value > GameCharacter.hp_cap):
            self._health = GameCharacter.hp_cap
        else:
            self._health = new_value
        
    @property
    def mana(self):
        return self._mana
    
    @mana.setter
    def mana(self, new_value):
        
        if(new_value < 0):
            self._mana = 0
        elif(new_value > GameCharacter.mp_cap):
            self._mana = GameCharacter.mp_cap
        else:
            self._mana = new_value
              
    @property
    def level(self):
        return self._level
    
    def level_up(self):
        self._level += 1
        self.health = 100
        self.mana = 50
        print(f"{self._name} leveled up to {self._level}!")
        
    def __str__(self):
        stats = vars(self)
        lines = []
        for stat, value in stats.items():
            lines.append(f"{stat.strip('_').capitalize()}: {value}\n")
        
        result = "".join(lines)
        return result
    
    
hero = GameCharacter("Kratos") # Creates a new character named Kratos
print(hero)  # Displays the character's stats

hero.health -= 30  # Decreases health by 30
hero.mana -= 10    # Decreases mana by 10
print(hero)  # Displays the updated stats

hero.level_up()  # Levels up the character
print(hero)  # Displays the stats after leveling up
