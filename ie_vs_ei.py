#Programmer: Mark Morreale
#Goal: Find probability of whether "ie" or "ei" occurs to make the sound IY (ARPABET) in English words

#Use the CMUDict Pronouncing Dictionary to find when words contain the sound IY
#It has the raw data (and entries data) and the sets will be made from those lines,
#excluding extra info from the set

#TODO: count occurences with "c" before ie and ei, also count sounds C, S, before IY

#create initial list of all entries regardless of letters and sounds
import cmudict
init_dict = cmudict.entries()

ie_entries = []
ei_entries = []
IY_entries = []

#we can count the basic combinations while making the sets
cie_counter = 0
cei_counter = 0

for entry in init_dict:
    if "ie" in entry[0]:
        ie_entries.append(entry)
    if "cie" in entry[0]:
        cie_counter += 1
        print(entry[0])
    if "ei" in entry[0]:
        ei_entries.append(entry) 
    if "cei" in entry[0]:
        cei_counter += 1

    if entry[0] == "science":
        print(entry[1])
    if entry[0] == "valencienne":
        print(entry[1])

    for sound in entry[1]:
        if "IY" in sound:
            IY_entries.append(entry)

#We now have three sets of words that contain letters or sounds we are investigating
#Can check statistics on those sets
ie_count = len(ie_entries)
ei_count = len(ei_entries)


#looking at the output, there is a 'u' character before all the
#parts of entries, but that seems to be how the list is printed, the parts are fine

print("EXCEPTIONS ARE NOT ACCOUNTED FOR.")
print("There are",ie_count,"entries containing ie")
print(cie_counter,"of those entries have the string \"cie\"")
print("That means",round(cie_counter/ie_count*100,2),"% of the ie have \"cie\"\n")

print("There are",ei_count,"entries containing \"ei\"")
print(cei_counter,"of those entries have the string \"cei\"")
print("That means",round(cei_counter/ei_count*100,2),"% of the ei have \"cei\"\n")

print("There are",len(IY_entries),"entries containing the sound IY")
'''print(ie_entries[0])
print(ei_entries[0])
print(IY_entries[0])'''

'''potential exclusions

for entry in ei_entries:
    if "eei" in entry[0]:
        print(entry[0])
    if entry[0][-3:] == "ing" or entry[0][-3:] == "ism":
        print(entry[0])
'''