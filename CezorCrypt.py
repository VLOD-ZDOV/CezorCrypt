#Основная функция разшифровки принимающая:
#text - текст для расшифровки
#shift - сдвиг 1-25 / 1-32
#alphabet - алфавит en/ru
def caesar_cipher(text, shift, alphabet):
    result = ''
    for char in text:
        if char.isalpha():
            idx = alphabet.index(char)
            shifted = (idx + shift) % len(alphabet)
            result += alphabet[shifted]
        else:
            result += char
    return result

def all_caesar_shifts(text, alphabet):                                 #Принимает исходный текст и алфавит
    for i in range(1, len(alphabet)):                                  #Цикл для каждой буквы алфавита
        print(f"Shift {i}: {caesar_cipher(text, i, alphabet)}")        #Собственно выводит все возможные комбинации

def choose_alphabet():
    language = input("Выберите язык (английский - 'en', русский - 'ru'): ")
    if language.lower() == 'en':
        return 'abcdefghijklmnopqrstuvwxyz'
    #ABCDEFGHIJKLMNOPQRSTUVWXYZ
    elif language.lower() == 'ru':
        return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    #АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ
    else:
        print("Неправильный выбор. Пожалуйста, выберите 'en' для английского или 'ru' для русского.")
        return choose_alphabet()                      #При неверном вводе просто перезапускает функцию
    
def main():
    alphabet = choose_alphabet()                      #Переменная алфавит равна функции выбора алфавита
    text = input("Введите текст для расшифровки: ")   
    all_caesar_shifts(text, alphabet)                 #Передает в функцию текст и алфавит
main()