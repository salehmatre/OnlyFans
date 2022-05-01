from .models import *
from django.db import connection, reset_queries
import time
import functools
from django.shortcuts import render


def get_query(func):
    def wrapper(obj, *args, **kwargs):
        try:
            obj.comments = Comments.objects.select_related("post").filter(post=kwargs.get('pk', 0)).order_by('-sent_at')
            obj.reply_to_comments = ReplyToComment.objects.select_related("post").filter(
                post=kwargs.get('pk', 0)).order_by('-sent_at')
            obj.reply_to_reply = ReplyToReply.objects.select_related("post").filter(post=kwargs.get('pk', 0)).order_by(
                '-sent_at')
            return func(obj, *args, **kwargs)
        except (Comments.DoesNotExist, ReplyToComment.DoesNotExist,
                ReplyToReply.DoesNotExist):
            return render(*args, 'errors/500.html')

    return wrapper


def query_debugger(func):
    @functools.wraps(func)
    def inner_func(*args, **kwargs):
        reset_queries()

        start_queries = len(connection.queries)

        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        end_queries = len(connection.queries)

        print(f"Function : {func.__name__}")
        print(f"Number of Queries : {end_queries - start_queries}")
        print(f"Finished in : {(end - start):.2f}s")
        return result

    return inner_func
