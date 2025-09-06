def dvig_chisl(text, sdvig = 3):

    result = []

    for char in text:
        if char.isalpha():
            dor = ord('A') if char.isupper() else ord('a')
            sdvig_char = chr((((ord(char))) - dor + sdvig) % 26 + dor)
            result.append(sdvig_char)
        else:
            result.append(char)
    return ''.join(result)
inp_text = 'Python_is_good'
sdvig_text = dvig_chisl(inp_text)
print(f"Исходный текст: {inp_text}")
print(f"Преобразованный текст {dvig_chisl(sdvig_text)}")
