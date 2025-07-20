from django.contrib import admin
from django.urls import path
from srmsApp import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView

from django.conf import settings
from django.conf.urls.static import static

context={
    'page':'login',
    'page_title':'Login',
    'system_name': views.context['system_name'],
    'short_name':views.context['short_name'],
    'has_navigation':False,
    'has_sidebar':False,
}
urlpatterns = [
    
    path('redirect-admin', RedirectView.as_view(url="/admin"),name="redirect-admin"),
    path('login',auth_views.LoginView.as_view(template_name="login.html",redirect_authenticated_user = True,extra_context = context),name='login'),
    path('logout',views.logoutuser,name='logout'),
    path('userlogin', views.login_user, name="login-user"),
    path('profile', views.profile, name="profile-page"),
    path('update_profile', views.update_profile, name="update-profile"),
    path('update_password', views.update_password, name="update-password"),
   
    path('civb', views.civb,name="civb"),
    path('mecb', views.mecb,name="mecb"),
    path('eleb', views.eleb,name="eleb"),
    path('stud3', views.stud3,name="stud3"),
    
    
    path('cosem2', views.cosem2,name="cosem2"),
    path('cosem3', views.cosem3,name="cosem3"),
    path('resultsemco', views.resultsemco,name="resultsemco"),
    
    path('cosem3_R', views.cosem3_R,name="cosem3_R"),
    path('cosem2_r', views.cosem2_r,name="cosem2_r"),
    path('cosem1_r', views.cosem1_r,name="cosem1_r"),

    path('mb1', views.mb1,name="mb1"),
    path('mb2', views.mb2,name="mb2"),
    path('mb3', views.mb3,name="mb3"),

    path('me1', views.me1,name="me1"),
    path('me3', views.me3,name="me3"),
    path('me5', views.me5,name="me5"),

    path('elb1', views.elb1,name="elb1"),
    path('elb2', views.elb2,name="elb2"),
    path('elb3', views.elb3,name="elb3"),

    path('chatcosem1', views.chatcosem1,name="chatcosem1"),
    path('chatcosem3', views.chatcosem3, name='chatcosem3'),
    path('chatcosem2', views.chatcosem2, name='chatcosem2'),
    path('chatel3', views.chatel3, name='chatel3'),
    path('chatel2', views.chatel2, name='chatel2'),

    path('civ1', views.civ1,name="civ1"),
    path('civ2', views.civ2,name="civ2"),
    path('civ3', views.civ3,name="civ3"),
    path('costud_m', views.costud_m,name="costud_m"),
    path('costud3_m', views.costud3_m,name="costud3_m"),
    path('teacher', views.teacher,name="teacher"),
    path('mec_teach', views.mec_teach,name="mec_teach"),
    path('menu_teach', views.menu_teach,name="menu_teach"),
    path('ele_teach', views.ele_teach,name="ele_teach"),
    path('civ_teach', views.civ_teach,name="civ_teach"),

    path('com_teach', views.com_teach,name="com_teach"),
    path('com_teacher1', views.com_teacher1,name="com_teacher1"),
    

    path('comsem_t', views.comsem_t,name="comsem_t"),
    path('', views.home,name="home-page"),
    path('class_mgt', views.class_mgt,name="class-page"),
    path('manage_class', views.manage_class,name="manage-class"),
    path('manage_class/<int:pk>', views.manage_class,name="manage-class-pk"),
    path('save_class', views.save_class,name="save-class"),
    path('delete_class', views.delete_class,name="delete-class"),
    path('student', views.student_mgt,name="student-page"),
    path('manage_student', views.manage_student,name="manage-student"),
    path('result', views.result_mgt,name="result-page"),
    path('manage_result', views.manage_result,name="manage-result"),
    path('manage_result/<int:pk>', views.manage_result,name="manage-result-pk"),
    path('view_result/<int:pk>', views.view_result,name="view-result-pk"),
    path('select_student_results', views.select_student_results,name="select_student_results"),
    path('list_result', views.list_student_result,name="list-result"),

    path('resultsem1', views.resultsem1,name="resultsem1"), 
    path('resultsem5', views.resultsem5,name="resultsem5"),
    path('resultsem3', views.resultsem3,name="resultsem3"),
    path('resultsemview', views.resultsemview,name="resultsemview"),
   
    path('list_result/<int:pk>', views.list_student_result),

    path("upload",views.upload,name="upload"),
    path("upload1",views.upload1,name="upload1"),
    path("upload2",views.upload2,name="upload2"),
    path("upload3",views.upload3,name="upload3")

]