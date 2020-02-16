from django.db import models


# About Model
class About(models.Model):
    short_description = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to="about")

    class Meta:
        verbose_name = "About me"
        verbose_name_plural = "About me"

    def __str__(self):
        return "About me"


# contactus Model
class ContactUs(models.Model):
    name = models.CharField(max_length=100, verbose_name="Contact Us")
    description = models.TextField(verbose_name="Contact Us")

    def __str__(self):
        return self.name


# Recent Work Model
class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name="Blog")
    image = models.ImageField(upload_to="Blog")

    def __str__(self):
        return self.title


# Reading Model
class Reading(models.Model):
    name = models.CharField(max_length=100, verbose_name="Reading ")
    description = models.TextField(verbose_name="Reading ")
    image = models.ImageField(upload_to="Reading", default="default.png")

    def __str__(self):
        return self.name
