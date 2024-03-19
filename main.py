what_do = input("Что мы делаем? (шифрование или дешифрование)\n")
what_language = input("Выберете язык. (русский или английский)\n")
what_step = int(input("Шаг сдвига? (Со сдвигом вправо)\n"))
sentenses = input("Введите запрос (на русском языке без буквы 'ё')\n")
chars = ""
if what_do == "шифрование":
    if what_language == "русский":
        for i in range(len(sentenses)):
            if 'А' <= sentenses[i] <= 'Я':
                chars = chars + chr((ord(sentenses[i]) - ord('А') + what_step) % 32 + ord('А')) 
            elif 'а' <= sentenses[i] <= 'я':
                chars = chars + chr((ord(sentenses[i]) - ord('а') + what_step) % 32 + ord('а')) 
            else:
                chars += sentenses[i]
        print(chars) 
    if what_language == "английский":
        for i in range(len(sentenses)):
            if 'A' <= sentenses[i] <= 'Z':
                chars = chars + chr((ord(sentenses[i]) - ord('A') + what_step) % 26 + ord('A')) 
            elif 'a' <= sentenses[i] <= 'z':
                chars = chars + chr((ord(sentenses[i]) - ord('a') + what_step) % 26 + ord('a')) 
            else:
                chars += sentenses[i]
        print(chars)
else:
    if what_language == "русский":
        for i in range(len(sentenses)):
            if 'А' <= sentenses[i] <= 'Я':
                chars = chars + chr((ord(sentenses[i]) - ord('А') - what_step) % 32 + ord('А')) 
            elif 'а' <= sentenses[i] <= 'я':
                chars = chars + chr((ord(sentenses[i]) - ord('а') - what_step) % 32 + ord('а')) 
            else:
                chars += sentenses[i]
        print(chars) 
    if what_language == "английский":
        for i in range(len(sentenses)):
            if 'A' <= sentenses[i] <= 'Z':
                chars = chars + chr((ord(sentenses[i]) - ord('A') - what_step) % 26 + ord('A')) 
            elif 'a' <= sentenses[i] <= 'z':
                chars = chars + chr((ord(sentenses[i]) - ord('a') - what_step) % 26 + ord('a')) 
            else:
                chars += sentenses[i]
        print(chars)