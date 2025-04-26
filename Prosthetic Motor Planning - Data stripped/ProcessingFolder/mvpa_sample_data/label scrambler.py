import os
import pandas
import numpy

"""
1. Find allevents file per subject
2. Read it all into a table
3. Scramble the labels
4. Save new events file

5. Go to matlab and use that new events file to make new model files
    6. Rerun analyses and get predictive accuraciess
"""
subs = ["07"]
# ["01", "02", "03", "05", "07", "08", "09", "10", "11", "12", "13", "14", "15", "20-pre", "21-pre"]

for subNum in subs:
    filepath = "C:/Users/5328r/Documents/Homewrk/Research/ProcessingFolder/mvpa_sample_data/SAL/sub-"+subNum+"/func/sub-"+subNum+"_allEvents.tsv"
    origData = pandas.read_csv(filepath, delimiter="\t")
    # print(filepath)
    # print(origData[:2])
    
    # Scrambling Step
    origData["TrialType"] = numpy.random.permutation(origData["TrialType"].values)
    newFile = "C:/Users/5328r/Documents/Homewrk/Research/ProcessingFolder/mvpa_sample_data/SAL/sub-"+subNum+"/func/sub-"+subNum+"_scrambledEvents.tsv"

    # newFile = open(newFile, "w")
    # newFile.write(origData.to_string(index=False,justify="left"))
    # newFile.close()

    for i in range(len(origData["Onset"])-1):
        if (origData["Onset"][i+1] - origData["Onset"][i] < 2):
            origData["Onset"][i] -= 2

    origData.to_csv(newFile, sep="\t",index=False)