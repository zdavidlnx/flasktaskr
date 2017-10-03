from fabric.api import local, settings, abort
from fabric.contrib.console import confirm


# prep
def test():
    with settings(warn_only=True):
        result = local("nosetests -v", capture=True)
    if result.failed and not confirm('Test failed. Continue?'):
        abort("Aborted at user promp")


def commit():
    message = input("Enter a git commit message: ")
    local("git add .")
    local('git commit -am "{}"'.format(message))


def push():
    local("git push origin master")


def prepare():
    test()
    commit()
    push()
