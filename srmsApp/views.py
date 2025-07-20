#from turtle import clear
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
import json
#from django.db import connection
from django.template import ContextPopException
import pdfplumber
import pandas as pd
import os
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
import mysql.connector as c
from srmsApp import forms, models
from unittest import result
from srmsApp.models import ELSEM2, ELSEM3, MESEM3, myuploadfile, myuploadfile1, myuploadfile2, myuploadfile3, user1, user12
from srmsApp.models import user
from django.db import connection
context={
    'page':'',
    'page_title':'',
    'system_name':'Result Analyzer System',
    'short_name':'RCPP',
    'has_navigation':True,
    'has_sidebar':True,
}

def teacher(request):
  

    return render(request,'teacher.html')
def menu_teach(request):
   
    cursor = connection.cursor()
    cursor.execute('select distinct DIST from COSEM2 ')
    row = cursor.fetchall()
    city_list = [item for i in row for item in i]
    result=user1.objects.all()
    cursor.execute('select avg(PERCENTAGE) from COSEM2')
    row = cursor.fetchall()
    avg = [item for i in row for item in i]
    return render(request,'com_teacher/menu_teach.html',{'city_list':city_list,'user':result,'avg':avg})
def com_teacher1(request):
   
    cursor = connection.cursor()
    cursor.execute('select distinct DIST from COSEM1 ')
    row = cursor.fetchall()
    city_list = [item for i in row for item in i]
    result=user12.objects.all()
    cursor.execute('select avg(PERCENTAGE) from COSEM1')
    row = cursor.fetchall()
    avg = [item for i in row for item in i]
    return render(request,'com_teacher/com_teacher1.html',{'city_list':city_list,'user':result,'avg':avg})

def comsem_t(request):
    context['page_title'] = 'Select SEM'
   
    return render(request,'com_teacher/comsem_t.html',context)
def chatcosem1(request):
    cursor = connection.cursor()
    cursor.execute('select count(ENROLLMENT_NO) from COSEM1')
    row = cursor.fetchall()
    city_list = [item for i in row for item in i]
    cursor.execute('select avg(PERCENTAGE) from COSEM1')
    row = cursor.fetchall()
    avg = [item for i in row for item in i]
  
    return render(request,'chartapp/chatcosem1.html',{'user':result,'city_list':city_list,'avg':avg})
    
def chatcosem3(request):
    cursor = connection.cursor()
    cursor.execute('select count(ENROLLMENT_NO) from COSEM3')
    row = cursor.fetchall()
    city_list = [item for i in row for item in i]
    cursor.execute('select avg(PERCENTAGE) from COSEM3')
    row = cursor.fetchall()
    avg = [item for i in row for item in i]
    
    return render(request,'chartapp/chatcosem3.html',{'user':result,'city_list':city_list,'avg':avg})   
def chatcosem2(request):
    cursor = connection.cursor()
    cursor.execute('select count(ENROLLMENT_NO) from COSEM2')
    row = cursor.fetchall()
    city_list = [item for i in row for item in i]
    cursor.execute('select avg(PERCENTAGE) from COSEM2')
    row = cursor.fetchall()
    avg = [item for i in row for item in i]
    
    return render(request,'chartapp/chatcosem2.html',{'user':result,'city_list':city_list,'avg':avg})   
def me1(request):
   
    return render(request,'mech_teacher/me1.html')
def me3(request):
   
    return render(request,'mech_teacher/me3.html')
def me5(request):
    cursor = connection.cursor()
    cursor.execute('select distinct DIST from MESEM3')
    row = cursor.fetchall()
    city_list = [item for i in row for item in i]
    result=MESEM3.objects.all()
    cursor.execute('select avg(PERCENTAGE) from MESEM3')
    row = cursor.fetchall()
    avg = [item for i in row for item in i]
    return render(request,'mech_teacher/me5.html',{'city_list':city_list,'user':result,'avg':avg})        
    

   
def com_teach(request):
    cursor = connection.cursor()
    cursor.execute('select distinct DIST from COSEM3 ')
    row = cursor.fetchall()
    city_list = [item for i in row for item in i]
    result=user.objects.all()
    cursor.execute('select avg(PERCENTAGE) from COSEM3')
    row = cursor.fetchall()
    avg = [item for i in row for item in i]
    return render(request,'com_teacher/com_teach.html',{'city_list':city_list,'user':result,'avg':avg})
def ele_teach(request):
    
    return render(request,'ele_teach.html')
def mec_teach(request):
    
   
    return render(request,'mech_teacher/mec_teach.html')
def civ_teach(request):
  
   
    return render(request,'civ_teach.html')                        

# Create your views here.
@login_required
def home(request):
    context['page'] = 'home'
    context['page_title'] = 'PDF SCRAPER'

   
    return render(request,'home.html',context)


@login_required
def cosem3(request):
    context['page_title'] = 'COM-SEM-1-3-5 branch'
    db = connection.cursor()
    context['class']= "DATABASE CONNECTED"
    if request.method == 'POST':
    
        def extract_pdf(pdf_path):
            linesOfFile = []
            with pdfplumber.open(pdf_path) as pdf:
                space = ' '
                page = pdf.pages[0]
                text = page.extract_text()
            p=text.split()
            if(p[2]=='PM' or p[2]=='AM'):
                ex1=p[19]
                if(ex1=='ENROLLMENT'):
                    p1=p[15]
                    p2=p[16]
                    p3=p[17]
                    p4=p[18]
                    P=p1+space+p2+space+p3+space+p4
                    e=p[21]
                    se=p[27]
                    E=e,se
                    if(p[28]=='FIRST'):
                        b1=p[31]
                        b2=p[32]
                        b3=p[33]
                        b4=p[34]
                        B=b1+space+b2+space+b3+space+b4
                        m1=p[58]
                        m2=p[70]
                        m3=p[83]
                        m4=p[95]
                        m5=p[108]
                        m6=p[123]
                        m7=p[137]
                        m8=p[151]
                        M=m1,m2,m3,m4,m5,m6,m7,m8
                        if(p[188]=='FAIL'):
                            per="00.00"
                            to=p[179]
                            e12='FAIL'
                        elif(p[188]=='A.T.K.T.'):
                            per="00.00"
                            to=p[179]
                            e12='A.T.K.T'	
                        elif((p[189]=='FIRST') and (p[190]=='CLASS') and (p[191]=='INSTRUCTIONS')):
                            per=p[179]
                            to=p[180]
                            e12='F.C'	
                        elif(p[189]=='FIRST' and p[190]=='CLASS' and p[191]=='DIST.'):
                            per=p[179]
                            to=p[180]
                            e12='FIRST CLASS DIST.'
                        elif(p[189]=='FIRST' and p[190]=='CLASS' and p[191]=='CON'):
                            per=p[179]
                            to=p[180]
                            e12='FIRST CLASS CON'
                        db.execute("INSERT INTO COSEM1(ENROLLMENT_NO,name,SEAT_NO ,BRANCH,ENGLISH,ENG_P,BASIC_SCIENCE,BS_P,BASIC_MATHEMATICS,ICT,EG,WP,PERCENTAGE,TOTAL,DIST) VALUES (%s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)",(e,P,se,B,m1,m2,m3,m4,m5,m6,m7,m8,per,to,e12))
                        context['name']=P
                        print(P,E,B,M,per,to,e12)
                    elif(p[28]=='THIRD'):
                        b1=p[31]
                        b2=p[32]
                        b3=p[33]
                        b4=p[34]
                        B=b1+space+b2+space+b3+space+b4
                        m1=p[62]
                        m2=p[74]
                        m3=p[89]
                        m4=p[111]
                        m5=p[114]
                        m6=p[126]
                        m7=p[140]
                        m8=p[152]
                        m9=p[165]
                        m10=p[177]
                        M=m1,m2,m3,m4,m5,m6,m7,m8,m9,m10
                        if(p[213]=='FAIL'):
                            per="00.00"
                            to=p[204]
                            e12='FAIL'
                        elif(p[213]=='A.T.K.T.'):
                            per="00.00"
                            to=p[204]
                            e12='A.T.K.T'	
                        elif((p[214]=='FIRST') and (p[215]=='CLASS') and (p[216]=='INSTRUCTIONS')):
                            per=p[204]
                            to=p[205]
                            e12='F.C'	
                        elif(p[214]=='FIRST' and p[215]=='CLASS' and p[216]=='DIST.'):
                            per=p[204]
                            to=p[205]
                            e12='FIRST CLASS DIST.'
                        elif(p[214]=='FIRST' and p[215]=='CLASS' and p[216]=='CON'):
                            per=p[204]
                            to=p[205]
                            e12='FIRST CLASS CON'
                        db.execute("INSERT INTO COSEM2(ENROLLMENT_NO,name,SEAT_NO ,BRANCH, OOP,OOP_P,DSU,DSU_P,CG, CG_P, DMS, DMS_P, DT,DT_P,PERCENTAGE,TOTAL,DIST) VALUES (%s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)",(e,P,se,B,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,per,to,e12))
                        context['name']=P
                        print(P,E,B,M,per,to,e12)	
                    elif(p[28]=='FIFTH'):
                        b1=p[31]
                        b2=p[32]
                        b3=p[33]
                        b4=p[34]
                        B=b1+space+b2+space+b3+space+b4
                        m1=p[59]
                        m2=p[73]
                        m3=p[85]
                        m4=p[99]
                        m5=p[111]
                        m6=p[124]
                        m7=p[136]
                        m8=p[151]
                        m9=p[163]
                        m10=p[176]
                        m11=p[191]
                        M=m1,m2,m3,m4,m5,m6,m7,m8,m9,m10
                        if(p[228]=='FAIL'):
                            per="00.00"
                            to=p[219]
                            e12='FAIL'
                        elif(p[228]=='A.T.K.T.'):
                            per="00.00"
                            to=p[219]
                            e12='A.T.K.T'	
                        elif((p[229]=='FIRST') and (p[230]=='CLASS') and (p[231]=='INSTRUCTIONS')):
                            per=p[219]
                            to=p[220]
                            e12='F.C'	
                        elif(p[229]=='FIRST' and p[230]=='CLASS' and p[231]=='DIST.'):
                            per=p[217]
                            to=p[220]
                            e12='FIRST CLASS DIST.'
                        elif(p[229]=='FIRST' and p[230]=='CLASS' and p[231]=='CON'):
                            per=p[217]
                            to=p[220]
                            e12='FIRST CLASS CON'		
                        print(P,E,B,M,per,to,e12)	
                        context['name']=P
                        db.execute("INSERT INTO COSEM3(ENROLLMENT_NO,name,SEAT_NO ,BRANCH, EVS,OS,OS_P, AJP, AJP_P, ST, ST_P,CSSL,CSSL_P,IT,CPP,PERCENTAGE,TOTAL,DIST) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)",(e,P,se,B,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,per,to,e12))
 	
                else:
                    p112=p[15]
                    p212=p[16]
                    p312=p[17]
                    P=p112+space+p212+space+p312
                    e=p[20]
                    se=p[26]
                    E=e,se
                    if(p[27]=='FIRST'):
                        b11=p[30]
                        b21=p[31]
                        b31=p[32]
                        b41=p[33]
                        B=b11+space+b21+space+b31+space+b41	
                        m1=p[57]
                        m2=p[69]
                        m3=p[82]
                        m4=p[94]
                        m5=p[107]
                        m6=p[122]
                        m7=p[136]
                        m8=p[150]
                        M=m1,m2,m3,m4,m5,m6,m7,m8
                        if(p[187]=='FAIL'):
                            per="00.00"
                            to=p[178]
                            e12='FAIL'
                        elif(p[187]=='A.T.K.T.'):
                            per="00.00"
                            to=p[178]
                            e12='A.T.K.T'	
                        elif((p[188]=='FIRST') and (p[189]=='CLASS') and (p[190]=='INSTRUCTIONS')):
                            per=p[178]
                            to=p[179]
                            e12='F.C'	
                        elif(p[188]=='FIRST' and p[189]=='CLASS' and p[190]=='DIST.'):
                            per=p[178]
                            to=p[179]
                            e12='FIRST CLASS DIST.'
                        elif(p[188]=='FIRST' and p[189]=='CLASS' and p[190]=='CON'):
                            per=p[178]
                            to=p[179]
                            e12='FIRST CLASS CON'
                        db.execute("INSERT INTO COSEM1(ENROLLMENT_NO,name,SEAT_NO ,BRANCH,ENGLISH,ENG_P,BASIC_SCIENCE,BS_P,BASIC_MATHEMATICS,ICT,EG,WP,PERCENTAGE,TOTAL,DIST) VALUES (%s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)",(e,P,se,B,m1,m2,m3,m4,m5,m6,m7,m8,per,to,e12))    	
                        context['name']=P
                        print(P,E,B,M,per,to,e12)	
                    elif(p[27]=='THIRD'):
                        b11=p[30]
                        b21=p[31]
                        b31=p[32]
                        b41=p[33]
                        B=b11+space+b21+space+b31+space+b41
                        m1=p[61]
                        m2=p[73]
                        m3=p[88]
                        m4=p[100]
                        m5=p[113]
                        m6=p[125]
                        m7=p[139]
                        m8=p[152]
                        m9=p[164]
                        m10=p[176]
                        M=m1,m2,m3,m4,m5,m6,m7,m8,m9,m10
                        if(p[212]=='FAIL'):
                            per="00.00"
                            to=p[203]
                            e12='FAIL'
                        elif(p[212]=='A.T.K.T.'):
                            per="00.00"
                            to=p[203]
                            e12='A.T.K.T'	
                        elif((p[213]=='FIRST') and (p[214]=='CLASS') and (p[215]=='INSTRUCTIONS')):
                            per=p[203]
                            to=p[204]
                            e12='F.C'
                        elif(p[213]=='FIRST' and p[214]=='CLASS' and p[215]=='DIST.'):
                            per=p[203]
                            to=p[204]
                            e12='FIRST CLASS DIST.'
                        elif(p[213]=='FIRST' and p[214]=='CLASS' and p[215]=='CON'):
                            per=p[203]
                            to=p[204]
                            e12='FIRST CLASS CON'
                        db.execute("INSERT INTO COSEM2(ENROLLMENT_NO,name,SEAT_NO ,BRANCH, OOP,OOP_P,DSU,DSU_P,CG, CG_P, DMS, DMS_P, DT,DT_P,PERCENTAGE,TOTAL,DIST) VALUES (%s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)",(e,P,se,B,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,per,to,e12))    	
                        context['name']=P
                        print(P,E,B,M,per,to,e12)
                    elif(p[28]=='FIFTH'):
                        b11=p[30]
                        b21=p[31]
                        b31=p[32]
                        b41=p[33]
                        B=b11+space+b21+space+b31+space+b41
                        m1=p[58]
                        m2=p[72]
                        m3=p[84]
                        m4=p[98]
                        m5=p[110]
                        m6=p[123]
                        m7=p[135]
                        m8=p[150]
                        m9=p[162]
                        m10=p[175]
                        m11=p[190]
                        M=m1,m2,m3,m4,m5,m6,m7,m8,m9,m10
                        if(p[227]=='FAIL'):
                            per="00.00"
                            to=p[218]
                            e12='FAIL'
                        elif(p[227]=='A.T.K.T.'):
                            per="00.00"
                            to=p[218]
                            e12='A.T.K.T'	
                        elif((p[228]=='FIRST') and (p[229]=='CLASS') and (p[230]=='INSTRUCTIONS')):
                            per=p[218]
                            to=p[219]
                            e12='F.C'	
                        elif(p[228]=='FIRST' and p[229]=='CLASS' and p[230]=='DIST.'):
                            per=p[218]
                            to=p[219]
                            e12='FIRST CLASS DIST.'
                        elif(p[228]=='FIRST' and p[229]=='CLASS' and p[230]=='CON'):
                            per=p[218]
                            to=p[219]
                            e12='FIRST CLASS CON'	
                        db.execute("INSERT INTO COSEM3(ENROLLMENT_NO,name,SEAT_NO ,BRANCH, EVS,OS,OS_P, AJP, AJP_P, ST, ST_P,CSSL,CSSL_P,IT,CPP,PERCENTAGE,TOTAL,DIST) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)",(e,P,se,B,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,per,to,e12))
                        context['name']=P
                        print(P,E,B,M,per,to,e12)		
            elif(p[0]=='Maharashtra'):
                ex1=p[16]
                if(ex1=='ENROLLMENT'):
                    p11=p[12]
                    p21=p[13]
                    p31=p[14]
                    p41=p[15]
                    P=p11+space+p21+space+p31+space+p41
                    e=p[17]
                    se=p[23]
                    E=e,se
                    if(p[24]=='FIRST'):
                        b11=p[27]
                        b21=p[28]
                        b31=p[29]
                        b41=p[30]
                        B=b11+space+b21+space+b31+space+b41
            
                        m1=p[54]
                        m2=p[66]
                        m3=p[79]
                        m4=p[92]
                        m5=p[104]
                        m6=p[119]
                        m7=p[133]
                        m8=p[147]
                        M=m1,m2,m3,m4,m5,m6,m7,m8
                        if(p[184]=='FAIL'):
                            per="00.00"
                            to=p[175]
                            e12='FAIL'
                        elif(p[184]=='A.T.K.T.'):
                            per="00.00"
                            to=p[175]
                            e12='A.T.K.T'	
                        elif((p[185]=='FIRST') and (p[186]=='CLASS') and (p[187]=='INSTRUCTIONS')):
                            per=p[175]
                            to=p[176]
                            e12='F.C'	
                        elif(p[185]=='FIRST' and p[186]=='CLASS' and p[187]=='DIST.'):
                            per=p[175]
                            to=p[176]
                            e12='FIRST CLASS DIST.'
                        elif(p[185]=='FIRST' and p[186]=='CLASS' and p[187]=='DIST.'):
                            per=p[175]
                            to=p[176]
                            e12='FIRST CLASS DIST.'	
                        elif(p[185]=='FIRST' and p[186]=='CLASS' and p[187]=='CON'):
                            per=p[175]
                            to=p[176]
                            e12='FIRST CLASS CON'	
                        db.execute("INSERT INTO COSEM1(ENROLLMENT_NO,name,SEAT_NO ,BRANCH,ENGLISH,ENG_P,BASIC_SCIENCE,BS_P,BASIC_MATHEMATICS,ICT,EG,WP,PERCENTAGE,TOTAL,DIST) VALUES (%s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)",(e,P,se,B,m1,m2,m3,m4,m5,m6,m7,m8,per,to,e12))
                        context['name']=P
                        print(P,E,B,M,per,to,e)	
                    if(p[24]=='THIRD'):
                        b11=p[27]
                        b21=p[28]
                        b31=p[29]
                        b41=p[30]
                        B=b11+space+b21+space+b31+space+b41
                        
                        m1=p[58]
                        m2=p[70]
                        m3=p[85]
                        m4=p[97]
                        m5=p[110]
                        m6=p[122]
                        m7=p[136]
                        m8=p[148]
                        m9=p[161]
                        m10=p[173]
                        M=m1,m2,m3,m4,m5,m6,m7,m8,m9,m10
                        
                        if(p[209]=='FAIL'):
                            per="00.00"
                            to=p[200]
                            e='FAIL'
                        elif(p[209]=='A.T.K.T.'):
                            per="00.00"
                            to=p[200]
                            e12='A.T.K.T'	
                        elif((p[210]=='FIRST') and (p[211]=='CLASS') and (p[212]=='INSTRUCTIONS')):
                            per=p[200]
                            to=p[201]
                            e12='F.C'	
                        elif(p[210]=='FIRST' and p[211]=='CLASS' and p[212]=='DIST.'):
                            per=p[200]
                            to=p[201]
                            e12='FIRST CLASS DIST.'
                        elif(p[210]=='FIRST' and p[211]=='CLASS' and p[212]=='CON'):
                            per=p[200]
                            to=p[201]
                            e12='FIRST CLASS CON'	
                        db.execute("INSERT INTO COSEM2(ENROLLMENT_NO,name,SEAT_NO ,BRANCH, OOP,OOP_P,DSU,DSU_P,CG, CG_P, DMS, DMS_P, DT,DT_P,PERCENTAGE,TOTAL,DIST) VALUES (%s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)",(e,P,se,B,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,per,to,e12))    	
                        context['name']=P
                        print(P,E,B,M,per,to,e12)		
                    elif(p[24]=='FIFTH'):
                        b11=p[27]
                        b21=p[28]
                        b31=p[29]
                        b41=p[30]
                        B=b11+space+b21+space+b31+space+b41
                    
                        m1=p[55]
                        m2=p[69]
                        m3=p[81]
                        m4=p[95]
                        m5=p[107]
                        m6=p[120]
                        m7=p[132]
                        m8=p[147]
                        m9=p[159]
                        m10=p[172]
                        m11=p[187]
                        M=m1,m2,m3,m4,m5,m6,m7,m8,m9,m10
        
                        
                        if(p[223]=='FAIL'):
                            per="00.00"
                            to=p[215]
                            e12='FAIL'
                        elif(p[223]=='A.T.K.T.'):
                            per="00.00"
                            to=p[215]
                            e12='A.T.K.T'	
                        elif((p[224]=='FIRST') and (p[225]=='CLASS') and (p[226]=='INSTRUCTIONS')):
                            per=p[215]
                            to=p[216]
                            e12='F.C'	
                        elif(p[224]=='FIRST' and p[225]=='CLASS' and p[226]=='DIST.'):
                            per=p[215]
                            to=p[216]
                            e12='FIRST CLASS DIST.'
                        elif(p[224]=='FIRST' and p[225]=='CLASS' and p[226]=='CON'):
                            per=p[215]
                            to=p[216]
                            e12='FIRST CLASS CON'		
                        db.execute("INSERT INTO COSEM3(ENROLLMENT_NO,name,SEAT_NO ,BRANCH, EVS,OS,OS_P, AJP, AJP_P, ST, ST_P,CSSL,CSSL_P,IT,CPP,PERCENTAGE,TOTAL,DIST) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)",(e,P,se,B,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,per,to,e12))
                        context['name']=P
                        print(P,E,B,M,per,to,e12)	

                else:
                    p112=p[12]
                    p212=p[13]
                    p312=p[14]
                    
                    P=p112+space+p212+space+p312
                    
                    e=p[17]
                    se=p[23]
                    E=e,se
                    
                    if(p[24]=='FIRST'):
                        b11=p[26]
                        b21=p[27]
                        b31=p[28]
                        b41=p[29]
                        B=b11+space+b21+space+b31+space+b41
                        print(B)
                        m1=p[53]
                        m2=p[65]
                        m3=p[78]
                        m4=p[90]
                        m5=p[103]
                        m6=p[118]
                        m7=p[132]
                        m8=p[146]
                        M=m1,m2,m3,m4,m5,m6,m7,m8
                        
                        
                        if(p[183]=='FAIL'):
                            per="00.00"
                            to=p[174]
                            e12='FAIL'
                        elif(p[183]=='A.T.K.T.'):
                            per="00.00"
                            to=p[174]
                            e12='A.T.K.T'	
                        elif((p[184]=='FIRST') and (p[185]=='CLASS') and (p[186]=='INSTRUCTIONS')):
                            per=p[174]
                            to=p[175]
                            e12='F.C'	
                        elif(p[184]=='FIRST' and p[185]=='CLASS' and p[186]=='DIST.'):
                            per=p[174]
                            to=p[175]
                            e12='FIRST CLASS DIST.'
                        elif(p[184]=='FIRST' and p[185]=='CLASS' and p[186]=='CON'):
                            per=p[174]
                            to=p[175]
                            e12='FIRST CLASS CON'	
                        db.execute("INSERT INTO COSEM1(ENROLLMENT_NO,name,SEAT_NO ,BRANCH,ENGLISH,ENG_P,BASIC_SCIENCE,BS_P,BASIC_MATHEMATICS,ICT,EG,WP,PERCENTAGE,TOTAL,DIST) VALUES (%s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)",(e,P,se,B,m1,m2,m3,m4,m5,m6,m7,m8,per,to,e12))
                        context['name']=P
                        print(P,E,B,M,per,to,e12)		
                    if(p[24]=='THIRD'):
                        b11=p[27]
                        b21=p[28]
                        b31=p[29]
                        b41=p[30]
                        B=b11+space+b21+space+b31+space+b41
                
                        m1=p[58]
                        m2=p[70]
                        m3=p[85]
                        m4=p[97]
                        m5=p[110]
                        m6=p[122]
                        m7=p[136]
                        m8=p[148]
                        m9=p[161]
                        m10=p[173]
                        M=m1,m2,m3,m4,m5,m6,m7,m8,m9,m10
                    
                        if(p[209]=='FAIL'):
                            per="00.00"
                            to=p[200]
                            e12='FAIL'
                        elif(p[209]=='A.T.K.T.'):
                            per="00.00"
                            to=p[200]
                            e12='A.T.K.T'	
                        elif((p[210]=='FIRST') and (p[211]=='CLASS') and (p[212]=='INSTRUCTIONS')):
                            per=p[200]
                            to=p[201]
                            e12='F.C'	
                        elif(p[210]=='FIRST' and p[211]=='CLASS' and p[212]=='DIST.'):
                            per=p[200]
                            to=p[201]
                            e12='FIRST CLASS DIST.'
                        elif(p[210]=='FIRST' and p[211]=='CLASS' and p[212]=='CON'):
                            per=p[200]
                            to=p[201]
                            e12='FIRST CLASS CON'	
                        db.execute("INSERT INTO COSEM2(ENROLLMENT_NO,name,SEAT_NO ,BRANCH, OOP,OOP_P,DSU,DSU_P,CG, CG_P, DMS, DMS_P, DT,DT_P,PERCENTAGE,TOTAL,DIST) VALUES (%s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)",(e,P,se,B,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,per,to,e12))
                        context['name']=P
                        print(P,E,B,M,per,to,e12)		
                    elif(p[24]=='FIFTH'):
                        b11=p[28]
                        b21=p[29]
                        b31=p[30]
                        b41=p[31]
                        B=b11+space+b21+space+b31+space+b41
            
                        m1=p[56]
                        m2=p[70]
                        m3=p[82]
                        m4=p[96]
                        m5=p[108]
                        m6=p[121]
                        m7=p[133]
                        m8=p[148]
                        m9=p[160]
                        m10=p[173]
                        m11=p[188]
                        M=m1,m2,m3,m4,m5,m6,m7,m8,m9,m10
                
                        if(p[224]=='FAIL'):
                            per="00.00"
                            to=p[216]
                            e12='FAIL'
                        elif(p[224]=='A.T.K.T.'):
                            per="00.00"
                            to=p[216]
                            e12='A.T.K.T'	
                        elif((p[225]=='FIRST') and (p[226]=='CLASS') and (p[227]=='INSTRUCTIONS')):
                            per=p[216]
                            to=p[217]
                            e12='F.C'	
                        elif(p[225]=='FIRST' and p[226]=='CLASS' and p[227]=='DIST.'):
                            per=p[216]
                            to=p[217]
                            e12='FIRST CLASS DIST.'
                        elif(p[225]=='FIRST' and p[226]=='CLASS' and p[227]=='CON'):
                            per=p[216]
                            to=p[217]
                            e12='FIRST CLASS CON'
                        db.execute("INSERT INTO COSEM3(ENROLLMENT_NO,name,SEAT_NO ,BRANCH, EVS,OS,OS_P, AJP, AJP_P, ST, ST_P,CSSL,CSSL_P,IT,CPP,PERCENTAGE,TOTAL,DIST) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)",(e,P,se,B,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,per,to,e12))
                        context['name']=P
                        print(P,E,B,M,per,to,e12)		
            else:
                ex1=p[18]
                if(ex1=='ENROLLMENT'):
                    p11=p[14]
                    p21=p[15]
                    p31=p[16]
                    p41=p[17]
                    P=p11+space+p21+space+p31+space+p41
        
                    e=p[20]
                    se=p[26]
                    E=e,se

                    if(p[27]=='FIRST'):
                        b11=p[30]
                        b21=p[31]
                        b31=p[32]
                        b41=p[33]
                        B=b11+space+b21+space+b31+space+b41

                        m1=p[57]
                        m2=p[69]
                        m3=p[82]
                        m4=p[95]
                        m5=p[107]
                        m6=p[122]
                        m7=p[136]
                        m8=p[150]
                        M=m1,m2,m3,m4,m5,m6,m7,m8
                    
                        if(p[187]=='FAIL'):
                            per="00.00"
                            to=p[178]
                            e12='FAIL'
                        elif(p[187]=='A.T.K.T.'):
                            per="00.00"
                            to=p[178]
                            e12='A.T.K.T'	
                        elif((p[188]=='FIRST') and (p[189]=='CLASS') and (p[190]=='INSTRUCTIONS')):
                            per=p[178]
                            to=p[179]
                            e12='F.C'	
                        elif(p[188]=='FIRST' and p[189]=='CLASS' and p[190]=='DIST.'):
                            per=p[178]
                            to=p[179]
                            e='FIRST CLASS DIST.'
                        elif(p[188]=='FIRST' and p[189]=='CLASS' and p[190]=='CON'):
                            per=p[178]
                            to=p[179]
                            e12='FIRST CLASS CON'	
                        db.execute("INSERT INTO COSEM1(ENROLLMENT_NO,name,SEAT_NO ,BRANCH,ENGLISH,ENG_P,BASIC_SCIENCE,BS_P,BASIC_MATHEMATICS,ICT,EG,WP,PERCENTAGE,TOTAL,DIST) VALUES (%s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)",(e,P,se,B,m1,m2,m3,m4,m5,m6,m7,m8,per,to,e12))
                        context['name']=P
                        print(P,E,B,M,per,to,e12)	
                    if(p[27]=='THIRD'):
                        b11=p[30]
                        b21=p[31]
                        b31=p[32]
                        b41=p[33]
                        B=b11+space+b21+space+b31+space+b41
                    
                        m1=p[61]
                        m2=p[73]
                        m3=p[88]
                        m4=p[100]
                        m5=p[113]
                        m6=p[125]
                        m7=p[139]
                        m8=p[151]
                        m9=p[164]
                        m10=p[176]
                        M=m1,m2,m3,m4,m5,m6,m7,m8,m9,m10
                        
                        if(p[212]=='FAIL'):
                            per="00.00"
                            to=p[203]
                            e12='FAIL'
                        elif(p[212]=='A.T.K.T.'):
                            per="00.00"
                            to=p[203]
                            e12='A.T.K.T'	
                        elif((p[213]=='FIRST') and (p[214]=='CLASS') and (p[215]=='INSTRUCTIONS')):
                            per=p[203]
                            to=p[204]
                            e12='F.C'	
                        elif(p[213]=='FIRST' and p[214]=='CLASS' and p[215]=='DIST.'):
                            per=p[203]
                            to=p[204]
                            e12='FIRST CLASS DIST.'
                        elif(p[213]=='FIRST' and p[214]=='CLASS' and p[215]=='CON'):
                            per=p[203]
                            to=p[204]
                            e12='FIRST CLASS CON'	
                        db.execute("INSERT INTO COSEM2(ENROLLMENT_NO,name,SEAT_NO ,BRANCH, OOP,OOP_P,DSU,DSU_P,CG, CG_P, DMS, DMS_P, DT,DT_P,PERCENTAGE,TOTAL,DIST) VALUES (%s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)",(e,P,se,B,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,per,to,e12))
                        context['name']=P
                        print(P,E,B,M,per,to,e12)		
                    elif(p[27]=='FIFTH'):
                        b11=p[30]
                        b21=p[31]
                        b31=p[32]
                        b41=p[33]
                        B=b11+space+b21+space+b31+space+b41
                    
                        m1=p[58]
                        m2=p[72]
                        m3=p[84]
                        m4=p[98]
                        m5=p[110]
                        m6=p[123]
                        m7=p[135]
                        m8=p[150]
                        m9=p[162]
                        m10=p[175]
                        m11=p[190]
                        M=m1,m2,m3,m4,m5,m6,m7,m8,m9,m10
                        
                        if(p[227]=='FAIL'):
                            per="00.00"
                            to=p[218]
                            e12='FAIL'
                        elif(p[227]=='A.T.K.T.'):
                            per="00.00"
                            to=p[218]
                            e12='A.T.K.T'	
                        elif((p[228]=='FIRST') and (p[229]=='CLASS') and (p[230]=='INSTRUCTIONS')):
                            per=p[218]
                            to=p[219]
                            e12='F.C'	
                        elif(p[228]=='FIRST' and p[229]=='CLASS' and p[230]=='DIST.'):
                            per=p[218]
                            to=p[219]
                            e12='FIRST CLASS DIST.'
                        elif(p[228]=='FIRST' and p[229]=='CLASS' and p[230]=='CON'):
                            per=p[218]
                            to=p[219]
                            e12='FIRST CLASS CON'
                        db.execute("INSERT INTO COSEM3(ENROLLMENT_NO,name,SEAT_NO ,BRANCH, EVS,OS,OS_P, AJP, AJP_P, ST, ST_P,CSSL,CSSL_P,IT,CPP,PERCENTAGE,TOTAL,DIST) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)",(e,P,se,B,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,per,to,e12))
                        context['name']=P
                        print(P,E,B,M,per,to,e12)	

                else:
                    p112=p[14]
                    p212=p[15]
                    p312=p[16]
                    P=p112+space+p212+space+p312
                    
                    e=p[19]
                    se=p[25]
                    E=e,se
                    
                    if(p[26]=='FIRST'):
                        b11=p[29]
                        b21=p[30]
                        b31=p[31]
                        b41=p[32]
                        B=b11+space+b21+space+b31+space+b41
          
                        m1=p[56]
                        m2=p[68]
                        m3=p[81]
                        m4=p[93]
                        m5=p[106]
                        m6=p[121]
                        m7=p[135]
                        m8=p[149]
                        M=m1,m2,m3,m4,m5,m6,m7,m8
                  
                        if(p[186]=='FAIL'):
                            per="00.00"
                            to=p[177]
                            e12='FAIL'
                        elif(p[186]=='A.T.K.T.'):
                            per="00.00"
                            to=p[177]
                            e12='A.T.K.T'	
                        elif((p[187]=='FIRST') and (p[188]=='CLASS') and (p[189]=='INSTRUCTIONS')):
                            per=p[177]
                            to=p[178]
                            e12='F.C'	
                        elif(p[187]=='FIRST' and p[188]=='CLASS' and p[189]=='DIST.'):
                            per=p[177]
                            to=p[178]
                            e12='FIRST CLASS DIST.'
                        elif(p[187]=='FIRST' and p[188]=='CLASS' and p[189]=='CON'):
                            per=p[177]
                            to=p[178]
                            e12='FIRST CLASS CON'	
                        db.execute("INSERT INTO COSEM1(ENROLLMENT_NO,name,SEAT_NO ,BRANCH,ENGLISH,ENG_P,BASIC_SCIENCE,BS_P,BASIC_MATHEMATICS,ICT,EG,WP,PERCENTAGE,TOTAL,DIST) VALUES (%s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)",(e,P,se,B,m1,m2,m3,m4,m5,m6,m7,m8,per,to,e12))
                        context['name']=P
                        print(P,E,B,M,per,to,e12)		
                    if(p[26]=='THIRD'):
                        b11=p[29]
                        b21=p[30]
                        b31=p[31]
                        b41=p[32]
                        B=b11+space+b21+space+b31+space+b41
                    
                        m1=p[60]
                        m2=p[72]
                        m3=p[87]
                        m4=p[99]
                        m5=p[112]
                        m6=p[124]
                        m7=p[138]
                        m8=p[150]
                        m9=p[163]
                        m10=p[175]
                        M=m1,m2,m3,m4,m5,m6,m7,m8,m9,m10
                      
                        if(p[211]=='FAIL'):
                            per="00.00"
                            to=p[202]
                            e12='FAIL'
                        elif(p[211]=='A.T.K.T.'):
                            per="00.00"
                            to=p[202]
                            e12='A.T.K.T'	
                        elif((p[212]=='FIRST') and (p[213]=='CLASS') and (p[214]=='INSTRUCTIONS')):
                            per=p[202]
                            to=p[203]
                            e12='F.C'	
                        elif(p[212]=='FIRST' and p[213]=='CLASS' and p[214]=='DIST.'):
                            per=p[202]
                            to=p[203]
                            e12='FIRST CLASS DIST.'
                        elif(p[212]=='FIRST' and p[213]=='CLASS' and p[214]=='CON'):
                            per=p[202]
                            to=p[203]
                            e12='FIRST CLASS CON'
                        db.execute("INSERT INTO COSEM2(ENROLLMENT_NO,name,SEAT_NO ,BRANCH, OOP,OOP_P,DSU,DSU_P,CG, CG_P, DMS, DMS_P, DT,DT_P,PERCENTAGE,TOTAL,DIST) VALUES (%s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)",(e,P,se,B,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,per,to,e12))    	
                        print(P,E,B,M,per,to,e12)
                        context['name']=P	
                    elif(p[26]=='FIFTH'):
                        b11=p[29]
                        b21=p[30]
                        b31=p[31]
                        b41=p[32]
                        B=b11+space+b21+space+b31+space+b41
                
                        m1=p[57]
                        m2=p[71]
                        m3=p[83]
                        m4=p[97]
                        m5=p[109]
                        m6=p[122]
                        m7=p[134]
                        m8=p[149]
                        m9=p[161]
                        m10=p[174]
                        m11=p[189]
                        M=m1,m2,m3,m4,m5,m6,m7,m8,m9,m10
                        
                        if(p[226]=='FAIL'):
                            per="00.00"
                            to=p[217]
                            e12='FAIL'
                        elif(p[226]=='A.T.K.T.'):
                            per="00.00"
                            to=p[217]
                            e12='A.T.K.T'	
                        elif((p[227]=='FIRST') and (p[228]=='CLASS') and (p[229]=='INSTRUCTIONS')):
                            per=p[217]
                            to=p[218]
                            e12='F.C'	
                        elif(p[227]=='FIRST' and p[228]=='CLASS' and p[229]=='DIST.'):
                            per=p[217]
                            to=p[218]
                            e12='FIRST CLASS DIST.'
                        elif(p[227]=='FIRST' and p[228]=='CLASS' and p[229]=='CON'):
                            per=p[217]
                            to=p[218]
                            e12='FIRST CLASS CON'	
                        db.execute("INSERT INTO COSEM3(ENROLLMENT_NO,name,SEAT_NO ,BRANCH, EVS,OS,OS_P, AJP, AJP_P, ST, ST_P,CSSL,CSSL_P,IT,CPP,PERCENTAGE,TOTAL,DIST) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)",(e,P,se,B,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,per,to,e12))
 	    	
                        print(P,E,B,M,per,to,e12)
                        context['name']=P
          
        pdf='C:/Users/91940/Desktop/myproj/Result_Analyzer_System/media/com'
        folder_with_pdfs = pdf
        linesOfFiles = []
        for pdf_file in os.listdir(folder_with_pdfs):
            if pdf_file.endswith('.pdf'):
                pdf_file_path = os.path.join(folder_with_pdfs, pdf_file)
                linesOfFile = extract_pdf(pdf_file_path)
                linesOfFiles.append(linesOfFile)  
    return render(request,'cosem3.html',context)        
@login_required
def mecb(request):
    context['page_title'] = 'Mechanical -3-5 branch'
  
    db = connection.cursor()
    context['class']= "DATABASE CONNECTED"
    if request.method == 'POST':
     
        def extract_pdf(pdf_path):
            string1=""
            linesOfFile = []
            with pdfplumber.open(pdf_path) as pdf:
                space = ' '
                page = pdf.pages[0]
                text = page.extract_text()
            p=text.split()
         
            if(p[2]=='PM' or p[2]=='AM'):
                ex1=p[19]
                if(ex1=='ENROLLMENT'):
                    p1=p[15]
                    p2=p[16]
                    p3=p[17]
                    p4=p[18]
                    P=p1+space+p2+space+p3+space+p4
                    e=p[21]
                    se=p[27]
                    E=e,se
                    if(p[28]=='FIFTH'):
                        b1=p[31]
                        b2=p[32]
                        b3=p[33]
                        b4=p[34]
                        B=b1+space+b2+space+b3+space+b4
                        m1=p[58]
                        m2=p[74]
                        m3=p[86]
                        m4=p[100]
                        m5=p[112]
                        m6=p[127]
                        m7=p[139]
                        m8=p[153]
                        m9=p[165]
                        m10=p[181]
                        m11=p[195]
                        m12=p[210]
                        M=[m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12]
           
                        if(p[247]=='FAIL'):
                            per="00.00"
                            to=p[238]
                            e12='FAIL'
                        elif(p[247]=='A.T.K.T.'):
                            per="00.00"
                            to=p[238]
                            e12='A.T.K.T'	
                        elif((p[248]=='FIRST') and (p[249]=='CLASS') and (p[250]=='INSTRUCTIONS')):
                            per=p[238]
                            to=p[239]
                            e12='F.C'	
                        elif(p[248]=='FIRST' and p[249]=='CLASS' and p[250]=='DIST.'):
                            per=p[238]
                            to=p[239]
                            e12='FIRST CLASS DIST.'
                        elif(p[248]=='FIRST' and p[249]=='CLASS' and p[250]=='CON'):
                            per=p[238]
                            to=p[239]
                            e12='FIRST CLASS CON'	
                        db.execute("INSERT INTO MESEM3(ENROLLMENT_NO,name,SEAT_NO ,BRANCH,MANAGEMENT,PER,PER_P,AMP,AMP_P,EMD,EMD_P,PPE,PPE_P,SMAM ,IT,CPP,PERCENTAGE,TOTAL,DIST) VALUES (%s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)",(e,P,se,B,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,per,to,e12))
 	    	    	    
                        print(P,E,B,M,per,to,e12) 
                else:
                    p1=p[15]
                    p2=p[16]
                    p3=p[17]
                    P=p1+space+p2+space+p3
                    e=p[20]
                    se=p[26]
                    E=e,se
                    if(p[27]=='FIFTH'):
                        b1=p[30]
                        b2=p[31]
                        b3=p[32]
                        b4=p[33]
                        B=b1+space+b2+space+b3+space+b4
                        m1=p[57]
                        m2=p[73]
                        m3=p[85]
                        m4=p[99]
                        m5=p[111]
                        m6=p[126]
                        m7=p[138]
                        m8=p[152]
                        m9=p[164]
                        m10=p[180]
                        m11=p[194]
                        m12=p[209]
                        M=[m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12]
           
                        if(p[246]=='FAIL'):
                            per="00.00"
                            to=p[237]
                            e12='FAIL'
                        elif(p[246]=='A.T.K.T.'):
                            per="00.00"
                            to=p[237]
                            e12='A.T.K.T'	
                        elif((p[247]=='FIRST') and (p[248]=='CLASS') and (p[249]=='INSTRUCTIONS')):
                            per=p[237]
                            to=p[238]
                            e12='F.C'	
                        elif(p[247]=='FIRST' and p[248]=='CLASS' and p[249]=='DIST.'):
                            per=p[237]
                            to=p[238]
                            e12='FIRST CLASS DIST.'
                        elif(p[247]=='FIRST' and p[248]=='CLASS' and p[249]=='CON'):
                            per=p[237]
                            to=p[238]
                            e12='FIRST CLASS CON'	
                        db.execute("INSERT INTO MESEM3(ENROLLMENT_NO,name,SEAT_NO ,BRANCH,MANAGEMENT,PER,PER_P,AMP,AMP_P,EMD,EMD_P,PPE,PPE_P,SMAM ,IT,CPP,PERCENTAGE,TOTAL,DIST) VALUES (%s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)",(e,P,se,B,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,per,to,e12))
 	    	    	    	
                        print(P,E,B,M,per,to,e12)

        pdf='C:/Users/91940/Desktop/myproj/Result_Analyzer_System/media/mec'
        folder_with_pdfs = pdf
        linesOfFiles = []
        for pdf_file in os.listdir(folder_with_pdfs):
            if pdf_file.endswith('.pdf'):
                pdf_file_path = os.path.join(folder_with_pdfs, pdf_file)
                linesOfFile = extract_pdf(pdf_file_path)
                linesOfFiles.append(linesOfFile)
    return render(request,'mecb.html',context)

def mb1(request):
    context['page_title'] = 'MEC-SEM-1 branch'
        
    return render(request,'mb1.html',context)    

def mb2(request):
    context['page_title'] = 'MEC-SEM-3 branch'
  
    return render(request,'mb2.html',context) 

def mb3(request):
    cursor = connection.cursor()
    cursor.execute('select count(ENROLLMENT_NO) from MESEM3')
    row = cursor.fetchall()
    city_list = [item for i in row for item in i]
    cursor.execute('select avg(PERCENTAGE) from MESEM3')
    row = cursor.fetchall()
    avg = [item for i in row for item in i]
    return render(request,'mb3.html',{'user':result,'city_list':city_list,'avg':avg})        
@login_required
def upload(request):
    context['page_title'] = 'Electrical-3-5 branch'
    
    if request.method == "POST" :
        name = request.POST.get("filename")
        myfile = request.FILES.getlist("uploadfoles")
        
        for f in myfile:
            myuploadfile(f_name=name,myfiles=f).save()
        
    return render(request,'upload.html',context)    
@login_required
def upload1(request):
    context['page_title'] = 'Computer-3-5 branch'
    
    if request.method == "POST" :
        name = request.POST.get("filename1")
        myfile = request.FILES.getlist("uploadfoles1")
        
        for f in myfile:
            myuploadfile1(f_name=name,myfiles=f).save()
        
    return render(request,'upload1.html',context)    
@login_required
def upload2(request):
    context['page_title'] = 'Civil-3-5 branch'
   
    if request.method == "POST" :
        name = request.POST.get("filename2")
        myfile = request.FILES.getlist("uploadfoles2")
        
        for f in myfile:
            myuploadfile2(f_name=name,myfiles=f).save()
        
    return render(request,'upload2.html',context)    
@login_required
def upload3(request):
    context['page_title'] = 'Mechanical-3-5 branch'
    
    if request.method == "POST" :
        name = request.POST.get("filename3")
        myfile = request.FILES.getlist("uploadfoles3")
        
        for f in myfile:
            myuploadfile3(f_name=name,myfiles=f).save()
        
     
    return render(request,'upload3.html',context)                        

def eleb(request):
    context['page_title'] = 'Electrical-3-5 branch'
    db = connection.cursor()
    context['class']= "DATABASE CONNECTED"

    if request.method == 'POST':

        def extract_pdf(pdf_path):
   
            linesOfFile = []
            with pdfplumber.open(pdf_path) as pdf:
                space = ' '
                page = pdf.pages[0]
                text = page.extract_text()
            p=text.split()
            # print(p)
        
            if(p[2]=='PM' or p[2]=='AM'):
                ex1=p[19]
                if(ex1=='ENROLLMENT'):
                    p1=p[15]
                    p2=p[16]
                    p3=p[17]
                    p4=p[18]
                    P=p1+space+p2+space+p3+space+p4
                    e=p[21]
                    se=p[27]
                    E=e,se
                    if(p[28]=='THIRD'):
                        b1=p[31]
                        b2=p[32]
                        b3=p[33]
                        b4=p[34]
                        B=b1+space+b2+space+b3+space+b4
                        m1=p[59]
                        m2=p[71]
                        m3=p[86]
                        m4=p[98]
                        m5=p[113]
                        m6=p[125]
                        m7=p[139]
                        m8=p[151]
                        m9=p[167]
                        m10=p[179]
                    
                        M=[m1,m2,m3,m4,m5,m6,m7,m8,m9,m10]
                        if(p[215]=='FAIL'):
                            per="00.00"
                            to=p[206]
                            e12='FAIL'
                        elif(p[215]=='A.T.K.T.'):
                            per="00.00"
                            to=p[206]
                            e12='A.T.K.T'	
                        elif((p[216]=='FIRST') and (p[217]=='CLASS') and (p[218]=='INSTRUCTIONS')):
                            per=p[206]
                            to=p[207]
                            e12='F.C'	
                        elif(p[216]=='FIRST' and p[217]=='CLASS' and p[218]=='DIST.'):
                            per=p[206]
                            to=p[207]
                            e12='FIRST CLASS DIST.'
                        elif(p[216]=='FIRST' and p[217]=='CLASS' and p[218]=='CON'):
                            per=p[206]
                            to=p[207]
                            e12='FIRST CLASS CON'	
                        elif(p[216]=='SECOND' and p[217]=='CLASS' and p[218]=='CON'):
                            per=p[206]
                            to=p[207]
                            e12='SECOND CLASS CON'  
                        elif(p[216]=='SECOND' and p[217]=='CLASS'):
                            per=p[206]
                            to=p[207]
                            e12='S.C'        
                        db.execute("INSERT INTO ELSEM2(ENROLLMENT_NO,name ,SEAT_NO ,BRANCH ,EC, EC_P ,EEM,EEM_P,FPE ,FPE_P,EPG,EPG_P,EMWP,EMWP_P,PERCENTAGE,TOTAL,DIST) VALUES ( %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)",(e,P,se,B,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,per,to,e12))
    	    	    	        	
                        print(P,E,B,M,per,to,e12)

                    elif(p[28]=='FIFTH'):
                        b1=p[31]
                        b2=p[32]
                        b3=p[33]
                        b4=p[34]
                        B=b1+space+b2+space+b3+space+b4
                        m1=p[58]
                        m2=p[73]
                        m3=p[85]
                        m4=p[99]
                        m5=p[111]
                        m6=p[126]
                        m7=p[138]
                        m8=p[153]
                        m9=p[165]
                        m10=p[178]
                        m11=p[192]
                        m12=p[207]
                        M=[m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12]
                        if(p[244]=='FAIL'):
                            per="00.00"
                            to=p[235]
                            e12='FAIL'
                        elif(p[244]=='A.T.K.T.'):
                            per="00.00"
                            to=p[235]
                            e12='A.T.K.T'	
                        elif((p[245]=='FIRST') and (p[246]=='CLASS') and (p[247]=='INSTRUCTIONS')):
                            per=p[235]
                            to=p[236]
                            e12='F.C'	
                        elif(p[245]=='FIRST' and p[246]=='CLASS' and p[247]=='DIST.'):
                            per=p[235]
                            to=p[236]
                            e12='FIRST CLASS DIST.'
                        elif(p[245]=='FIRST' and p[246]=='CLASS' and p[247]=='CON'):
                            per=p[235]
                            to=p[236]
                            e12='FIRST CLASS CON'
                        elif(p[245]=='SECOND' and p[246]=='CLASS' and p[247]=='CON'):
                            per=p[235]
                            to=p[236]
                            e12='SECOND CLASS CON'     
                        elif(p[245]=='SECOND' and p[246]=='CLASS'):
                            per=p[235]
                            to=p[236]
                            e12='S.C'         
                        db.execute("INSERT INTO ELSEM3(ENROLLMENT_NO,name ,SEAT_NO ,BRANCH ,MANAGEMENT, IAM ,IAM_P,SP,SP_P ,ECA,ECA_P,EIA,EIA_P,ED,IT,CPP,PERCENTAGE,TOTAL,DIST) VALUES (%s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)",(e,P,se,B,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,per,to,e12))
    	    	
                        print(P,E,B,M,per,to,e12)
                else:
                    p1=p[15]
                    p2=p[16]
                    p3=p[17]
                    P=p1+space+p2+space+p3
                    e=p[20]
                    se=p[26]
                    E=e,se
                    if(p[27]=='THIRD'):
                        b1=p[30]
                        b2=p[31]
                        b3=p[32]
                        b4=p[33]
                        B=b1+space+b2+space+b3+space+b4
                        m1=p[58]
                        m2=p[70]
                        m3=p[85]
                        m4=p[97]
                        m5=p[112]
                        m6=p[124]
                        m7=p[138]
                        m8=p[150]
                        m9=p[166]
                        m10=p[178]
                        M=[m1,m2,m3,m4,m5,m6,m7,m8,m9,m10]
                    
                        if(p[214]=='FAIL'):
                            per="00.00"
                            to=p[205]
                            e12='FAIL'
                        elif(p[214]=='A.T.K.T.'):
                            per="00.00"
                            to=p[205]
                            e12='A.T.K.T'	
                        elif((p[215]=='FIRST') and (p[216]=='CLASS') and (p[217]=='INSTRUCTIONS')):
                            per=p[205]
                            to=p[206]
                            e12='F.C'	
                        elif(p[215]=='FIRST' and p[216]=='CLASS' and p[217]=='DIST.'):
                            per=p[205]
                            to=p[206]
                            e12='FIRST CLASS DIST.'
                        elif(p[215]=='FIRST' and p[216]=='CLASS' and p[217]=='CON'):
                            per=p[205]
                            to=p[206]
                            e12='FIRST CLASS CON'
                        elif(p[215]=='SECOND' and p[216]=='CLASS' and p[217]=='CON'):
                            per=p[205]
                            to=p[206]
                            e12='SECOND CLASS CON'
                        elif(p[215]=='SECOND' and p[216]=='CLASS'):
                            per=p[205]
                            to=p[206]
                            e12='S.C'        	
                        db.execute("INSERT INTO ELSEM2(ENROLLMENT_NO,name ,SEAT_NO ,BRANCH ,EC, EC_P ,EEM,EEM_P,FPE ,FPE_P,EPG,EPG_P,EMWP,EMWP_P,PERCENTAGE,TOTAL,DIST) VALUES ( %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)",(e,P,se,B,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,per,to,e12))
    	    	    	        	
                        print(P,E,B,M,per,to,e12)
                    elif(p[27]=='FIFTH'):
                        b1=p[30]
                        b2=p[31]
                        b3=p[32]
                        b4=p[33]
                        B=b1+space+b2+space+b3+space+b4
                        m1=p[57]
                        m2=p[72]
                        m3=p[84]
                        m4=p[98]
                        m5=p[110]
                        m6=p[125]
                        m7=p[137]
                        m8=p[152]
                        m9=p[164]
                        m10=p[177]
                        m11=p[191]
                        m12=p[206]
                        M=[m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12]
                        if(p[243]=='FAIL'):
                            per="00.00"
                            to=p[234]
                            e12='FAIL'
                        elif(p[243]=='A.T.K.T.'):
                            per="00.00"
                            to=p[234]
                            e12='A.T.K.T'	
                        elif((p[244]=='FIRST') and (p[245]=='CLASS') and (p[246]=='INSTRUCTIONS')):
                            per=p[234]
                            to=p[235]
                            e12='F.C'	
                        elif(p[244]=='FIRST' and p[245]=='CLASS' and p[246]=='DIST.'):
                            per=p[234]
                            to=p[235]
                            e12='FIRST CLASS DIST.'
                        elif(p[244]=='FIRST' and p[245]=='CLASS' and p[246]=='CON'):
                            per=p[234]
                            to=p[235]
                            e12='FIRST CLASS CON'
                        elif(p[244]=='SECOND' and p[245]=='CLASS' and p[246]=='CON'):
                            per=p[234]
                            to=p[235]
                            e12='SECOND CLASS CON' 
                        elif(p[244]=='SECOND' and p[245]=='CLASS'):
                            per=p[234]
                            to=p[235]
                            e12='S.C'        
                            
                        db.execute("INSERT INTO ELSEM3(ENROLLMENT_NO,name ,SEAT_NO ,BRANCH ,MANAGEMENT, IAM ,IAM_P,SP,SP_P ,ECA,ECA_P,EIA,EIA_P,ED,IT,CPP,PERCENTAGE,TOTAL,DIST) VALUES (%s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)",(e,P,se,B,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,per,to,e12))
    	    	    	    	
                        print(P,E,B,M,per,to,e12)

            else:
                ex1=p[18]
                if(ex1=='ENROLLMENT'):
                    p1=p[14]
                    p2=p[15]
                    p3=p[16]
                    p4=p[17]
                    P=p1+space+p2+space+p3+space+p4
                    e=p[20]
                    se=p[26]
                    E=e,se
                    if(p[27]=='THIRD'):
                        b1=p[30]
                        b2=p[31]
                        b3=p[32]
                        b4=p[33]
                        B=b1+space+b2+space+b3+space+b4
                        m1=p[58]
                        m2=p[70]
                        m3=p[85]
                        m4=p[97]
                        m5=p[112]
                        m6=p[124]
                        m7=p[138]
                        m8=p[150]
                        m9=p[166]
                        m10=p[178]
                      
                        M=[m1,m2,m3,m4,m5,m6,m7,m8,m9,m10]
                        if(p[214]=='FAIL'):
                            per="00.00"
                            to=p[205]
                            e12='FAIL'
                        elif(p[214]=='A.T.K.T.'):
                            per="00.00"
                            to=p[205]
                            e12='A.T.K.T'	
                        elif((p[215]=='FIRST') and (p[216]=='CLASS') and (p[217]=='INSTRUCTIONS')):
                            per=p[205]
                            to=p[206]
                            e12='F.C'	
                        elif(p[215]=='FIRST' and p[216]=='CLASS' and p[217]=='DIST.'):
                            per=p[205]
                            to=p[206]
                            e12='FIRST CLASS DIST.'
                        elif(p[215]=='FIRST' and p[216]=='CLASS' and p[217]=='CON'):
                            per=p[205]
                            to=p[206]
                            e12='FIRST CLASS CON'   
                        elif(p[215]=='SECOND' and p[216]=='CLASS' and p[217]=='CON'):
                            per=p[205]
                            to=p[206]
                            e12='SECOND CLASS CON'
                        elif(p[215]=='SECOND' and p[216]=='CLASS'):
                            per=p[205]
                            to=p[206]
                            e12='S.C'          	
                        db.execute("INSERT INTO ELSEM2(ENROLLMENT_NO,name ,SEAT_NO ,BRANCH ,EC, EC_P ,EEM,EEM_P,FPE ,FPE_P,EPG,EPG_P,EMWP,EMWP_P,PERCENTAGE,TOTAL,DIST) VALUES ( %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)",(e,P,se,B,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,per,to,e12))
    	    	    	    
                        print(P,E,B,M,per,to,e12)
                    elif(p[27]=='FIFTH'):
                        b1=p[30]
                        b2=p[31]
                        b3=p[32]
                        b4=p[33]
                        B=b1+space+b2+space+b3+space+b4
                        m1=p[57]
                        m2=p[72]
                        m3=p[84]
                        m4=p[98]
                        m5=p[110]
                        m6=p[125]
                        m7=p[137]
                        m8=p[152]
                        m9=p[164]
                        m10=p[177]
                        m11=p[191]
                        m12=p[206]
                        M=[m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12]
                        if(p[243]=='FAIL'):
                            per="00.00"
                            to=p[234]
                            e12='FAIL'
                        elif(p[243]=='A.T.K.T.'):
                            per="00.00"
                            to=p[234]
                            e12='A.T.K.T'	
                        elif((p[244]=='FIRST') and (p[245]=='CLASS') and (p[246]=='INSTRUCTIONS')):
                            per=p[234]
                            to=p[235]
                            e12='F.C'	
                        elif(p[244]=='FIRST' and p[245]=='CLASS' and p[246]=='DIST.'):
                            per=p[234]
                            to=p[235]
                            e12='FIRST CLASS DIST.'
                        elif(p[244]=='FIRST' and p[245]=='CLASS' and p[246]=='CON'):
                            per=p[234]
                            to=p[235]
                            e12='FIRST CLASS CON'
                        elif(p[244]=='SECOND' and p[245]=='CLASS' and p[246]=='CON'):
                            per=p[234]
                            to=p[235]
                            e12='SECOND CLASS CON'   
                        elif(p[244]=='SECOND' and p[245]=='CLASS'):
                            per=p[234]
                            to=p[235]
                            e12='S.C'       
                        db.execute("INSERT INTO ELSEM3(ENROLLMENT_NO,name ,SEAT_NO ,BRANCH ,MANAGEMENT, IAM ,IAM_P,SP,SP_P ,ECA,ECA_P,EIA,EIA_P,ED,IT,CPP,PERCENTAGE,TOTAL,DIST) VALUES (%s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)",(e,P,se,B,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,per,to,e12))
    	    	
                        print(P,E,B,M,per,to,e12)
                else:
                    p1=p[14]
                    p2=p[15]
                    p3=p[16]
                    P=p1+space+p2+space+p3
                    e=p[19]
                    se=p[25]
                    E=e,se
                    if(p[26]=='THIRD'):
                        b1=p[29]
                        b2=p[30]
                        b3=p[31]
                        b4=p[32]
                        B=b1+space+b2+space+b3+space+b4
                        m1=p[57]
                        m2=p[69]
                        m3=p[84]
                        m4=p[96]
                        m5=p[111]
                        m6=p[123]
                        m7=p[137]
                        m8=p[149]
                        m9=p[165]
                        m10=p[177]
                    
                        M=[m1,m2,m3,m4,m5,m6,m7,m8,m9,m10]
                        if(p[213]=='FAIL'):
                            per="00.00"
                            to=p[204]
                            e12='FAIL'
                        elif(p[213]=='A.T.K.T.'):
                            per="00.00"
                            to=p[204]
                            e12='A.T.K.T'	
                        elif((p[214]=='FIRST') and (p[215]=='CLASS') and (p[216]=='INSTRUCTIONS')):
                            per=p[204]
                            to=p[205]
                            e12='F.C'	
                        elif(p[214]=='FIRST' and p[215]=='CLASS' and p[216]=='DIST.'):
                            per=p[204]
                            to=p[205]
                            e12='FIRST CLASS DIST.'
                        elif(p[214]=='FIRST' and p[215]=='CLASS' and p[216]=='CON'):
                            per=p[204]
                            to=p[205]
                            e12='FIRST CLASS CON'	
                        elif(p[214]=='SECOND' and p[215]=='CLASS' and p[216]=='CON'):
                            per=p[204]
                            to=p[205]
                            e12='SECOND CLASS CON'
                        elif(p[214]=='SECOND' and p[215]=='CLASS'):
                            per=p[204]
                            to=p[205]
                            e12='S.C'        
                        db.execute("INSERT INTO ELSEM2(ENROLLMENT_NO,name ,SEAT_NO ,BRANCH ,EC, EC_P ,EEM,EEM_P,FPE ,FPE_P,EPG,EPG_P,EMWP,EMWP_P,PERCENTAGE,TOTAL,DIST) VALUES ( %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)",(e,P,se,B,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,per,to,e12))
    	    	    	    	
                        print(P,E,B,M,per,to,e12)
                    elif(p[26]=='FIFTH'):
                        b1=p[29]
                        b2=p[30]
                        b3=p[31]
                        b4=p[32]
                        B=b1+space+b2+space+b3+space+b4
                        m1=p[56]
                        m2=p[71]
                        m3=p[83]
                        m4=p[97]
                        m5=p[109]
                        m6=p[124]
                        m7=p[136]
                        m8=p[151]
                        m9=p[163]
                        m10=p[176]
                        m11=p[190]
                        m12=p[205]
                        M=[m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12]
                        if(p[242]=='FAIL'):
                            per="00.00"
                            to=p[233]
                            e12='FAIL'
                        elif(p[242]=='A.T.K.T.'):
                            per="00.00"
                            to=p[233]
                            e12='A.T.K.T'	
                        elif((p[243]=='FIRST') and (p[244]=='CLASS') and (p[245]=='INSTRUCTIONS')):
                            per=p[233]
                            to=p[234]
                            e12='F.C'	
                        elif(p[243]=='FIRST' and p[244]=='CLASS' and p[245]=='DIST.'):
                            per=p[233]
                            to=p[234]
                            e12='FIRST CLASS DIST.'
                        elif(p[243]=='FIRST' and p[244]=='CLASS' and p[245]=='CON'):
                            per=p[233]
                            to=p[234]
                            e12='FIRST CLASS CON'
                        elif(p[243]=='SECOND' and p[244]=='CLASS' and p[245]=='CON'):
                            per=p[233]
                            to=p[234]
                            e12='SECOND CLASS CON'    
                        elif(p[243]=='SECOND' and p[244]=='CLASS'):
                            per=p[233]
                            to=p[234]
                            e12='S.C'        
                        db.execute("INSERT INTO ELSEM3(ENROLLMENT_NO,name ,SEAT_NO ,BRANCH ,MANAGEMENT, IAM ,IAM_P,SP,SP_P ,ECA,ECA_P,EIA,EIA_P,ED,IT,CPP,PERCENTAGE,TOTAL,DIST) VALUES (%s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)",(e,P,se,B,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,per,to,e12))
    	    	    	    	
                        print(P,E,B,M,per,to,e12)    
        pdf='C:/Users/91940/Desktop/Result_Analyzer_System/media/ele'
        folder_with_pdfs = pdf
        linesOfFiles = []
        for pdf_file in os.listdir(folder_with_pdfs):
            if pdf_file.endswith('.pdf'):
                pdf_file_path = os.path.join(folder_with_pdfs, pdf_file)
                linesOfFile = extract_pdf(pdf_file_path)
                linesOfFiles.append(linesOfFile)


    return render(request,'eleb.html',context)

def elb1(request):
    
    return render(request,'elb1.html',context)    

def elb2(request):
    cursor = connection.cursor()
    cursor.execute('select distinct DIST from ELSEM2 ')
    row = cursor.fetchall()
    city_list = [item for i in row for item in i]
    result=ELSEM2.objects.all()
    cursor.execute('select avg(PERCENTAGE) from ELSEM2')
    row = cursor.fetchall()
    avg = [item for i in row for item in i]
        
    return render(request,'elb2.html',{'city_list':city_list,'user':result,'avg':avg}) 
def chatel2(request):
    cursor = connection.cursor()
    cursor.execute('select count(ENROLLMENT_NO) from ELSEM2')
    row = cursor.fetchall()
    city_list = [item for i in row for item in i]
    cursor.execute('select avg(PERCENTAGE) from ELSEM2')
    row = cursor.fetchall()
    avg = [item for i in row for item in i]  
    return render(request,'chartapp/chatel2.html',{'city_list':city_list,'user':result,'avg':avg}) 


def elb3(request):
    cursor = connection.cursor()
    cursor.execute('select distinct DIST from ELSEM3 ')
    row = cursor.fetchall()
    city_list = [item for i in row for item in i]
    result=ELSEM3.objects.all()
    cursor.execute('select avg(PERCENTAGE) from ELSEM3')
    row = cursor.fetchall()
    avg = [item for i in row for item in i]
     
    return render(request,'elb3.html',{'city_list':city_list,'user':result,'avg':avg})        
def chatel3(request):
    cursor = connection.cursor()
    cursor.execute('select count(ENROLLMENT_NO) from ELSEM3')
    row = cursor.fetchall()
    city_list = [item for i in row for item in i]
    cursor.execute('select avg(PERCENTAGE) from ELSEM3')
    row = cursor.fetchall()
    avg = [item for i in row for item in i]  
    return render(request,'chartapp/chatel3.html',{'city_list':city_list,'user':result,'avg':avg}) 


@login_required
def civb(request):
    context['page_title'] = 'Civil branch'
    return render(request,'civb.html',context)
@login_required
def civ1(request):
    context['page_title'] = 'CIV-SEM-1 branch'
        
    
    return render(request,'civ1.html',context)    
@login_required
def civ2(request):
    context['page_title'] = 'CIV-SEM-3 branch'
        
      
    return render(request,'civ2.html',context) 
@login_required
def civ3(request):
    context['page_title'] = 'CIV-SEM-5 branch'
        
    return render(request,'civ3.html',context)        

#login
def login_user(request):
    logout(request)
    resp = {"status":'failed','msg':''}
    username = ''
    password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                resp['status']='success'
            else:
                resp['msg'] = "Incorrect username or password"
        else:
            resp['msg'] = "Incorrect username or password"
    return HttpResponse(json.dumps(resp),content_type='application/json')

#Logout
def logoutuser(student):
    logout(student)
    return redirect('/')


@login_required
def update_profile(request):
    context['page_title'] = 'Update Profile'
    user = User.objects.get(id = request.user.id)
    if not request.method == 'POST':
        form = forms.UpdateProfile(instance=user)
        context['form'] = form
        print(form)
    else:
        form = forms.UpdateProfile(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile has been updated")
            return redirect("profile-page")
        else:
            context['form'] = form
            
    return render(request, 'manage_profile.html',context)


@login_required
def update_password(request):
    context['page_title'] = "Update Password"
    if request.method == 'POST':
        form = forms.UpdatePasswords(user = request.user, data= request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your Account Password has been updated successfully")
            update_session_auth_hash(request, form.user)
            return redirect("profile-page")
        else:
            context['form'] = form
    else:
        form = forms.UpdatePasswords(request.POST)
        context['form'] = form
    return render(request,'update_password.html',context)

@login_required
def profile(request):
    context['page'] = 'profile'
    context['page_title'] = "Profile"
    return render(request,'profile.html', context)


# Class
@login_required
def class_mgt(request):
    context['page'] = 'class_mgt'
    context['page_title'] = 'Class Management'
    classes = models.Class.objects.all()
    context['classes'] = classes
    return render(request,'class_mgt.html',context)


@login_required
def manage_class(request, pk = None):
    if not pk is None:
        classData = models.Class.objects.get(id = pk)
        context['classData'] = classData
    else:
        context['classData'] = {}
    return render(request, 'manage_class.html', context)

@login_required
def save_class(request):
    resp = { 'status':'failed', 'msg' : '' }
    if not request.method == 'POST':
        resp['msg'] = 'Request has been sent without data.'
    else:
        post = request.POST
        if post['id'] == None or post['id'] == '':
            form = forms.SaveClass(post)
        else:
            _class = models.Class.objects.get(id = post['id'])
            form = forms.SaveClass(post, instance=_class)

        if form.is_valid():
            form.save()
            resp['status'] = 'success'
            messages.success(request, "Class Detail has been saved successfully.")
        else:
            resp['msg'] = 'Class Detail has failed to save.'
            for field in form:
                for error in field.errors:
                    resp['msg'] += str("<br/>"+error)
    return HttpResponse(json.dumps(resp),content_type="application/json")    

@login_required
def delete_class(request):
    resp = { 'status':'failed', 'msg' : '' }
    if not request.method == 'POST':
        resp['msg'] = 'Request has been sent without data.'
    else:
        post = request.POST
        try:
            models.Class.objects.get(id = post['id']).delete()
            resp['status'] = 'success'
            messages.success(request, "Class Detail has been deleted successfully.")
        except:
            resp['msg'] = 'Class Detail has failed to delete.'

    return HttpResponse(json.dumps(resp),content_type="application/json")



#Subject
@login_required
def subject_mgt(request):
    context['page'] = 'subject_mgt'
    context['page_title'] = 'Subject Management'
    subjects = models.Subject.objects.all()
    context['subjects'] = subjects
    return render(request,'subject_mgt.html',context)


@login_required
def manage_subject(request, pk = None):
    if not pk is None:
        subject = models.Subject.objects.get(id = pk)
        context['subject'] = subject
    else:
        context['subject'] = {}
    return render(request, 'manage_subject.html', context)

@login_required
def view_subject(request, pk = None):
    if not pk is None:
        subject = models.Subject.objects.get(id = pk)
        context['subject'] = subject
    else:
        context['subject'] = {}
    return render(request, 'view_subject.html', context)

@login_required
def save_subject(request):
    resp = { 'status':'failed', 'msg' : '' }
    if not request.method == 'POST':
        resp['msg'] = 'Request has been sent without data.'
    else:
        post = request.POST
        if post['id'] == None or post['id'] == '':
            form = forms.SaveSubject(post)
        else:
            subject = models.Subject.objects.get(id = post['id'])
            form = forms.SaveSubject(post, instance=subject)

        if form.is_valid():
            form.save()
            resp['status'] = 'success'
            messages.success(request, "Subject Detail has been saved successfully.")
        else:
            resp['msg'] = 'Subject Detail has failed to save.'
            for field in form:
                for error in field.errors:
                    resp['msg'] += str(f"<br/>"+error)
    return HttpResponse(json.dumps(resp),content_type="application/json")    

@login_required
def delete_subject(request):
    resp = { 'status':'failed', 'msg' : '' }
    if not request.method == 'POST':
        resp['msg'] = 'Request has been sent without data.'
    else:
        post = request.POST
        try:
            models.Subject.objects.get(id = post['id']).delete()
            resp['status'] = 'success'
            messages.success(request, "Subject Detail has been deleted successfully.")
        except:
            resp['msg'] = 'Subject Detail has failed to delete.'

    return HttpResponse(json.dumps(resp),content_type="application/json")

#Students
@login_required
def costud_m(request):
    context['page'] = 'student_mgt'
    context['page_title'] = 'Student Management'
    
    return render(request,'stud_com_list/costud_m.html',context)
@login_required
def costud3_m(request):
    context['page'] = 'student_mgt'
    context['page_title'] = 'Student Management'
    result=user1.objects.all()
    context['user1']=result
    return render(request,'stud_com_list/costud3_m.html',context)
@login_required
def cosem2(request):
    context['page'] = 'student_mgt'
    context['page_title'] = 'Student Management'
    result=user12.objects.all()
    context['user12']=result
    return render(request,'stud_com_list/cosem2.html',context)    
@login_required
def costud2_m(request):
    context['page'] = 'student_mgt'
    context['page_title'] = 'Student Management'
    context['page_title'] = 'Student Management'
    cursor = connection.cursor()
    cursor.execute('select distinct DIST from COSEM3')
    result=user1.objects.all()
    context['user1']=result
    return render(request,'stud_com_list/costud2_m.html',context)
@login_required
def student_mgt(request):
    context['page'] = 'student_mgt'
    context['page_title'] = 'Student Management'
    
    return render(request,'student_mgt.html',context)
@login_required
def stud3(request):
    context['page'] = 'student_mgt'
    context['page_title'] = 'Student Management'
    cursor = connection.cursor()
    cursor.execute('select distinct DIST from COSEM3')
    result=user.objects.all()
    context['user']=result
    return render(request,'stud_com_list/stud3.html',context)

@login_required
def manage_student(request, pk = None):
    classes = models.Class.objects.filter(status = 1).all()
    context['classes'] = classes
    if not pk is None:
        student = models.Student.objects.get(id = pk)
        context['student'] = student
    else:
        context['student'] = {}
    return render(request, 'manage_student.html', context)

@login_required
def view_student(request, pk = None):
    if not pk is None:
        student = models.Student.objects.get(id = pk)
        context['student'] = student
    else:
        context['student'] = {}
    return render(request, 'view_student.html', context)

@login_required
def save_student(request):
    resp = { 'status':'failed', 'msg' : '' }
    if not request.method == 'POST':
        resp['msg'] = 'Request has been sent without data.'
    else:
        post = request.POST
        if post['id'] == None or post['id'] == '':
            form = forms.SaveStudent(post)
        else:
            student = models.Student.objects.get(id = post['id'])
            form = forms.SaveStudent(post, instance=student)

        if form.is_valid():
            form.save()
            resp['status'] = 'success'
            messages.success(request, "Student Detail has been saved successfully.")
        else:
            resp['msg'] = 'Student Detail has failed to save.'
            for field in form:
                for error in field.errors:
                    resp['msg'] += str(f"<br/> [{field.name}] "+error)
    return HttpResponse(json.dumps(resp),content_type="application/json")    

@login_required
def delete_student(request):
    resp = { 'status':'failed', 'msg' : '' }
    if not request.method == 'POST':
        resp['msg'] = 'Request has been sent without data.'
    else:
        post = request.POST
        try:
            models.Student.objects.get(id = post['id']).delete()
            resp['status'] = 'success'
            messages.success(request, "Student Detail has been deleted successfully.")
        except:
            resp['msg'] = 'Student Detail has failed to delete.'

    return HttpResponse(json.dumps(resp),content_type="application/json")

#Result
@login_required
def result_mgt(request):
    context['page'] = 'result_mgt'
    context['page_title'] = 'Result Management'
    
    
    return render(request,'result_mgt.html',context)

@login_required
def resultsemco(request):
    context['page'] = 'result_mgt'
    context['page_title'] = 'Result Management'
    
    return render(request,'resultsemco.html',context)
@login_required
def cosem1_r(request):
    context['page'] = 'result_mgt'
    context['page_title'] = 'Result Management'
    cursor = connection.cursor()
    cursor.execute('select distinct DIST from COSEM3')
    result=user12.objects.all()
    context['user']=result
    return render(request,'cosem1_r.html',context)
@login_required
def cosem3_R(request):
    context['page'] = 'result_mgt'
    context['page_title'] = 'Result Management'
    cursor = connection.cursor()
    cursor.execute('select distinct DIST from COSEM3')
    result=user.objects.all()
    context['user']=result
    return render(request,'cosem3_R.html',context)
@login_required
def cosem2_r(request):
    context['page'] = 'result_mgt'
    context['page_title'] = 'Result Management'
    cursor = connection.cursor()
    cursor.execute('select distinct DIST from COSEM3')
    result=user1.objects.all()
    context['user1']=result
    return render(request,'cosem2_r.html',context)
@login_required
def resultsem(request):
    context['page'] = 'result_mgt'
    context['page_title'] = 'Result Management'
   
    return render(request,'resultsem.html',context)

@login_required
def manage_result(request, pk = None):
    students = models.Student.objects.filter(status = 1).all()
    context['students'] = students
    subjects = models.Subject.objects.filter(status = 1).all()
    context['subjects'] = subjects
    if not pk is None:
        result =models.Result.objects.get(id = pk)
        marks =models.Student_Subject_Result.objects.filter(result = result)
        context['marks'] = marks
        context['result'] = result
    else:
        context['result'] = {}
        context['marks'] = {}
    return render(request, 'manage_result.html', context)

def view_result(request, pk = None):
    if not pk is None:
        result =models.Result.objects.get(id = pk)
        context['result'] = result
        marks =models.Student_Subject_Result.objects.filter(result = result)
        context['marks'] = marks
    else:
        context['result'] = {}
        context['marks'] = {}
    return render(request, 'view_result.html', context)

@login_required
def save_result(request):
    resp = { 'status':'failed', 'msg' : '' }
    if not request.method == 'POST':
        resp['msg'] = 'Request has been sent without data.'
    else:
        post = request.POST
        if post['id'] == None or post['id'] == '':
            form = forms.SaveResult(post)
        else:
            result =models.Result.objects.get(id = post['id'])
            form = forms.SaveResult(post, instance=result)
        if form.is_valid():
            form.save()
            is_new = False
            if post['id'] == '':
                rid = models.Result.objects.all().last().id
                result =models.Result.objects.get(id = rid)
                is_new = True
            else:
                rid = post['id']
            models.Student_Subject_Result.objects.filter(result = result).delete()
            has_error = False
            subjects= request.POST.getlist('subject[]')
            grade= request.POST.getlist('grade[]')
            i = 0
            for subject in subjects:
                data = {
                    'result' :rid,
                    'subject' :subject,
                    'grade' : grade[i]
                }
                form2 = forms.SaveSubjectResult(data = data)
                if form2.is_valid():
                    form2.save()
                else:
                    resp['msg'] = 'Result Detail has failed to save.'
                    for field in form2:
                        for error in field.errors:
                            resp['msg'] += str(f"<br/> [{field.name}] "+error)
                    has_error = True
                    break
                i +=1
            if has_error == False:
                resp['status'] = 'success'
                messages.success(request, "Result Detail has been saved successfully.")
            else:
                if is_new:
                    models.Result.objects.get(id = post['id']).delete()
        else:
            resp['msg'] = 'Result Detail has failed to save.'
            for field in form:
                for error in field.errors:
                    resp['msg'] += str(f"<br/> [{field.name}] "+error)
    return HttpResponse(json.dumps(resp),content_type="application/json")    

@login_required
def delete_result(request):
    resp = { 'status':'failed', 'msg' : '' }
    if not request.method == 'POST':
        resp['msg'] = 'Request has been sent without data.'
    else:
        post = request.POST
        try:
            models.Result.objects.get(id = post['id']).delete()
            resp['status'] = 'success'
            messages.success(request, "Result Detail has been deleted successfully.")
        except:
            resp['msg'] = 'result Detail has failed to delete.'

    return HttpResponse(json.dumps(resp),content_type="application/json")


def select_student_results(request):
    context['page'] = 'Select Student'
    context['page_title'] = 'Select Student'
    
  
    return render(request, 'select_student_results.html', {'user':result})

def resultsemview(request):
    
    return render(request, 'resultsemview.html')
def resultsem1(request):
    cursor = connection.cursor()
    cursor.execute('select distinct DIST from COSEM1 ')
    row = cursor.fetchall()
    result=user12.objects.all()
    return render(request, 'resultsem1.html',{'user':result})
def resultsem3(request):
    cursor = connection.cursor()
    cursor.execute('select distinct DIST from COSEM2 ')
    row = cursor.fetchall()
    result=user1.objects.all()
    return render(request, 'resultsem3.html',{'user':result})

def resultsem5(request):
    cursor = connection.cursor()
    cursor.execute('select distinct ENROLLMENT_NO from COSEM3')
    row = cursor.fetchall()
    result1=user.objects.all()
    return render(request, 'resultsem5.html',{'user':result1})
   

def list_student_result(request, pk=None):
    if pk is None:
        messages.error(request, "Invalid Student ID")
        return redirect('login')
    else:
        cursor = connection.cursor()
        cursor.execute('select distinct DIST from COSEM3')
        result=user.objects.all()
        context['user']=result
  

    return render(request, 'list_results.html', context)