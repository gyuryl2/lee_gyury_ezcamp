from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from courseinfo.forms import CounselorForm, CabinForm, SessionForm, CourseForm, CamperForm, RegistrationForm
from courseinfo.models import (
    Counselor,
    Cabin,
    Course,
    Session,
    Camper,
    Registration
)
from courseinfo.utils import PageLinksMixin


class CounselorList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 25
    model = Counselor
    permission_required = 'courseinfo.view_counselor'


class CounselorDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Counselor
    permission_required = 'courseinfo.view_counselor'

    def get_context_data(self, **kwargs):
        context=super(DetailView, self).get_context_data(**kwargs)
        counselor = self.get_object()
        cabin_list = counselor.cabins.all()
        context['cabin_list'] = cabin_list
        return context


class CounselorCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = CounselorForm
    model = Counselor
    permission_required = 'courseinfo.add_counselor'


class CounselorUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = CounselorForm
    model = Counselor
    template_name = 'courseinfo/counselor_form_update.html'
    permission_required = 'courseinfo.change_counselor'


class CounselorDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Counselor
    success_url = reverse_lazy('courseinfo_counselor_list_urlpattern')
    permission_required = 'courseinfo.delete_counselor'

    def get(self, request, pk):
        counselor = get_object_or_404(Counselor, pk=pk)
        cabins = counselor.cabins.all()
        if cabins.count() > 0:
            return render(
                request,
                'courseinfo/counselor_refuse_delete.html',
                {'counselor': counselor,
                 'cabins': cabins,
                 }
            )
        else:
            return render(
                request,
                'courseinfo/counselor_confirm_delete.html',
                {'counselor': counselor}
            )





class CabinList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Cabin
    permission_required = 'courseinfo.view_cabin'

class CabinDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Cabin
    permission_required = 'courseinfo.view_cabin'

    def get_context_data(self, **kwargs):
        context=super(DetailView, self).get_context_data(**kwargs)
        cabin = self.get_object()
        session = cabin.session
        course = cabin.course
        counselor = cabin.counselor
        registration_list = cabin.registrations.all()
        context['session'] = session
        context['course'] = course
        context['counselor'] = counselor
        context['registration_list'] = registration_list
        return context


class CabinCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = CabinForm
    model = Cabin
    permission_required = 'courseinfo.add_cabin'

class CabinUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = CabinForm
    model = Cabin
    template_name = 'courseinfo/cabin_form_update.html'
    permission_required = 'courseinfo.change_cabin'


class CabinDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Cabin
    success_url = reverse_lazy('courseinfo_cabin_list_urlpattern')
    permission_required = 'courseinfo.delete_cabin'

    def get(self, request, pk):
        cabin = get_object_or_404(Cabin, pk=pk)
        registrations = cabin.registrations.all()
        if registrations.count() > 0:
            return render(
                request,
                'courseinfo/cabin_refuse_delete.html',
                {'cabin': cabin,
                 'registrations': registrations,
                 }
            )
        else:
            return render(
                request,
                'courseinfo/cabin_confirm_delete.html',
                {'cabin': cabin}
            )


class CourseList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Course
    permission_required = 'courseinfo.view_course'

class CourseDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Course
    permission_required = 'courseinfo.view_course'

    def get_context_data(self, **kwargs):
        context=super(DetailView, self).get_context_data(**kwargs)
        course = self.get_object()
        cabin_list = course.cabins.all()
        context['cabin_list'] = cabin_list
        return context


class CourseCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = CourseForm
    model = Course
    permission_required = 'courseinfo.add_course'


class CourseUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = CourseForm
    model = Course
    template_name = 'courseinfo/course_form_update.html'
    permission_required = 'courseinfo.change_course'

class CourseDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Course
    success_url = reverse_lazy('courseinfo_course_list_urlpattern')
    permission_required = 'courseinfo.delete_course'

    def get(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        cabins = course.cabins.all()
        if cabins.count() > 0:
            return render(
                request,
                'courseinfo/course_refuse_delete.html',
                {'course': course,
                 'cabins': cabins,
                 }
            )
        else:
            return render(
                request,
                'courseinfo/course_confirm_delete.html',
                {'course': course}
            )


class SessionList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Session
    permission_required = 'courseinfo.view_session'

class SessionDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Session
    permission_required = 'courseinfo.view_session'

    def get_context_data(self, **kwargs):
        context=super(DetailView, self).get_context_data(**kwargs)
        session = self.get_object()
        cabin_list = session.cabins.all()
        context['cabin_list'] = cabin_list
        return context


class SessionCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = SessionForm
    model = Session
    permission_required = 'courseinfo.add_session'


class SessionUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = SessionForm
    model = Session
    template_name = 'courseinfo/session_form_update.html'
    permission_required = 'courseinfo.change_session'


class SessionDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Session
    success_url = reverse_lazy('courseinfo_session_list_urlpattern')
    permission_required = 'courseinfo.delete_session'

    def get(self, request, pk):
        session = get_object_or_404(Session, pk=pk)
        cabins = session.cabins.all()
        if cabins.count() > 0:
            return render(
                request,
                'courseinfo/session_refuse_delete.html',
                {'session': session,
                 'cabins': cabins,
                 }
            )
        else:
            return render(
                request,
                'courseinfo/session_confirm_delete.html',
                {'session': session}
            )



class CamperList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 25
    model = Camper
    permission_required = 'courseinfo.view_camper'

class CamperDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Camper
    permission_required = 'courseinfo.view_camper'

    def get_context_data(self, **kwargs):
        context=super(DetailView, self).get_context_data(**kwargs)
        camper = self.get_object()
        registration_list = camper.registrations.all()
        context['registration_list'] = registration_list
        return context


class CamperCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = CamperForm
    model = Camper
    permission_required = 'courseinfo.add_camper'


class CamperUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = CamperForm
    model = Camper
    template_name = 'courseinfo/camper_form_update.html'
    permission_required = 'courseinfo.change_camper'

class CamperDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Camper
    success_url = reverse_lazy('courseinfo_camper_list_urlpattern')
    permission_required = 'courseinfo.delete_camper'

    def get(self, request, pk):
        camper = get_object_or_404(Camper, pk=pk)
        registrations = camper.registrations.all()
        if registrations.count() > 0:
            return render(
                request,
                'courseinfo/camper_refuse_delete.html',
                {'camper': camper,
                 'registrations': registrations,
                 }
            )
        else:
            return render(
                request,
                'courseinfo/camper_confirm_delete.html',
                {'camper': camper}
            )


class RegistrationList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Registration
    permission_required = 'courseinfo.view_registration'

class RegistrationDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Registration
    permission_required = 'courseinfo.view_registration'

    def get_context_data(self, **kwargs):
        context=super(DetailView, self).get_context_data(**kwargs)
        registration = self.get_object()
        return context


class RegistrationCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = RegistrationForm
    model = Registration
    permission_required = 'courseinfo.add_registration'


class RegistrationUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = RegistrationForm
    model = Registration
    template_name = 'courseinfo/registration_form_update.html'
    permission_required = 'courseinfo.change_registration'


class RegistrationDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Registration
    success_url = reverse_lazy('courseinfo_registration_list_urlpattern')
    permission_required = 'courseinfo.delete_registration'