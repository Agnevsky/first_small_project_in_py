def caesars_cipher(step, text_to_change, name):
    alphabet_ru = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
                   'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    alphabet_en = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                   "u", "v", "w", "x", "y", "z"]
    n_ru = len(alphabet_ru)
    n_en = len(alphabet_en)
    new_list = []

    direction = input("Хотите шифровать - 1 или дешифровать - 2 текст? Do you want to encrypt - 1 or decrypt - 2 text? ")
    if direction == "1":
        lang = input(f"На каком языке хотите выполнить шифрование? What language do you want to encrypt in? ")

        def encryption():
            if lang == "ru":
                for i in text_to_change:
                    new_list.append(i)

                for j in range(len(text_to_change)):
                    if new_list[j].isalpha() and new_list[j].lower() in alphabet_ru:
                        x = alphabet_ru.index(new_list[j].lower())
                        y = (x + step) % n_ru
                        if new_list[j].istitle():
                            new_list[j] = alphabet_ru[y].title()
                        else:
                            new_list[j] = alphabet_ru[y]
                    else:
                        new_list[j] = new_list[j]



            elif lang == "en":
                for i in text_to_change:
                    new_list.append(i)

                for j in range(len(text_to_change)):
                    if new_list[j].isalpha() and new_list[j].lower() in alphabet_en:
                        x = alphabet_en.index(new_list[j].lower())
                        y = (x + step) % n_en
                        if new_list[j].istitle():
                            new_list[j] = alphabet_en[y].title()
                        else:
                            new_list[j] = alphabet_en[y]
                    else:
                        new_list[j] = new_list[j]

        encryption()
        print(*new_list, sep='')

    elif direction == "2":
        lang = input(f"На каком языке хотите выполнить дешифрование? What language do you want to decrypt in? ")

        def decryption():
            if lang == "ru":
                for i in text_to_change:
                    new_list.append(i)

                for j in range(len(text_to_change)):
                    if new_list[j].isalpha() and new_list[j].lower() in alphabet_ru:
                        y = alphabet_ru.index(new_list[j].lower())
                        x = (y - step) % n_ru
                        if new_list[j].istitle():
                            new_list[j] = alphabet_ru[x].title()
                        else:
                            new_list[j] = alphabet_ru[x]
                    else:
                        new_list[j] = new_list[j]

            elif lang == "en":
                for i in text_to_change:
                    new_list.append(i)

                for j in range(len(text_to_change)):
                    if new_list[j].isalpha() and new_list[j].lower() in alphabet_en:
                        y = alphabet_en.index(new_list[j].lower())
                        x = (y - step) % n_en
                        if new_list[j].istitle():
                            new_list[j] = alphabet_en[x].title()
                        else:
                            new_list[j] = alphabet_en[x]
                    else:
                        new_list[j] = new_list[j]

        decryption()
        print(*new_list, sep='')


name = input("Введите ваше имя: Enter your name: ")
print(f"Привет {name}")
text_to_change = input("Введите текст, с которым предстоит работать: Enter the text you want to work with:")
step = int(input("Введите шаг движения шифра: Enter the cipher movement step:"))
caesars_cipher(step, text_to_change, name)
