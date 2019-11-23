
from django.conf.urls.defaults import patterns, url
from django.views.generic import DetailView, TemplateView
urlpatterns = patterns('myproject.CBT.views',
    
    url(r'^home/$', 'chroose'),
    url(r'^set_user/subject/$', 'assignment'),
    url(r'^schedulling/active/$', 'cbtstat'),

    ###****questions************
    url(r'^enter/question/$', 'qstn'),
    url(r'^enter/image/(\d+)/$', 'cbtimage'),
    url(r'^enter/ajaxclass/$', 'ajaxclass'),
    url(r'^getcbtsubject/$', 'getcbtsubject'),
    url(r'^enter/question/getqstn/$', 'getcbtqst'),
    
    url(r'^enter/question/ajax/$', 'editcbtqst'),

    url(r'^enter/question/majax/$', 'editcbtpix'),

##*******options *******************
    url(r'^enter/options/getopt/$', 'getcbtopt'),
    url(r'^options/$', 'options'),
    url(r'^options/options/(\d+)/$', 'myoptions'),
    url(r'^options/options/image/(\d+)/$', 'myoptionsimage'),
    url(r'^options/enteropt/$', 'optajax'),
    url(r'^options/choose/$', 'chooseopt'),
    url(r'^options/texts/(\d+)/$', 'textts'),
    url(r'^input_text/(\w+)/(\w+)/(\w+)/(\w+)/(\w+)/(\w+)/$', 'save_text'),
    url(r'^options/images/(\d+)/$', 'images'),
    url(r'^input_images/(\w+)/(\w+)/(\w+)/(\w+)/(\w+)/(\w+)/$', 'save_images'),


#***--------------theory------------------
    url(r'^enter/theory/$', 'theory'),

    ##****** student's view**************
    url(r'^cbt/exam/$', 'exxxam'),
    url(r'^take_test/start/$', 'pupilcbt'),
    url(r'^take_test/next/$', 'next'),
    url(r'^take_test/clear/$', 'clear'),
    url(r'^take_test/previous/$', 'beefore'),
    url(r'^take_test/skip/$', 'skip'),

    ##*******edit *******************
    url(r'^enter/options/edit/$', 'editquestion'),
    url(r'^edit/$', 'editq'),
  
    url(r'^edit/editentry/$', 'doentry'),


    url(r'^edit/editqst/$', 'editqst'),
    url(r'^change/question/(\d+)/$', 'changeqst'),


    url(r'^edit/edita/$', 'editoptiona'),
    url(r'^change/optiona/(\d+)/$', 'optiona'),

    url(r'^edit/editb/$', 'editoptionb'),
    url(r'^change/optionb/(\d+)/$', 'optionb'),

    url(r'^edit/editc/$', 'editoptionc'),
    url(r'^change/optionc/(\d+)/$', 'optionc'),

    url(r'^edit/editd/$', 'editoptiond'),
    url(r'^change/optiond/(\d+)/$', 'optiond'),

    url(r'^edit/imageqst/$', 'sdfgsf'),


    url(r'^question/imageedit/(\d+)/$', 'chngqstimage'),

#**********##mark guides*********************
    url(r'^mark_guides/$', 'markguide'),

    url(r'^markguide/getmg/$', 'guides'),    

    url(r'^assessment/set/$', 'setass'),  

    #***************schedulling####
    url(r'^assess/getassess/$', 'getassessment'),
    url(r'^getsubject/$', 'getcbtsub'),
    url(r'^getscheduledsubject/$', 'getscheduledsubject'), 
    url(r'^getcbtklass/$', 'getcbtklass'), 


###***User***********
url(r'^finduser/$', 'autocomplete'), 
    )
