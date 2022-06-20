from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
title = models.CharField(max_length=200,)
    text = models.TextField()
    author = models.get_user_model()
    Created_date = models.DateTimeField()
    Published_date = models.DateTimeField()