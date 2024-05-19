from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=60)

    def __str__(self):
        return self.title


class Todo(models.Model):
    title = models.CharField(max_length=60)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name="todos", blank=True)

    class Meta:
        ordering = ["completed", "-created_at"]

    def __str__(self):
        return f"{self.title} - {self.completed}"
