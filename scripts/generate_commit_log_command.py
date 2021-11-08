import glob
from tqdm import tqdm

repo_path=glob.glob('repos/*/')
f=open ('commit_info.bash', 'w')
for path in tqdm(repo_path):
    
    #filename='../commit_info/'+path.split('/')[1]+'.txt'
    filename='../commit_info/'+path.split('/')[1].split('-')[-1]+'.txt'
    
    cmd= 'cd '+ path + '; git log --pretty=format:"%h \t  %an \t  %ad \t  %cn \t  %cd \t  %s" >'+ filename +'; cd ..; cd ..'
    f.write(cmd)
    f.write('\n')
f.close()
