# Steel Rumors

I followed the tutorial from [here](http://arunrocks.com/building-a-hacker-news-clone-in-django-part-1/). I used Django 1.7 and a few things had to be modified.

### Things needed to be changed
- `django.contrib.sites` in `settings.py`
- `SITE_ID = 1` also in `settings.py`
- `django-registration-redux` instead of `django-registration` (in `requirements.txt`)