from random import choice

class Words:
    def __init__(self):
        # Getting list of words from redacted file which lengthier than 3
        # from alice in wonderland txt
        self.list_of_words = [word for word in open('data/wonderland_redacted.txt').read().split() if len(word) > 3]
        self.words_to_be_typed = []
        self.words_input = []

    def give_random_word(self):
        return choice(self.list_of_words)

    def clear_lists(self):
        self.words_to_be_typed = []
        self.words_input = []

    def show_results(self):
        points = 0
        incorrect_words = 0
        shown_words = len(self.words_to_be_typed)
        for i in range(shown_words):
            if self.words_input[i] == self.words_to_be_typed[i]:
                points += 1
            else:
                incorrect_words += 1
        return (points, incorrect_words, shown_words)