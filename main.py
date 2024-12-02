import sys
import time

def print_lyrics():
    lines = [
        ("You can't fight it, you can't breathe", 0.03),
        ("You say something so lovin', but", 0.03),
        ("Now I gotta let you go", 0.03),
        ("You'll be better off in someone new", 0.03),
        ("I don't wanna be alone", 0.03),
        ("You know it hurts me too", 0.03),
        ("You look so broken when you cry", 0.03),
        ("One more and then I say goodbye", 0.03),
        ("Sometimes, all I think about is you", 0.03),
        ("Late nights in the middle of June", 0.03),
        ("Heat waves been fakin' me out", 0.03),
        ("Can't make you happier now", 0.03)
    ]

    base_delay = 0.02       #Базова затримка для плавності
    increment = 0.001       #Збільшення для створення ефекту уповільнення

    for line, char_delay in lines:
        current_delay = base_delay
        for char in line:
            print(char, end='', flush=True)
            time.sleep(current_delay)
            current_delay += increment  # Поступове збільшення затримки
        print('')           #Перехід на новий рядок
        time.sleep(0.5)     # Невелика пауза між рядками

print_lyrics()
