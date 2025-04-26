
% Defines the variable order and durations vector (even though not used)
subNum = ['16'];
modelName = 'IntvsPros';
names = {'intact','pros', 'readyTxt', 'promptTxt','fixation'};
    % Note; the above categories are currently oversimplifications. These
    % do not account for the potential alternating objects or alternations
    % between prosthetic and intact limb viewing. This is merely a first
    % step to be able to run the script and get some basic result.
durations = {0, 0, 0, 0,0};
    % Note; Although durations don't seem to be used anywhere, the
    % information still exists within allEvents so if we ever need it we
    % can update this. For now though, all zeroes is fine

% Reads the trial names, onsets, and durations into a table.
filename = strcat("C:\Users\5328r\Documents\Homewrk\Research\ProcessingFolder\mvpa_sample_data\SAL\sub-",subNum,"\func\sub-",subNum,"_allEvents.tsv");
T = readtable(filename, "FileType","text",'Delimiter', '\t');
    % THE FILE OPENS YAAAAAAAAAY 

%Seperates the table into each type of variable
intact = T(contains(T.TrialType, {'intact'}, "IgnoreCase", true),:);

pros = T(contains(T.TrialType, {'pros'}, "IgnoreCase", true),:);
toDelete = startsWith(pros.TrialType,"IntProsAlt"); 
% ^^^ We're deleting these for now since I have no idea which in the
% alternating pattern is the prosthetic and which is the intact
pros(toDelete,:) = [];

ready =  T(contains(T.TrialType, {'ready'}, "IgnoreCase", true),:);

prompt = T(contains(T.TrialType, {'prompt'}, "IgnoreCase", true),:);

fixation = T(contains(T.TrialType, {'fixation'}, "IgnoreCase", true),:);


% TODO HERE

% Initializing vectors for onsets. We just need to extract the onsets
% column from the separated tables
intactVec = [intact(:,'Onset')];
prosVec = [pros(:,"Onset")];
readyVec = [ready(:,"Onset")];
promptVec = [prompt(:,"Onset")];
fixationVec = [fixation(:,"Onset")];

% Saving onsets to its own collected variable in the same order as the
% names
onsets = {intactVec, prosVec, readyVec, promptVec, fixationVec};

if ~exist(strcat('./sub-',subNum,'/results-',subNum), 'dir')
     mkdir(strcat('./sub-',subNum,'/results-',subNum))
end

save(strcat('./sub-',subNum,'/results-',subNum,"/sub-",subNum,"_Model_",modelName),"names","onsets","durations");