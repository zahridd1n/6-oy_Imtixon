from django.db import models


# sayitning yuqori qismidagi email,telefon raqamlar uchun
class Head_info(models.Model):
    location = models.CharField(max_length=30)
    email = models.EmailField()
    call_center = models.CharField(max_length=255)


# asosiy sahifaning baner qismi baner rasmi fa uning matni yoziladi
class Banner(models.Model):
    image = models.ImageField(upload_to='banner/')
    title = models.CharField(max_length=100)


# titile soha haqida ,subtitle firma haqida, body ga malumotlar ajratilishi uchun vergul bilan yozish kerak
class About(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=255)
    body = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='about/')

    def __str__(self):
        return self.title


# Xizamat turlari: name xizmat nomi, detail qoshimcha, iconga esa font awsemdagi iconlar clasi yoziladi text ko'rinishida
class Service(models.Model):
    image = models.ImageField(upload_to='service/')
    name = models.CharField(max_length=100)
    detail = models.TextField()
    icon = models.CharField(max_length=255)  # font awsemdagi clarlar yozilsin


# contanct yani saytga tashrif buyurganlar o'z contaklari va xabarlarini qoldirish uchun
class Contact(models.Model):
    full_name = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)
    email = models.EmailField(null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return self.full_name


class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio/')
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=40)

    def __str__(self):
        return self.name



# workers yani ishchilar jadvalli  bu yerda job ishchining lavozimi
class Workers(models.Model):
    image = models.ImageField(upload_to='workers/')
    name = models.CharField(max_length=100)
    job = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# qilinayotkan ishlar yuritib boriladi,
class Blog(models.Model):
    image = models.ImageField(upload_to='blog/')
    body = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=30)
    avatar = models.ImageField(upload_to='blog/avatar/')
