import sqlite3, glob, os, athletemodel, sys, pprint

connection = sqlite3.Connection('coachdata.sqlite')
cursor = connection.cursor()

allFiles = os.listdir(os.getcwd() + '/data')
athFiles = ['/data/'+item for item in allFiles if item.endswith('.txt')]

all_athletes = athletemodel.put_to_store(athFiles)
pprint.pprint(all_athletes)


for athlete in all_athletes:
    name = all_athletes[athlete].name
    dob = all_athletes[athlete].dob
    cursor.execute("INSERT INTO athletes (name, dob) VALUES (?, ?)", (name, dob))
    connection.commit()
    curr_athlete_id, = cursor.execute("SELECT id FROM athletes WHERE name=? AND dob=?", (name, dob)).fetchone()
    print('curr_athlete_id from fetchone -> ', curr_athlete_id)
    timeValues = all_athletes[athlete].getCleanedupData
    for timeValue in timeValues:        
        cursor.execute("INSERT INTO timing_data (athlete_id, value) VALUES (?, ?)", (curr_athlete_id, timeValue))
        print('inserting this:', curr_athlete_id, timeValue)
        connection.commit()
connection.close()
    