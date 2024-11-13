from django.db import models
# Create your models here.


class Category(models.Model):
    '''room types'''
    
    name = models.CharField(
        max_length=30,unique=True)
    description = models.TextField()
    max_occupants = models.IntegerField()
    image_url = models.ImageField(
        null=True, blank=True, upload_to='category/', default='default-category.png')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['name', 'max_occupants']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def save(self, *args, **kwargs):
        '''when image gets deleted set the default image as the image'''
        if self.image_url is None:
            self.image_url = 'default-category.png'
        super().save(*args, **kwargs)


class Room(models.Model):
    room_number = models.CharField(
        max_length=10, unique=True, help_text='e.g 101,102')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='rooms')
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    bed_type = models.CharField(
        max_length=100, null=True, blank=True, help_text='E.g., "King Size", "Queen Size"')  #
    floor = models.IntegerField(
        null=True, blank=True, help_text='e.g ground floor, fist floor')
    image_url = models.ImageField(
        null=True, blank=True, upload_to='room/', default='default-room.png',
        # validators=[validate_file_size],
        help_text='upload a suitable image.')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['is_available', 'room_number', 'price_per_night']

    def __str__(self):
        return f"Room {self.room_number} ({self.category.name})"

    def book(self):
        """Set the room as unavailable after booking"""
        self.is_available = False
        self.save()

    def save(self, *args, **kwargs):
        '''when image gets deleted set the default image as the image'''
        if self.image_url is None:
            self.image_url = 'default-room.png'
        super().save(*args, **kwargs)
