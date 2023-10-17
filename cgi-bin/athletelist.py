import os, sys

class AthleteList(list):
    def __init__(self, name= '', dob= '', times= []):
        '''Initialize the object here'''
        super().__init__(times)
        self.name = name
        self.dob = dob
        
    def sanitize (self):
        '''Takes a string and returns the string with all accurances of either " : " or " - " subbed with " . " '''
        sanitizeTimes = []
        for item in self:
            if '-' in item:
                sanitizeTimes.append(item.replace('-', '.'))
            elif ':' in item:
                sanitizeTimes.append(item.replace(':', '.'))
            else:
                sanitizeTimes.append(item)                
        return sanitizeTimes
    
    def top(self, top=3):
        '''Compute and returns list of an athlete's x best time records. it defaults to top 3 '''
        return sorted(list(set(self.sanitize())))[0: top]
    
    def addtime(self, value):
        '''Appends a single time value to the end of the times list'''
        try:
            if len(value) > 0 and float(self.cleanup(value)):
                self.append(value)
        except ValueError:
            pass
    def addtimes(self, valuelist):
        '''Appends a list if time values to the end of the times list'''
        for value in valuelist:
            self.addtime(value)       

    def cleanup(self, strvalue):
        if '-' in strvalue:
            return strvalue.replace('-', '.')
        elif ':' in strvalue:
            return strvalue.replace(':', '.')  
        else:
            return strvalue
    @property    
    def getCleanedupData(self): 
        return sorted(list(set(self.sanitize())))
    
def readData(file):
    '''Reads the data from the provided file path and returns a list of strings'''
    MAIN_PATH = os.getcwd()
    try:
        with open(MAIN_PATH + file, mode='r+', encoding='utf8') as file:
            return file.readline().strip().split(',')
    except (Exception, IOError, NotADirectoryError) as e:
        print(e)
        if e is IOError:            
            return []
        else:
            sys.exit()

def displayRecords (athletelist = ['james2', 'julie2', 'sarah2', 'mikey2'], bestcount = 5):
    '''Initiate, process and display raw and process data for each athlete in the list'''
    for athl in athletelist:
        athlData = readData(athl)
        athlRecord = AthleteList(athlData.pop(0), athlData.pop(0), athlData)
        print('\n\n' + athlRecord.name + ' with dob ' + athlRecord.dob + ' got a best {} time of '.format(bestcount), 
              athlRecord.top(bestcount), '\n\nFrom initial set ', athlRecord, '\n\n')
        athlRecord.addtime('1:50')
        athlRecord.addtimes(['1:89', '1*22', '', '1-21', '1.10'])
        print('\n\n ***********After addint time here are the results again*********** \n\n')
        print('\n\n' + athlRecord.name + ' with dob ' + athlRecord.dob + ' got a best {} time of '.format(bestcount), 
              athlRecord.top(bestcount), '\n\nFrom initial set ', athlRecord, '\n\n')
#displayRecords()

