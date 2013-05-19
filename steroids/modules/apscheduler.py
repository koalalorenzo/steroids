import os

__help__ = """
"""

requirements = [
    "apscheduler"
]

directories = [
    "[base]",
    "[base]/[name]",
    ]

files = [
    "[base]/clock.py",
    "[base]/[name]/clock.py",
    ]

def install(basepath, name):
    """
        Install apscheduler Module
    """
    
    clock_file = open(os.path.join(basepath,"clock.py"), "w")
    clock_file.write("from %s.clock import sched\n" % name)    
    clock_file.write("""
sched.start()
while True:
    if not sched.running:
        break
    sleep(30)
        
""")
    clock_file.close()

    nameclock_file = open(os.path.join(basepath,"%s/clock.py" % name), "w")    
    nameclock_file.write("import sys\n")
    nameclock_file.write("from apscheduler.scheduler import Scheduler\n")
    nameclock_file.write("\n")
    nameclock_file.write("sched = Scheduler()\n")
    nameclock_file.close()
    return
    
def install_examples(basepath, name):
    """
        Install Tornado Module with example files
    """
    nameclock_file = open(os.path.join(basepath,"%s/clock.py" % name), "a")    
    nameclock_file.write("""
# Examples APScheduler

@sched.interval_schedule(minutes=5)
def every_five_minutes():
    print "5 minutes"

@sched.cron_schedule(day='last sun')
def some_decorated_task():
    print "I am printed at 00:00:00 on the last Sunday of every month!"

# End Examples
""")
    nameclock_file.close()
    return