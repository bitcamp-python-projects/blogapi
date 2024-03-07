import os
import sys
import django
from timeit import timeit

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogapi.settings')

django.setup()

from blog import models

def query_posts_ordered_by_created_at():
    return list(models.Post.objects.order_by('created_at'))

number_of_executions = 100

time_taken = timeit('query_posts_ordered_by_created_at()', globals=globals(), number=number_of_executions)
average_time = time_taken / number_of_executions
print(f"Average time per ordered query : {average_time} seconds")
