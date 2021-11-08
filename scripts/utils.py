from library import *

def parallel_process (files, process):
    
    pbar = tqdm(total=len([1 for _ in files]))
    def update(*a): pbar.update()
    with Pool(processes=multiprocessing.cpu_count()) as p:
        data_ = []

        for f in files:
            data_.append(p.apply_async(process, [f], callback=update))


        p.close()
        p.join() # Wait for all child processes 
        data=[]
        ct=0
        for r in data_:
            try:
                data.append(r.get())
            except:
                ct+=1
       # data = [r.get() for r in data_]
    
    
    return data