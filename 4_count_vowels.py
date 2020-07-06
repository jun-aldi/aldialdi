def count_vowels(txt):
    count=0
    for i in txt:
        if i == "a" or i=="i" or i=="u" or i=="e" or i=="o":
            count += 1
    return count
print (count_vowels("Prediction"))