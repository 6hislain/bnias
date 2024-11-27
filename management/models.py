from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Citizen(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    birth_date = models.DateField(auto_now=False, auto_now_add=False)
    phone = models.IntegerField()
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    mother = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, related_name="child_of_mother"
    )
    father = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, related_name="child_of_father"
    )

    def __str__(self):
        return self.first_name + " " + self.last_name


class Province(models.Model):
    name = models.CharField(max_length=30)
    head = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Commune(models.Model):
    name = models.CharField(max_length=30)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, null=True)
    chief = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.province.name + " -> " + self.name


class Colline(models.Model):
    name = models.CharField(max_length=30)
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE, null=True)
    chief = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return (
            self.commune.province.name + " -> " + self.commune.name + " -> " + self.name
        )


class LostIdCardReport(models.Model):
    report = models.TextField(null=True)
    date = models.DateField(auto_now=True)
    citizen = models.ForeignKey(Citizen, on_delete=models.CASCADE, null=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, null=True)
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE, null=True)
    colline = models.ForeignKey(Colline, on_delete=models.CASCADE, null=True)


class Publication(models.Model):
    title = models.CharField(max_length=20)
    files = models.FileField(upload_to="publication/")
    pub_date = models.DateField(auto_now=False, auto_now_add=False)


class RegisteredIdCardApplication(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    birth_date = models.DateField(auto_now=False, auto_now_add=False)
    email = models.CharField(max_length=50)
    phone = models.IntegerField()
    picture = models.ImageField(upload_to="applicants/")
    residence = models.CharField(max_length=50)
    is_approved = models.BooleanField(default=False)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, null=True)
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE, null=True)
    colline = models.ForeignKey(Colline, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class RegisteredIdCard(models.Model):
    citizen = models.ForeignKey(Citizen, on_delete=models.CASCADE, null=True)
    applicant = models.ForeignKey(
        RegisteredIdCardApplication, on_delete=models.CASCADE, null=True
    )


class Service(models.Model):
    name = models.CharField(max_length=20)
    requirement = models.TextField()

    def __str__(self):
        return self.name
