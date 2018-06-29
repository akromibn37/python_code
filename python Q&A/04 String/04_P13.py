t = input().strip().lower()
n = 0
in_vowel_group = False
for e in t:
    if e in 'aeiou':
        if not in_vowel_group:
            n += 1
            in_vowel_group = True
    else:
        in_vowel_group = False
print(n)
