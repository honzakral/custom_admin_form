from django.db import models


class Poll(models.Model):
    name = models.CharField(unique=True, max_length=231)
    question = models.TextField()

    def __unicode__(self):
        return self.name

class PollOption(models.Model):
    poll = models.ForeignKey(Poll)
    text = models.TextField()
    votes = models.PositiveIntegerField(editable=False, default=0)

    def __unicode__(self):
        return '%s: %s' % (self.poll, self.text)


