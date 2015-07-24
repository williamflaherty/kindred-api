from django.db import models

# I left comments for future fields in some of the models.

class Challenge(models.Model):
    challenge = models.CharField(max_length = 140, unique = True)
    pub_date = models.DateTimeField('date_published')
    completions = models.IntegerField(default = 0)

    def __unicode__ (self):
        return u'%s' % (self.challenge)

class User(models.Model):
    username = models.CharField(max_length = 100)
    ig_token = models.CharField(max_length = 200)
    ig_token_expiry = models.DateTimeField('instagram_token_expiration')
    join_date = models.DateTimeField('join_date')
    #number of challenges completed

class Photo(models.Model):
    url = models.CharField(max_length = 2083)
    challenge = models.ForeignKey(Challenge)
    user = models.ForeignKey(User)
    pub_date = models.DateTimeField('date_published')
    updoots = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    instagram = models.BooleanField(default=False)
    #there would be a t/f field for whether it was shared on fb,instagram,etc
    #thought about making this an array or dictionary type but meh
    flagged = models.BooleanField(default=False)
    city = models.CharField(max_length=85)
    top_tf = models.BooleanField('top_twenty_five', default=False)


