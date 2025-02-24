from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _




class About(models.Model):
    """
    Stores basic information about you for the 'About Me' section.
    You can add or remove fields as needed.
    """
    Aname = models.CharField(_('Name'),max_length=100)
    Ajop_name = models.CharField(_('Jop Name'),max_length=100,null=True,blank=True)
    Adate_of_birth = models.DateField(_('Date of birth'))
    Aaddress = models.CharField(_('Address'),max_length=200)
    Azip_code = models.CharField(_('Zip Code '),max_length=20)
    Aemail = models.EmailField(_('Email'))
    Aphone = models.CharField(_('Phone'),max_length=20)
    Aabout_text = models.TextField(_('Description'),help_text="Short bio or introduction")
    Aprofile_image = models.ImageField(_('Image'),upload_to='about/', blank=True, null=True)

    def __str__(self):
        return self.Aname


from django.db import models

class ResumeItem(models.Model):
    # A choice field to distinguish Education vs. Experience
    TYPE_CHOICES = [
        ('education', 'Education'),
        ('experience', 'Experience'),
    ]
    RIitem_type = models.CharField(_('Type'),max_length=20, choices=TYPE_CHOICES)

    # Shared fields
    RItitle = models.CharField(_('Title'),max_length=200, help_text="Degree or Position")
    RIinstitution_or_company = models.CharField(_('Institution or Company'),max_length=200)
    RIfrom_year = models.IntegerField(_('From'))
    RIto_year = models.IntegerField(_('To'))
    RIdescription = models.TextField(_('Description'))

    def __str__(self):
        return f"{self.get_RIitem_type_display()}: {self.RItitle}"



class Service(models.Model):
    """
    For the 'Services' section.
    """
    Stitle = models.CharField(_('Title'),max_length=100)
    Sdescription = models.TextField(_('Description'))


    def __str__(self):
        return self.Stitle


class Skill(models.Model):
    """
    For the 'Skills' section.
    """
    Sname = models.CharField(_('Name'),max_length=100)
    Sproficiency = models.PositiveIntegerField(_('Proficiency'),
        help_text="Percentage (0-100)."
    )

    def __str__(self):
        return f"{self.Sname} ({self.Sproficiency}%)"


def project_image_upload(instance, filename):
    image_name, extension = filename.split(".")
    return "Project Images/%s/%s.%s" % (instance.Ptitle, instance.Ptitle, extension)



class Project(models.Model):
    """
    For the 'Projects' section.
    """
    Ptitle = models.CharField(_('Title'),max_length=200)
    Pdescription = models.TextField(_('Description'))
    Pimage = models.ImageField(_('Images'),upload_to=project_image_upload, blank=True, null=True)
    Pcategory = models.CharField(_('Category'),max_length=100, blank=True, null=True)
    Pproject_url = models.URLField(_('Project Url'),blank=True, null=True)

    def __str__(self):
        return self.Ptitle


from django.db import models

class SiteStatistic(models.Model):
    SSawards = models.PositiveIntegerField(_('Awards'),default=0)
    SScomplete_projects = models.PositiveIntegerField(_('Complate Projects'),default=0)
    SShappy_customers = models.PositiveIntegerField(_('Happy Customers'),default=0)
    SScups_of_coffee = models.PositiveIntegerField(_('Cups of Coffee'),default=0)

    def __str__(self):
        return "Site Statistics"




class BlogPost(models.Model):
    """
    For the 'My Blog' section.
    """
    BPtitle = models.CharField(max_length=200)
    BPslug = models.SlugField(unique=True)
    BPcontent = models.TextField()
    BPimage=models.ImageField(_('image'),upload_to='blog_posts/',null=True,blank=True)
    BPcreated_at = models.DateTimeField(auto_now_add=True)
    BPupdated_at = models.DateTimeField(auto_now=True)

    # Optionally add fields like author, featured image, etc.

    def __str__(self):
        return self.BPtitle


class ContactMessage(models.Model):
    """
    For storing messages from the contact form.
    """
    CMname = models.CharField(max_length=100)
    CMemail = models.EmailField()
    CMsubject = models.CharField(max_length=200)
    CMmessage = models.TextField()
    CMnamecreated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.CMname} - {self.CMsubject}"

