from django.conf.urls import patterns, url

from .views import (
    ProjectIndexView,
    ProjectProposeView,
    ProjectDetailView,
    ProjectEditView,
    ProjectApplyView,
    ProjectApplicantsView,
    ProjectApplicants,
)
#from projects import views
#from apps.projects import views

urlpatterns = patterns("",
    # url: /projects/ list view
    url(r"^$", ProjectIndexView.as_view(), name="project_index"),

    #project proposal url: /projects/propose-project
    url(r"^propose-project/$", ProjectProposeView.as_view(), name="project_propose"),

    # project details url: /projects/(id)-(slug)/
    url(r"^(?P<pk>\d+)(?:-(?P<slug>[\w|\s|-]+))?/$", ProjectDetailView.as_view(), name="project_detail"),

    # project edit page url: /projects/(id)-(slug)/edit-project
    url(r"^(?P<pk>\d+)(?:-(?P<slug>[\w|\s|-]+))?/edit-project/$", ProjectEditView.as_view(), name="project_edit"),

    # apply to project url: /projects/(id)-(slug)/apply-to-project
    url(r"^(?P<pk>\d+)(?:-(?P<slug>[\w|\s|-]+))?/apply-to-project/$", ProjectApplyView.as_view(), name="project_apply"),

    url(r"^(?P<pk>\d+)(?:-(?P<slug>[\w|\s|-]+))?/applicants/$", ProjectApplicants.as_view(), name="project_applicants"),

    # view applicants url: /projects/(id)-(slug)/view-applicants
#url(r"^(?P<project_id>\d+)-?[\w]*/view-applicants$", ProjectApplicantsView.as_view(), name="project_applicants"),

    # project details for /projects/(id)-(slug)/view-applicants/accept-applicants
#url(r"^(?P<project_id>\d+)-[\w]+/view-applicants/accept-applicants$", views.ProjectAcceptApplicantsView.as_view(), name="project_accept_applicants"),
)