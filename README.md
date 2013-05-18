#Steroids
## 
**Steroids** provides a set of scripts to **help developers** to build their **real-time ready**, **non-blocking**, **python web application** reducing efforts and time.

##Quick install
*not ready*

##Quick Use
*not ready*

## Structure
The structure of a Project built on Steroids is derived from Flask one. It provides Objects, Statics file, Views, Templates, Custom Decorators and others.

*insert tree here*

This structure give a lot of freedom to developers: they can modify it without problems. Steroids structure is just an ordered way to create web services in python.

##Defaults Modules
By defaults Steroids uses these modules:

  * [Tornado](http://www.tornadoweb.org/)
  * [Flask](http://flask.pocoo.org/)
  * [MongoDB](http://www.mongodb.org/)
  * [Honcho](https://pypi.python.org/pypi/honcho) / [Foreman](http://ddollar.github.io/foreman/)
 
Using Tornado combined with Python Flask, Steroids help developer to create a non-blocking, real-time ready web server. MongoDB is used as database Storage.

Once the Steroids structure is created, every developer can modify files in base of his needs. For example you can avoid MongoDB and use other modules. Foreman/Honcho helps to manage the server ( *it also generates init scripts if needed* ).