from fabric.api import env
from fabric.contrib.project import rsync_project
from fabric.decorators import hosts

#env.hosts=['bre@192.168.11.25']
#env.password=('192.168.11.25', 'bre@daydayup')
env.passwords = {'root@192.168.3.150:3222': 'rootforbre'}


@hosts('bre@192.168.11.25')
def sync_breconf():
    ldir = '/home/zhiyong.liu/code/svn/brewebconf'
    rdir = '/home/bre/pyenv'
    edir = ['*.pyc', '*.log']
    rsync_project(local_dir=ldir, remote_dir=rdir, exclude=edir, delete=True)

@hosts('bre@192.168.11.25')
def sync_rest():
    ldir = '/home/zhiyong.liu/code/svn/UtilService'
    rdir = '/home/bre/pyrestenv'
    edir = ['*.pyc', '*.log']
    rsync_project(local_dir=ldir, remote_dir=rdir, exclude=edir, delete=True)

@hosts('bre@192.168.3.150:3222')
def conf2test():
    ldir = '/home/zhiyong.liu/code/svn/brewebconf'
    rdir = '/opt/bre/pyenv'
    edir = ['*.pyc', '*.log']
    rsync_project(local_dir=ldir, remote_dir=rdir, exclude=edir, delete=True)

