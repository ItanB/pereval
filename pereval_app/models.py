from django.db import models


class Users(models.Model):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=12)
    fam = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    otc = models.CharField(max_length=30, null=True)

    def __str__(self):
        return f'{self.fam}'


class Coords(models.Model):
    latitude = models.FloatField(max_length=5, blank=True)
    longitude = models.FloatField(max_length=5, blank=True)
    height = models.IntegerField(max_length=5, blank=True)


class Season(models.Model):
    LEVELS = [
        ('', 'не указано'),
        ('1A', '1a'),
        ('1B', '1б'),
        ('2А', '2а'),
        ('2В', '2б'),
        ('3А', '3а'),
        ('3В', '3б'),
    ]

    winter = models.CharField(max_length=2, choices=LEVELS)
    spring = models.CharField(max_length=2, choices=LEVELS)
    summer = models.CharField(max_length=2, choices=LEVELS)
    autumn = models.CharField(max_length=2, choices=LEVELS)

    def __str__(self):
        return f'зима:{self.winter}, лето:{self.summer}, весна:{self.spring}, осень:{self.autumn}'


class PerevalImage(models.Model):
    image = models.ImageField(upload_to='media/', null=True, blank=True)


class PerevalAdded(models.Model):
    STATUS = [
        ('new', 'новый'),
        ('pending', 'на модерации'),
        ('accepted', 'принят'),
        ('rejected', 'не принят'),
    ]

    BEAUTYTITLE = [
        ('poss', 'перевал'),
        ('gorge', 'ущелье'),
        ('plateau', 'плато'),
    ]

    users = models.ForeignKey(Users, on_delete=models.CASCADE)
    beautyTitle = models.CharField(max_length=20, choices=BEAUTYTITLE)
    title = models.CharField(max_length=50)
    other_titles = models.CharField(max_length=30)
    connect = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)
    coords = models.ForeignKey(Coords, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    images = models.ForeignKey(PerevalImage, on_delete=models.CASCADE, default=0)
    status = models.CharField(max_length=20, choices=STATUS, default='new')

    def __str__(self):
        return f'{self.title}'
