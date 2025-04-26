"""
Author: Jason Miller
Date: 6/15/24
This file reads events.tsv files from Dr. John Johnson's study and
concatenates the names, onsets, and durations to one tsv file. 

Using this one tsv file, we can then read it and create specific model
files with classes we wish to pass into MVPA
"""

import os


# Subject 16 doesnt have events files
subjectNumber = "16" # The numbers that show up after "sub-" within the study folder

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# 1. Get into sub+subjectNumber/func and search for all the events.tsv files 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
eventsFiles = [] # eventsFiles will contain DirEntry objects for every events file
filepath = "./sub-" + subjectNumber + "/func"

files = os.scandir(filepath)

for entry in files :
    if "events.tsv" in entry.name:
        eventsFiles.append(entry) 
print("Ensure that the events files are listed in ascending order. Whatever order they are in is the order the model file will be built in")
print(eventsFiles)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# 2. Open each file in ascending numerical order and extract their names, onsets, and durations to 
#    a few lists which we define first
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
names = [] # Predefined names of the classes we wish to classify using MVPA
onsets = [] # When each event starts  
durations = [] # How long each trial lasts after onset

    # Because we're concatenating runs, runs after the 1st will have additional time after them based on how many 
    # BOLD scans are in each run. For this we need both the TR of the scanner and the BOLDS per run.
repTime = 2.0 
boldsPerRun = 238 # Same as the number of files in the individual run folders
betweenRunTimeOffset = repTime * boldsPerRun

for i in range(len(eventsFiles)):
    
    file = open(eventsFiles[i].path)
    data = file.readlines()
    file.close()

    print(data[0])
    data = data[1:] #This line should get rid of the header

    for line in data:
        components = line.split()
        onsets.append(round(float(components[0]) + (i* betweenRunTimeOffset)))
        durations.append(components[1])
        names.append(components[2])


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# 3. Save these lists to a new tsv file 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
newFileName = "sub-" + subjectNumber + "_allEvents.tsv"
newFile = open(filepath + "/" + newFileName, "w")

newFile.write("TrialType\tOnset\tDuration\n") #Header
for i in range(len(names)):
    newFile.write(names[i] + "\t" + str(onsets[i]) + "\t" + durations[i] + "\n")
newFile.close()