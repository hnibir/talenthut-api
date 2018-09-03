from django.urls import path

from .th_views.views import RecruiterEventList, RecruiterEventDetail
from .th_views.views import ExpertiseList, ExpertiseDetail
from .th_views.views import TalentList, TalentDetail
from .th_views.views import RecruiterActivities, RecruiterActivityDetail
from .th_views.views import RecruiterList, RecruiterDetail
from .th_views.views import TalentListByExpertise, RecruiterActivityList
from .th_views.views import RecruiterActivityListByRecruiterEvent, RecruiterActivitiesByRecruiterAndTalent
from .th_views.views import UserList, UserDetail
from .th_views.views import HomeView
from .th_views.views import LoginView

app_name = 'talenthut'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('recruiter-events/', RecruiterEventList.as_view(), name="recruiter_event_list"),
    path('recruiter-events/<pk>/', RecruiterEventDetail.as_view(), name="recruiter_event_detail"),

    path('expertises/', ExpertiseList.as_view(), name="expertise_list"),
    path('expertises/<pk>/', ExpertiseDetail.as_view(), name="expertise_detail"),

    path('users/', UserList.as_view(), name="user_list"),
    path('users/<pk>/', UserDetail.as_view(), name="user_detail"),

    path('talents/', TalentList.as_view(), name="talent_list"),
    path('talents/<pk>/', TalentDetail.as_view(), name="talent_detail"),
    path('talents/expertises/<int:expertise_pk>/', TalentListByExpertise.as_view(), name="talent_list_by_expertise"),

    # path('addresses/', AddressList.as_view(), name="address_list"),
    # path('addresses/<pk>/', AddressDetail.as_view(), name="address_detail"),

    # path('resumes/', ResumeList.as_view(), name="resume_list"),
    # path('resumes/<pk>/', ResumeDetail.as_view(), name="resume_detail"),

    # path('job-experiences/', JobExperienceList.as_view(), name="job_experience_list"),
    # path('job-experiences/<pk>/', JobExperienceDetail.as_view(), name="job_experience_detail"),

    # path('technical-skills/', TechnicalSkillList.as_view(), name="technical_skill_list"),
    # path('technical-skills/<pk>/', TechnicalSkillDetail.as_view(), name="technical_skill_detail"),

    # path('educations/', EducationList.as_view(), name="education_list"),
    # path('educations/<pk>/', EducationDetail.as_view(), name="education_detail"),

    # path('language-skills/', LanguageSkillList.as_view(), name="language_skill_list"),
    # path('language-skills/<pk>/', LanguageSkillDetail.as_view(), name="language_skill_detail"),

    path('recruiters/', RecruiterList.as_view(), name="recruiter_list"),
    path('recruiters/<pk>/', RecruiterDetail.as_view(), name="recruiter_detail"),

    path('recruiter-activities/', RecruiterActivities.as_view(), name="recruiter_activities_list"),
    path('recruiter-activities/<pk>/', RecruiterActivityDetail.as_view(), name="recruiter_activity_detail"),
    path('recruiter-activities/recruiters/<int:recruiter_pk>/talents/', RecruiterActivityList.as_view(),
         name="talent_list_by_recruiter"),
    path('recruiter-activities/recruiters/<int:recruiter_pk>/talents/<int:talent_pk>/',
         RecruiterActivitiesByRecruiterAndTalent.as_view(), name="recruiter_activities_by_recruiter_and_talent"),
    path('recruiter-activities/<int:recruiter_event_pk>/recruiters/<int:recruiter_pk>/talents/',
         RecruiterActivityListByRecruiterEvent.as_view(), name="recruiter_activity_list_by_recruiter_event"),

]
