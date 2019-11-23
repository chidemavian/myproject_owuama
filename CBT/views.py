# Create your views here.
from django.shortcuts import render_to_response
from django.http import  Http404, HttpResponseRedirect, HttpResponse
from myproject.CBT.forms import *
from myproject.setup.models import *
from myproject.sysadmin.models import *
from myproject.student.models import *
from myproject.CBT.models import *
from django.core.serializers.json import json
import random
from django.db.models import Max,Sum
from myproject.academics.models import *
from myproject.utilities.views import *

currse = currentsession.objects.get(id = 1)
term =tblterm.objects.get(status="ACTIVE")
term=term.term
school=School.objects.get(id =1)
ex=tblcbtexams.objects.get(status='ACTIVE')


switch=0

    



def chroose(request):
    if  "userid" in request.session:
        varuser=request.session['userid']
        return render_to_response('CBT/success.html',{'varuser':varuser})
    else:
        return HttpResponseRedirect('/login/')

def assignment(request):
    if "userid" in request.session:
        varuser=request.session['userid']
        user = userprofile.objects.get(username = varuser)
        uenter = user.createuser
        if uenter is False :
            return HttpResponseRedirect('/welcome/')

        if request.method=='POST':
            form= subform(request.POST)
            if form.is_valid():
                session=form.cleaned_data['session']
                klass=form.cleaned_data['klass']
                subject=form.cleaned_data['subject']
                user=form.cleaned_data['user']
                if tblcbtuser.objects.filter(session=session,klass=klass,user=user,subject=subject).count()==0:
                    tblcbtuser(session=session,klass=klass,subject=subject,user=user).save()
                    return HttpResponseRedirect('/cbt/set_user/subject/')

            else:
                user = tblcbtuser.objects.all()
                return render_to_response('CBT/entub.html',{'varuser':varuser,'form':form,'user':user})


        else:
            form = subform()
            user = tblcbtuser.objects.all()
            return render_to_response('CBT/entub.html',{'varuser':varuser,'form':form,'user':user})


    else:
        return HttpResponseRedirect('/login')


# Wrapper to make a view handle both normal and api request
def json_view(func):
    def wrap(req, *args, **kwargs):
        resp = func(req, *args, **kwargs)
        if isinstance(resp, HttpResponse):
            return resp
        return HttpResponse(json.dumps(resp), mimetype="application/json")

    return wrap

@json_view
def autocomplete(request):
    term = request.GET.get('term')
    gset = userprofile.objects.filter(username__contains = term)[:10]
    suggestions = []
    for i in gset:
        suggestions.append({'label': '%s :: %s' % (i.username,i.staffname), 'username': i.username})
    return suggestions



def getcbtklass(request):
    if  "userid" in request.session:
        if request.is_ajax():
            if request.method == 'POST':
                varuser = request.session['userid']
                varerr =""
                post = request.POST.copy()
                acccode = post['userid']
                kk = []
                sdic = {}
                data = Class.objects.filter(klass__startswith = acccode).order_by('id')
                for j in data:
                    j = j.klass
                    kk.append(j)

                return HttpResponse(json.dumps(kk), mimetype='application/json')
            else:
                gdata = ""
                return render_to_response('index.html',{'gdata':gdata})
        else:

            gdata = ""
            return render_to_response('getlg.htm',{'gdata':gdata})
    else:
        return HttpResponseRedirect('/login/')


def getscheduledsubject(request):
    if  "userid" in request.session:
        if request.is_ajax():
            if request.method == 'POST':
                varuser = request.session['userid']
                varerr =""
                post = request.POST.copy()
                acccode = post['userid']
                klass,exam,term,subject=acccode.split(':')
                data = tblcbtsubject.objects.filter(klass=klass,exam_type=exam,term=term).order_by('id')

                return render_to_response('CBT/schedule.html',{'sub':data})
            else:
                gdata = ""
                return render_to_response('index.html',{'gdata':gdata})
        else:

            gdata = ""
            return render_to_response('getlg.htm',{'gdata':gdata})
    else:
        return HttpResponseRedirect('/login/')



def getassessment(request):
    if  "userid" in request.session:
        if request.is_ajax():
            if request.method == 'POST':
                varuser = request.session['userid']
                varerr =""
                post = request.POST.copy()
                acccode = post['userid']
                kk = []
                data = tblcbtexams.objects.filter(status='ACTIVE').order_by('id')
                for j in data:
                    j = j.exam_type
                    kk.append(j)

                return HttpResponse(json.dumps(kk), mimetype='application/json')
            else:
                gdata = ""
                return render_to_response('index.html',{'gdata':gdata})
        else:

            gdata = ""
            return render_to_response('getlg.htm',{'gdata':gdata})
    else:
        return HttpResponseRedirect('/login/')



def getcbtsub(request):
    if  "userid" in request.session:
        if request.is_ajax():
            if request.method == 'POST':
                varuser = request.session['userid']
                varerr =""
                post = request.POST.copy()
                acccode = post['userid']
                kk = []
                data = Subject.objects.filter(category=acccode).order_by('id')
                for j in data:
                    j = j.subject
                    kk.append(j)

                return HttpResponse(json.dumps(kk), mimetype='application/json')
            else:
                gdata = ""
                return render_to_response('index.html',{'gdata':gdata})
        else:

            gdata = ""
            return render_to_response('getlg.htm',{'gdata':gdata})
    else:
        return HttpResponseRedirect('/login/')



def cbtstat(request):
    if "userid" in request.session:
        varuser= request.session['userid']
        if request.method=='POST':
            form=formactive(request.POST)
            if form.is_valid():
                session=form.cleaned_data['session']
                klass=form.cleaned_data['sfrom']
                subject=form.cleaned_data['subject']
                to=form.cleaned_data['sto']
                term=form.cleaned_data['term']
                exam=form.cleaned_data['exam_type']
                fromklass,ss=klass.split(' ')
                toklass,sp=to.split(' ')
                dif = int(sp)-int(ss)
                one=[klass, to]
                two = ['JS 1', 'JS 2', 'JS 3']

                if dif == 0:
                    try:
                        tblcbtsubject.objects.get(session=session,klass=klass,
                            exam_type=exam,term=term,
                            status='ACTIVE',subject=subject)
                    except:
                        tblcbtsubject(session=session,klass=klass,
                            exam_type=exam,term=term,
                            status='ACTIVE', duration = '45',subject=subject).save()

                elif dif == 1:
                    for k in one:
                        try:

                            tblcbtsubject.objects.get(session=session,klass=k,
                                exam_type=exam,term=term,
                                status='ACTIVE',subject=subject)
                        except:
                            tblcbtsubject(session=session,klass=k,
                              exam_type=exam,term=term,
                              status='ACTIVE', duration = '45',subject=subject).save()


                elif dif == 2:
                    for k in two:
                        try:

                            tblcbtsubject.objects.get(session=session,klass=k,
                                exam_type=exam,term=term,
                                status='ACTIVE',subject=subject)
                        except:
                            tblcbtsubject(session=session,klass=k,
                              exam_type=exam,term=term,
                              status='ACTIVE', duration = '45',subject=subject).save()
            else:
                return HttpResponseRedirect('/cbt/schedulling/active/')
        else:
            form = formactive()
        return render_to_response('CBT/active.html',{'varuser':varuser,'form':form})
	
    else:
		return HttpResponseRedirect('/login')

def qstn(request):
    if 'userid' in request.session:
        varuser = request.session['userid']
        if request.method=='POST':
            form = qstnform(request.POST, request.FILES)
            if form.is_valid():
                session=form.cleaned_data['session']
                klass=form.cleaned_data['klass']
                term=form.cleaned_data['term']
                subject=form.cleaned_data['subject']
                exam_type=form.cleaned_data['exam_type']
                question=form.cleaned_data['question']
                rfile=form.cleaned_data['pix']

                if rfile is None:
                    pix = '/ax/image'
                else:
                    pix = request.FILES['pix']

                data = tblquestion(instruction_to=  'instruction',session=session,
                    klass=klass,section='A',term=term,subject=subject,
                    exam_type=  exam_type,qstn =question,
                    topic='topic', image=pix).save()
                err= 'question saved successfully'
            else:
                err = 'spaces left not filled'
        else:
            form = qstnform()
            err=''
        return render_to_response('CBT/qstn.html',{'varuse':varuser,'form':form,'qstn':qstn,'err':err})
    else:
        return HttpResponseRedirect('/login')


def editcbtqst(request):
    if  "userid" in request.session:
        if request.is_ajax():
            if request.method == 'POST':
                varuser = request.session['userid']
                varerr =""
                post = request.POST.copy()
                acccode = post['userid']
                state=acccode
                getdetails=[]
                details = tblquestion.objects.get(id = state)

                try:

                    options=tbloptions.objects.get(qstn=details)
                except:

                    options=''

                try:
                    answer= tblans.objects.get(qstn=details)

                except:
                     answer=''
                dicdetails={'options':options,'question':details,'answer':answer}
                return render_to_response('CBT/viewimage.html',{'getdetails':dicdetails,'state':options})
            else:
                gdata = ""
                return render_to_response('index.html',{'gdata':gdata})
        else:

            getdetails = tblcontents.objects.filter(topic=id)
            return render_to_response('lesson/entersub.html',{'gdata':getdetails})
    else:
        return HttpResponseRedirect('/login/')



def editcbtpix(request):
    if  "userid" in request.session:
        if request.is_ajax():
            if request.method == 'POST':
                varuser = request.session['userid']
                varerr =""
                post = request.POST.copy()
                acccode = post['userid']
                state=acccode
                getdetails=[]
                details = tblquestion.objects.get(id = state)

                try:

                    options=tbloptions.objects.get(qstn=details)
                except:

                    options=''

                try:
                    answer= tblans.objects.get(qstn=details)

                except:
                     answer=''
                dicdetails={'options':options,'question':details,'answer':answer}
                return render_to_response('CBT/putimage.html',{'getdetails':dicdetails,'state':options})
            else:
                gdata = ""
                return render_to_response('index.html',{'gdata':gdata})
        else:

            getdetails = tblcontents.objects.filter(topic=id)
            return render_to_response('lesson/entersub.html',{'gdata':getdetails})
    else:
        return HttpResponseRedirect('/login/')








def getcbtqst(request):
    if  "userid" in request.session:
        if request.is_ajax():
            if request.method == 'POST':
                varuser = request.session['userid']
                varerr =""
                post = request.POST.copy()
                acccode = post['userid']
                state=acccode
                session,term,klass,subject,exam_type= acccode.split(':')
                myqst=[]
                myqst=tblquestion.objects.filter(session=session,
                	term=term,
                	klass=klass,
                	subject=subject,
                	exam_type=exam_type).order_by('klass')

                return render_to_response('CBT/myqst.html',{'myqst':myqst,
                'term':term,'subject':subject,'exam':exam_type,'klass':klass,'session':session})
        else:

            gdata = ""
            return render_to_response('getlg.htm',{'gdata':gdata})
    else:
        return HttpResponseRedirect('/login/')



def optajax(request):
        if  "userid" in request.session:
            if request.is_ajax():
                if request.method == 'POST':
                    varuser = request.session['userid']
                    varerr =""
                    post = request.POST.copy()
                    acccode = post['userid']
                    state=acccode

                    getdetails=[]


                    details = tblquestion.objects.get(id = state)

                    try:

                        options=tbloptions.objects.get(qstn=details)

                        # answer= tblans.objects.get(qstn=details)

                    except:

                        options=''

                    try:
                        answer= tblans.objects.get(qstn=details)

                    except:
                         answer=''
                        
                    dicdetails={'options':options,'question':details,'answer':answer}

                    return render_to_response('CBT/enteropt.html',{'getdetails':dicdetails,'state':options})
                    # return render_to_response('CBT/enteropt.html',{'getdetails':getdetails,'state':options})
                else:
                    gdata = ""
                    return render_to_response('index.html',{'gdata':gdata})
            else:

                getdetails = tblcontents.objects.filter(topic=id)
                return render_to_response('lesson/entersub.html',{'gdata':getdetails})
        else:
            return HttpResponseRedirect('/login/')


def chooseopt(request):
    if  "userid" in request.session:
        if request.is_ajax():
            if request.method == 'POST':
                varuser = request.session['userid']
                varerr =""
                post = request.POST.copy()
                acccode = post['userid']
                state=acccode
            
                getdetails=[]
                details = tblquestion.objects.get(id = state)

                if tbloptions.objects.filter(qstn=details).count()> 0:
                    options=tbloptions.objects.get(qstn=details)
                    answer= tblans.objects.get(qstn=details)

                    dicdetails={'options':options,'question':details,'answer':answer}                    
                    return render_to_response('CBT/enteroption.html',{'getdetails':dicdetails,})
                     
                else:
                    return render_to_response('CBT/choose.html',{'state':state})
    else:
        return HttpResponseRedirect('/login/')









def doentry(request):
        if  "userid" in request.session:
            if request.is_ajax():
                if request.method == 'POST':
                    varuser = request.session['userid']
                    varerr =""
                    post = request.POST.copy()
                    acccode = post['userid']
                    state=acccode
                    getdetails=[]
                    details = tblquestion.objects.get(id = state)
                    try:

                        options=tbloptions.objects.get(qstn=details)

                    except:

                        options=''

                    try:
                        answer= tblans.objects.get(qstn=details)

                    except:
                         answer=''          
                    dicdetails={'options':options,'question':details,'answer':answer}

            return render_to_response('CBT/edditall.html',{'getdetails':dicdetails,'state':options})
        else:
            return HttpResponseRedirect('/login/')


def sdfgsf(request):
        if  "userid" in request.session:
            if request.is_ajax():
                if request.method == 'POST':
                    varuser = request.session['userid']
                    varerr =""
                    post = request.POST.copy()
                    acccode = post['userid']
                    state=acccode
                    getdetails=[]
                    details = tblquestion.objects.get(id = state)
                    try:

                        options=tbloptions.objects.get(qstn=details)

                    except:

                        options=''

                    try:
                        answer= tblans.objects.get(qstn=details)

                    except:
                         answer=''          
                    dicdetails={'options':options,'question':details,'answer':answer}

            return render_to_response('CBT/editimagedialog.html',{'getdetails':dicdetails,'state':options})
        else:
            return HttpResponseRedirect('/login/')








def editqst(request):
        if  "userid" in request.session:
            if request.is_ajax():
                if request.method == 'POST':
                    varuser = request.session['userid']
                    varerr =""
                    post = request.POST.copy()
                    acccode = post['userid']
                    state=acccode

                    getdetails=[]


                    details = tblquestion.objects.get(id = state)

                    try:

                        options=tbloptions.objects.get(qstn=details)

                        # answer= tblans.objects.get(qstn=details)

                    except:

                        options=''

                    try:
                        answer= tblans.objects.get(qstn=details)

                    except:
                         answer=''

                        
                    dicdetails={'options':options,'question':details,'answer':answer}


                    # getdetails=getdetails.append(dicdetails)


                    return render_to_response('CBT/editqst.html',{'getdetails':dicdetails,'state':options})
                    
                else:
                    gdata = ""
                    return render_to_response('index.html',{'gdata':gdata})
            else:

                getdetails = tblcontents.objects.filter(topic=id)
                return render_to_response('lesson/entersub.html',{'gdata':getdetails})
        else:
            return HttpResponseRedirect('/login/')

def changeqst(request,vid):
    if  "userid" in request.session:
        varuser = request.session['userid']
        getdetails = tblquestion.objects.get(id = vid)
        if request.method == 'POST':
            question = request.POST['question']
            if question == '':
                return HttpResponseRedirect ('/cbt/edit')
            getdetails.qstn = question
            getdetails.save()
            return HttpResponseRedirect('/cbt/edit/')

    else:
        return HttpResponseRedirect('/login/')

def editoptiona(request):
        if  "userid" in request.session:
            if request.is_ajax():
                if request.method == 'POST':
                    varuser = request.session['userid']
                    varerr =""
                    post = request.POST.copy()
                    acccode = post['userid']
                    state=acccode
                    getdetails=[]
                    details = tblquestion.objects.get(id = state)
                    ans= tbloptions.objects.filter(qstn=details).count()
                    if ans==0:
                        myans = tbloptioni.objects.get(qstn=details)
                    else:
                        myans = tbloptions.objects.get(qstn=details)
                    getdetails={'options':myans.a,'question':details}
                    return render_to_response('CBT/editoptiona.html',{'getdetails':getdetails})
                    
        else:
            return HttpResponseRedirect('/login/')

def optiona(request,vid):
    if  "userid" in request.session:
        varuser = request.session['userid']
        getdetails = tblquestion.objects.get(id = vid)
        answers=tblans.objects.get(qstn=getdetails)
        boxoption = tbloptions.objects.get(qstn=getdetails)
        if request.method == 'POST':
            optiona = request.POST['optiona']
            if optiona == '':
                return HttpResponseRedirect ('/cbt/edit')

            if answers.ans == boxoption.a:
                boxoption.a = optiona,
                answers.ans = optiona
                answers.save()
                boxoption.save()
            else:
                boxoption.a = optiona
                boxoption.save()

        return HttpResponseRedirect('/cbt/edit/')

    else:
        return HttpResponseRedirect('/login/')



def optionb(request,vid):
    if  "userid" in request.session:
        varuser = request.session['userid']
        getdetails = tblquestion.objects.get(id = vid)
        answers=tblans.objects.get(qstn=getdetails)
        boxoption = tbloptions.objects.get(qstn=getdetails)
        if request.method == 'POST':
            optionb = request.POST['optionb']
            if optionb == '':
                return HttpResponseRedirect ('/cbt/edit')

            if answers.ans == boxoption.b:
                boxoption.b = optionb,
                answers.ans = optionb
                answers.save()
                boxoption.save()
            else:
                boxoption.b = optionb
                boxoption.save()

        return HttpResponseRedirect('/cbt/edit/')

    else:
        return HttpResponseRedirect('/login/')




def optionc(request,vid):
    if  "userid" in request.session:
        varuser = request.session['userid']
        getdetails = tblquestion.objects.get(id = vid)
        answers=tblans.objects.get(qstn=getdetails)
        boxoption = tbloptions.objects.get(qstn=getdetails)
        if request.method == 'POST':
            optionc = request.POST['optionc']
            if optionc == '':
                return HttpResponseRedirect ('/cbt/edit')

            if answers.ans == boxoption.c:
                boxoption.c = optionc,
                answers.ans = optionc
                answers.save()
                boxoption.save()
            else:
                boxoption.c = optionc
                boxoption.save()

        return HttpResponseRedirect('/cbt/edit/')

    else:
        return HttpResponseRedirect('/login/')


def optiond(request,vid):
    if  "userid" in request.session:
        varuser = request.session['userid']
        getdetails = tblquestion.objects.get(id = vid)
        answers=tblans.objects.get(qstn=getdetails)
        boxoption = tbloptions.objects.get(qstn=getdetails)
        if request.method == 'POST':
            optiond = request.POST['optiond']
            if optiond == '':
                return HttpResponseRedirect ('/cbt/edit')

            if answers.ans == boxoption.d:
                boxoption.d = optiond,
                answers.ans = optiond
                answers.save()
                boxoption.save()
            else:
                boxoption.d = optiond
                boxoption.save()

        return HttpResponseRedirect('/cbt/edit/')

    else:
        return HttpResponseRedirect('/login/')




def chngqstimage(request,vid):
    if "userid" in request.session:
            if request.method=='POST':
                if request.FILES:
                    a=request.FILES['qstimagefile']
                    if a=='':
                        return HttpResponseRedirect('/cbt/edit/')                        
                    qst=tblquestion.objects.get(id=vid)
                    a='questions/'+str(a)
                    qst.image=a
                    qst.save()

            return HttpResponseRedirect('/cbt/edit/')
    else:
        return HttpResponseRedirect('/login/')



def editoptionb(request):
        if  "userid" in request.session:
            if request.is_ajax():
                if request.method == 'POST':
                    varuser = request.session['userid']
                    varerr =""
                    post = request.POST.copy()
                    acccode = post['userid']
                    state=acccode
                    getdetails=[]
                    details = tblquestion.objects.get(id = state)
                    ans= tbloptions.objects.filter(qstn=details).count()
                    if ans==0:
                        myans = tbloptioni.objects.get(qstn=details)
                    else:
                        myans = tbloptions.objects.get(qstn=details)
                    getdetails={'options':myans.b,'question':details}
                    return render_to_response('CBT/editoptionb.html',{'getdetails':getdetails})
                    
        else:
            return HttpResponseRedirect('/login/')


def editoptionc(request):
        if  "userid" in request.session:
            if request.is_ajax():
                if request.method == 'POST':
                    varuser = request.session['userid']
                    varerr =""
                    post = request.POST.copy()
                    acccode = post['userid']
                    state=acccode
                    getdetails=[]
                    details = tblquestion.objects.get(id = state)
                    ans= tbloptions.objects.filter(qstn=details).count()
                    if ans==0:
                        myans = tbloptioni.objects.get(qstn=details)
                    else:
                        myans = tbloptions.objects.get(qstn=details)
                    getdetails={'options':myans.c,'question':details}
                    return render_to_response('CBT/editoptionc.html',{'getdetails':getdetails})
                    
        else:
            return HttpResponseRedirect('/login/')


def editoptiond(request):
        if  "userid" in request.session:
            if request.is_ajax():
                if request.method == 'POST':
                    varuser = request.session['userid']
                    varerr =""
                    post = request.POST.copy()
                    acccode = post['userid']
                    state=acccode
                    getdetails=[]
                    details = tblquestion.objects.get(id = state)
                    ans= tbloptions.objects.filter(qstn=details).count()
                    if ans==0:
                        myans = tbloptioni.objects.get(qstn=details)
                    else:
                        myans = tbloptions.objects.get(qstn=details)
                    getdetails={'options':myans.d,'question':details}
                    return render_to_response('CBT/editoptiond.html',{'getdetails':getdetails})
                    
        else:
            return HttpResponseRedirect('/login/')




def myoptions(request,vid):
    if "userid" in request.session:
        varuser=request.session['userid']
        if 'option' in request.POST:
            if request.method=='POST':
                a=request.POST['optiona']
                b=request.POST['optionb']
                c=request.POST['optionc']
                d=request.POST['optiond']
                if a=='' or b=='' or c=='' or d=='':
                    g='na me be this?'
                    return HttpResponseRedirect('/cbt/options/')
                qst=tblquestion.objects.get(id=vid)
                tbloptions(a=a,b=b,c=c,d=d,e='non of the above',qstn=qst).save()
                option = request.POST['option']
                if option=='A':
                    tblans(ans =a,option=option,qstn=qst).save()
                elif option=='B':
                    tblans(ans =b,option=option,qstn=qst).save()
                elif option=='C':
                    tblans(ans =c,option=option,qstn=qst).save()
                elif option=='D':
                    tblans(ans =d,option=option,qstn=qst).save()
                g= 'my name is mathew'
                return HttpResponseRedirect('/cbt/options/')# 

            else:
                return HttpResponseRedirect('/login/')
        else:
            f = 'my name is black'
            return HttpResponseRedirect('/cbt/options/')
    else:
        return HttpResponseRedirect('/login/')


def cbtimage(request,vid):
    if 'userid' in request.session:
        if request.method=='POST':
            if request.FILES:
                a=request.FILES['filetoupload']
                qt = tblquestion.objects.get(id=vid)
                qt.image=a
                qt.save()
        return HttpResponseRedirect('/cbt/enter/question/')
    else:
        return HttpResponseRedirect('/login/')


def myoptionsimage(request,vid):
    if "userid" in request.session:
            if request.method=='POST':
                if request.FILES:                
                    if 'option' in request.POST:
                        a=request.FILES['filea']
                        b=request.FILES['fileb']
                        c=request.FILES['filec']
                        d=request.FILES['filed']
                        option = request.POST['option']

                        if a=='' or b=='' or c=='' or d=='':
                            return HttpResponseRedirect('/cbt/options/')
                        
                        qst=tblquestion.objects.get(id=vid)
                        
                        tbloptioni(a=a,b=b,c=c,d=d,e='non of the above',qstn=qst).save()

                        a='questions/'+str(a)
                        b='questions/'+str(b)
                        c='questions/'+str(c)
                        d='questions/'+str(d)

                        if option=='A':
                            tblans(ans =a,option=option,qstn=qst).save()
                        elif option=='B':
                            tblans(ans =b,option=option,qstn=qst).save()
                        elif option=='C':
                            tblans(ans =c,option=option,qstn=qst).save()
                        elif option=='D':
                            tblans(ans =d,option=option,qstn=qst).save()
            return HttpResponseRedirect('/cbt/options/')
    else:
        return HttpResponseRedirect('/login/')




def cbtimage(request,vid):
    if 'userid' in request.session:
        if request.method=='POST':
            if request.FILES:
                a=request.FILES['filetoupload']
                qt = tblquestion.objects.get(id=vid)
                qt.image=a
                qt.save()
        return HttpResponseRedirect('/cbt/enter/question/')
    else:
        return HttpResponseRedirect('/login/')


def editquestion(request):
    if  "userid" in request.session:
        if request.is_ajax():
            if request.method == 'POST':
                varuser = request.session['userid']
                varerr =""
                post = request.POST.copy()
                acccode = post['userid']
                # state=acccode
                session,term,klass,subject,exam_type= acccode.split(':')
                sublist=[]
                myqst=tblquestion.objects.filter(session=session,
                    term=term,
                    klass=klass,
                    subject=subject,
                    exam_type=exam_type).order_by('klass')
                if myqst.count()==0:
                    varerr = 'NO QUESTIONS ENTERED'
                    return render_to_response('CBT/myopt.html',{'varerr':varerr})
                else:
                    for j in myqst:    
                        k = tbloptions.objects.filter(qstn=j).count()
                        if k == 0:
                            k = tbloptioni.objects.filter(qstn=j)
                            img='hi'
                        else:
                            k = tbloptions.objects.filter(qstn=j)
                            img='low'

                        intr= {'question':j,'options':k, 'image':img}
                        sublist.append(intr)
                return render_to_response('CBT/myedit.html',{'sublist':sublist})
        else:
            return HttpResponseRedirect('/login/')
    else:
        return HttpResponseRedirect('/login/')




def getcbtopt(request):
    if  "userid" in request.session:
        if request.is_ajax():
            if request.method == 'POST':
                varuser = request.session['userid']
                varerr =""
                post = request.POST.copy()
                acccode = post['userid']
                # state=acccode
                session,term,klass,subject,exam_type= acccode.split(':')
                sublist=[]


                myqst=tblquestion.objects.filter(session=session,
                	term=term,
                	klass=klass,
                	subject=subject,
                	exam_type=exam_type)

                if myqst.count()==0:
                	varerr = 'NO QUESTIONS ENTERED'
                	return render_to_response('CBT/myopt.html',{'varerr':varerr})

                else:

                    for j in myqst:    
                        k = tbloptions.objects.filter(qstn=j).count()
                        if k == 0:
                            k = tbloptioni.objects.filter(qstn=j)
                            img='hi'
                        else:
                            k = tbloptions.objects.filter(qstn=j)
                            img='low'

                        intr= {'question':j,'options':k, 'image':img}
                        sublist.append(intr)
                return render_to_response('CBT/myopt.html',{'sublist':sublist,})
        else:
            return HttpResponseRedirect('/login/')
    else:
        return HttpResponseRedirect('/login/')




        
def options(request):
    if "userid" in request.session:
        varuser=request.session['userid']
        form= qstnform
        qst = tblquestion.objects.all()
        return render_to_response('CBT/options.html',{'varuser':varuser,'form':form,'qst':qst})
    else:
        return HttpResponseRedirect('/login')


def editq(request):
    if "userid" in request.session:
        varuser=request.session['userid']
        form= qstnform
        qst = tblquestion.objects.all()
        return render_to_response('CBT/edit.html',{'varuser':varuser,'form':form,'qst':qst})
    else:
        return HttpResponseRedirect('/login')



def theory(request):
    if "userid" in request.session:
        varuser=request.session['userid']
        if request.method=='POST':
            form=qstnform(request.POST)
            if form_is.is_valid():
                session=form.cleaned_data['session']
                term=form.cleaned_data['term']
                klass=form.cleaned_data['klass']
                exam_type=form.cleaned_data['exam_type']
                subject=form.cleaned_data['subject']
                return HttpResponseRedirect('/cbt/enter/theory/')
        else:
            form = qstnform()
        return render_to_response('CBT/theory.html',{'varuser':varuser,'form':form})

    else:
        return HttpResponseRedirect('/login/')




def markguide(request):
    if "userid" in request.session:
        varuser=request.session['userid']
        form= qstnform
        qst = tblquestion.objects.all()
        return render_to_response('CBT/markguide.html',{'varuser':varuser,'form':form,'qst':qst})
    else:
        return HttpResponseRedirect('/login')



def clear(request):
    if "userid" in request.session:
        if request.method=='POST':            
            varuser=request.session['userid']
            student=Student.objects.get(admitted_session=currse, fullname=varuser,gone=False)
            session=student.admitted_session
            cbttrans.objects.filter(student=student, 
                term=term,session=session,exam_type=ex.exam_type,subject='BASIC SCIENCE').delete()

            cbtcurrentquestion.objects.filter(student=student,
                session=currse,term=term,exam_type=ex.exam_type,subject='BASIC SCIENCE').delete()
            cbtold.objects.filter(student=student,session=currse,term=term,
                exam_type=ex.exam_type,subject='BASIC SCIENCE').delete()

            return HttpResponseRedirect('/welcome/')
        else:
            return HttpResponseRedirect('/login/')
    else:
        return HttpResponseRedirect('/login/')


def pupilcbt(request):
    if "userid" in request.session:
        if request.method=='POST':
            varuser=request.session['userid']
            student=Student.objects.get(admitted_session=currse, fullname=varuser,gone=False) 


            now_scheduled= scheduled.objects.get(student=student,term=term,assessment=ex.exam_type,session=currse)

            subject=now_scheduled.subject
            # sublist=[]

###****************8 First error***************  

            fq=cbtcurrentquestion.objects.filter(student=student,
                session=currse,
                term=term,
                subject=subject,
                exam_type=ex.exam_type).count()

            if fq==0: #student just starting exam or i am done

##COLLECTING ANSWERED QUESTIONS BY ID
                trans=cbttrans.objects.filter(session=currse,
                    exam_type=ex.exam_type,
                    student=student, #or student.id 
                    subject=subject,
                    term=term)
                nu=cbttrans.objects.filter(session=currse,
                    exam_type=ex.exam_type,
                    student=student, #or student.id 
                    subject=subject,
                    term=term).count()
                transid=[]
                for k in trans:
                    fb= k.qstcode.split('-')[0]
                    fb=int(fb)   
                    transid.append(fb)

##COLLECTING ENTERED QUESTIONS BY ID
                qstns=tblquestion.objects.filter(term=term, 
                    exam_type=ex.exam_type, 
                    session=currse,
                    subject=subject,
                    klass=student.admitted_class)#student.admitted_class
                myq=[]               
                for q in qstns:
                    myq.append(q.id)


##SORTING OUT UNIQUE QUESTIONS
                qu=[]
                qu= [item for item in myq  if item not in transid]


                if qu == []:

                    return render_to_response('CBT/done.html')


##PICKING A RANDOM UNIQUE QUESTION BY ID
                uid = 0
                uid = random.choice(qu)
                tk=0
                
                tk = tblquestion.objects.get(id=uid)

                cbtold(session=currse,
                    question=tk,
                    term=q.term,
                    exam_type=q.exam_type,
                    klass=student.admitted_class,
                    subject=subject,
                    student=student,
                    qstcode=tk.id).save()       

                tk1 =tk.qstn

                k = tbloptions.objects.filter(qstn=tk).count()
                if k == 0:
                    opt = tbloptioni.objects.filter(qstn=tk)
                    image='hi'
                else:
                    opt = tbloptions.objects.filter(qstn=tk)
                    image='low'


                img=tk.image
                ans=''

                number=nu + 1
                cbtcurrentquestion(student=student,
                    term = term,
                    session=currse,
                    subject=subject,
                    exam_type=ex.exam_type,
                    number=number).save()
                
                number=number



            elif fq==1:
                fq=cbtcurrentquestion.objects.get(student=student,
                    session=currse,
                    term=term,
                    subject=subject,
                    exam_type=ex.exam_type,)

                number=int(fq.number)
                
                try:
                    mqst =cbttrans.objects.get(student=student,session=currse,
                        term=term,
                        exam_type=ex.exam_type,
                        subject=subject,
                        no=number)

                    ans=mqst.stu_ans

                    tk = tblquestion.objects.get(term=term, 
                        exam_type=ex.exam_type, 
                        session=currse,
                        subject=subject,
                        klass=student.admitted_class,
                        id=mqst.qstcode)

                    tk1 =tk.qstn
                    img=tk.image

                    k = tbloptions.objects.filter(qstn=tk).count()
                    if k == 0:
                        opt = tbloptioni.objects.filter(qstn=tk)
                        image='hi'
                    else:
                        opt = tbloptions.objects.filter(qstn=tk)
                        image='low'
                    
                    uid= tk.id

                except:

                    mqst =cbtold.objects.get(student=student,session=currse,
                        term=term,
                        exam_type=ex.exam_type,
                        subject=subject,
                        klass=student.admitted_class)

                    ans=''

                    tk = tblquestion.objects.get(term=term, 
                        exam_type=ex.exam_type, 
                        session=currse,
                        subject=subject,
                        klass=student.admitted_class,
                        id=mqst.qstcode)

                    tk1 =tk.qstn
                    img=tk.image

                    k = tbloptions.objects.filter(qstn=tk).count()
                    if k == 0:
                        opt = tbloptioni.objects.filter(qstn=tk)
                        image='hi'
                    else:
                        opt = tbloptions.objects.filter(qstn=tk)
                        image='low'
                    
                    uid= tk.id
                    

            return render_to_response('CBT/pupiltest.html',{'question':tk1,
                'school':school,
                'count':number,
                'image':img,
                'pos':image,
                'ans':ans,
                'form':student,
                'session':currse,
                'name':student.fullname,
                'klass':student.admitted_class,
                'adm':student.admissionno,
                'options':opt,
                'term':term,
                'uid':uid,
                'subject':subject})



        else:
            return HttpResponseRedirect('/login/')
    else:
        return HttpResponseRedirect('/login/')



def guides(request):
    if  "userid" in request.session:
        if request.is_ajax():
            if request.method == 'POST':
                varuser = request.session['userid']
                varerr =""
                post = request.POST.copy()
                acccode = post['userid']
                state=acccode
                session,term,klass,subject,exam_type= acccode.split(':')
                qst=[]
                myqst=tblquestion.objects.filter(session=session,
                    term=term,
                    klass=klass,
                    subject=subject,
                    exam_type=exam_type).order_by('klass')

                for q in myqst:
                    try:
                        myanswer = tblans.objects.get(qstn=q)
                        myanswer=myanswer.option
                    except:
                        myanswer='No Ans'
                    pair={'qst':q,'answer':myanswer}
                    qst.append(pair)

                # a,b = divmod(qst,15)


                return render_to_response('CBT/myguide.html',{'myqst':qst,
                'term':term,'subject':subject,'exam':exam_type,'klass':klass,'session':session})
        else:

            gdata = ""
            return render_to_response('getlg.htm',{'gdata':gdata})
    else:
        return HttpResponseRedirect('/login/')
















def getcbtsubject(request):
    if  "userid" in request.session:
        if request.is_ajax():
            if request.method == 'POST':
                varuser = request.session['userid']
                varerr =""
                post = request.POST.copy()
                acccode = post['userid']
                session,klass = acccode.split(':')
                kk = []
                sdic = {}
                data = tblcbtuser.objects.filter(session=session,klass = klass,user = varuser )
                for j in data:
                    j = j.subject
                    #print j
                    s = {j:j}
                    sdic.update(s)
                klist = sdic.values()
                for p in klist:
                   # print 'The Subject :',p
                    kk.append(p)
                return HttpResponse(json.dumps(kk), mimetype='application/json')
            else:
                gdata = ""
                return render_to_response('index.html',{'gdata':gdata})
        else:

            gdata = ""
            return render_to_response('getlg.htm',{'gdata':gdata})
    else:
        return HttpResponseRedirect('/login/')

def ajaxclass(request):
    if  "userid" in request.session:
        if request.is_ajax():
            if request.method == 'POST':
                varuser = request.session['userid']
                varerr =""
                post = request.POST.copy()
                acccode = post['userid']
                # state = acccode
                kk = []
                sdic = {}
                data = tblcbtuser.objects.filter(user = varuser,session = acccode).order_by('klass')
                for j in data:
                    j = j.klass
                    s = {j:j}
                    sdic.update(s)
                klist = sdic.values()
                for p in klist:
                    kk.append(p)
                return HttpResponse(json.dumps(kk), mimetype='application/json')
            else:
                gdata = ""
                return render_to_response('index.html',{'gdata':gdata})
        else:

            gdata = ""
            return render_to_response('getlg.htm',{'gdata':gdata})
    else:
        return HttpResponseRedirect('/login/')


def exxxam(request):

## A SUBJECT MUST BE SCHEDULLED BEFORE IT CAN BE AVAILABLE FOR WRITITING
    if "userid" in request.session:

        varuser=request.session['userid']


#current student
        pop =Student.objects.get(fullname=varuser,admitted_session=currse,gone=False)

       
##current essessment
        exam=tblcbtexams.objects.get(status='ACTIVE')
        exam=exam.exam_type


##current term
        term=tblterm.objects.get(status='ACTIVE')
        term=term.term

## STUDEnT subject list
        akrec = StudentAcademicRecord.objects.get(student=pop,term=term)
        subs = SubjectScore.objects.filter(academic_rec=akrec,term=term)
        subb=[]
        for mys in subs:
            mys=mys.subject
            subb.append(mys)

        
##currently scheduled subjects
        mysub =[]   
        activesub = tblcbtsubject.objects.filter(session=currse,klass=pop.admitted_class,term=term)
        for k in activesub:
            k=k.subject
            mysub.append(k)


##currently written subjects
        donsub=donesubjects.objects.filter(student=pop,exam_type=exam,term=term,session=currse)
        don =[] 
        for dd in donsub:
            dd=dd.subject
            don.append(dd)


#SCHEDULED  BUT NOT WRITTEN
        qu= [item for item in mysub if item not in don] 

        if qu == []:
            msg= 'HELLOssssss NO EXAMS SCHEDULED FOR YOU. CONTACT THE ADMIN'
            return render_to_response('CBT/nosub.html',{'varerr':msg})

#ACTIVATED  AND AvIALABLE TO BE WRITTEN 
        qp= [item for item in subb if item in qu]
        if qp == []:
            msg= 'HELLOpppppp NO EXAMS SCHEDULED FOR YOU. CONTACT THE ADMIN'
            return render_to_response('CBT/nosub.html',{'varerr':msg})

#subjects with questions
        stqst = []
        qsts = tblquestion.objects.filter(session=pop.admitted_session,
            klass=pop.admitted_class,term=term,exam_type=exam,section ='A')
        for ks in qsts:
            sub = ks.subject
            stqst.append(sub)

        qpick= [item for item in stqst if item in qp]
        if qpick == []:
            msg= 'NO QUESTIONS FOUND'
            return render_to_response('CBT/nosub.html',{'varerr':msg})



#NOW SCHEDULLED
        qpick=qpick[0]

#KEEPING A SAFE OF NOW SCHEDULLED
        try:
            now_schedulled = scheduled.objects.get(student=pop, term=term,assessment=exam,session=pop.admitted_session)
        except:
            scheduled(student=pop,session=pop.admitted_session,term=term,assessment=exam,subject=qpick).save()


#CASE 1. CHECK ACCREDITATION TABLE FOR CODE(OCCIRRENCE)
#IF ITS FOUND, ASK USER OF IT



#CASE2:
#ELLSE, GENERATE A RANDOM NO, SAVE IT AND REDIRECT TO ANOTHER PAGE 
#WHERE DJANGO WILL DEMAND FOR IT

#GENERATE ACCREDITATION COD FOR THIS EXAM 
#AND KEEP IT SAFE



        return render_to_response('CBT/cbt.html',{'term':term,
            'varuser':varuser,
            'sch':school,
            'sub':activesub,
            'subw':donsub,
            'qu':qu,
            'qp':qp,
            'qpick':qpick,
            'subb':subb,
            'pop':pop,'exam':exam})

    else:
		return HttpResponseRedirect('/login/')



def beefore(request):
    if "userid" in request.session:
        if request.method=='POST':
            varuser=request.session["userid"]
            student= Student.objects.get(fullname=varuser,admitted_session=currse,gone=False)

            now_scheduled= scheduled.objects.get(student=student,term=term,assessment=ex.exam_type,session=currse)
            subject=now_scheduled.subject
            qc=cbtcurrentquestion.objects.get(student=student,
                term =term,
                subject=subject,
                session=currse,
                exam_type=ex.exam_type)

            number=int(qc.number)

            
            if number==1:
                
                try:
                    pik = cbttrans.objects.get(student=student,session=currse,term=term,               
                    exam_type=ex.exam_type,no=number,subject=subject)
                    ans=pik.stu_ans
                except:
                    pik=cbtold.objects.get(student=student,
                        session=currse,
                        term=term,
                        klass=student.admitted_class,
                        subject=subject,
                        exam_type=ex.exam_type)
                    ans=''
            else:
                n2=number-1
                pik = cbttrans.objects.get(student=student,session=currse,term=term,               
                exam_type=ex.exam_type,no=n2,subject=subject)
                ans=pik.stu_ans

                hl=cbtcurrentquestion.objects.filter(student=student,
                    session=currse,
                    term = term,
                    subject=subject,
                    exam_type=ex.exam_type,
                    number=number).update(number=n2)
                number=n2

            tk = tblquestion.objects.get(session=currse,term=term, klass=student.admitted_class,
                exam_type=ex.exam_type, subject=subject,id=pik.qstcode)


            tk1 =tk.qstn
            tk2=tk.id
            img=tk.image

            k = tbloptions.objects.filter(qstn=tk).count()
            if k == 0:
                opt = tbloptioni.objects.filter(qstn=tk)
                image='hi'
            else:
                opt = tbloptions.objects.filter(qstn=tk)
                image='low'
            
            
            return render_to_response('CBT/pupiltest.html',{'question':tk1,
                'school':school,
                'count':number,
                'pos':image,
                'ans':ans,
                'image':img,
                'form':student,
                'session':currse,
                'name':student.fullname,
                'klass':student.admitted_class,
                'adm':student.admissionno,
                'options':opt,
                'term':term,
                'uid':tk.id,
                'subject':subject})

        else:
            return HttpResponseRedirect('/welcome/')
    else:
        return HttpResponseRedirect('/login/')




def skip(request):
    if "userid" in request.session:
        if request.method=='POST':
            varuser=request.session["userid"]
            student= Student.objects.get(fullname=varuser,admitted_session=currse,gone=False)

            now_scheduled= scheduled.objects.get(student=student,term=term,assessment=ex.exam_type,session=currse)
            subject=now_scheduled.subject
            
            qc=cbtcurrentquestion.objects.get(student=student,
                term =term,
                subject=subject,
                session=currse,
                exam_type=ex.exam_type)

            number=int(qc.number)   

            try:
                tk = cbttrans.objects.get(student=student,session=currse,term=term,               
                exam_type=ex.exam_type,no=number,subject=subject)
                ans=tk.stu_ans
                seen = 'tim'
            except:
                seen = 'tom'
            

            if seen == 'tom':

##generate another random question from the pool

##COLLECTING ANSWERED QUESTIONS BY ID
                trans=cbttrans.objects.filter(session=currse,
                    exam_type=ex.exam_type,
                    student=student, #or student.id 
                    subject=subject,
                    term=term)
                transid=[]
                for k in trans:
                    fb= k.qstcode.split('-')[0]
                    fb=int(fb)   
                    transid.append(fb)

##COLLECTING ENTERED QUESTIONS BY ID
                qstns=tblquestion.objects.filter(term=term, 
                    exam_type=ex.exam_type, 
                    session=currse,
                    subject=subject,
                    klass=student.admitted_class)#student.admitted_class
                myq=[]               

                for q in qstns:
                    myq.append(q.id)


##SORTING OUT UNIQUE QUESTIONS
                qu=[]
                qu= [item for item in myq  if item not in transid]


                if qu != []:



##PICKING A RANDOM UNIQUE QUESTION BY ID
                    uid = 0
                    uid = random.choice(qu)
                    tk=0
                    
                    tk = tblquestion.objects.get(id=uid)
#delete old question
                    current_q=cbtold.objects.get(session=currse,
                        term=q.term,
                        exam_type=q.exam_type,
                        klass=student.admitted_class,
                        subject=subject,
                        student=student)

                    current_q.delete() 


                    cbtold(session=currse,
                        question=tk,
                        term=q.term,
                        exam_type=q.exam_type,
                        klass=student.admitted_class,
                        subject=subject,
                        student=student,
                        qstcode=tk.id).save()       

                    tk1 =tk.qstn

                    k = tbloptions.objects.filter(qstn=tk).count()
                    if k == 0:
                        opt = tbloptioni.objects.filter(qstn=tk)
                        image='hi'
                    else:
                        opt = tbloptions.objects.filter(qstn=tk)
                        image='low'


                    img=tk.image
                    ans=''
                    
                    number=number

            elif seen == 'tim':
                
                tk=tblquestion.objects.get(id=tk.qstcode)#student.admitted_class
                tk1 =tk.qstn

                k = tbloptions.objects.filter(qstn=tk).count()
                if k == 0:
                    opt = tbloptioni.objects.filter(qstn=tk)
                    image='hi'
                else:
                    opt = tbloptions.objects.filter(qstn=tk)
                    image='low'


                img=tk.image
                # ans=''
                
                number=number

                
            return render_to_response('CBT/pupiltest.html',{'question':tk1,
                'school':school,
                'count':number,
                'pos':image,
                'ans':ans,
                'image':img,
                'form':student,
                'session':currse,
                'name':student.fullname,
                'klass':student.admitted_class,
                'adm':student.admissionno,
                'options':opt,
                'term':term,
                'uid':tk.id,
                'subject':subject})

        else:
            return HttpResponseRedirect('/welcome/')
    else:
        return HttpResponseRedirect('/login/')



def next(request):
    if "userid" in request.session:            
        if request.method=='POST':
            varuser=request.session['userid']
            student=Student.objects.get(admitted_session=currse,fullname=varuser,gone=False)
            now_scheduled= scheduled.objects.get(student=student,term=term,assessment=ex.exam_type,session=currse)
            subject=now_scheduled.subject

            qc=cbtcurrentquestion.objects.get(student=student,
                term =term,
                subject=subject,
                session=currse,
                exam_type=ex.exam_type)

            number=int(qc.number)

            if 'gender' in request.POST:
                a= request.POST['gender']

                    
                try:
                    dt = cbttrans.objects.get(student=student,session=currse,term=term,
                        exam_type=ex.exam_type,no=number,subject=subject)

                    ty='update'
                except:
                 
                    dt=cbtold.objects.get(student=student,session=currse,
                        term=term,exam_type=ex.exam_type,
                        klass=student.admitted_class,subject=subject)

                    ty='save'

                selq= tblquestion.objects.get(session=currse,term=term,
                    exam_type=ex.exam_type,klass=student.admitted_class,
                    subject= subject,id=dt.qstcode)

                sek=selq.qstn                 
                ans=tblans.objects.get(qstn=selq)
                ans=ans.ans
                b=str(ans)


                try:
                    opti = tbloptions.objects.get(qstn=selq)
                except:
                    opti = tbloptioni.objects.get(qstn=selq)

                d=opti.a
                e=opti.b
                g=opti.c
                w=opti.d

                if a == b: # if my answer is correct
                    if ty=='update':
                        k=cbttrans.objects.filter(student=student,session=currse,term=term,
                            exam_type=ex.exam_type,qstcode=selq.id,
                            subject=subject,).update(score =1,stu_ans=a)

                    elif ty=='save':
                        
                        k=cbttrans(student=student,session=currse,term=term,
                            exam_type=ex.exam_type,question=selq,stu_ans=a, score = 1, 
                            no=number,qstcode=selq.id,subject=subject).save()
                else:#if my ans is wrong
                   
                    if a == str(d) or a == str(e) or a == str(g) or a == str(w):
                        if ty=='update':    
                            cbttrans.objects.filter(student=student,session=currse,term=term,exam_type=ex.exam_type,
                                qstcode=selq.id,subject=subject).update(score=0,stu_ans=a)
        
                        elif ty=='save':
                            cbttrans(student=student,term=term, exam_type=ex.exam_type,question=selq,
                                stu_ans=a, score = 0,no=number,status=0,qstcode=selq.id,subject=subject,
                                session=currse).save()
                    else:
                        ty='whales'
                        tk = selq
                        ans=''
             
### porting to reportsheet module****************
                add=cbttrans.objects.filter(student=student,session=currse,term=term,                        
                        exam_type=ex.exam_type,
                        subject=subject).aggregate(Sum('score'))

                add = add['score__sum']

                acaderec = StudentAcademicRecord.objects.get(student = student, term=term)


                if ex.exam_type=='Mid term':
                    subsco = SubjectScore.objects.filter(academic_rec = acaderec,
                        subject=subject,term=term,session=currse).update(second_ca=add)
                if ex.exam_type=='Ca 1':
                    subsco = SubjectScore.objects.filter(academic_rec = acaderec,
                        subject=subject,term=term,session=currse).update(first_ca=add)
                if ex.exam_type=='Ca 2':
                    subsco = SubjectScore.objects.filter(academic_rec = acaderec,
                        subject=subject,term=term,session=currse).update(fourth_ca=add)
                if ex.exam_type=='End term':
                    subsco = SubjectScore.objects.filter(academic_rec = acaderec,
                        subject=subject,term=term,session=currse).update(fifth_ca=add)

                 
                if ty == 'save': #if i added a new entry to cbttrans

                    hu=cbtold.objects.get(session=currse,term=term,exam_type=ex.exam_type,klass=selq.klass,
                        subject=subject,student=student).delete()
    

                    trans=cbttrans.objects.filter(session=student.admitted_session,
                        exam_type=ex.exam_type,
                        student=student, #or student.id 
                        subject=subject,
                        term=term)

                    count=trans.count()+1

                    transid=[]

                    for k in trans:
                            fb= k.qstcode.split('-')[0]
                            fb=int(fb)   
                            transid.append(fb)


                    qstns=tblquestion.objects.filter(term=term, 
                            exam_type=ex.exam_type, 
                            session=student.admitted_session,
                            subject=subject,
                            klass=student.admitted_class)#student.admitted_class
                        

                    myq=[]
                       
                    for q in qstns:
                            myq.append(q.id)

                    qu=[]
            
                    qu= [item for item in myq  if item not in transid]


                    if qu == []:
                          cbtcurrentquestion.objects.filter(student=student,session=currse,term=term,
                                exam_type=ex.exam_type,
                                subject=subject).delete()
                          scheduled.objects.filter(student=student,session=currse,
                                term=term,assessment=ex.exam_type,subject=subject).delete()
                          donsub=donesubjects(student=student,exam_type=ex.exam_type, subject=subject, term=term,session=currse).save()
        
                          return render_to_response('CBT/done.html')

                    uid = 0


                    uid = random.choice(qu)
                    tk=0
                        
                    tk = tblquestion.objects.get(term=q.term, 
                            exam_type=q.exam_type, 
                            session=student.admitted_session,
                            subject=subject,
                            klass=student.admitted_class,
                            id=uid)

                    gh=cbtold.objects.filter(session=currse,
                            question=tk,
                            term=term,
                            exam_type=ex.exam_type,
                            klass=student.admitted_class,
                            subject=subject,
                            student=student,
                            qstcode=tk.id).count()

                    if gh==0:
                        cbtold(session=currse,
                                question=tk,
                                term=term,
                                exam_type=ex.exam_type,
                                klass=student.admitted_class,
                                subject=subject,
                                student=student,
                                qstcode=tk.id).save()

                        n2=number+1
                        hj= cbtcurrentquestion.objects.filter(student=student,
                            term = term,
                            session=currse,
                            subject=subject,
                            exam_type=ex.exam_type,
                            number=number).update(number=n2)


                elif ty=='update':     #if i updated

                    try:
                        c='i update'

                        n2=number+1
                        # subject='BASIC SCIENCE'

                        hj= cbtcurrentquestion.objects.filter(student=student,
                            term = term,
                            session=currse,
                            subject=subject,
                            exam_type=ex.exam_type,
                            number=number).update(number=n2)                     

                        qs= cbttrans.objects.get(student=student,session=currse,
                            term=term,exam_type=ex.exam_type,no=n2,subject=subject)
                        ans=qs.stu_ans

                        tk = tblquestion.objects.get(term=term, 
                        exam_type=ex.exam_type, 
                        session=currse,
                        subject=subject,
                        klass=student.admitted_class,
                        id=qs.qstcode)
                        
                    except:

                        n2=number+1
                        # subject='BASIC SCIENCE'

                        hj= cbtcurrentquestion.objects.filter(student=student,
                            term = term,
                            session=currse,
                            subject=subject,
                            exam_type=ex.exam_type,
                            number=number).update(number=n2) 

                        qs=cbtold.objects.get(student=student,
                            session=currse,
                            term=term,                            
                            exam_type=ex.exam_type,
                            klass=student.admitted_class,
                            subject=subject)
                        ans=''

                        tk = tblquestion.objects.get(term=term, 
                        exam_type=ex.exam_type, 
                        session=currse,
                        subject=subject,
                        klass=student.admitted_class,
                        id=qs.qstcode)
                  
                if ty != 'whales':
                    number=number+1

            else: #if i didnt chose an option
                try:
                    qs = cbttrans.objects.get(student=student,session=currse,term=term,
                        exam_type=ex.exam_type,no=number,subject=subject)
                    ans=qs.stu_ans

                except:

                    qs=cbtold.objects.get(student=student,session=currse,term=term,
                        exam_type=ex.exam_type,klass=student.admitted_class,subject=subject)
                    ans=''


                tk = tblquestion.objects.get(term=term, 
                        exam_type=ex.exam_type, 
                        session=currse,
                        subject=subject,
                        klass=student.admitted_class,
                        id=qs.qstcode)

                
            k = tbloptions.objects.filter(qstn=tk).count()
            if k == 0:
                opt = tbloptioni.objects.filter(qstn=tk)
                image='hi'
            else:
                opt = tbloptions.objects.filter(qstn=tk)
                image='low'


            tk1 =tk.qstn
            # opt = tbloptions.objects.filter(qstn=tk)
            img =tk.image

        

            return render_to_response('CBT/pupiltest.html',{'question':tk1,
                'school':school,
                'count':number,
                'form':student,
                'pos':image,
                'ans':ans,
                'image':img,
                'session':currse,
                'name':student.fullname,
                'klass':student.admitted_class,
                'adm':student.admissionno,
                'options':opt,
                'term':term,
                'uid':tk.id,
                'subject':subject})
       
        else:
            return HttpResponseRedirect('/cbt/take_test/start/')
    else:
        return HttpResponseRedirect('/login/')



def textts(request,vid):
    if 'userid' in request.session:
        if request.method=='POST':
            qst=tblquestion.objects.get(id=vid)
            session=qst.session
            klass=qst.klass
            subject=qst.subject
            term=qst.term
            exam=qst.exam_type
            code=qst.id

            return HttpResponseRedirect('/cbt/input_text/%s/%s/%s/%s/%s/%s/'%(code,str(session).replace('/','k'),str(klass).replace(' ','m'),term,str(subject).replace(' ','w'),str(exam).replace(' ','p')))

    else:
        return HttpResponseRedirect ('/login')


def save_text(request,code,session,klass,term,subject,exam):
    session = str(session).replace('k','/')
    klass = str(klass).replace('m',' ')
    subject = str(subject).replace('w',' ')
    exam = str(exam).replace('p',' ')

    if request.method == 'GET':
        getdetails=[]
        details = tblquestion.objects.get(id = code)
        try:
            options=tbloptions.objects.get(qstn=details)
        except:
            options=''
        try:
            answer= tblans.objects.get(qstn=details)

        except:
             answer=''
            
        dicdetails={'options':options,'question':details,'answer':answer}

        return render_to_response('CBT/enteropt.html',{'getdetails':dicdetails,})
    # return render_to_response('CBT/enteroption.html',{'getdetails':qst,'exam':exam,'session':session,'klass':klass,'term':term,'subject':subject})#'state':options})




def images(request,vid):
    if 'userid' in request.session:
        if request.method=='POST':
            qst=tblquestion.objects.get(id=vid)
            session=qst.session
            klass=qst.klass
            subject=qst.subject
            term=qst.term
            exam=qst.exam_type
            code=qst.id

            return HttpResponseRedirect('/cbt/input_images/%s/%s/%s/%s/%s/%s/'%(code,str(session).replace('/','k'),str(klass).replace(' ','m'),term,str(subject).replace(' ','w'),str(exam).replace(' ','p')))

    else:
        return HttpResponseRedirect ('/login')


def setass(request):
    if  "userid" in request.session:
        varuser = request.session['userid']
        user = userprofile.objects.get(username = varuser)
        uenter = user.createuser
        if uenter is False :
            return HttpResponseRedirect('/welcome/')

        t1=['Ca 2','Mid term','End Term']
        t2=['Ca 1','Mid term','End Term']
        t4=['Ca 2','Mid term','Ca 1']
        t3=['Ca 2','End Term','Ca 1']

        varerr = ""
        getdetails =""
        if request.method == 'POST':
            form =assessmentform(request.POST) # A form bound to the POST data
            if form.is_valid():
                assess = form.cleaned_data['assess']
                status = form.cleaned_data['status']
                if assess == 'Ca 1':
                    if status =='ACTIVE':
                        tblcbtexams.objects.filter(exam_type=assess).update(status=status)
                        for t in t1:
                            tblcbtexams.objects.filter(exam_type=t).update(status='INACTIVE')
                
                elif assess == 'Ca 2':
                    if status =='ACTIVE':
                        tblcbtexams.objects.filter(exam_type=assess).update(status=status)
                        for t in t2:
                            tblcbtexams.objects.filter(exam_type=t).update(status='INACTIVE')

                elif assess == 'End Term':
                    if status =='ACTIVE':
                        tblcbtexams.objects.filter(exam_type=assess).update(status=status)
                        for t in t4:
                            tblcbtexams.objects.filter(exam_type=t).update(status='INACTIVE')

                elif assess == 'Mid term':
                    if status =='ACTIVE':
                        tblcbtexams.objects.filter(exam_type=assess).update(status=status)
                        for t in t3:
                            tblcbtexams.objects.filter(exam_type=t).update(status='INACTIVE')

                return HttpResponseRedirect('/cbt/assessment/set/')
        else:
            form = assessmentform()
            getdetails = tblcbtexams.objects.all().order_by('status')
        return render_to_response('CBT/assessment.html',{'varuser':varuser,'varerr':varerr,'form':form,'getdetails':getdetails},context_instance = RequestContext(request))
    else:
        return HttpResponseRedirect('/login/')




def save_images(request,code,session,klass,term,subject,exam):
    session = str(session).replace('k','/')
    klass = str(klass).replace('m',' ')
    subject = str(subject).replace('w',' ')
    exam = str(exam).replace('p',' ')

    if request.method == 'GET':
        getdetails=[]
        details = tblquestion.objects.get(id = code)
        try:
            options=tbloptions.objects.get(qstn=details)
        except:
            options=''
        try:
            answer= tblans.objects.get(qstn=details)

        except:
             answer=''
            
        dicdetails={'options':options,'question':details,'answer':answer}

        return render_to_response('CBT/qstoptions.html',{'getdetails':dicdetails,'state':options})
