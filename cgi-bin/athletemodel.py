import pickle
from athletelist import AthleteList, readData
import sqlite3, pprint

databaseName = 'coachdata.sqlite' 
def get_coach_data(file):   
    print('line 5 of athlete model', file) 
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


def get_names_from_db_store():
    cxn = sqlite3.Connection('coachdata.sqlite')
    cursor = cxn.cursor()
    names = cursor.execute("""SELECT id, name FROM athletes""").fetchall()
    names = [{"id": row[0], "name": row[1]} for row in names]
    cxn.close()
    return names

print(get_names_from_db_store())

def get_athlete_from_db_by_id(athlete_id):
    cxn = sqlite3.Connection('coachdata.sqlite')
    cursor = cxn.cursor()
    (name, dob) = cursor.execute("SELECT name, dob FROM athletes WHERE id=?", (athlete_id,)).fetchone()
    cxn.commit()
    results = cursor.execute("SELECT value FROM timing_data WHERE athlete_id=?", (athlete_id,)).fetchall()
    results = [row[0] for row in results]
    cxn.commit()
    cxn.close()
    response = {
        "name": name, "dob": dob, "data": results, "top3": results[0:3]
    }
    return (response)

