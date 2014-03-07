from django.db import models

# Create your models here.

class Athlete(models.Model):
    name = models.CharField(unique=True, max_length=50)
    img= models.URLField()
    video=models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    age = models.IntegerField(max_length=50)
    birthplace=models.CharField(max_length=50)
    birthday=models.CharField(max_length=50)
    team_event=models.CharField(max_length=50)
    team_event_score=models.IntegerField(max_length=50)
    team_score=models.IntegerField(max_length=50)
    team_event2=models.CharField(max_length=50, null=True)
    team_event2_score=models.IntegerField(max_length=50, null=True)
    team_score2=models.IntegerField(max_length=50, null= True)
    indiv_event=models.CharField(max_length=50)
    indiv_short_score=models.IntegerField(max_length=50)
    indiv_short_place=models.IntegerField(max_length=50)
    indiv_free_score=models.IntegerField(max_length=50)
    indiv_free_place=models.IntegerField(max_length=50)
    indiv_overall=models.IntegerField(max_length=50)
    medal=models.CharField(max_length=50)
    img=models.URLField(unique=False)
    
    class Meta(object):
        verbose_name_plural = "Athletes"
        ordering = ('name',)
        
    def __unicode__(self):
        return U'%s' %(self.name)
    def save(self, *args, **kwargs):
        self.name=self.name.upper()
        super(Athlete, self).save(*args, **kwargs)
    
        
