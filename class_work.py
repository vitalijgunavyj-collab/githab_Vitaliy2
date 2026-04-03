#Створити стрічку тексту
#Розбити її по пробілам на слова
#Знайти найкоротше та найдовше слова
from lists_practice import length_of_string

text = "i like play football"
words = text.split()

longest_word = ''
shortest_word = ''
longest_word_lenth = 0
shortest_word_lenth = 0

for word in words:
    print(word)
    current_word_lenth = len(word)
    print(current_word_lenth)

if current_word_lenth > longest_word_lenth:
    longest_word_lenth = current_word_lenth
    longest_word = word
