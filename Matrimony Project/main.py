#!/usr/bin/env python3

import cx_Oracle
from flask import Flask,make_response, render_template, request, url_for, redirect,session,g
from flask_cors import CORS
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import base64
import webbrowser
import numpy as np
import cv2
import os


con = cx_Oracle.connect('MATRIMONY/admin123@localhost')
cursor = con.cursor()

def get_data():    
      cursor.execute("SELECT * FROM UserDetails")
      userdata = cursor.fetchall()
      # for data in userdata:
      #       print(data[0],data[1])
      return userdata
            

def uservalidate(username,password):
       userdata = get_data()
       flag = False
       #print(len(userdata))
       for data in userdata:
              if(data[0]==username and data[1]==password):
                     flag = True
                     break
       return flag


def checkuser(username):
       userdata = get_data()
       flag = False
       for data in userdata:
              if(data[0] == username):
                     #print("account already exist")
                     flag = True
                     break
       return flag
             

def add_data(username,password):
    print(username, password)
    cursor.execute("INSERT INTO UserDetails VALUES('{}','{}')".format(username,password))
    con.commit()


def uploadData():
       if request.method == 'POST':
         email = request.form.get('username')
         password = request.form.get('password')
         add_data(email,password)
         #print('User added')
         

def RegisterFormData(fname,age,gender,highest_education,profession,salary,city,native_place,height,complexion,mother_tounge,religion,physical_status,father,mother,father_occ,mother_occ,num_of_brothers,num_of_sisters,about_famly,register_as,email,mobile_number,address):
      # cursor.execute("INSERT INTO TESTMALE VALUES('firstname','secondname','male')")
       if gender == 'male':
              # print(fname,lname,gender,dob,age,religion,country,father,mother,father_occ,mother_occ,mother_tounge,qualification,occupation,salary,address,pincode,state,addhar,mobile_number,alternate_number)
              # cursor.execute("INSERT INTO MALE VALUES('afasdf','j','male','3-23-2001',25,'kajhlsj','jsalhkjfk','father','mother','Mechanic','Housewife','Tamil','Student','MAnager',25000,'as,jdgfkssaf',63,'Pondy',7325876,29468,8747)")
              cursor.execute("INSERT INTO MALE VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(fname,age,gender,highest_education,profession,salary,city,native_place,height,complexion,mother_tounge,religion,physical_status,father,mother,father_occ,mother_occ,num_of_brothers,num_of_sisters,about_famly,register_as,email,mobile_number,address))
       elif gender == 'female':
              # print(fname,lname,gender,dob,age,religion,country,father,mother,father_occ,mother_occ,mother_tounge,qualification,occupation,salary,address,pincode,state,addhar,mobile_number,alternate_number)
              cursor.execute("INSERT INTO FEMALE VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(fname,age,gender,highest_education,profession,salary,city,native_place,height,complexion,mother_tounge,religion,physical_status,father,mother,father_occ,mother_occ,num_of_brothers,num_of_sisters,about_famly,register_as,email,mobile_number,address))
       con.commit()

def uploadform(profile_id,username,dob,fname,age,gender,height,complexion,qualification,profession,salary,working_place,natvie,mother_tounge,religion,caste,maritel_status,physical_status,father,mother,father_occ,mother_occ,brothers,sister,about,photo,mobile_number,alternate,email,address,password):
       cursor.execute("INSERT INTO UserDetails VALUES('{}','{}')".format(username,password))
       cursor.execute("INSERT INTO PROFILEDETAILS VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(profile_id,username,dob,fname,age,height,complexion,qualification,profession,salary,working_place,natvie,mother_tounge,religion,caste,maritel_status,physical_status,father,mother,father_occ,mother_occ,brothers,sister,about,photo,mobile_number,alternate,email,address,gender))
       con.commit()

def find_match(gender,from_age,to_age,from_height,to_height,mother_tounge,religion,caste,maritel_status):
      cursor.execute("SELECT PROFILE_ID, FNAME, AGE, HEIGHT, CASTE, RELIGION, PHOTO FROM PROFILEDETAILS WHERE (GENDER = '{}') AND (age BETWEEN '{}' AND '{}') AND (HEIGHT BETWEEN '{}' AND '{}') AND (MOTHER_TOUNGE = '{}') AND (RELIGION = '{}') AND ( MARITEL_STATUS = '{}')".format(gender,from_age,to_age,from_height,to_height,mother_tounge,religion,maritel_status))
      search_result = cursor.fetchall()
      return search_result

def fetch_profile_details(profile_id):
       cursor.execute("SELECT * FROM PROFILEDETAILS WHERE PROFILE_ID = '{}'".format(profile_id))
       profile_details = cursor.fetchall()
       return profile_details

def fetch_all_profiles():
      cursor.execute("SELECT PROFILE_ID, FNAME, AGE, HEIGHT, CASTE, RELIGION, PHOTO FROM PROFILEDETAILS")
      search_result = cursor.fetchall()
      return search_result       

def fetch_my_profile(username):
       cursor.execute("SELECT * FROM PROFILEDETAILS  WHERE USER_NAME= '{}'".format(username))
       profile = cursor.fetchall()
       return profile

def update_data(profile_id,username,dob,fname,age,gender,height,complexion,highest_education,profession,salary,working_place,native_place,mother_tounge,religion,caste,maritel_status,physical_status,father,mother,father_occ,mother_occ,num_of_brothers,num_of_sisters,about_famly,mobile_number,alt_mobile_number,email_id,address):
       # print(username)
       cursor.execute("UPDATE PROFILEDETAILS SET DOB= '{}', FNAME= '{}', AGE= '{}', HEIGHT= '{}', COMPLEXION= '{}', QUALIFICATION= '{}', PROFESSION= '{}', SALARY= '{}', WORKING_PLACE= '{}', NATIVE_PLACE= '{}', MOTHER_TOUNGE= '{}', RELIGION= '{}', CASTE= '{}', MARITEL_STATUS= '{}', PHYSICAL_STATUS= '{}' ,  FATHER= '{}', FATHER_OCC= '{}',MOTHER='{}', MOTHER_OCC= '{}', BROTHERS= '{}', SISTERS= '{}', ABOUT_FAMILY= '{}', MOBILE_NUMBER= '{}', ALTERNATE_NUMBER= '{}', EMAIL_ID= '{}', ADDRESS= '{}', GENDER= '{}' WHERE USER_NAME = '{}'".format(dob,fname,age,height,complexion,highest_education,profession,salary,working_place,native_place,mother_tounge,religion,caste,maritel_status,physical_status,father,mother,father_occ,mother_occ,num_of_brothers,num_of_sisters,about_famly,mobile_number,alt_mobile_number,email_id,address,gender,username))
       con.commit()
       print("done")
                                                                                                                                                     
def save_feedback(feedback_id,name,partner_name,content,photo_path):
       cursor.execute("INSERT INTO FEEDBACK VALUES('{}','{}','{}','{}','{}')".format(feedback_id,photo_path,name,partner_name,content))
       con.commit()

def fetch_feedback():
       cursor.execute("SELECT * FROM FEEDBACK")
       feedback = cursor.fetchall()
       return feedback

def update_IntrestTable(interest_id,fromid,toid,status):
       cursor.execute("INSERT INTO NTEREST_TABLE VALUES ('{}', '{}', '{}', '{}')".format(interest_id,fromid,toid,status))
       con.commit()

def fetch_interest():
       cursor.execute("SELECT * FROM NTEREST_TABLE")
       interests = cursor.fetchall()
       return interests

def remove_interest(id):
       cursor.execute("DELETE FROM NTEREST_TABLE WHERE INTEREST_ID = '{}' ".format(id))
       con.commit()

def response(id,status):
       cursor.execute("UPDATE NTEREST_TABLE SET ACCEPT_STATUS = '{}' WHERE INTEREST_ID = '{}'".format(status,id))
       con.commit()

app = Flask(__name__)
CORS(app)
PEOPLE_FOLDER = os.path.join('static','users_photos')
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

app.secret_key = 'abcd123'

@app.route('/')
def home():
       feedback = fetch_feedback()
       if g.user:
              profile = True
              return render_template("home2.html",profile = profile, feedback=feedback)
       return render_template('home2.html',feedback = feedback)

@app.route('/logedin')
def index():
   return render_template('index.html')

@app.route('/login', methods = ['POST','GET'])
def login():
       alert = True
       profile = False
       accountAdded = True
       username = request.form.get('username')
       password = request.form.get('password')
       check =  uservalidate(username,password)
       if request.method == 'POST':
              session.pop('user',None)
              if check:
                     session['user'] = username
                     profile = True
                     feedback = fetch_feedback()
                     return render_template("home2.html",profile = profile,feedback=feedback)
                     #return redirect(url_for('home2'))
              else:
                     return render_template('MainLogin.html',alert = alert)                    
       return render_template('MainLogin.html')


@app.route('/Successfully')
def registered():
       accountAdded = True
       return render_template('MainLogin.html',accountAdded=accountAdded)

    
@app.route('/newUser',methods = ['POST', 'GET'])
def newUser():
       return render_template('newUser.html')    

@app.route('/uploader', methods = ['GET', 'POST'])
def upload():
       alert = False
       accountAdded = False
       if request.method == 'POST':
              fname = request.form.get('fname')
              dob = request.form.get('dob')
              print(dob)
              age = request.form.get('age')
              gender = request.form.get('gender')
              height = request.form.get('height')
              complexion = request.form.get('complexion')
              highest_education = request.form.get('highest_education')
              profession = request.form.get('profession')
              salary = request.form.get('salary')
              working_place = request.form.get('working_place')
              native_place = request.form.get('native_place')
              mother_tounge = request.form.get('mother_tounge')
              religion = request.form.get('religion')
              caste = request.form.get('caste')
              maritel_status = request.form.get('material_status')
              physical_status = request.form.get('physical_status')
              father = request.form.get('father')
              mother = request.form.get('mother')
              father_occ = request.form.get('father_occ')
              mother_occ = request.form.get('mother_occ')
              num_of_brothers = request.form.get('num_of_brothers')
              num_of_sisters = request.form.get('num_of_sisters')
              about_famly = request.form.get('about_famly')
              photos=request.form.get("photos")
              register_as = request.form.get('register_as')
              mobile_number = request.form.get('mobile_number')
              alt_mobile_number = request.form.get('alt_mobile_number')
              email_id = request.form.get('email_id')
              address = request.form.get('address')
              photo = request.files['photo']
              degree_certificate = request.files['degree_certificate']
              caste_certificate = request.files['caste_certificate']
              birth_certificate = request.files['birth_certificate']
              #user Details\
              username = request.form.get('username')
              password = request.form.get('password')
              profile_id = 'MA_ID-' + username[:-4]
              photo_name = username[:-10]+'.jpg'
              Birth_C_name = username[:-10]+'-birth.pdf'
              Caste_C_name = username[:-10]+'-caste.pdf'
              degree_C_name = username[:-10]+'-degree.pdf'
              checkuser(username)
              usercheck = checkuser(username)
              if usercheck:
                     alert = True
                     return render_template('newUser.html',alert = alert)
              elif usercheck == False:
                     # uploadData()
                     # dir = username
                     path = os.path.join("static/users_profiles/user-" +username[:-4])
                     # path = "static/user_profiles/" +username 
                     # print(path)
                     os.mkdir(path)
                     photo_path = os.path.join(path, secure_filename(photo_name))
                     degree_path = os.path.join(path, secure_filename(degree_C_name))
                     birth_path = os.path.join(path, secure_filename(Birth_C_name))
                     caste_path = os.path.join(path, secure_filename(Caste_C_name))
                     # print("Path is "+photo_path)
                     # photo_path=username
                     # photo.save(photo_path)
                     uploadform(profile_id,username,dob,fname,age,gender,height,complexion,highest_education,profession,salary,working_place,native_place,mother_tounge,religion,caste,maritel_status,physical_status,father,mother,father_occ,mother_occ,num_of_brothers,num_of_sisters,about_famly,photo_path,mobile_number,alt_mobile_number,email_id,address,password)
                     photo.save(os.path.join(path, secure_filename(photo_name)))
                     degree_certificate.save(os.path.join(path, secure_filename(degree_C_name)))
                     caste_certificate.save(os.path.join(path, secure_filename(Caste_C_name)))
                     birth_certificate.save(os.path.join(path, secure_filename(Birth_C_name)))
                     accountAdded = True
                     # return render_template('newUser.html',accountAdded = True)
                     return render_template('security_check.html') 
                     


@app.route('/MatchFinder',methods=["POST","GET"])
def match_finder():
   if g.user:
          profile = True
          if request.method =="POST":
                     gender = request.form.get("gender")
                     from_age = request.form.get("from_age")
                     to_age = request.form.get("to_age")
                     from_height = request.form.get("from_height")
                     to_height = request.form.get("to_height")
                     mother_tounge = request.form.get("mother_tounge")
                     religion = request.form.get("religion")
                     caste = request.form.get("caste")
                     material_status = request.form.get("material_status")
                     # print(gender)
          return render_template('match_finder.html',profile=profile)
   return redirect(url_for('login'))

@app.route('/searchResult',methods=['POST','GET'])
def search_result():
       if g.user:
          if request.method =="POST":
                     gender = request.form.get("gender")
                     from_age = request.form.get("from_age")
                     to_age = request.form.get("to_age")
                     from_height = request.form.get("from_height")
                     to_height = request.form.get("to_height")
                     mother_tounge = request.form.get("mother_tounge")
                     print(mother_tounge)
                     religion = request.form.get("religion")
                     print(religion)
                     caste = request.form.get("caste")
                     print(caste)
                     maritel_status = request.form.get("material_status")
                     print(maritel_status)
                     # print(gender)
                     search_result = find_match(gender,from_age,to_age,from_height,to_height,mother_tounge,religion,caste,maritel_status)
                     profile_id  = "MA_ID-"+ g.user[:-4]
                     re = []
                     for item in search_result:
                            if profile_id not in item:
                                   re.append(item)
                     # print(re)
                     search_result = re
                     # print(search_result)
                     return render_template("search_result.html",profile = True,search_result=search_result)
       return redirect(url_for('login'))

@app.route('/interest')
def interest():
       if g.user:
              username = "MA_ID-"+g.user[:-4]
              profile = True
              interest = fetch_interest()
              r=[]
              s = []
              for item in interest:
                     if username in item[2]:
                            r.append(item)
              for ele in  interest:
                     if username in ele[1]:
                            s.append(ele)
              print(s)
              return render_template('interestPage.html',received_interest = r,sent_interest= s,profile = profile)
       return redirect(url_for('login'))

@app.route('/myProfile')
def myProfile():
       if g.user:
              username = g.user
              profile = True
              profile_details = fetch_my_profile(username)
              return render_template ('My_profile.html',profile_details = profile_details,profile = profile)

@app.route("/finalCheck",methods=["GET","POST"])
def live_image():
       return render_template('live_image.html')

@app.before_request
def before_request():
       g.user = None
       if 'user' in session:
              g.user = session['user']

@app.route('/securityCheck', methods=['POST','GET'])
def security_check():
    return render_template('security_check.html')  


def save_img(img_base64,username):
    #binary <- string base64
    img_binary = base64.b64decode(img_base64)
    #jpg <- binary
    img_jpg=np.frombuffer(img_binary, dtype=np.uint8)
    #raw image <- jpg
    img = cv2.imdecode(img_jpg, cv2.IMREAD_COLOR)
    #Path to save the decoded image
#     path = 'static/users_profilesuser-vinoth@gmail'
    #Save image
    img_path = 'static/users_profiles/user-'+ username[:-4] +'/'+username[:-10]+'-live-img'
    cv2.imwrite(img_path+'.jpg', img)
    return "SUCCESS"


@app.route('/capture_img', methods=['POST','GET'])
def capture_img():
    username = request.form['username']
    msg = save_img(request.form["img"],username)
    accountAdded = True
    return make_response(msg)
    return redirect(url_for('login'))
    return render_template('MainLogin.html',accountAdded=accountAdded)


@app.route('/camera')
def camera():
    return render_template('cmaera.html')


@app.route('/profilepage/<id>',methods = ['POST',"GET"])
def view_profile(id):
       # webbrowser.open("url_for")
       # print(foo)
       profile = True
       profile_id = id
       # print(profile_id)
       profile_details = fetch_profile_details(profile_id)
       # print(profile_details)
       return render_template("profilePage.html",profile_details = profile_details,profile=profile)

@app.route('/allProfiles',methods = ['POST','GET'])
def show_all_profiles():
       if g.user:
              search_result = fetch_all_profiles()
              profile_id  = "MA_ID-"+ g.user[:-4]
              re = []
              for item in search_result:
                     if profile_id not in item:
                            re.append(item)
              # print(re)
              search_result = re              
              return render_template("search_result.html",profile = True,search_result=search_result)
       return redirect(url_for('login'))

@app.route('/updateProfile',methods = ['POST','GET'])
def update_profile():
    if g.user:
       if request.method == 'POST':
              fname = request.form.get('fname')
              dob = request.form.get('dob')
              age = request.form.get('age')
              gender = request.form.get('gender').strip()
              height = request.form.get('height')
              complexion = request.form.get('complexion')
              highest_education = request.form.get('highest_education')
              profession = request.form.get('profession')
              salary = request.form.get('salary')
              working_place = request.form.get('working_place')
              native_place = request.form.get('native_place')
              mother_tounge = request.form.get('mother_tounge').strip()
              religion = request.form.get('religion').strip()
              caste = request.form.get('caste').strip()
              maritel_status = request.form.get('material_status').strip()
              physical_status = request.form.get('physical_status')
              father = request.form.get('father')
              mother = request.form.get('mother')
              father_occ = request.form.get('father_occ')
              mother_occ = request.form.get('mother_occ')
              num_of_brothers = request.form.get('num_of_brothers')
              num_of_sisters = request.form.get('num_of_sisters')
              about_famly = request.form.get('about_famly')
              photos=request.form.get("photos")
              register_as = request.form.get('register_as')
              mobile_number = request.form.get('mobile_number')
              alt_mobile_number = request.form.get('alt_mobile_number')
              email_id = request.form.get('email_id')
              address = request.form.get('address')
              username = g.user
              profile_id = 'MA_ID-' + username[:-4]
              update_data(profile_id,username,dob,fname,age,gender,height,complexion,highest_education,profession,salary,working_place,native_place,mother_tounge,religion,caste,maritel_status,physical_status,father,mother,father_occ,mother_occ,num_of_brothers,num_of_sisters,about_famly,mobile_number,alt_mobile_number,email_id,address)
              return redirect(url_for("myProfile"))

@app.route('/changeProfilePhoto',methods=['POST','GET'])
def change_photo():
    if g.user:
           photo = request.files['profile_photo']
           username = g.user
           photo_name = username[:-10]+'.jpg'
           path = os.path.join("static/users_profiles/user-" +username[:-4])
           photo_path = os.path.join(path, secure_filename(photo_name))
           photo.save(os.path.join(path, secure_filename(photo_name)))
           return redirect(url_for("myProfile")) 


@app.route('/feedback',methods=['POST','GET'])
def feedback():
       if g.user:
              return render_template("feedback.html")
       else:
              return render_template("MainLogin.html")

@app.route('/uploadFeedback',methods=['POST','GET'])
def upload_feedback():
    if g.user:
           username = g.user
           feedback_id = 'FB_ID_'+username[:-4]
           name = request.form.get("name")
           partner_name = request.form.get("partner_name")
           content = request.form.get("feedback")
           photo = request.files['feedback_photo'] 
           photo_name = username[:-10]+'-feedback.jpg'
           path = os.path.join("static/users_feedback/user-" +username[:-4])
           os.mkdir(path)
           photo_path = os.path.join(path, secure_filename(photo_name))
           save_feedback(feedback_id,name,partner_name,content,photo_path)
           photo.save(os.path.join(path, secure_filename(photo_name)))           
           return redirect(url_for('home'))

@app.route('/sendInterest/<to_id>/<to_user>',methods=['POST','GET'])
def send_interest(to_id,to_user):
    if g.user:
           fromid = "MA_ID-"+g.user[:-4]
           status = 'waiting'
           interest_id = 'IN_ID-'+g.user[:-4]+"-"+to_user[:-4]
           interest = fetch_interest()
           id = to_id
           for inter in interest:
                  if interest_id in inter: #"<script> window.alert('Already request sent to this profile')</script>"
                     return redirect(url_for('interest'))
           update_IntrestTable(interest_id,fromid,to_id,status)
           return  redirect(url_for('interest'))

@app.route('/deleteInterest/<id>')
def delete_interest(id):
    remove_interest(id)
    return redirect(url_for('interest'))
@app.route('/acceptInterest/<id>',methods=['POST','GET'])
def accept_interest(id):
       status = 'accepted'
       response(id,status)
       return redirect(url_for('interest'))
@app.route('/rejectInterest/<id>')
def reject_interest(id):
       status = 'Rejected'
       response(id,status)
       return redirect(url_for('interest'))
    

@app.route('/dropsession')
def dropsession():
   session.pop('user',None)
   return redirect(url_for('login'))

      


if __name__ == '__main__':
    app.run(port=8000,debug= True)
    app.config["CACHE_TYPE"] = "null"
    
