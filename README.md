#Steroids
## 
**Steroids** provides a set of scripts to **help developers** to build their **real-time ready**, **non-blocking**, **python web application** reducing efforts and time.

In other words: Python Flask with Steroids

##Quick install
If you are using Unix-like OS, to install Steroids use this command, right from your terminal:

    curl http://projects.setale.me/Steroids/install | sh

In case the machine some requirements, the script will do it for you.

##Quick Use
To generate a new project with examples use this command:

    steroids init ProjectName --examples=True

If you need help you can use:

    steroids --help

## Structure
The structure of a Project built on Steroids is derived from Flask one. It provides Objects, Statics file, Views, Templates, Custom Decorators and others.

*insert tree here*

This structure give a lot of freedom to developers: they can modify it without problems. Steroids structure is just an ordered way to create web services in python.

##Defaults Modules
  * [Tornado](http://www.tornadoweb.org/)
  * [Flask](http://flask.pocoo.org/)
  * [MongoDB](http://www.mongodb.org/)
  * [APScheduler](http://pythonhosted.org/APScheduler/)
  * [Honcho](https://pypi.python.org/pypi/honcho) / [Foreman](http://ddollar.github.io/foreman/)
 
Using **Tornado** combined with Python Flask, Steroids help developer to create a non-blocking, real-time ready web server. 

**MongoDB** is used as default database: is an advantage to save python objects in MongoDB.

**APScheduler** helps to create cron or scheduled jobs. 

Foreman/Honcho helps to manage the server ( *it also generates init scripts if needed* ).

Once the Steroids structure is created, every developer can modify files in base of his needs. For example you can avoid MongoDB and use other modules.