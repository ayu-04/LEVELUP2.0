from flask_sqlalchemy import SQLAlchemy
from flask import  jsonify, request
import uuid
from sqlalchemy.dialects.sqlite import BLOB
from  werkzeug.security import generate_password_hash, check_password_hash
import jwt
from datetime import datetime, timedelta
from functools import wraps
from flask_cors import CORS, cross_origin
from sqlalchemy import ForeignKey, true, and_
from models import *
from flask import current_app as app

#enable cors
CORS(app, supports_credentials=True, resources={r'/*': {'origins': '*'}})


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authoriaztion' in request.headers:
            token = request.headers['Authoriaztion']
          
        if not token:
            return jsonify({'message' : 'Token is missing !!'}), 401
  
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'],algorithms=['HS256'])
            user = User.query.filter_by(public_id = data['public_id']).first()
        except:
            data = jwt.decode(token, app.config['SECRET_KEY'],algorithms=['HS256'])
            print(data)
            return jsonify({
                'message' : 'Token is not valid !!'
            }), 401
        print("token works")
        return  f(user)
  
    return decorated

#-------------LOGIN-------------

@app.route('/api/login', methods=['POST'])
@cross_origin()
def login():
    if request.method=='POST':
        #get post data
        post_data = request.get_json()
        u_name=post_data.get('username')
        p_word=post_data.get('password')
        rol=post_data.get('role') 
        print(u_name, p_word,rol)
        #query user
        user = User.query.filter_by(username=u_name, role=rol).first()
        #if user doesn't exist
        if user==None:
            print("no such user")
            return '', 404
        if user is not None:
            #if correct password
            if check_password_hash(user.password, p_word):
                # generates the JWT Token
                token = jwt.encode({
                    'public_id': user.public_id,
                    'exp' : datetime.utcnow() + timedelta(minutes = 30)
                }, app.config['SECRET_KEY'])
                print(token)
                return jsonify({'token' : token}), 200
            else: 
                #incorrect password
                return '', 401
    else:
        return '', 500

#----------MENTOR-SIGNUP----------
@app.route('/api/signup/mentor', methods=['POST'])
@cross_origin()
def register_mentor():
    if request.method=='POST':
        #get post data
        post_data = request.get_json()
        u_name=post_data.get('username')
        p_word=post_data.get('password')
        pfp=post_data.get('profile')
        e_mail=post_data.get('emailid')
        p_no=post_data.get('phno')
        ag=post_data.get('age')
        loc=post_data.get('location')
        langs=make_string(post_data.get('languages'))
        l_link=post_data.get('linkedin_link')
        c_link=post_data.get('calendly_link')
        sk=make_string(post_data.get('skills'))
        desc=post_data.get('description')
        #query user
        print('eihioh')
        user = User.query.filter_by(username=u_name).first()
        #if user exists
        if user!=None:
            return '', 404
        else:
            print('hioiui')
            new_user = User(public_id = str(uuid.uuid4()), username=u_name, password=generate_password_hash(p_word), role="mentor")
            print(new_user.username)
            print(new_user.password)
            db.session.add(new_user)
            db.session.commit()
            new_mentor=Mentor(username=u_name,
            profile=pfp, 
            email_id=e_mail, 
            phone_number=p_no, 
            age=ag, 
            location = loc, 
            languages=langs, 
            linkedin_link=l_link, 
            calendly_link=c_link, 
            skills=sk, 
            description=desc)
            db.session.add(new_mentor)
            db.session.commit()
            token = jwt.encode({
                                'public_id': new_user.public_id,
                                'exp' : datetime.utcnow() + timedelta(minutes = 30)
                                }, app.config['SECRET_KEY'])
            print(token)
            newusr = User.query.filter_by(username=new_user.username)
            print(newusr)
            return jsonify({'token' : token}), 200


#-----------MENTEE-SIGNUP----------------
@app.route('/api/signup/mentee', methods=['POST'])
@cross_origin()
def register_mentee():
    if request.method=='POST':
        #get post data
        post_data = request.get_json()
        u_name=post_data.get('username')
        p_word=post_data.get('password')
        pfp=post_data.get('profile')
        e_mail=post_data.get('emailid')
        p_no=post_data.get('phno')  
        ag=post_data.get('age')
        loc=post_data.get('location')
        langs=make_string(post_data.get('languages'))
        wk=make_string(post_data.get('weaknesses'))
        sk=make_string(post_data.get('skills'))
        desc=post_data.get('description')
        #query user
        user = User.query.filter_by(username=u_name).first()
        #if user exists
        if user!=None:
            return '', 404
        else:
            new_user = User(public_id = str(uuid.uuid4()), username=u_name, password=generate_password_hash(p_word), role="mentee")
            db.session.add(new_user)
            db.session.commit()
            new_mentee=Mentee(username=u_name,
            profile=pfp, 
            email_id=e_mail, 
            phone_number=p_no, 
            age=ag, 
            location = loc, 
            languages=langs, 
            weaknesses=wk, 
            skills=sk, 
            description=desc)
            db.session.add(new_mentee)
            db.session.commit()
            token = jwt.encode({
                                'public_id': new_user.public_id,
                                'exp' : datetime.utcnow() + timedelta(minutes = 30)
                                }, app.config['SECRET_KEY'])
            print(token)
            return jsonify({'token' : token}), 200

#---------MENTOR-DASHBOARD---------
@app.route('/api/dashboard/mentor/<username>', methods=['GET'])
@cross_origin()
@token_required
def dashboard_mentor(user):
    if request.method=="GET":
        print("in get")
        mentor= Mentor.query.filter_by(username=user.username).first()
        print("got mentor")
        mentorship_recs=Mentorship.query.filter_by(mentor_username=mentor.username, status="accepted").all()
        d=[]
        for r in mentorship_recs:
            mentee=Mentee.query.filter_by(username=r.mentee_username).first()
            l={}
            l["username"]=mentee.username
            l['profile']=mentee.profile
            l["skills"]=make_list(mentee.skills)
            l["phone_number"]=mentee.phone_number
            l["weaknesses"]=make_list(mentee.weaknesses)
            d.append(l)
        response_object={"mentee_list": d, "profile": mentor.profile}
        return jsonify(response_object), 200
    return '', 500


#---------MENTEE-DASHBOARD---------

@app.route('/api/dashboard/mentee/<username>', methods=['GET', 'POST'])
@cross_origin()
@token_required
def dashboard_mentee(user):
    if request.method=='GET':
        mentee = Mentee.query.filter_by(username= user.username).first()
        q = Mentor.query.all()
        d=[]
        for mentor in q:
            l={}
            l["username"]=mentor.username
            l['profile']=mentor.profile
            l["languages"]=make_list(mentor.languages)
            l["skills"]=make_list(mentor.skills)
            l["phno"]=mentor.phone_number
            l["calendly_link"]=mentor.calendly_link
            d.append(l)
        response_object={"mentor_list": d,"profile": mentee.profile}
        return jsonify(response_object), 200
    return '', 500


#---------MENTOR-EDIT---------

@app.route('/api/mentor/<username>/<mentorname>', methods=['GET', 'PUT'])
@cross_origin()
def mentor_details(username, mentorname):
    mentor= Mentor.query.filter_by(username=mentorname).first()
    if request.method == "GET":
        l={}
        l["username"]=mentor.username
        l['profile']=mentor.profile
        l["emailid"]=mentor.email_id
        l["description"]=mentor.description
        l["location"]=mentor.location
        l["languages"]=make_list(mentor.languages)
        l["age"]= mentor.age
        l["skills"]=make_list(mentor.skills)
        l["phno"]=mentor.phone_number
        l["linkedin_link"] = mentor.linkedin_link
        l["calendly_link"] = mentor.calendly_link
        return jsonify(l), 200

    if request.method=='PUT':
        data= request.get_json()
        mentor.profile=data['profile']
        mentor.email_id=data['emailid']
        mentor.description=data["description"]
        mentor.location=data["location"]
        mentor.languages=make_string(data["languages"])
        mentor.age= data["age"]
        mentor.skills=make_string(data["skills"])
        mentor.phone_number=data["phno"]
        mentor.linkedin_link= data["linkedin_link"]
        mentor.calendly_link = data["calendly_link"]
        db.session.commit()
        return '', 200
    return '', 500

#---------MENTEE-EDIT---------

@app.route('/api/mentee/<username>/<menteename>', methods=['GET', 'PUT'])
@cross_origin()
def mentee_details(username, menteename):
    mentee= Mentee.query.filter_by(username=menteename).first()
    if request.method == "GET":
        l={}
        l["username"]=mentee.username
        l['profile']=mentee.profile
        l["emailid"]=mentee.email_id
        l["description"]=mentee.description
        l["location"]=mentee.location
        l["languages"]=make_list(mentee.languages)
        l["age"]= mentee.age
        l["skills"]=make_list(mentee.skills)
        l["phno"]=mentee.phone_number
        l["weaknesses"]=make_list(mentee.weaknesses)
        return jsonify(l),200
    if request.method=='PUT':
        data= request.get_json()
        mentee.profile=data['profile']
        mentee.email_id=data["emailid"]
        mentee.description=data["description"]
        mentee.location=data["location"]
        mentee.languages=make_string(data["languages"])
        mentee.age= data["age"]
        mentee.skills=make_string(data["skills"])
        mentee.phone_number=data["phno"]
        mentee.weaknesses=make_string(data["weaknesses"])
        db.session.commit()
        return '', 200
    return '', 500 

#---------MENTORSHIPREQUESTS-MENTEE---------

@app.route('/api/mentorshiprequest/mentee/<username>', methods=['GET', 'POST'])
@cross_origin()
@token_required
def mentorshiprequest_mentee(user):
    username = user.username
    if request.method=='GET':
        l=[]
        reqs=Mentorship.query.filter_by(mentee_username=username).all()
        for r in reqs:
            d={}
            mentor=Mentor.query.filter_by(username=r.mentor_username).first()
            d['username']=r.mentor_username
            d['status']=r.status
            d['profile']=mentor.profile
            l.append(d)
        res={'mentorlist':l}
        return jsonify(res), 200
    if request.method=='POST':
        data=request.get_json()
        mentor_n=data['mentorname']
        m=Mentorship.query.filter_by(mentor_username=mentor_n, mentee_username=username).first()
        if m!=None:
            return '', 500
        else: 
            new_req=Mentorship(mentor_username=mentor_n, mentee_username=username, status="pending")
            db.session.add(new_req)
            db.session.commit()
            return '', 200


#---------MENTORSHIPREQUESTS-MENTOR---------

@app.route('/api/mentorshiprequest/mentor/<username>', methods=['GET', 'POST'])
@cross_origin()
@token_required
def mentorshiprequest_mentor(user):
    username = user.username
    if request.method=='GET':
        m=Mentorship.query.filter_by(mentor_username=username).all()
        l=[]
        for i in m:
            d={}
            mentee = Mentee.query.filter_by(username=i.mentee_username).first() 
            d['username']=i.mentee_username
            print(mentee)
            d['status']=i.status
            d['profile']=mentee.profile
            l.append(d)
        res={'menteelist': l}
        return jsonify(res), 200
    
    if request.method=='POST':
        data=request.get_json()
        req=Mentorship.query.filter_by(mentor_username=username, mentee_username=data['menteename']).first()
        req.status=data['decision']
        db.session.commit()
        return '', 200
    return '', 500

#---------GET-MENTOR-PROFILE---------

@app.route('/api/mentor/profile/<username>', methods=['GET'])
@cross_origin()
def get_mentor_profile(username):
    print(username)
    if request.method == 'GET':
        mentor = Mentor.query.filter_by(username = username).first()
        return jsonify({'profile': mentor.profile}), 200
    return '', 500


@app.route('/api/mentee/profile/<username>', methods=['GET'])
@cross_origin()
def get_mentee_profile(username):
    if request.method == 'GET':
        mentee = Mentee.query.filter_by(username = username).first()
        return jsonify({'profile': mentee.profile}), 200
    return '', 500


@app.route('/api/id/<username>', methods=['GET'])
@cross_origin()
def get_id(username):
    if request.method=='GET':
        u=User.query.filter_by(username=username).first()
        return jsonify({'id':u.id, 'username':u.username, 'role':u.role}), 200
    return '', 500

def make_string(l):
    return ','.join(l)

def make_list(s):
    return s.split(',')

# @token_required
# @app.route('/api/user/info/<username>', methos=['GET'])
# @cross_origin()
# def get_id(username):
#     if request.method == 'GET':
#         user = User.query.filter_by(username = username).first()
#         return jsonify({'id:'})