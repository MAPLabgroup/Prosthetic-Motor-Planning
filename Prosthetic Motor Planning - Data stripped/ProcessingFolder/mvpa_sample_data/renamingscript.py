import os

def replace(fpath, old_str, new_str):
    for path, subdirs, files in os.walk(fpath):
        for name in files:
            os.rename(os.path.join(path,name), os.path.join(path,name.lower().replace(old_str,new_str)))

cwd = "C:/Users/5328r/Documents/Homewrk/Research/ProcessingFolder/mvpa_sample_data/SAL/"

subs = ["05", "06", "07", "08", "09", "10", "11", "12","13", "14", "15", "16"]
runs = ["01", "02", "03", "04"]

for sub in subs:
    for run in runs:
        runDir = cwd + "sub-" + sub + "/func/run" + run

        replace(runDir, "sub-" + sub + "_task-ao_run-" + run + "_bold", "run" + run)