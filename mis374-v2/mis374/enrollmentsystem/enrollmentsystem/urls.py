from __future__ import unicode_literals
from django.urls import include, path
from enrollment.views import enrollment, parents, teachers, admins
from django.contrib import admin

try:
    from django.urls import re_path, include
except ImportError:
    # For Django 1.8 compatibility
    from django.conf.urls import url as re_path, include
from django.contrib import admin
from django.shortcuts import render

from forms_builder.forms.models import Form
from forms_builder.forms import urls as form_urls


admin.autodiscover()
urlpatterns = [
    path('', enrollment.home, name="home"),
   # path('admin/', admin.site.urls),
    path('', include('enrollment.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', enrollment.SignUpView.as_view(), name='signup'),
    path('accounts/signup/parent/', parents.ParentSignUpView.as_view(), name='parent_signup'),
    path('accounts/signup/teacher/', teachers.TeacherSignUpView.as_view(), name='teacher_signup'),
    path('accounts/signup/admin/', admins.AdminSignUpView.as_view(), name='admin_signup'),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^forms/', include(form_urls)),
    re_path(r'^$', lambda request: render(request, "index.html",
                                      {"forms": Form.objects.all()})),
]


