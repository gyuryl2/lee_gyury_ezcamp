from django.db import models
from django.db.models import UniqueConstraint
from django.urls import reverse


class Period(models.Model):
    period_id = models.AutoField(primary_key=True)
    period_sequence = models.IntegerField(unique=True)
    period_name = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return '%s' % self.period_name

    class Meta:
        ordering = ['period_sequence']


class Year(models.Model):
    year_id = models.AutoField(primary_key=True)
    year = models.IntegerField(unique=True)

    def __str__(self):
        return '%s' % self.year

    class Meta:
        ordering = ['year']


class Session(models.Model):
    session_id = models.AutoField(primary_key=True)
    year = models.ForeignKey(Year, related_name='session', on_delete=models.PROTECT)
    period = models.ForeignKey(Period, related_name='session', on_delete=models.PROTECT)

    def __str__(self):
        return '%s - %s' % (self.year.year, self.period.period_name)

    def get_absolute_url(self):
        return reverse('courseinfo_session_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('courseinfo_session_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('courseinfo_session_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['year__year', 'period__period_sequence']
        constraints = [
            UniqueConstraint(fields=['year', 'period'], name='unique_session')
        ]


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_number = models.CharField(max_length=20)
    course_name = models.CharField(max_length=255)

    def __str__(self):
        return '%s - %s' % (self.course_number, self.course_name)

    def get_absolute_url(self):
        return reverse('courseinfo_course_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('courseinfo_course_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('courseinfo_course_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['course_number', 'course_name']
        constraints = [
            UniqueConstraint(fields=['course_number', 'course_name'], name='unique_course')
        ]


class Counselor(models.Model):
    counselor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    disambiguator = models.CharField(max_length=45, blank=True, default='')

    def __str__(self):
        result = ''
        if self.disambiguator == '':
            result = '%s, %s' % (self.last_name, self.first_name)
        else:
            result = '%s, %s (%s)' % (self.last_name, self.first_name, self.disambiguator)
        return result

    def get_absolute_url(self):
        return reverse('courseinfo_counselor_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('courseinfo_counselor_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('courseinfo_counselor_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['last_name', 'first_name', 'disambiguator']
        constraints = [
            UniqueConstraint(fields=['last_name', 'first_name', 'disambiguator'], name='unique_counselor')
        ]


class Camper(models.Model):
    camper_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    disambiguator = models.CharField(max_length=45, blank=True, default='')

    def __str__(self):
        result = ''
        if self.disambiguator == '':
            result = '%s, %s' % (self.last_name, self.first_name)
        else:
            result = '%s, %s (%s)' % (self.last_name, self.first_name, self.disambiguator)
        return result

    def get_absolute_url(self):
        return reverse('courseinfo_camper_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('courseinfo_camper_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('courseinfo_camper_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['last_name', 'first_name', 'disambiguator']
        constraints = [
            UniqueConstraint(fields=['last_name', 'first_name', 'disambiguator'],
                             name='unique_camper')
        ]


class Cabin(models.Model):
    cabin_id = models.AutoField(primary_key=True)
    cabin_name = models.CharField(max_length=20)
    session = models.ForeignKey(Session, related_name='cabins', on_delete=models.PROTECT)
    course = models.ForeignKey(Course, related_name='cabins', on_delete=models.PROTECT)
    counselor = models.ForeignKey(Counselor, related_name='cabins', on_delete=models.PROTECT)

    def __str__(self):
        return '%s - %s (%s)' % (self.course.course_number, self.cabin_name, self.session.__str__())

    def get_absolute_url(self):
        return reverse('courseinfo_cabin_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('courseinfo_cabin_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('courseinfo_cabin_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['course', 'cabin_name', 'session']
        constraints = [
            UniqueConstraint(fields=['session', 'course', 'cabin_name'], name='unique_cabin')
        ]


class Registration(models.Model):
    registration_id = models.AutoField(primary_key=True)
    camper = models.ForeignKey(Camper, related_name='registrations', on_delete=models.PROTECT)
    cabin = models.ForeignKey(Cabin, related_name='registrations', on_delete=models.PROTECT, default=1)

    def __str__(self):
        return '%s / %s' % (self.cabin, self.camper)

    def get_absolute_url(self):
        return reverse('courseinfo_registration_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('courseinfo_registration_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('courseinfo_registration_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['cabin', 'camper']
        unique_together = (('cabin', 'camper'),)
        constraints = [
            UniqueConstraint(fields=['cabin', 'camper'],
                             name='unique_registration')
        ]
