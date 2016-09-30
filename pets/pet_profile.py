from __future__ import unicode_literals

from django.db import models


class PetType(models.Model):
    type = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Type"
        verbose_name_plural = "Types"

    def __unicode__(self):
        return unicode(self.name)


class PetBreed(models.Model):
    pet_type = models.ForeignKey("PetType")
    breed = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Breed"
        verbose_name_plural = "Breeds"

    def __unicode__(self):
        return "%s : %s" % (self.pet_type.type, self.breed)


class PetProfile(models.Model):
    owner = models.ForeignKey("auth.User")
    type = models.ForeignKey("PetType")
    breed_1 = models.ForeignKey("PetBreed")
    breed_2 = models.ForeignKey("PetBreed", null=True, blank=True, related_name="breed_2")
    name = models.CharField(max_length=250)
    gender = models.CharField(max_length=1, choices=(("m", "Male"), ("f", "Female")))
    dob = models.DateTimeField(null=True, blank=True)
    is_lost = models.BooleanField(default=False)
    other_details = models.TextField(null=True, default='{"":""}')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __unicode__(self):
        return "%s : %s" % (self.owner.username, self.name)


class PetPhoto(models.Model):
    pet = models.ForeignKey("PetPhoto")
    url = models.CharField(max_length=500)
    height = models.FloatField(default=0.0)
    width = models.FloatField(default=0.0)
    is_primary = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return unicode(self.created_at)