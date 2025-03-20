from die import Die

class Player:
    def __init__(self):
        self.die = [Die(), Die(), Die()]
        self.die.sort()
        self._points = 0

    @property
    def points(self):
        return self._points
    
    def roll_dice(self):
        for die in self.die:
            die.roll()
        self.die.sort()

    def has_pair(self):
        if self.die[0] == self.die[1] or self.die[1] == self.die[2] or self.die[0] == self.die[2]:
            self._points += 1
            return True
        return False

    def has_three_of_a_kind(self):
        if self.die[0] == self.die[1] == self.die[2]:
            self._points += 3
            return True
        return False

    def has_series(self):
        values = [die.value for die in self.die]
        if values[1] - values[0] == 1 and values[2] - values[1] == 1:
            self._points += 2
            return True
        return False
    
    def __str__(self):
        return f"D1 = {self.die[0]}, D2 = {self.die[1]}, D3 = {self.die[2]}"