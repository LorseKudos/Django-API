import uuid
from django.db import models

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return str(self.id)

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=100, blank=False)
    parent_post_id = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)
    comment_count = models.PositiveIntegerField(default=0)
    posted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('posted_at',)

    def __str__(self):
        return self.text
