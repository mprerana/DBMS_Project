import os
from .models import Message
from django.contrib.auth.models import User
from django.db.models import Q


def unique(sequence):
    seen = set()
    return [x for x in sequence if not (x[0].username in seen or seen.add(x[0].username))]

def log_message(sender,roomname,message):
    Message.objects.create(sender=User.objects.get(username=sender),roomname=roomname,message=message,receiver=User.objects.get(username=receiver_gen(sender,roomname)))

def load_log(roomname):
    return Message.objects.filter(roomname=roomname)

def roomname_gen(username1,username2):
    return "".join(sorted([username1,username2]))


def print_path():
    print(os.path.abspath(__file__))