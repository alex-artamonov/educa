from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Course

class OwnerMixin:
    def get_queryset(self) -> QuerySet[Any]:
        qs =  super().get_queryset()
        return qs.filter(owner=self.request.user)

class OwnerEditMixin:
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
class OwnerCourseMixin(OwnerMixin):
    model = Course
    fields = ['subjec', 'title', 'slug', 'overview']
    success_url = reverse_lazy('manage_course_list')

class ManageCourseListView(OwnerMixin, ListView):
    template_name = 'courses/manage/course/list.html'
    

    