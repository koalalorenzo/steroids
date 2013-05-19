#Steroids
## 
**Steroids** is a set of tools to **help python developers** to build **real-time ready**, **non-blocking**, **web application** reducing efforts and time.

##Quick install
If you are using Unix-like OS, to install Steroids use this command, right from your terminal:

    curl http://projects.setale.me/Steroids/install | bash

In case the machine some requirements, the script will do it for you.

##Quick Use
To generate a new project with examples use this command:

    steroids init ProjectName --examples=True

If you need help you can use:

    steroids --help
    
You can specify to use small group of modules:

    steroids init ProjectName --modules flask mongodb --examples=True

## Structure
The structure of a Project built on Steroids is derived from Flask one. It provides Objects, Statics file, Views, Templates, Custom Decorators and others.

The following structure is based on the default modules used: Flask, MongoDB, Tornado and Honcho.

    ./configuration.py          # Configuration File
    ./server.py                 # script to start Server
    ./tornado.py                # script to start Tornado Server
    ./clock.py                  # script to start the Scheduler
    ./Procfile                  # Foreman/Honcho file
    ./requirements.txt          # python packages required
    ./project/                  # Where the magic happens
             /__init__.py       # Server declarations 
             /conventions.py    # Generic conventions
             /database.py       # Database conventions
             /decorators.py     # Common decorators 
             /views/            # Directory of Views
             /templates/        # Directory of Templates and HTML files
             /static/           # Directory of static files
             /objects/          # Directory of Objects
                     /Master.py # Objects should be derived from Master
               

This structure give a lot of freedom to developers: they can modify it without problems adapting the structure in base of what they do. Steroids structure is just an ordered way to create web services in python.

To **understand the structure** is suggested to enable the **examples** when initalizing a project.

## Modules
These are the current modules available

  * [Tornado](http://www.tornadoweb.org/)
  * [Flask](http://flask.pocoo.org/)
  * [MongoDB](http://www.mongodb.org/)
  * [APScheduler](http://pythonhosted.org/APScheduler/)
  * [Honcho](https://pypi.python.org/pypi/honcho) / [Foreman](http://ddollar.github.io/foreman/)
 
Using **Tornado** combined with Python Flask, Steroids help developer to create a non-blocking, real-time ready web server. 

**MongoDB** is used as default database: is an advantage to save python objects in MongoDB.

**APScheduler** helps to create cron or scheduled jobs. 

Foreman/Honcho helps to manage the server ( *it also generates init scripts if needed* ).

Once the Steroids structure is created, every developer can modify files in base of his needs. For example you can avoid MongoDB and use a different database type.

## License
Steroids is licensed under a Creative Commons Attribution-ShareAlike 3.0 Unported License. To view a copy of this license, visit [http://creativecommons.org/licenses/by-sa/3.0/](http://creativecommons.org/licenses/by-sa/3.0/)

## Liks

  * Project Site: [http://projects.setale.me/Steroids](http://projects.setale.me/Steroids)
  * GitHub: [https://github.com/koalalorenzo/Steroids](https://github.com/koalalorenzo/Steroids)
  * PyPi page: [https://pypi.python.org/pypi/steroids/](https://pypi.python.org/pypi/steroids/)    
  * Author Website: [http://who.is.lorenzo.setale.me/?](http://setale.me/)
  * Author Blog: [http://blog.setale.me/](http://blog.setale.me/)
