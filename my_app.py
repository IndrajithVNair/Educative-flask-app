from asyncio.windows_events import NULL
from atexit import register
from werkzeug.utils import secure_filename
from distutils.log import debug
from flask import Flask, render_template,request,redirect,session,Response,url_for,flash,send_file
from flask_mysqldb import MySQL
import docx
import qbgen as qb
import os
from plagarismCheck import *
from copyCat import *
from datetime import date
import time
import threading
from flask import current_app
import cv2
import face_recognition as fr
from playsound import playsound
today = date.today()
app = Flask(__name__)
app.jinja_env.globals.update(VideoCapture=cv2.VideoCapture(0))
@app.context_processor#importing packages to be used in jinja template

def add_imports():
    return dict(time=time)
global examdata
global user_id
examdata ={}
examrunning = False
# Enter your database connection details below
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'educative'
app.config["UPLOAD_FOLDER"] = "static" #folder to upload

# Intialize MySQL
mysql = MySQL(app)

           

@app.route('/takephoto')
def takephoto():
    camera = cv2.VideoCapture(0)
    return_value, image = camera.read()#capturimg photo from webcam using opencv
    del(camera)
    filepath=r'C:\Users\acer\Downloads\flask\my_app\static\images'#path where image has to be stored
    currentdir=os.getcwd()
    os.chdir(filepath)
    filename=session['register_num']+".JPG"
    imgpath=os.path.join("studentimages/",filename)
    cv2.imwrite(filename, image)
    os.chdir(currentdir)
   
    
   
    storedphoto=session['register_num']+".jpg"#storedphoto at the time of user registration
    #filepath=r'C:\Users\DA\AppData\Local\Programs\Python\Python39\examguru\static\images'#path where captured image is stored
    #currentdir=os.getcwd()
    #os.chdir(filepath)
    filename=session['register_num']+".JPG"
    #storedfilename="stored"+session['sid']+".JPG"
    imgpath=os.path.join(r"C:\Users\acer\Downloads\flask\my_app\static\studentimages",filename)
    os.chdir(currentdir)
    capturedphotopath=os.path.join(r"C:\Users\acer\Downloads\flask\my_app\static\images",storedphoto)
    capturedphoto=fr.load_image_file(capturedphotopath) 
    storedphotopath=os.path.join(r"C:\Users\acer\Downloads\flask\my_app\static\studentimages",storedphoto)
    storedphoto=fr.load_image_file(storedphotopath)                            
    encoding1=fr.face_encodings(storedphoto)[0]
    encoding2=fr.face_encodings(capturedphoto)[0]
    res=fr.compare_faces([encoding1],encoding2)
    if(res[0]==True):
        print("Face data matches")
    else:
        print("Face data mismatch")
   
@app.route('/examguru/shome')
def shome():
    try:
        cur=mysql.connection.cursor()
        cur.execute("SELECT SPHOTO FROM STUDENT WHERE SID='"+session['sid']+"'")
        mysql.connection.commit
        photolist=cur.fetchall()
        storedphoto=photolist[0]#storedphoto
        filepath=r'C:\Users\DA\AppData\Local\Programs\Python\Python39\examguru\static\studentimages'#path where captured image is stored
        currentdir=os.getcwd()
        os.chdir(filepath)
        filename=session['sid']+".JPG"
        #storedfilename="stored"+session['sid']+".JPG"
        storedfilename=photolist[0][0]
        imgpath=os.path.join(r"C:\Users\DA\AppData\Local\Programs\Python\Python39\examguru\static\studentimages",filename)
        os.chdir(currentdir)
        capturedphoto=fr.load_image_file(os.path.join(r"C:\Users\DA\AppData\Local\Programs\Python\Python39\examguru\static\studentimages",filename))#capturedphoto
        storedphotopath=os.path.join(r"C:\Users\DA\AppData\Local\Programs\Python\Python39\examguru\static\images",storedfilename)
        storedphoto=fr.load_image_file(storedphotopath)                            
        encoding1=fr.face_encodings(storedphoto)[0]
        encoding2=fr.face_encodings(capturedphoto)[0]
        res=fr.compare_faces([encoding1],encoding2)
        if(res[0]==True):
            cur=mysql.connection.cursor()
            cur.execute("SELECT * FROM COURSE")
            mysql.connection.commit
            courses=cur.fetchall()
            cur.execute("SELECT SNAME FROM STUDENT WHERE SID='"+session['sid']+"'")
            res2=cur.fetchall()
            sname=res2[0][0]
            return(render_template('sindex.html',courses=courses,sname=sname))
        else:
            return(render_template('messtemplate.html',u1='login',mess='Unable to find a match'))
    except:
        return(render_template('messtemplate.html',u1='takephoto',mess='Unable to find a match'))


@app.route('/auth-forgot-password-basic.html')
def auth_forgot_password_basic():
    return render_template('auth-forgot-password-basic.html')

@app.route('/auth-login-basic.html')
def auth_login_basic():
    return render_template('auth-login-basic.html')

@app.route('/auth-register-basic.html')
def auth_register_basic():
    return render_template('auth-register-basic.html')

@app.route('/cards-basic.html')
def cards_basic():
    return render_template('cards-basic.html')

@app.route('/extended-ui-perfect-scrollbar.html')
def extended_ui_perfect_scrollbar():
    return render_template('extended-ui-perfect-scrollbar.html')

@app.route('/extended-ui-text-divider.html')
def extended_ui_text_divider():
    return render_template('extended-ui-text-divider.html')

@app.route('/form-layouts-horizontal.html')
def form_layouts_horizonta():
    return render_template('form-layouts-horizontal.html')

@app.route('/form-layouts-vertical.html')
def form_layouts_vertica():
    return render_template('form-layouts-vertical.html')

@app.route('/forms-basic-inputs.html')
def forms_basic_inputs():
    if session['user']=='teacher':
        global examdata
        examdata.clear()

        examdata['CourseCode']=request.args.get('CourseCode')
        examdata['CourseName']=request.args.get('CourseName')
        examdata['Department']=request.args.get('Dept')
        examdata['Academicyear']=request.args.get('Academicyear')
        print("exam data: ",examdata)
        return render_template('forms-basic-inputs.html')
    else:
        return render_template('forms-basic-inputs.html')

@app.route('/forms-input-groups.html')
def forms_input_groups():
    return render_template('forms-input-groups.html')

@app.route('/icons-boxicons.html')
def icons_boxicons():
    return render_template('icons-boxicons.html')

@app.route('/index.html',methods=['GET', 'POST'])
def check_user():
    session.pop('login',None)  
    username=request.form['email-username']
    password=request.form['password']
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    mysql.connection.commit()
    res=cur.fetchall()
    global Flag
    Flag= False
    global user_type
    user_type = 0
    account_status=2
    for row in res:
        if (username==row[1] and password==row[4] and account_status==row[9]):
            user_type=row[8]
            Flag= True
            session['login']=True
            session['user_id']=row[0]
            session['register_num']=row[14]
            user_id=row[0]
            session['username']=row[1]
            break

            # using the flag= True check for the user role
        
    if(Flag):
            if(user_type==0):
                #render admin dashboard
                # set user session as admin session
                session['user']='admin'
                return redirect('/admin-dashboard')
            elif(user_type==1):
                session['user']='teacher'
                return redirect('/teacher-dashboard')
            elif(user_type==2):
                session['user']='student'
                return redirect('/student-dashboard')
    else:
            # when the username or password is not found or when the account is not operational, then
            #redirect to the login page and display the error message
            session['login']=False
            return redirect('/')

    

            

@app.route('/admin-dashboard')
def admin_dashboard():
    return render_template('index_admin.html')

@app.route('/teacher-dashboard')
def teacher_dashboard():
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM courses WHERE Faculty_ID=%s",(session['register_num'],))
    res=cur.fetchall()
    return render_template('index_teacher.html',course_details=res)

@app.route('/schedule-exam',methods=['GET', 'POST'])
def exam_schedule():
    SubjectName=request.form['SubjectName']
    ExamName=request.form['ExamName']
    department=request.form['Department']
    Academicyear=request.form['Academicyear']
    QuestionPaper=request.form['QuestionPaper']
    Date=request.form['Date']
    StartAt=request.form['StartAt']
    EndAt=request.form['EndAt']
    Duration=request.form['Duration']
    mysql.connection.commit()
    faculty=session.get('username')
    number_of_questions=request.form['questions']
    number_of_questions=int(number_of_questions)
    print(faculty)
    global examdata

    examdata['Subject']=SubjectName
    examdata['Exam']=ExamName
    examdata['Department']=department
    examdata['Academicyear']=Academicyear
    examdata['Date']=Date
    examdata['StartAt']=StartAt
    examdata['faculty']=faculty

    cur=mysql.connection.cursor()
    cur.execute("INSERT INTO exams(NAME,SUB,Dept,Academicyear,Date,STARTS_AT,ENDS_AT,Duration,ScheduledBy) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s) ",(ExamName,SubjectName,department,Academicyear,Date,StartAt,EndAt,Duration,faculty))
    mysql.connection.commit()
    return render_template('/set-questions.html',res=True,questions=number_of_questions)


@app.route('/schedule-exam-as-teacher',methods=['GET', 'POST'])
def teacher_exam_schedule():
    #SubjectName=request.form['SubjectName']
    ExamName=request.form['ExamName']
    #department=request.form['Department']
    #Academicyear=request.form['Academicyear']
    QuestionPaper=request.form['QuestionPaper']
    Date=request.form['Date']
    StartAt=request.form['StartAt']
    EndAt=request.form['EndAt']
    Duration=request.form['Duration']
    mysql.connection.commit()
    faculty=session.get('username')
    number_of_questions=request.form['questions']
    number_of_questions=int(number_of_questions)
    print(faculty)
    global examdata

   
    SubjectName= examdata['CourseName']
    department= examdata['Department']
    Academicyear= examdata['Academicyear']



    examdata['Subject']=SubjectName
    examdata['Exam']=ExamName
    examdata['Department']=department
    examdata['Academicyear']=Academicyear
    examdata['Date']=Date
    examdata['StartAt']=StartAt
    examdata['faculty']=faculty

    cur=mysql.connection.cursor()
    cur.execute("INSERT INTO exams(NAME,SUB,Dept,Academicyear,Date,STARTS_AT,ENDS_AT,Duration,ScheduledBy) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s) ",(ExamName,SubjectName,department,Academicyear,Date,StartAt,EndAt,Duration,faculty))
    mysql.connection.commit()
    return render_template('/set-questions.html',res=True,questions=number_of_questions)
    
@app.route('/edit-exam')
def editexam():
     EID=request.args.get('EID')
     cur=mysql.connection.cursor()
     cur.execute("SELECT * FROM exams WHERE EID=%s",(EID,))
     res=cur.fetchall()
     session['EID']=EID
     return render_template('/edit-exam.html',EID=EID,exam_data=res)

@app.route('/edit-exam-data',methods=['GET', 'POST'])
def editexamdata():
    EID=session['EID']
    SubjectName=request.form['SubjectName']
    ExamName=request.form['ExamName']
    department=request.form['Department']
    Academicyear=request.form['Academicyear']
    QuestionPaper=request.form['QuestionPaper']
    Date=request.form['Date']
    StartAt=request.form['StartAt']
    EndAt=request.form['EndAt']
    Duration=request.form['Duration']
    mysql.connection.commit()
    faculty=session.get('username')
    number_of_questions=request.form['questions']
    number_of_questions=int(number_of_questions)

    cur=mysql.connection.cursor()
    cur.execute("update exams SET NAME=%s,SUB=%s,Dept=%s,Academicyear=%s,Date=%s, STARTS_AT=%s, ENDS_AT=%s,Duration=%s,ScheduledBy=%s ,Status=0 WHERE EID=%s",(ExamName,SubjectName,department,Academicyear,Date,StartAt,EndAt,Duration,faculty,EID))
    #print("update exam SET NAME={},SUB={},Dept={},Academicyear={}".format(ExamName,SubjectName,department,Academicyear,Date,StartAt,EndAt,Duration,faculty))
    
    mysql.connection.commit()

    cur.execute("SELECT * from exam_data WHERE EID=%s",(EID,))
    res=cur.fetchall()
    return render_template('edit-questions.html',res=True,questions=number_of_questions,question_data=res)


@app.route('/update-exam-questions',methods=['GET', 'POST'])
def update_exam_questions():
    number_of_questions = request.form['numberofquestions']
    number_of_questions = int(number_of_questions)
    questions = []
   
    for i in range(1,number_of_questions+1):
        num=str(i)
        questions.append(request.form['question'+num])
    # delete the rows of EID in the exam_data 
    EID=session['EID']
    cur=mysql.connection.cursor()
    cur.execute('delete from exam_data where EID=%s',(EID,))

    question_number=1
    for i in questions:
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO exam_data (EID,Question_Number,Question_Text) VALUES (%s,%s,%s)",(EID,question_number,i))
        mysql.connection.commit()
        question_number+=1
        session['ExamAdded']=True
    return redirect('/manage-exams.html')




@app.route('/set-exam-questions',methods=['GET', 'POST'])
def setquestions():
    number_of_questions = request.form['numberofquestions']
    number_of_questions = int(number_of_questions)
    questions = []
   
    for i in range(1,number_of_questions+1):
        num=str(i)
        questions.append(request.form['question'+num])
   
   # find the exam id of the question for which the question text is being encountered
    SubjectName=examdata['Subject']
    ExamName=examdata['Exam']
    department=examdata['Department']
    Academicyear=examdata['Academicyear']
    Date=examdata['Date']
    StartAt=examdata['StartAt']
    faculty=examdata['faculty']

    cur=mysql.connection.cursor()
    #print("SELECT EID FROM exams WHERE NAME={} AND SUB={} AND Dept={} AND Academicyear={} AND Date={} AND STARTS_AT={} AND ScheduledBy={}".format(ExamName,SubjectName,department,Academicyear,Date,StartAt,faculty))
    cur.execute("SELECT EID FROM exams WHERE NAME=%s AND SUB=%s AND Dept=%s AND Academicyear=%s AND Date=%s AND STARTS_AT=%s AND ScheduledBy=%s",(ExamName,SubjectName,department,Academicyear,Date,StartAt,faculty))
    res=cur.fetchall()
    mysql.connection.commit()
    EID=res[0][0]
    

    # insert the questions into exam_data table
    question_number=1
    for i in questions:
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO exam_data (EID,Question_Number,Question_Text) VALUES (%s,%s,%s)",(EID,question_number,i))
        mysql.connection.commit()
        question_number+=1
        session['ExamAdded']=True
        if session['user']=='teacher':
            return redirect('/teacher-dashboard')
        else:
            return redirect('/manage-exams.html')

    
@app.route('/list-exams')
def evaluate_answers():
    cur=mysql.connection.cursor()
    username= session['username']
    cur.execute("SELECT * FROM exams WHERE ScheduledBy=%s",(username,))
    res=cur.fetchall()
    return render_template('list-exams.html',examlist=res)



@app.route('/see-attended')
def see_attended():
    EID=request.args.get('EID')
    cur= mysql.connection.cursor()
    cur.execute("SELECT * FROM attended_list WHERE EID=%s",(EID,))
    attended=cur.fetchall()
    attended_count=len(attended)
    register_num=[]
    names=[]
    marks={}
    print("EID: ",EID)
    for i in range(len(attended)):
        # fetching the register number of the students who attended the exam
        user_id=attended[i][2]
        print(user_id)
        cur.execute("SELECT RegisterNum FROM users WHERE Id=%s",(user_id,))
        register_num.append(cur.fetchall())
       

        #fetching the name of the students who attended the exam
        cur.execute("SELECT Name FROM users WHERE Id=%s",(user_id,))
        names.append(cur.fetchall())

    # if mark is recorded for the student for the exam id, display it
    mark=0
    for i in range(len(register_num)):
        RollNumber=register_num[i][0][0]
        
       
        
        cur=mysql.connection.cursor()
        cur.execute("SELECT Marks FROM exam_marks WHERE EID=%s AND RollNumber=%s",(EID,RollNumber))
        res=cur.fetchall()
        Totalmarks=0
        for i in res:
            print("Marks data: ",i[0])
            Totalmarks+=i[0]
            if not RollNumber in marks:
                marks[RollNumber]=i[0]
            elif RollNumber in marks:
                score=marks[RollNumber]
                score= int(score)
                score+=i[0]
                marks[RollNumber]=score

        mysql.connection.commit()

      
        
        

    print("marks: ",marks)






    session['EID']=EID
    register_num=tuple(register_num)
    names=tuple(names)

    return render_template('see-attended.html',attended_count=attended_count,register_num=register_num,name=names,marks=marks)


@app.route('/view-uploaded-answers',methods=['POST', 'GET'])
def view_uploaded_answers():
    cur=mysql.connection.cursor()
    RollNumber= request.args.get('RegisterNum')
    Name= request.args.get('Name')
    EID= session['EID']

    #fetch the answers
    cur.execute("SELECT * FROM exam_answers WHERE EID=%s AND RollNumber=%s",(EID,RollNumber,))
    res=cur.fetchall()
    answers=res
    #print("answers: ",answers)

    #fetch the questions
    cur.execute("SELECT Question_Text FROM exam_data WHERE EID=%s",(EID,))
    res=cur.fetchall()
    qlist=res
    questions=len(res)
    #print("questions: ",questions)
    return render_template('view-uploaded-asnwers.html',answer=answers,Name=Name,questions=questions,qlist=qlist,RollNumber=RollNumber)



@app.route('/manage-exams.html')
def manage_exams():
    if session['user']=='teacher':
        cur=mysql.connection.cursor()
        username=session['username']
        cur.execute("SELECT * FROM exams where Status=0 AND ScheduledBy=%s",(username,))
        res=cur.fetchall()
        mysql.connection.commit()
        return render_template('manage-exams.html',elist=res,ExamAdded=False)
    else:

        # this should be executed only if the user is admin
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM exams where Status=0")
        res=cur.fetchall()
        mysql.connection.commit()
    
        return render_template('manage-exams.html',elist=res,ExamAdded=False)
@app.route('/attend-exams')
def attend_exams():
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM exams where Status=0")
    res=cur.fetchall()
    mysql.connection.commit()
    #print(res[0][5])
    # display only those exams which are set to be attended today
    d1 = today.strftime("%Y-%m-%d")
    elist=()
    for i in range(len(res)):
        date=res[i][5]
        date=str(date)
        if(date==d1):
            temp=(res[i],)
            elist=elist+temp
       
    #print(elist)
    return render_template('attend-exams.html',elist=elist)



@app.route('/attendexam')
def attendexam():
    EID= request.args.get('EID')
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM exams where EID=%s and Status=0",(EID,))
    res=cur.fetchall()
    global attended
    #check whether the current date and time is within the scheduled time span for the exam 
    t= time.localtime()
    current_time = time.strftime("%H:%M", t)
    STARTS_AT=res[0][6]
    STARTS_AT =str(STARTS_AT)
    ENDS_AT=res[0][7]
    ENDS_AT =str(ENDS_AT)


    if(current_time> STARTS_AT and current_time<ENDS_AT ):
        # render template for attending the exams
        
        # check if the user has already attended the exam from the attended_list
        cur=mysql.connection.cursor()
        user_id=''
        user_id=session['user_id']
        cur.execute("SELECT * FROM attended_list where EID=%s and user_id=%s",(EID,user_id,))
        res=cur.fetchall()
        mysql.connection.commit()

        if len(res)==0:
            # this means that the user hasent attempted the exam yet 
            # record the attempt in the attended_list table
            
            cur.execute("INSERT INTO attended_list (EID,user_id,Attended) VALUES(%s,%s,%s)",(EID,user_id,1))
            mysql.connection.commit()
            # fetch the questions for the exam
            cur.execute("SELECT Question_Text FROM exam_data WHERE EID=%s",(EID,))
            question_data=cur.fetchall()
            res=cur.execute("SELECT Question_Number FROM exam_data WHERE EID=%s",(EID,))
            number_of_questions=res
            print("number of questions:",number_of_questions)
            global examrunning
            examrunning=True
            # fetch the exam name from the exams table
            cur.execute("SELECT SUB,NAME FROM exams WHERE EID=%s",(EID,))
            exam_details=cur.fetchall()

            # check the face data
            camera = cv2.VideoCapture(0)
            return_value, image = camera.read()#capturimg photo from webcam using opencv
            del(camera)
            filepath=r'C:\Users\acer\Downloads\flask\my_app\static\images'#path where image has to be stored
            currentdir=os.getcwd()
            os.chdir(filepath)
            filename=session['register_num']+".JPG"
            imgpath=os.path.join("studentimages/",filename)
            cv2.imwrite(filename, image)
            os.chdir(currentdir)
        
            
        
            try:
                storedphoto=session['register_num']+".jpg"#storedphoto at the time of user registration
                #filepath=r'C:\Users\DA\AppData\Local\Programs\Python\Python39\examguru\static\images'#path where captured image is stored
                #currentdir=os.getcwd()
                #os.chdir(filepath)
                filename=session['register_num']+".JPG"
                #storedfilename="stored"+session['sid']+".JPG"
                imgpath=os.path.join(r"C:\Users\acer\Downloads\flask\my_app\static\studentimages",filename)
                os.chdir(currentdir)
                capturedphotopath=os.path.join(r"C:\Users\acer\Downloads\flask\my_app\static\images",storedphoto)
                capturedphoto=fr.load_image_file(capturedphotopath) 
                storedphotopath=os.path.join(r"C:\Users\acer\Downloads\flask\my_app\static\studentimages",storedphoto)
                storedphoto=fr.load_image_file(storedphotopath)                            
                encoding1=fr.face_encodings(storedphoto)[0]
                encoding2=fr.face_encodings(capturedphoto)[0]
                res=fr.compare_faces([encoding1],encoding2)
            except:
                message="Face data mismatch, move to a well lit place and try again"
                return render_template('pages-misc-error.html',message=message)
                

            if(res[0]==True):
                return render_template('attend-exam-submit-answers.html',qlist=question_data,questions=number_of_questions,exam_name=exam_details,EID=EID)
            else:
                # this means that there is a face data mismatch
                message="Face data mismatch, move to a well lit place and try again"
                return render_template('pages-misc-error.html',message=message)
            
            
            
            return render_template('attend-exam-submit-answers.html',qlist=question_data,questions=number_of_questions,exam_name=exam_details,EID=EID)
        else:
            # this means that the user has already attempted the exam
            message="You have already attempted the exam"
            return render_template('pages-misc-error.html',message=message)
    else:
        # this means that the user has tried to attempt the exam after the allocated time
        message="The time allocated for the exam has elapsed"
        return render_template('pages-misc-error.html',message=message)
    



        # update the attended column in the exam table
        # after the time set the exam as unavailable
        # add the users name to the attended_list table
        


    return render_template('pages-misc-under-maintenance.html')
    
    

@app.route('/submit-exam-answers',methods=['GET', 'POST'])
def submit_answers():
    global examrunning
    examrunning=False
    number_of_questions = request.form['numberofquestions']
    Exam_ID= request.form['EID']
    user_id=session['user_id']
    cur=mysql.connection.cursor()
    cur.execute("SELECT RegisterNum FROM users WHERE Id=%s",(user_id,))
    RegisterNum= cur.fetchall()

    number_of_questions = int(number_of_questions)
    answers = []
   
    for i in range(1,number_of_questions+1):
        num=str(i)
        answers.append(request.form['answer'+num])

    # insert the questions into exam_data table
    question_number=1
    for i in answers:
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO exam_answers (EID,Question_Number,Answer_Text,RollNumber) VALUES (%s,%s,%s,%s)",(Exam_ID,question_number,i,RegisterNum[0][0]))
        mysql.connection.commit()
        question_number+=1
        session['ExamAttended']=True
    return redirect('/attend-exams')

@app.route('/submit-exam-marks',methods=['GET','POST'])
def submit_exam_marks():
    number_of_questions = request.form['numberofquestions']
    Exam_ID= request.form['EID']
    RollNumber= request.form['RollNumber']
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM attended_list WHERE EID=%s",(Exam_ID,))
    attended=cur.fetchall()
    attended_count=len(attended)

    RollNumber=RollNumber.strip()

    number_of_questions = int(number_of_questions)
    marks = []


    for i in range(1,number_of_questions+1):
        num=str(i)
        marks.append(request.form['mark'+num])


    # insert the answers into exam_marks table
    question_number=1
    for i in marks:
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO exam_marks (EID,RollNumber,QuestionNumber,Marks) VALUES (%s,%s,%s,%s)",(Exam_ID,RollNumber,question_number,i,))
        mysql.connection.commit()
        question_number+=1
        session['MarksAdded']=True
    
    return redirect('/list-exams')



@app.route('/delete-exams')
def deleteexam():
    EID=request.args.get('EID')
    cur=mysql.connection.cursor()
    cur.execute("DELETE FROM exams where EID={}".format(EID))
    mysql.connection.commit()
    session['exam_deleted']=True
    return redirect('/manage-exams.html')

_FILE2 = ""
@app.route('/create-question-paper.html', methods=['GET', 'POST'])
def createquestionpaper():
    qb.deleteStaticFiles()
    if request.method == 'POST':
        upload_questionbank = request.files['qb_file']
        if upload_questionbank.filename != '':
            filepath = os.path.join(app.config["UPLOAD_FOLDER"],upload_questionbank.filename)
            upload_questionbank.save(filepath)
            fpath = filepath.split("'\'")
            qb.acceptPath(fpath[0])
            return render_template("qbresult.html")
    return render_template('create-question-paper.html')

@app.route('/check-assignments')
def checkassignments():
    return render_template('check-assignments.html')

@app.route('/plagarism',methods=['GET', 'POST'])
def checkplgweb():
    if(request.method=='POST'):
        srcurl=request.form['url1']
        ansfile=request.files['src1']
        alltext=[]
        data=""
        doc=docx.Document(ansfile)
        for docpar in doc.paragraphs:
            alltext.append(docpar.text)
        data=''.join(alltext)
        copied=checkpg(data,srcurl)
        return(render_template('plagarismResult.html',c=copied))

@app.route('/check-copycat')
def check_copycat():
    return render_template('check-copycat.html')

@app.route('/checkcpycat',methods=['GET','POST'])
def updateres():
        if(request.method=='POST'):
            srcfile=request.files['src']
            ansfile=request.files['ans']
            per,matchlist=plgcheck(srcfile,ansfile)
            return(render_template('copycatResult.html',per=per,m=matchlist))


@app.route('/qbresult')
def download_qb_file():
    p = r'C:\Users\acer\Downloads\flask\my_app\static\demo.docx'
    return send_file(p,as_attachment=True)

@app.route('/student-dashboard')
def student_dashboard():
    user_id=session['user_id']
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM users where Id={}".format(str(user_id)))
    res=cur.fetchall()
    Dept= res[0][2]
    Dept= str(Dept)
    #cur.execute("SELECT Name FROM sub WHERE CLASS='{}' and C_CODE={}".format(Dept,str(res[0][13])))
    cur.execute("SELECT * FROM courses WHERE Department='{}' AND Academicyear={}".format(Dept,str(res[0][13])))
    course=cur.fetchall()
    return render_template('index_student.html',course=course)

@app.route('/')
def index():
    return render_template('auth-login-basic.html')

@app.route('/user-register',methods=['GET','POST'])
def user_register():
    sphoto=request.files['sphoto']
    register_num=request.form['RegisterNumber']
    path = "C:\\Users\\acer\\Downloads\\flask\\my_app\\static\\studentimages"
    filename = secure_filename(register_num+".JPG")
    sphoto.save(os.path.join(path, filename))

    name=request.form['Name']
    
    email=request.form['email']
    phone=request.form['phoneNumber']
    password=request.form['Password']
    department=request.form['Department']
    country=request.form['Country']
    zipcode=request.form['zipCode']
    state=request.form['state']
    address=request.form['address']
    age=request.form['Age']
    role=2
    account_status=1
    cls=1
    cur=mysql.connection.cursor()
    cur.execute("INSERT INTO users(Name,Dept,Age,Password,email,phone,Address,Role,account_status,State,Country,Zipcode,Class,RegisterNum) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(name,department,age,password,email,phone,address,role,account_status,state,country,zipcode,cls,register_num))
    mysql.connection.commit()
    session['User_Created']=True
    return redirect('/')

   
@app.route('/pages-add-courses.html',methods=['GET', 'POST'])
def add_courses():
    return render_template('add_courses.html')
    






@app.route('/layouts-blank.html')
def ayouts_blank():
    return render_template('layouts-blank.html')

@app.route('/layouts-container.html')
def ayouts_container():
    return render_template('layouts-container.html')

@app.route('/layouts-fluid.html')
def ayouts_fluid():
    return render_template('layouts-fluid.html')

@app.route('/layouts-without-menu.html')
def ayouts_without_menu():
    return render_template('layouts-without-menu.html')

@app.route('/layouts-without-navbar.html')
def ayouts_without_navbar():
    return render_template('layouts-without-navbar.html')

@app.route('/pages-account-settings-account.html')
def pages_account_settings_accoun():
    return render_template('pages-account-settings-account.html')


@app.route('/edit-account')
def editaccount():
    # fetching the id
    rid=request.args.get('rid')
    # fetching details of the account
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE Id=%s",(rid,))
    res=cur.fetchall()
    mysql.connection.commit()
    return render_template('pages-account-settings-edit.html',rlist=res)

@app.route('/update-account',methods=['GET', 'POST'])
def updateaccount():
    rid=request.args.get('rid')
    name=request.form['Name']
    register_num=request.form['RegisterNumber']
    email=request.form['email']
    phone=request.form['phoneNumber']
    password=request.form['Password']
    department=request.form['Department']
    country=request.form['Country']
    zipcode=request.form['zipCode']
    state=request.form['state']
    address=request.form['address']
    role=request.form['Role']
    account_status=2
    cls=1
    try:
        cur=mysql.connection.cursor()
        cur.execute("UPDATE users SET Name=%s,Dept=%s,Password=%s,email=%s,phone=%s,Address=%s,Role=%s,account_status=%s,State=%s,Country=%s,Zipcode=%s,Class=%s WHERE Id=%s",name,department,password,email,phone,address,role,account_status,state,country,zipcode,cls,register_num,rid)
        mysql.connection.commit()
        return redirect('/pages-account-settings-connections.html')
    except mysql.IntegrityError:
        return redirect('/pages-misc-error.html')
    finally:
        return redirect('/pages-account-settings-connections.html')



@app.route('/add-new-course',methods=['GET','POST'])
def add_new_course():
    #updation of the already existing courses are also performed with this function
    CourseName= request.form['CourseName']
    CourseCode = request.form['CourseCode']
    department=request.form.get('Department')
    Academicyear = request.form.get('Academicyear')
    facultyid = request.form['facultyid']
    facultyid='MCK'+facultyid

    print("Course details:",CourseName, CourseCode,department,Academicyear,facultyid)
    cur=mysql.connection.cursor()
    cur.execute("INSERT INTO courses(CourseCode,Name,Faculty_ID,Department,Academicyear) VALUES(%s,%s,%s,%s,%s)",(CourseCode,CourseName,facultyid,department,Academicyear))
    mysql.connection.commit()
    session['course_added']=True
    return redirect('/pages-add-courses.html')


@app.route('/pages-view-courses.html')
def view_courses():

    # two results should be fetched one for admin listing all the courses
    # and one for faculty to edit their own courses
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM courses")
    admin_res=cur.fetchall()
    mysql.connection.commit()
    return render_template('view-courses.html',admin_res=admin_res)
   
@app.route('/delete-course')
def deletecourse():
    course_code=request.args.get('course_code')
    cur=mysql.connection.cursor()
    cur.execute("DELETE FROM courses where CourseCode='{}'".format(course_code))
    mysql.connection.commit()
    session['course_deleted']=True
    return redirect('/pages-view-courses.html')

@app.route('/edit-course')
def editcourse():
    course_code=request.args.get('course_code')
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM courses WHERE CourseCode='{}'".format(course_code))
    res=cur.fetchall()
    mysql.connection.commit()
    session['editcourse']=True
    session['course_code']=course_code
    return render_template('edit-courses.html',course_code=res)

# function that handles the course edit operation
@app.route('/edit-course-data',methods=['GET','POST'])
def editcoursedata():
    CourseName= request.form['CourseName']
    CourseCode = request.form['CourseCode']
    department=request.form.get('Department')
    Academicyear = request.form.get('Academicyear')
    facultyid = request.form['facultyid']
    facultyid='MCK'+facultyid
  
    print("The edit course data function is being executed")

    cur=mysql.connection.cursor()
    cur.execute("update courses SET Name=%s,Faculty_ID=%s,Department=%s,Academicyear=%s WHERE CourseCode=%s",(CourseName,facultyid,department,Academicyear,CourseCode))
    #print("update courses SET CourseCode={},Name={},Faculty_ID={},Department={},Academicyear={} WHERE CourseCode={}".format(CourseCode,CourseName,facultyid,department,Academicyear,Course))
    mysql.connection.commit()
    session['course_editted']=True
    return redirect('/pages-view-courses.html')
    




@app.route('/admin-user-register',methods=['GET', 'POST'])
def admin_user_register():
    name=request.form['Name']
    register_num=request.form['RegisterNumber']
    email=request.form['email']
    phone=request.form['phoneNumber']
    password=request.form['password']
    department=request.form.get('Department')
    country=request.form.get('Country')
    zipcode=request.form['zipCode']
    state=request.form['state']
    address=request.form['address']
    if(session['user']=='admin'):
        role=request.form.get('Role')
    else:
        role='Student'
        
    role_code=0

    if(role=='Admin'):
        role_code=0
    elif(role=='Teacher'):
        role_code=1
    elif(role=='Student'):
        role_code=2


    account_status=2
    cls=1
    cur=mysql.connection.cursor()
    cur.execute("INSERT INTO users(Name,Dept,Password,email,phone,Address,Role,account_status,State,Country,Zipcode,Class,RegisterNum) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(name,department,password,email,phone,address,role_code,account_status,state,country,zipcode,cls,register_num))
    mysql.connection.commit()

    return redirect('/pages-account-settings-account.html')


@app.route('/pages-account-settings-edit.html')
def pages_account_settings_edit():
     return render_template('pages-account-settings-edit.html')



@app.route('/pages-account-settings-connections.html')
def pages_account_settings_connections():
    # fetching details of all students
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE Role=2 AND account_status=2")
    res=cur.fetchall()
    mysql.connection.commit()

    # fetching details of faculty
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE Role=1 AND account_status=2")
    tres=cur.fetchall()
    mysql.connection.commit()

    return render_template('pages-account-settings-connections.html',slist=res,tlist=tres)



@app.route('/pages-account-settings-notifications.html')
def pages_account_settings_notifications():
    # fetching details of users in the users table with account_status 1
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE account_status=1")
    res=cur.fetchall()
    mysql.connection.commit()
    return render_template('pages-account-settings-notifications.html',rlist=res)

@app.route('/delete-account')
def deleteaccount():
    # fetching the id
    rid=request.args.get('rid')
    # deleting the account with the corresponding id
    cur=mysql.connection.cursor()
    cur.execute("DELETE FROM users WHERE Id=%s",rid)
    mysql.connection.commit()
    return(redirect(url_for('pages_saccount_settings_notifications')))

@app.route('/approve-account')
def approveaccount():
    # fetching Id
    rid=request.args.get('rid')
    cur=mysql.connection.cursor()
    cur.execute(" UPDATE users SET account_status=2 WHERE Id=%s",(rid,))
    mysql.connection.commit()
    return(redirect(url_for('pages_account_settings_notifications')))






@app.route('/pages-misc-error.html')
def pages_misc_error():
    return render_template('pages-misc-error.html')

@app.route('/pages-misc-under-maintenance.html')
def pages_misc_under_maintenance():
    return render_template('pages-misc-under-maintenance.html')

@app.route('/tables-basic.html')
def ables_basic():
    return render_template('tables-basic.html')

@app.route('/ui-accordion.html')
def ui_accordion():
    return render_template('ui-accordion.html')

@app.route('/ui-alerts.html')
def ui_alerts():
    return render_template('ui-alerts.html')

@app.route('/ui-badges.html')
def ui_badges():
    return render_template('ui-badges.html')

@app.route('/ui-buttons.html')
def ui_buttons():
    return render_template('ui-buttons.html')

@app.route('/ui-carousel.html')
def ui_carouse():
    return render_template('ui-carousel.html')

@app.route('/ui-collapse.html')
def ui_collapse():
    return render_template('ui-collapse.html')

@app.route('/ui-dropdowns.html')
def ui_dropdowns():
    return render_template('ui-dropdowns.html')

@app.route('/ui-footer.html')
def ui_footer():
    return render_template('ui-footer.html')

@app.route('/ui-list-groups.html')
def ui_list_groups():
    return render_template('ui-list-groups.html')

@app.route('/ui-modals.html')
def ui_modals():
    return render_template('ui-modals.html')

@app.route('/ui-navbar.html')
def ui_navbar():
    return render_template('ui-navbar.html')

@app.route('/ui-offcanvas.html')
def ui_offcanvas():
    return render_template('ui-offcanvas.html')

@app.route('/ui-pagination-breadcrumbs.html')
def ui_pagination_breadcrumbs():
    return render_template('ui-pagination-breadcrumbs.html')

@app.route('/ui-progress.html')
def ui_progress():
    return render_template('ui-progress.html')

@app.route('/ui-spinners.html')
def ui_spinners():
    return render_template('ui-spinners.html')

@app.route('/ui-tabs-pills.html')
def ui_tabs_pills():
    return render_template('ui-tabs-pills.html')

@app.route('/ui-toasts.html')
def ui_toasts():
    return render_template('ui-toasts.html')

@app.route('/ui-tooltips-popovers.html')
def ui_tooltips_popovers():
    return render_template('ui-tooltips-popovers.html')

@app.route('/ui-typography.html')
def ui_typography():
    return render_template('ui-typography.html')

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    #app.app_context().push()
    app.run(debug=True)