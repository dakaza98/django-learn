from django.contrib import admin
from .models import Question
from django_object_actions import DjangoObjectActions


class QuestionAdmin(DjangoObjectActions, admin.ModelAdmin):
    def publish_this(modeladmin, request, queryset):
        self.message_user(request, "We good")
    
    def toolfunc(self, request, obj):
        self.message_user(request, "We goodie")
    publish_this.label = "Publish"  # optional
    publish_this.short_description = "Submit this article"  # optional

    change_actions = ('toolfunc', )
    changelist_actions  = ('publish_this', )

admin.site.register(Question, QuestionAdmin)
