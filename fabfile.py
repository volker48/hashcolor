from fabric.api import run, cd, sudo

def deploy():
    with cd('/var/www/hashcolor'):
        run('git pull')
        sudo('supervisorctl restart hashcolor')