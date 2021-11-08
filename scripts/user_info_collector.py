
from library import *

user_pd=pd.read_pickle('new_user_to_download.pickle')

startTime = time.time()

for i, row in tqdm(enumerate(user_pd[:50000].iterrows())):
    url=row[1]['actor_url']
    filename='user_profiles_new/'+str(row[1]['actor_id'])+'.txt'
    
    #!curl -u 42261d9a908c778989b3:bcb278145fba3ea9fe7b1d2bfe76ca9960d9c798 $url  > "$filename"
    cmd='curl -u 42261d9a908c778989b3:bcb278145fba3ea9fe7b1d2bfe76ca9960d9c798 ' + url + ' > ' + filename 
    print (cmd)
    os.system(cmd)
    elapsedTime=time.time()-startTime
    if i>0 and i%5000==0 and elapsedTime < 3600:
        time.sleep(3600-elapsedTime)
        startTime = time.time()
        
