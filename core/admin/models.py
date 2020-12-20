import sys
from datetime import datetime
try:
    from django.db import models
except Exception:
    print("Exception: Django Not Found, please install it with \"pip install django\".")
    sys.exit()

class Example(models.Model):
    ex = models.Charfield(max_lenght=200, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
        def __str__(self):
        return self.ex