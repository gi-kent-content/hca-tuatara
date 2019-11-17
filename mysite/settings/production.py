# -*- coding: utf-8 -*-
from .base import *

DEBUG = False
 
ALLOWED_HOSTS = ["tuatara.data.humancellatlas.org", "hgwdev.gi.ucsc.edu", "3.15.142.222", "127.0.0.1", "172.31.12.176"]

# Settings to better secure the cookies from security exploits
# since we are serving production deployment over https
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

STATIC_ROOT="/home/ec2-user/hca-tuatara/static"

INSTALLED_APPS += 'mod_wsgi.server'

MEDIA_ROOT = '/home/ec2-user/hca-tuatara/media'
