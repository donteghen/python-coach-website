import pickle
from athletelist import AthleteList, readData

def get_coach_data(file):    
    file_raw_data = readData(file)
    athlete = AthleteList(file_raw_data.pop(0), file_raw_data.pop(0), file_raw_data)
    return athlete


def put_to_store(files_list): 
    all_athletes = {}
    for file_item in files_list:
       file_processed_data = get_coach_data(file_item)
       all_athletes[file_processed_data.name] = file_processed_data
    try:
        with open('data/athletes.pickle', mode='wb') as f:
            pickle.dump(all_athletes, f)
    except IOError as e:
        print('File error (put_and_store): ' + str(e))            
     
    return (all_athletes)

 

def get_from_store(): 
    all_athletes = {}
    try:
        with open('data/athletes.pickle', 'rb') as athf:
            all_athletes = pickle.load(athf) 
    except IOError as ioerr:
        print('File error (get_from_store): ' + str(ioerr))
    return(all_athletes)