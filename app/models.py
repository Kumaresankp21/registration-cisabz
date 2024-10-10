from django.db import models

class Event(models.Model):
    EVENT_TYPE_CHOICES = [
        ('technical', 'Technical'),
        ('non_technical', 'Non-Technical'),
    ]
    
    name = models.CharField(max_length=100)
    event_type = models.CharField(max_length=20, choices=EVENT_TYPE_CHOICES)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.name

class Registration(models.Model):
    paper_id = models.CharField(max_length=20, null=True)  # Paper ID can be NULL
    team_name = models.ForeignKey('Team', related_name='registrations', on_delete=models.CASCADE, null=True)  # ForeignKey to Team
    college = models.CharField(max_length=255, null=True, blank=True)  # College can be NULL
    department = models.CharField(max_length=100, null=True, blank=True)  # Department can be NULL
    phone = models.CharField(max_length=15, null=True, blank=True)  # Phone can be NULL
    email = models.EmailField(null=True, blank=True)  # Email can be NULL
    paper_title = models.CharField(max_length=255, null=True, blank=True)  # Paper title can be NULL
    paper_submission_link = models.URLField(null=True, blank=True)  # Paper submission link can be NULL

    def __str__(self):
        return f'{self.team_name} ({self.college})'

class TeamMember(models.Model):
    registration = models.ForeignKey(Registration, related_name='members', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)  # Name can be NULL
    email = models.EmailField(null=True, blank=True)  # Email can be NULL
    phone = models.CharField(max_length=15, null=True, blank=True)  # Phone can be NULL
    def __str__(self):
        return self.name
