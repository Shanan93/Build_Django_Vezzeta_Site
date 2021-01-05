from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.utils.text import slugify

TYPE_OF_PERSON = (
    ('M',"Male"),
    ('F',"Female"),
)


# Create your models here.
class Profile(models.Model):
    """Model definition for Profile."""
    
    DIR_IN = {
        ('طب الأطفال',"طب الأطفال"),
        ('طب الأنف والأذن والحنجرة',"طب الأنف والأذن والحنجرة"),
        ('طب التوليد والنسائيات',"طب التوليد والنسائيات"),
        ('طب الجهاز البولي',"طب الجهاز البولي"),
        ('طب الطوارئ',"طب الطوارئ"),
        ('طب الطوارئ الدولي',"طب الطوارئ الدولي"),
        ('طب العيون',"طب العيون"),
        ('طب باطني',"طب باطني"),
        ('أسنان',"أسنان"),

    }
    
    user  = models.OneToOneField( User, verbose_name=_("user"), on_delete=models.CASCADE)
    name = models.CharField(_("الاسم: "), max_length=50)
    subtitle = models.CharField(_("نبذه عنك: "), max_length=50)
    adress = models.CharField(_("المحافظة: "), max_length=50)
    adress_details = models.CharField(_("العنوان بالتفصيل: "), max_length=50)
    phone_number = models.CharField(_("الهاتف"), max_length=50)
    working_hours = models.CharField(_("عدد ساعات العمل: "), max_length=50)
    waiting_time = models.IntegerField(_("مدة الانتظار "),blank=True, null=True)
    doctor_specialist = models.CharField(_("متخصص في؟"), max_length=50,blank=True, null=True)
    who_i = models.TextField(_("من أنا: "), max_length=50)
    price = models.IntegerField(_("سعر الكشف"),blank=True, null=True)
    facebook = models.CharField(max_length=50,blank=True, null=True)
    twittre = models.CharField(max_length=50,blank=True, null=True)
    google = models.CharField(max_length=50,blank=True, null=True)
    join_new = models.DateField(_("وقت الإنضمام :"), auto_now_add=True)
    type_of_person = models.CharField(_("النوع"),choices=TYPE_OF_PERSON, max_length=50)
    image = models.ImageField(_("الصورة الشخصية"), upload_to='profile',blank=True, null=True)
    slug = models.SlugField(_("slug"), blank=True, null=True)
    doctor = models.CharField(_("دكتور ؟"),choices=DIR_IN, max_length=50,blank=True, null=True)
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        
        super(Profile,self).save(*args,**kwargs)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Profile."""

        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        """Unicode representation of Profile."""
        return '%s' %(self.user.username)


def creat_profile(sender, **kwargs):
    
    if kwargs['created']:
        Profile.objects.create(user = kwargs['instance'])


post_save.connect(creat_profile, sender= User)      

    # TODO: Define custom methods here
