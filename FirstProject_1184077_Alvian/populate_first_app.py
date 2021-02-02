import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','FirstProject_1184077_Alvian.settings')

import django

django.setup()

#Fake Script
import random
from first_app_1184077.models import AccessRecord,Webpage,Topic
from faker import Faker

fakegen = Faker()
topics = ['Search','Social','News','Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t

def populate(N=10):

    for entry in range (N):
        #get the topic for the entry

        top = add_topic()
        #create the fake data
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        #create the new web page
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__=='__main__':
    print("Populating the database.... Please Wait")
    populate(7)
    print("Populating Complete!")