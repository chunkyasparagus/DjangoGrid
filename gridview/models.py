from django.db import models


class Gender(models.Model):
    GENDERS = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
    )
    gender = models.CharField(max_length=6, choices=GENDERS)

    def __str__(self):
        return self.gender

    def __repr__(self):
        return self.__str__()


class Person(models.Model):
    name = models.CharField(max_length=30, default='')
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'people'

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


class Bond(models.Model):
    bonder = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='bonder')
    bondee = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='bondee')
    bond_level = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.bonder} vs {self.bondee}'

    def __repr__(self):
        return self.__str__()

