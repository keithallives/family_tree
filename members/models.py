from django.db import models
from datetime import datetime

class Member(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(
        max_length=1,
        choices=(('M', 'Male'), ('F', 'Female')),
        blank=False,
        default=None
        )
    birth_date = models.DateField()
    birth_place = models.CharField(max_length=100)
    is_living = models.BooleanField(default=True)
    mother = models.ForeignKey(
        'self',
        models.SET_NULL,
        blank=True,
        null=True,
        limit_choices_to={'gender': 'F'},
        related_name='children_of_mother',
        )
    father = models.ForeignKey(
        'self',
        models.SET_NULL,
        blank=True,
        null=True,
        limit_choices_to={'gender': 'M'},
        related_name='children_of_father',
        )
    date_added = models.DateTimeField(default=datetime.now)


    # def full_name(self):
    #     return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Marriage(models.Model):
    husband = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        limit_choices_to={'gender': 'M'},
        related_name='husband_of',
        )
    wife = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        limit_choices_to={'gender': 'F'},
        related_name='wife_of',
        )
    date = models.DateField()
    location = models.CharField(max_length=250)


    def __str__(self):
        return f'{self.husband.first_name} & {self.wife.first_name}'

