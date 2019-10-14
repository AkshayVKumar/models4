#setting up the Django environment
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","P6.settings")

#setting up the django platform
import django
django.setup()

#population area is going to start
from myapp.models import *
import random
from faker import Faker
topics=["Social Media","Music","Videos","Sports","News"]
f=Faker()
def add_topics():
    t=Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    t.save()
    return t
    
def add_webpages(webpagename,url):
    top_name=add_topics()
    w=Webpage.objects.get_or_create(topic_name=top_name,\
        name=webpagename,url=url)[0]
    w.save()
    return w

def add_record(webpagename,url,date):
    w=add_webpages(webpagename,url)
    a=Access_Records.objects.get_or_create(name=w,date=date)[0]
    a.save()

def add_data(N=10):
    for i in range(N):
        fake_name=f.first_name()
        fake_url=f.url()
        fake_date=f.date()
        add_record(fake_name,fake_url,fake_date)
if __name__=="__main__":
    print("data tranferring is started")
    add_data()
    print("data tranferring ended")

























