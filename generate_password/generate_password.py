#generate password
import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''

n = int(input('Введите количество паролей для генерации: Enter the number of passwords to generate: '))
length = int(input('Введите длину пароля: Enter password length: '))
add_digit = input('Включить цифры? (д = да, н = нет) Include numbers? (y = yes, n = no)').strip()
add_lowercase = input('Включить прописные буквы? (д = да, н = нет) Include capital letters? (y = yes, n = no) ').strip()
add_uppercase = input('Включить строчные буквы? (д = да, н = нет) Include lowercase letters? (y = yes, n = no)').strip()
add_punctuation = input('Включить символы, такие как !#$%&*+-=?@^_? (д = да, н = нет) Include characters such as !#$%&*+-=?@^_? (y = yes, n = no)').strip()
remove_badsymbols = input('Исключить символы il1Lo0O? (д = да, н = нет) Exclude characters il1Lo0O? (y = yes, n = no) ').strip()

if add_digit.lower() == 'д' or add_digit.lower() == 'y':
    chars += digits
if add_lowercase.lower() == 'д' or add_digit.lower() == 'y':
    chars += lowercase_letters
if add_uppercase.lower() == 'д' or add_digit.lower() == 'y':
    chars += uppercase_letters
if add_punctuation.lower() == 'д' or add_digit.lower() == 'y':
    chars += punctuation
if remove_badsymbols.lower() == 'д' or add_digit.lower() == 'y':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')


def generate_password(length, chars):
    password = ''
    for j in range(length):
        password += random.choice(chars)
    return password

for _ in range(n):
    print(generate_password(length, chars))

generate_password(length, chars)