from django.db import models

class Author(models.Model):
    STATUS_CHOICES = (
        ('Inactive', 'Inactive'),
        ('Active', 'Active'),
    )
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    info = models.CharField(max_length=255)
    image = models.ImageField(upload_to='author/')
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES)
    
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='post')
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name='post')
    tag = models.ManyToManyField('Tag',related_name='post')
    file = models.ManyToManyField('File',related_name='post')
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    
    def __str__(self):
        return self.title

class File(models.Model):
    title = models.CharField(max_length=255)
    type=models.CharField(max_length=255)
    image=models.ImageField(upload_to='files/')

    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'Files'
    
    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    STATUS_CHOICES = (
        ('Inactive', 'Inactive'),
        ('Active', 'Active'),
    )
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.name

class Category(models.Model):
    title = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.title

class Navigation(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Navigation'
        verbose_name_plural = 'Navgations'

    def __str__(self):
        return self.title

class SubNavigation(models.Model):
    navigation = models.ForeignKey(Navigation, on_delete=models.CASCADE, related_name='subnav')
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'SubNavigation'
        verbose_name_plural = 'SubNavigations'

    def __str__(self):
        return self.title 

class Setting(models.Model):
    logo = models.ImageField(upload_to='logo/')
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    adress = models.CharField(max_length=255)
    copyright = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Setting'
        verbose_name_plural = 'Settings'
    
    def __str__(self):
        return 'Setting'


class Slider(models.Model):
    STATUS_CHOICES = (
        ('Inactive', 'Inactive'),
        ('Active', 'Active'),
    )
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    image = models.ImageField(upload_to='sliders/')
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES)

    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Sliders'

    def __str__(self):
        return self.title

class Social(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    iconPath = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Social'
        verbose_name_plural = 'Socials'
    
    def __str__(self):
        return self.title