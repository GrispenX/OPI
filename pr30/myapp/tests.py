from django.test import TestCase
from django.urls import reverse

from .models import TodoItem


class TodoListTests(TestCase):
	def test_can_add_and_toggle_todo(self):
		response = self.client.post(
			reverse("todo-list"),
			{"action": "add", "title": "Buy milk", "prefix": "VIP-"},
		)
		self.assertRedirects(response, reverse("todo-list"))
		todo = TodoItem.objects.get()
		self.assertEqual(todo.title, "Buy milk")
		self.assertEqual(todo.prefix, "VIP-")
		self.assertFalse(todo.completed)

		response = self.client.post(
			reverse("todo-list"),
			{"action": "toggle", "todo_id": str(todo.pk)},
		)
		self.assertRedirects(response, reverse("todo-list"))
		todo.refresh_from_db()
		self.assertTrue(todo.completed)

	def test_missing_prefix_defaults_to_default(self):
		self.client.post(reverse("todo-list"), {"action": "add", "title": "No prefix"})
		todo = TodoItem.objects.get()
		self.assertEqual(todo.prefix, "default")
		response = self.client.get(reverse("todo-list"))
		self.assertContains(response, "<span class=\"prefix-badge\">default</span>", html=False)

	def test_request_modifier_updates_rendered_context(self):
		response = self.client.get(reverse("todo-list") + "?source=tablet&prefix=VIP-")
		self.assertContains(response, "Request source set by middleware: tablet")
		self.assertContains(response, "Current prefix value: VIP-")

	def test_blocked_path_is_forbidden(self):
		response = self.client.get("/blocked/")
		self.assertEqual(response.status_code, 403)
