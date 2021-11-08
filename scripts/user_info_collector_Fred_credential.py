
from library import *

user_pd=pd.read_pickle('new_user_to_download.pickle')

startTime = time.time()

for i, row in tqdm(enumerate(user_pd[50000:].iterrows())):
    url=row[1]['actor_url']
    filename='user_profiles_new/'+str(row[1]['actor_id'])+'.txt'
    
    cmd='curl -u 12fa1eb28865f5821ad4:e69364d9c5e7ef1aa989c15bfc90da5294b46e5d ' + url + ' > ' + filename 
    print (cmd)
    os.system(cmd)
    elapsedTime=time.time()-startTime
    if i>0 and i%5000==0 and elapsedTime < 3600:
        time.sleep(3600-elapsedTime)
        startTime = time.time()
        
