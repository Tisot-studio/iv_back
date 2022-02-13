from django.db import models


class Release(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    cover = models.ImageField(upload_to='track_covers', null=True, blank=True)
    date_of_release = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ('-date_of_release',)

    
    def __str__(self):
        return str(self.title)


class Link(models.Model):
    release = models.OneToOneField(Release, on_delete=models.CASCADE, null=True)
    spotify = models.URLField(null=True)
    beatport = models.URLField(null=True)
    itunes = models.URLField(null=True)
    soundcloud = models.URLField(null=True)


    def __str__(self):
        return str(self.release)


class Podcast(models.Model):
    podId = models.AutoField(primary_key=True, editable=False)
    cover = models.ImageField(upload_to='podcast_covers', null=True, blank=True)
    header = models.CharField(max_length=100, null=True, blank=True)
    episode = models.CharField(max_length=100, null=True, blank=True)
    color = models.CharField(max_length=100, null=True, blank=True)
    tracklist = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    audio = models.FileField(upload_to='audio', null=True, blank=True)


    def __str__(self):
            return str(self.header + self.episode)

    class Meta:
        ordering = ('-episode',)