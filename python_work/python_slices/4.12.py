crystal_activies = ["camping", "hiking", "biking", "outdoor"]
vikram_activites = ["computer", "driving", "music", "instruments"]
vikram_activites = crystal_activies[:]
vikram_activites.append("hiking")
#print (vikram_activites)
crystal_activies = vikram_activites[:]
crystal_activies.append("tweet")
#print(crystal_activies)

for vik_act in vikram_activites:
    print(f"Vikram's favortite activites are {vik_act.title()}")
print("\n")
for cry_act in crystal_activies:
    print (f"Crystal's favorite activites are {cry_act.title()}")
