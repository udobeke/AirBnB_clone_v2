from fabric.api import *

env.hosts = ['ubuntu@54.81.120.113', 'ubuntu@334.229.136.16']

def copy():
    put('0-setup_web_static.sh', '~/')
