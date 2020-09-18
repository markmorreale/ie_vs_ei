#Programmer: Mark Morreale
#Goal: Find probability of whether "ie" or "ei" occurs to make the sound IY (ARPABET) in English words

#Use the CMUDict Pronouncing Dictionary to find when words contain the sound IY
#pronouncing has a method "phones_for_word" which will let us find the ARPABET version of English words
import pronouncing

#test word
word = "perceive"
print("The CMUDict Pronouncing Dictionary will give the ARPABET pronunciation for the string assigned to 'word':", word)
print(pronouncing.phones_for_word(word))

#TODO: add list of all CMUDict words containing the sound IY @markmorreale
#use more methods to work with all the words in the dictionary

