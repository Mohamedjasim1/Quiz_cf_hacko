import json

class quiz_pro():
    """
    NOTE: This is a Singleton class
    """

    # Constants
    FILE_PATH    = ".\mydb\quiz_detail.json"

    # Static Variables
    db_instance = None

    def __init__(self):
        if(quiz_pro.db_instance == None):  # No instance created so far
            with open(quiz_pro.FILE_PATH, 'r') as fp:
                self.db = json.loads(fp.read())
                #self.db["total_quiz"]=0
            quiz_pro.db_instance = self
        else:                                         # Already an instance has been created
            raise Exception("More than one instance is tried to be created for a Singleton class")


    def flush_data(self):
        with open(quiz_pro.FILE_PATH, 'w') as fp:
            
            json_object = json.dumps(self.db, indent = 4)
            fp.write(json_object)


    def get_quiz_detail(self,quiz_name,creator,quiz,options,co,count):
        
        if(count not in self.db):
            self.db[count]={}
            #self.db["total_quiz"]+=1

        
            
        
        
        self.db[count]["creator"]=creator
        self.db[count]["name"]=quiz_name
        if("quizzes" not in self.db[count]):
             self.db[count]["quizzes"]=[]

        qtns={}
        qtns["quiz"]=quiz
        qtns["options"]=options
        qtns["correct"]=co

        self.db[count]["quizzes"].append(qtns)
        # self.db[quiz_name]["quiz"][count]={}
        # self.db[quiz_name]["quiz"][count]["qtn"]=quiz
        # self.db[quiz_name]["quiz"][count]["options"]=options
        # self.db[quiz_name]["quiz"][count]["correct"]=co
        
        self.flush_data()


    def all_quiz_data(self):
        return self.db

    def quiz_data(self,creator):
        return self.db[creator]
    
    def creator_quiz(self,creator):
        return(self.db[creator]["quizzes"])
    
    def quiz_count(self):
        return self.db["total_quiz"]
    
    def quiz_name_by_id(self,id):
        return self.db[id]["name"]
    
    def current_quiz(self,name):
        a=[]
        store=list(self.db.values())
        for x in store:
            a.append(x["name"])
        
        if(name not in a):
            try:
                x=list(self.db.keys())[-1]
                s=int(x)+1
                return str(s)
            except:
                return "1"
        else:
            return list(self.db.keys())[-1]


    
    def correct_options(self,quiz_id):
        a=[]
        for k in self.db[quiz_id]["quizzes"]:
            a.append(k["correct"])
        return a



        
    
