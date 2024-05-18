from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=60)

    def __str__(self):
        return self.title


class Todo(models.Model):
    DONE = "Done"
    NOT_DONE = "Not Done"

    STATUS_CHOICES = [
        (DONE, "Done"),
        (NOT_DONE, "Not Done")
    ]

    title = models.CharField(max_length=60)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=NOT_DONE)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name="todos", blank=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title} - {self.status}"
