#Programmer: Mark Morreale
#Goal: Find probability of whether "ie" or "ei" occurs to make the sound IY (ARPABET) in English words

#Use the CMUDict Pronouncing Dictionary to find when words contain the sound IY
#It has the raw data (and entries data) and the sets will be made from those lines,
#excluding extra info from the set

#TODO: add list of all CMUDict words containing the sound IY @markmorreale
#use more methods to work with all the words in the dictionary

#create initial list of all entries regardless of letters and sounds
import cmudict
init_dict = cmudict.entries()

ie_entries = []
ei_entries = []
IY_entries = []

for entry in init_dict:
    if "ie" in entry[0]:
        ie_entries.append(entry)
    if "ei" in entry[0]:
        ei_entries.append(entry) 
    for sound in entry[1]:
        if "IY" in sound:
            IY_entries.append(entry)

#We now have three sets of words that contain letters or sounds we are investigating
#Can check statistics on those sets


#looking at the output, there is a 'u' character before all the
# parts of entries, but that seems to be how the list is printed, the parts are fine
print("There are",len(ie_entries),"entries containing \"ie\"")
print("There are",len(ei_entries),"entries containing \"ei\"")
print("There are",len(IY_entries),"entries containing the sound IY")
print(ie_entries[0])
print(ei_entries[0])
print(IY_entries[0])

'''potential exclusions

for entry in ei_entries:
    if "eei" in entry[0]:
        print(entry[0])
    if entry[0][-3:] == "ing" or entry[0][-3:] == "ism":
        print(entry[0])
'''