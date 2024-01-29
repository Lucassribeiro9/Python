def translate(text):
    vowels = "aeiou"
    pigged_text = ""
    for word in text.split():
        if word[0] in vowels or word[:2] in ["xr", "yt"]:
            pigged_text += word + "ay"
        elif "qu" in word:
            index = word.index("qu") + 2
            pigged_text += word[index:] + word[:index] + "ay"
        elif all(letter not in vowels for letter in word):
            return word + "ay"
        else:
            index = 0
            while index < len(word) and word[index] not in vowels:
                index += 1
            pigged_text += word[index:] + word[:index] + "ay"
    return pigged_text
    
print(translate("quick fast run"))