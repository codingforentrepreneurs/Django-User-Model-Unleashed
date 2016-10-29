from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    city = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return str(self.user.username)

    def __unicode__(self):
        return str(self.user.username)


def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
    if created:
        try:
            Profile.objects.create(user=instance)
        except:
            pass

post_save.connect(post_save_user_model_receiver, sender=settings.AUTH_USER_MODEL)
