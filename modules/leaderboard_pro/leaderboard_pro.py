import json
from modules.quiz_pro.quiz_pro import quiz_pro
class leaderboard_pro():
    

    # Constants
    FILE_PATH    = ".\mydb\leaderboard.json"

    # Static Variables
    db_instance = None

    def __init__(self):
        if(leaderboard_pro.db_instance == None): 
            with open(leaderboard_pro.FILE_PATH, 'r') as fp:
                self.db = json.loads(fp.read())
             
            leaderboard_pro.db_instance = self
        else:                                        
            raise Exception("More than one instance is tried to be created for a Singleton class")


    def flush_data(self):
        with open(leaderboard_pro.FILE_PATH, 'w') as fp:
            
            json_object = json.dumps(self.db, indent = 4)
            fp.write(json_object)


    def store_data(self,user,quiz_name,get,total):
        if(user not in self.db):
            self.db[user]=[]
        
        
        quiz={}
        if(quiz_name not in quiz):
            quiz[quiz_name]={}
        quiz[quiz_name]["got"]=get
        quiz[quiz_name]["total"]=total

        self.db[user].append(quiz)

        
        
        self.flush_data()

    
    def update_mark(self,name,quiz_name):#,,
        pre=(self.db[name][0][quiz_name]["got"])

        

        return pre




    def get_leaderboard(self,quiz_name):
        
        a=[]
      
        for x,v in self.db.items():
            temp={}
            for i in v:
     
                if( quiz_name in i):
                    
                    
                    temp["name"]=x
                    temp["got"]=i[quiz_name]["got"]
                    temp["total"]=i[quiz_name]["total"]
                
                    a.append(temp)
            
       
        return a
    
                
                



