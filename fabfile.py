from fabric.api import run, cd, sudo
from fabric.state import env

env.use_ssh_config = True

def deploy():
    with cd('/var/www/hashcolor'):
        run('git pull')
        sudo('supervisorctl restart hashcolor')