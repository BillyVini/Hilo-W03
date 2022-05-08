from cards import Cards

initial_card = Cards()

class Hilo:

    def __init__(self):
        
        self.is_playing = True
        self.points = 300
        self.guess = ''
        self.initial_card = initial_card.number()
        self.next_card = 0

    def start_game(self):

        while self.is_playing and self.points > 0:
            self.get_guess()
            self.get_next_card()
            self.update_points()
            self.play_again()
    
    def get_guess(self):

        print(f'The card is: {self.initial_card}')
        self.guess = input('Higher or lower? [h/l] ')
        while self.guess not in ['h', 'l']:
            self.guess = input('Please enter either a lowercase "h" or a lower case "l"')
    
    def get_next_card(self):
        
        next_card = Cards()
        self.next_card = next_card.number()
        print(f'Next card was: {self.next_card}')
    
    def update_points(self):

        if self.next_card > self.initial_card:
            if self.guess == 'h':
                self.points += 100
            else:
                self.points -= 75
        
        if self.next_card < self.initial_card:
            if self.guess == 'h':
                self.points -= 75
            else:
                self.points += 100
        
        print(f"Your score is: {self.points}")
    
    def play_again(self):

        if self.points < 0:
            self.is_playing = False
            return
        
        self.is_playing = input('Play again? [y/n]')
        while self.is_playing not in ['y', 'n']:
            self.is_playing = input('Please enter either a lowercase "y" or a lowercase "n"')
        self.is_playing = (self.is_playing == 'y')
        self.initial_card = initial_card.number()