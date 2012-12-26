from fabric.api import run
from fabric.contrib.project import rsync_project
from fabric.decorators import hosts

LOCAL_DIR = '/home/zhiyong.liu/code/svn/bfd/ptech/rec/brewebconf/branches/branch_zhiyong.liu/src/brewebconf'

@hosts('bre@192.168.11.25')
def conf():
    ldir = LOCAL_DIR
    rdir = '/home/bre/pyenv'
    edir = ['*.pyc', '*.log', '_project', '.svn']
    rsync_project(local_dir=ldir, remote_dir=rdir, exclude=edir, delete=True)

@hosts('bre@192.168.3.150:3222')
def conf2test():
    ldir = LOCAL_DIR
    rdir = '/opt/bre/pyenv'
    edir = ['*.pyc', '*.log', '_project', '.svn', 'uwsgi.pid']
    rsync_project(local_dir=ldir, remote_dir=rdir, exclude=edir, delete=True)
    run('kill -1 `cat /opt/bre/pyenv/brewebconf/uwsgi.pid`')

@hosts('bre@alg-1:3222')
def conf2oversea():
    ldir = LOCAL_DIR
    rdir = '/opt/bre/pyenv'
    edir = ['settings.py', '*.pyc', '*.log', '_project', 'uwsgi.*', '.svn', '.json']
    rsync_project(local_dir=ldir, remote_dir=rdir, exclude=edir, delete=True)
    run('cd /opt/bre/pyenv;fab conf2oversea')

@hosts('bre@rec-1:3222')
def conf2rec():
    ldir = LOCAL_DIR
    rdir = '/opt/bre/pyenv'
    edir = ['settings.py', '*.pyc', '*.log', '_project', 'uwsgi.*', '.svn', '.json']
    rsync_project(local_dir=ldir, remote_dir=rdir, exclude=edir, delete=True)
    run('kill -1 `cat /opt/bre/pyenv/brewebconf/uwsgi.pid`')

@hosts('bre@bfd5-rec1:3222')
def conf2alg2oversea():
    ldir = '/opt/bre/pyenv/brewebconf'
    rdir = '/opt/bre/pyenv'
    edir = []
    rsync_project(local_dir=ldir, remote_dir=rdir, exclude=edir, delete=True)
    run('kill -1 `cat /opt/bre/pyenv/brewebconf/uwsgi.pid`')