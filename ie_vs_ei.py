import pronouncing


word = "perceive"
print("The CMUDict Pronouncing Dictionary will give the ARPABET pronunciation for the string assigned to 'word':", word)
print(pronouncing.phones_for_word(word))