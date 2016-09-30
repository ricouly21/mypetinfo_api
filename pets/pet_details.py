from __future__ import unicode_literals

from django.db import models


class PetVital(models.Model):
    pet = models.ForeignKey("PetProfile")
    height = models.FloatField(null=True, default=0.0)
    weight = models.FloatField(null=True, default=0.0)
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s : %s" % (self.pet.name, self.modified_at)


class TrainingCategory(models.Model):
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Training Categories"

    def __unicode__(self):
        return unicode(self.title)


class PetTraining(models.Model):
    pet = models.ForeignKey("pets.PetProfile")
    category = models.ForeignKey("TrainingCategory")
    is_certified = models.BooleanField(default=False)
    registration_no = models.CharField(max_length=250)
    date_certified = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Special Training"
        verbose_name_plural = "Special Trainings"

    def __unicode__(self):
        return "%s_%s" % (self.pet.name, self.created_at)


class PetTrainingPhoto(models.Model):
    training = models.ForeignKey("PetTraining")
    url = models.CharField(max_length=500)
    height = models.FloatField(default=0.0)
    width = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return unicode(self.created_at)


class PetInsurance(models.Model):
    pet = models.ForeignKey("pets.PetProfile")
    reference_no = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    other_details = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Insurance"
        verbose_name_plural = "Insurances"

    def __unicode__(self):
        return "%s_%s" % (self.pet.name, self.created_at)


class PetInsurancePhoto(models.Model):
    insurance = models.ForeignKey("PetInsurance")
    url = models.CharField(max_length=500)
    height = models.FloatField(default=0.0)
    width = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return unicode(self.created_at)


class MissingPetAlert(models.Model):
    pet = models.ForeignKey("pets.PetProfile")
    title = models.CharField(max_length=250)
    contact_info = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return unicode(self.pet.name)