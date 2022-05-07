from random import randint
from abc import abstractmethod


class Game:
    _words = ['hamak', 'ognisko', 'pies', 'arbuz', 'oranżada', 'pomarańcza', 'herbata', 'słońce']
    _possible_chars = [
        'a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i',
        'j','k', 'l', 'ł', 'm', 'n', 'ń', 'o', 'ó', 'p', 'q', 'r',
        's', 'ś', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ź', 'ż'
    ]
    
    
    def __init__(self, dif_level):
        self.dif_level = dif_level
    
    
    def _play(self, num_players):
        self.num_players = num_players
        print("\nNowa gra rozpoczęta, liczba graczy:", self.num_players)
    
    
    @abstractmethod
    def start_game(self):
        ...
    
    
    def validate_char(self, char):
        return True if char in self._possible_chars else False


class Hangman(Game):
    def __init__(self):
        dif_level = self.choose_difficulty()
        super().__init__(dif_level)
        
        num_players = self.choose_num_players()
        super()._play(num_players)
        
        self.cur_word = ''
        self.errors = 0
        self.guessed_letters = []
        
        self.start_game()
    
    
    def choose_difficulty(self):
        print("Wybierz poziom trudności:")
        print("1. Początkujący - 8 możliwych pomyłek")
        print("2. Średni - 5 możliwych pomyłek")
        print("3. Zaawansowany - 3 możliwe pomyłki")
        
        try:
            difficulty = int(input("Twój wybór: "))
        except ValueError:
            print("Niepoprawny wybór, wybierz liczbę od [1-3]\n")
            return self.choose_difficulty()
        
        if difficulty not in [1, 2, 3]:
            print("Niepoprawny wybór, wybierz liczbę od [1-3]\n")
            return self.choose_difficulty()
        
        diff_dic = {1: 8, 2: 5, 3: 3}
        return diff_dic[difficulty]
    
    
    def choose_num_players(self):
        try:
            np_input = int(input("\nPodaj liczbę graczy: "))
        except ValueError:
            print("Podaj 1 lub 2 jako liczbę graczy")
            return self.choose_num_players()
        
        if np_input not in [1, 2]:
            print("Niepoprawna liczba graczy! Graczy może być jeden lub dwóch!")
            return self.choose_num_players()
        
        return np_input
    
    
    def start_game(self):
        if self.num_players == 1:
            self.cur_word = super()._words[randint(0, len(super()._words) - 1)]
        elif self.num_players == 2:
            self.take_word()
            
        while not self.check_if_win():
            if self.errors == self.dif_level:
                self.defeat()
                return
            else:
                self.take_letter()
        
        self.victory()
    
    
    def check_if_win(self):
        for letter in self.cur_word:
            if letter not in self.guessed_letters:
                return False
        return True
    
    
    def restart_game(self):
        print("Restart gry\n")
        self.__init__()
    
    
    def display_word(self):
        print("\nLiczba możliwych pomyłek:", self.dif_level - self.errors)
        
        for c in self.cur_word:
            if c not in self.guessed_letters:
                print("_", end="")
            else:
                print(c, end="")
        print()
    
    
    def defeat(self):
        print("Przegrałeś/aś! Poprawnym hasłem było", self.cur_word)
        
        if input("\nCzy chcesz zagrać ponownie [t/n]? ") == 't':
            self.restart_game()
        else:
            print("Koniec gry")
    
    
    def victory(self):
        print("\nWygrałeś/aś! Odgadnięte hasło:", self.cur_word)
        print("Zostało Ci przy tym", self.dif_level - self.errors, "dodatkowych prób")
        
        if input("\nCzy chcesz zagrać ponownie [t/n]? ") == 't':
            self.restart_game()
        else:
            print("Koniec gry")
    
    
    def take_letter(self):
        self.display_word()
        
        letter = input("Podaj literę do hasła: ")
        
        if not super().validate_char(letter):
            print('Niepoprawny znak')
        else:
            if letter in self.guessed_letters:
                print("Ta litera została już wpisana")
                print(self.guessed_letters)
            else:
                self.guessed_letters.append(letter)
                self.check_if_letter_in_cur_word(letter)
    
    
    def check_if_letter_in_cur_word(self, letter):
        if letter not in self.cur_word:
            self.errors += 1
            print("Litera '" + letter + "' nie znajduje się w haśle.")
        else:
            print("Poprawny strzał!")
    
    
    def take_word(self):
        while self.cur_word == '':
            new_word = input("Podaj hasło do zgadnięcia: ")
            self.validate_word(new_word)
    
    
    def validate_word(self, word):
        if self.validate_length(word):
            if self.validate_chars(word):
                self.cur_word = word
            else:
                print("W haśle znajdują się niepoprawne znaki")
        else:
            print("Niepoprawna długość hasła. Liczba liter powinna zawierać się w (3, 10] znakach.")
    
    
    def validate_length(self, word):
        return True if 3 < len(word) <= 10 else False
    
    
    def validate_chars(self, word):
        for c in word:
            if not super().validate_char(c):
                return False
        return True


game = Hangman()