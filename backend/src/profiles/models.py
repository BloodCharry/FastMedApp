from django.contrib.auth.models import AbstractUser
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save


class UserNet(AbstractUser):
    """ Custom user model """
    email = models.EmailField(max_length=100, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


class Patient(models.Model):
    """ Patient model """
    GENDER = (
        ('male', 'male'),
        ('female', 'female')
    )
    ROLE = (
        ('patient', 'patient'),
        ('doctor', 'doctor')
    )

    user = models.OneToOneField(UserNet, on_delete=models.CASCADE, related_name='profile')
    verified = models.BooleanField(default=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='user/avatar/', blank=True, null=True)
    gender = models.CharField(max_length=6, choices=GENDER, default='male')
    birthday = models.DateField(blank=True, null=True)
    role = models.CharField(max_length=7, choices=ROLE, default='patient')
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.first_name

    def save(self, *args, **kwargs):
        # Track if the role is changing to 'doctor'
        role_changed_to_doctor = self.pk is not None and Patient.objects.get(
            pk=self.pk).role != 'doctor' and self.role == 'doctor'
        super().save(*args, **kwargs)
        if role_changed_to_doctor:
            Doctor.objects.create(user=self)

    @receiver(post_save, sender=UserNet)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Patient.objects.create(user=instance)

    @receiver(post_save, sender=UserNet)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Doctor(models.Model):
    """ Doctor model """
    user = models.OneToOneField(Patient, on_delete=models.CASCADE, related_name='doctor')
    bio = models.TextField(blank=True)
    specialization = models.CharField(max_length=50, blank=True)
    education = models.CharField(max_length=50, blank=True)
    certification = models.CharField(max_length=50, blank=True)
    experience = models.IntegerField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.specialization

    @receiver(post_save, sender=Patient)
    def create_doctor_profile(sender, instance, created, **kwargs):
        if created and instance.role == 'doctor':
            Doctor.objects.create(user=instance)

    @receiver(post_save, sender=Patient)
    def save_doctor_profile(sender, instance, **kwargs):
        try:
            if instance.role == 'doctor' and hasattr(instance, 'doctor'):
                instance.doctor.save()
        except Doctor.DoesNotExist:
            pass
