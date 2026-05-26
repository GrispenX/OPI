import logging

from django.http import HttpResponseForbidden

logger = logging.getLogger(__name__)


class TodoLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger.info("Incoming %s %s", request.method, request.path)
        response = self.get_response(request)
        logger.info("Completed %s %s -> %s", request.method, request.path, response.status_code)
        return response


class TodoRequestModifierMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.todo_source = request.GET.get("source", "browser")

        prefix = request.POST.get("prefix") or request.GET.get("prefix") or "default"
        request.todo_title_prefix = prefix.strip() or "default"
        return self.get_response(request)


class BlockTodoRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == "/blocked/" or request.GET.get("block") == "1":
            return HttpResponseForbidden("This request is blocked by middleware.")
        return self.get_response(request)
