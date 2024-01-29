VOWEL = {'a', 'e', 'i', 'o', 'u'}
VOWEL_END = {'a', 'e', 'i', 'o', 'u', 'y'}
SPECIALS = {'xr', 'yt'}


def translate(text):
    piggyLatin = []
    for word in text.split():
        if word[0] in VOWEL or word[:2] in SPECIALS:
            piggyLatin.append(word + "ay")
            continue
        for pos in range(1, len(word)):
            if word[pos] in VOWEL_END:
                pos += 1 if word[pos] == 'u' and word[pos-1] == 'q' else 0
                piggyLatin.append(word[pos:] + word[:pos] + "ay")
                break
    return " ".join(piggyLatin)
    
print(translate("queen"))   