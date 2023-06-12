#Задача34

def check_rhythm(poem):
    words = poem.split()  
    syllables = []  

    for word in words:
        syllables.append(count_syllables(word))  # Подсчитываем слоги в каждом слове

    if len(set(syllables)) == 1:
        return "Парам пам-пам"
    else:
        return "Пам парам"

def count_syllables(word):
    vowels = "аеёиоуыэюя"  # Список гласных букв

    count = 0
    for char in word.lower():
        if char in vowels:
            count += 1

    return count

poem = input("Введите стихотворение Винни-Пуха: ")
result = check_rhythm(poem)
print(result)