def scrabble(symbols: str, word: str) -> bool:
    symbols = symbols.lower()
    word = word.lower()
    symbols_count = {}
    word_count = {}
    for symbol in symbols:
        symbols_count[symbol] = symbols_count.get(symbol, 0) + 1
    for letter in word:
        word_count[letter] = word_count.get(letter, 0) + 1
    for letter in word_count:
        if letter not in symbols_count:
            return False
        if word_count[letter] > symbols_count[letter]:
            return False
    return True


from collections import Counter

def scrabble_(symbols: str, word: str) -> bool:
    symbols_count = Counter(symbols.lower())
    word_count = Counter(word.lower())
    
    return all(word_count[letter] <= symbols_count.get(letter, 0) for letter in word_count)


def main():
    print(scrabble_('rkqOdlw', 'world'))  # True
    print(scrabble_('AVJ', 'java'))  # False
    print(scrabble_('avjafff', 'java'))  # True
    print(scrabble_('', 'hexlet'))  # False
    print(scrabble_('scriptingjava', 'JavaScript'))  # True


if __name__ == "__main__":
    main()


# Реализуйте функцию-предикат scrabble, которая принимает на вход два параметра: набор символов (строку) и слово. Функция должна проверять, можно ли из переданного набора составить это слово. В результате вызова функция возвращает True или False.

# При проверке учитывается количество символов, которые нужны для составления слова, но не учитывается их регистр.

# Для решения используйте встроенный инструмент — Counter.

# Пример
# scrabble('rkqodlw', 'world')  # True
# scrabble('avj', 'java')  # False
# scrabble('avjafff', 'java')  # True
# scrabble('', 'hexlet')  # False
# scrabble('scriptingjava', 'JavaScript')  # True