import sys
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


def print_usage():
    print("""
Usage: ./gp-edit [action] [section]
    """)

def list_tasks(d):
    print("Define how Gitpod prepares & builds your project and how it can start the project’s development server(s).\n\nTasks:")
    for t in d['tasks']:
        try:
            print(t['name'])
        except KeyError:
            print("Unnamed Task")

def add_tasks(d):
    print("Define how Gitpod prepares & builds your project and how it can start the project’s development server(s).\n\nTasks:")
    t = {}
    t['name'] = input("Name (Name your task)> ")
    t['before'] = input("Before (A shell command to run before init and the main command)> ")
    t['init'] = input("Init (A shell command to run between before and the main command)> ")
    t['command'] = input("Command (The main shell command to run after before and init)> ")
    t['openMode'] = input("Terminal open mode (tab-after, tab-before, split-right, split-left)> ")
    d['tasks'].append(t)
    open(".gitpod.yml", 'w').write(dump(d, Dumper=Dumper))


initial = load(open(".gitpod.yml"), Loader=Loader)

if len(sys.argv) < 3:
    print("ERROR: gp-edit requires 3 positional arguments")
    print_usage()

elif sys.argv[1] == "list":
    if sys.argv[2] == "tasks":
        list_tasks(initial)

elif sys.argv[1] == "add":
    if sys.argv[2] == "tasks":
        add_tasks(initial)

