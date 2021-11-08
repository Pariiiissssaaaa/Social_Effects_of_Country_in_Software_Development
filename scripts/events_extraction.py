from library import *
from utils import *

path_1="/lfs1/GitHubAPI/events/"
path_2="/lfs1/GitHubAPI/events/2020/"



# with open('ai_repo_ids.data', 'rb') as filehandle:
#     repo_ids=pickle.load(filehandle)
with open('case_study_repo_ids.data', 'rb') as filehandle:
    repo_ids=pickle.load(filehandle)

    
    
    
repo_ids=set(repo_ids)
print (len(repo_ids))

event_profiles_1=glob.glob(path_1+"*.json.gz")
event_profiles_2=glob.glob(path_2+"*.json.gz")
event_profiles=event_profiles_1+event_profiles_2

print (len(event_profiles))

def process_event (f):
    output=[]
    for line in (gzip.open(f, 'r')):
        line=json.loads(line)
        if (line['repo']['id']) in repo_ids:
            output.append([line['id'], line['type'], line['repo']['id'], line['repo']['name'], line['actor']['id'], f.split('/')[-1][:-8]])
    return output



files=event_profiles
process=process_event
data=parallel_process (files, process)

result_event=(list(itertools.chain.from_iterable(data)))
print (len(result_event))

good_columns=['event_id', 'event_type', 'repo_id', 'repo_name', 'actor_id', 'file_date']
event_pd=pd.DataFrame(result_event, columns=good_columns)
event_pd.to_pickle('events_case_study.pickle')
