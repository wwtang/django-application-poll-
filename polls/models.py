from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
from django.contrib import admin

class Poll(models.Model):
    question = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.question

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.TextField(max_length=200)
    votes = models.IntegerField()

    def __unicode__(self):
        return self.choice_text

#active the admin site

class ChoiceInline(admin.TabularInline):
    model =Choice
    extra= 3

class PollAdmin(admin.ModelAdmin):
    fieldset = [
            (None, {'fields':['question']}),
            ("Date information", {'fields':['pub_date'], "classes":['collapse']})
            ]
    inlines = [ChoiceInline]
    list_display = ('question','pub_date',"was_published_recently")
    list_filter = ["pub_date"]
    search_fileds = ['question']
    date_hierarchy = 'pub_date'
admin.site.register(Poll, PollAdmin)
