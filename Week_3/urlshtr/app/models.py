from django.db import models

class ShortenedURL(models.Model):
    original_url = models.URLField()
    shrtd = models.CharField(max_length=16, db_index=True)
    
    def __unicode__(self):
        return "original : {}, shortened: {}".format(
        self.original_url, self.shrtd
        )
        
    def __repr__(self):
        return self.__unicode__()
    


    

