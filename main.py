def count_words_in_line(line, word):
    # Zlicza wystąpienia danego słowa w linijce
    return line.lower().count(word.lower())

def main():
    # 1. Pobranie liczby linijek tekstu
    num_lines = int(input(""))

    # 2. Pobranie tekstu od użytkownika
    lines = []
    for i in range(num_lines):
        line = input(f"")
        lines.append(line)

    # 3. Pobranie liczby słów do wyszukania
    num_words = int(input(""))

    # 4. Pobranie słów od użytkownika
    words = []
    for i in range(num_words):
        word = input(f"")
        words.append(word)

    # 5. Dla każdego słowa zliczenie i posortowanie linijek
    for word in words:
        counts = [(i, count_words_in_line(line, word)) for i, line in enumerate(lines)]
        # Sortowanie według liczby wystąpień (najpierw najwięcej)
        sorted_counts = sorted(counts, key=lambda x: x[1], reverse=True)
        sorted_lines = [line_num for line_num, count in sorted_counts if count > 0]

        print(sorted_lines)

if __name__ == "__main__":
    main()

