from django.shortcuts import render, redirect
from django.views import View
from .models import Question, Mark
from django.conf import settings
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from modules.quiz_pro.quiz_pro import quiz_pro
from modules.leaderboard_pro.leaderboard_pro import leaderboard_pro
quiz_p=quiz_pro()
LBoard=leaderboard_pro()
# Create your views here.
# @method_decorator(login_required, name="dispatch")


class Quiz_module(View):
    def get(self,request):
        
        context=quiz_p.all_quiz_data()
        return render(request,"quiz/quiz_module.html",{"context":context})

class Quiz(View):
    def get(self, request,quiz_id):
      
        questions =quiz_p.creator_quiz(str(quiz_id))
        seconds=quiz_p.get_seconds(str(quiz_id))
      
        return render(
            request,
            "quiz/quiz.html",
            {"questions": questions,"quiz_id":str(quiz_id),"seconds":seconds}
        )

    def post(self, request,quiz_id):
        # mark = Mark(user=request.user, total=Question.objects.filter(verified=True).count())
        mark=0
        b=quiz_p.correct_options(str(quiz_id))
        data=quiz_p.quiz_data(str(quiz_id))
       
        name=str(request.user)
        quiz_name=data["name"]
        
        for i,v in enumerate(b):
           
            #print(request.POST.get(f"q{i+1}o", ""),v)
            if(request.POST.get(f"q{i+1}o", "")==v):
                mark+=1
        
        total=len(b)
        try:
            LBoard.update_mark(name,quiz_name,mark)
        except:
            pass
        LBoard.store_data(name,quiz_name,mark,total)
            
        
        
        
        
        
        
        # for i in range(1,3):
        #     q = Question.objects.filter(pk=request.POST.get(f"q{i}", 0), verified=True).first()
        #     if request.POST.get(f"q{i}o", "") == q.correct_option:
        #         # mark.got += 1
        #         mark+=1
        # mark.save()
        # messages.success(request, "Marks updated")
        return render(request,"quiz/result.html",{"content":mark,"quiz_id":str(quiz_id)})

# @method_decorator(login_required, name="dispatch")
    

# class Quiz_detail(View):


#     def get(self, request):
#         return render(
#             request, 
#             "quiz/quiz_detail.html",
          
#         ) 

#     def post(self, request):

#         data = request.POST
#         name=data.get("quiz_name")
#         seconds=data.get("seconds")
#         x=data.get("quiz_no")
        
#         return redirect("add_question",)
        

class AddQuestion(View):
    db={"qtns":{}}
    def get(self, request):
        return render(
            request, 
            "quiz/add_questions.html",{"questions":range(1,2)}
        )
    
    def post(self, request):

    

        already_exists=0
        
        for i in range(1, 2):
            data = request.POST
            q = data.get(f"q{i}", "")
            o1 = data.get(f"q{i}o1", "")
            o2 = data.get(f"q{i}o2", "")
            o3 = data.get(f"q{i}o3", "")
            o4 = data.get(f"q{i}o4", "")
            co = data.get(f"q{i}c", "")
            quiz_name=data.get("quiz_name")
            seconds=data.get("seconds")
            # self.db["creator"]=request.user
            # self.db["qtns"][q]=list([o1,o2,o3,o4])
            quiz_p.get_quiz_detail(quiz_name,str(request.user),q,list([o1,o2,o3,o4]),co,quiz_p.current_quiz(quiz_name),seconds)


            

            
            if Question.objects.filter(question=q).first():
                already_exists += 1
                continue



            question = Question(
                question=q,
                option1=o1,
                option2=o2,
                option3=o3,
                option4=o4,
                correct_option=co,
                quiz_name=quiz_name,
                creator=request.user
            )
            question.save()
           
        
        return redirect("add_question")

# @method_decorator(login_required, name="dispatch")
class Result(View):
    def get(self, request):
        results = Mark.objects.filter(user=request.user)
        return render(request, "quiz/result.html", {"results": results})

class Leaderboard(View):
    def get(self, request,quiz_id):
        q_name=quiz_p.quiz_name_by_id(str(quiz_id))
        result=(LBoard.get_leaderboard(q_name))
        return render(
            request, 
            "quiz/leaderboard.html", 
            {"results":result})
    
class Leaderboards(View):
    def get(self,request):
        leaderboard=quiz_p.get_quiznames()

        return render(
            request, 
            "quiz/leaderboards.html", 
            {"leaderboard":leaderboard})

