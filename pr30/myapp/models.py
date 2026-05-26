from django.db import models


class TodoItem(models.Model):
	prefix = models.CharField(max_length=50, default="default")
	title = models.CharField(max_length=200)
	completed = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		status = "done" if self.completed else "open"
		return f"[{self.prefix}] {self.title} ({status})"
