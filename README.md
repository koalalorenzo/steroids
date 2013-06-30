#Steroids
## 
**Steroids** is a set of tools to **help python developers** to build **cool stuff** reducing efforts and time.

<div align="center">

<iframe src="http://ghbtns.com/github-btn.html?user=koalalorenzo&repo=Steroids&type=follow&size=large&count=true"
  allowtransparency="true" frameborder="0" scrolling="0" width="270" height="30"></iframe>

<iframe src="http://ghbtns.com/github-btn.html?user=koalalorenzo&repo=Steroids&type=watch&size=large&count=true"
  allowtransparency="true" frameborder="0" scrolling="0" width="150" height="30"></iframe>

</div>

##Quick install
If you are using Unix-like OS, to install Steroids use this command, right from your terminal:

    curl -s http://projects.setale.me/Steroids/install | sudo sh 
    

This script will install everything you do it for you. It works on Debian-derived, Arch Linux, MacOS or every operative sistem with *easy_install*.

Alternatively You can also install Steroids via *python pip* command:

    sudo pip install Steroids

##Quick Use
To generate a new project with examples use this command:

    steroids init ProjectName --examples=True

If you need help you can use:

    steroids --help
    
## Structure
The structure of a Project built on Steroids is derived from [Flask](http://flask.pocoo.org/docs/patterns/packages/#simple-packages) one. It provides Objects, Statics file, Views, Templates, Custom Decorators and others.

The following structure is based on the default modules used: Flask, MongoDB and Honcho.

    ./settings.py           # Configuration File
    ./server.py             # script to start Server
    ./Procfile              # Foreman/Honcho file
    ./requirements.txt      # Everything you need goes here
    ./project/              # Where the magic happens
             /__init__.py   # Package declarations 
             /views/        # Directory of Views
             /templates/    # Directory of Templates
             /static/       # Directory of static files
             /objects/      # Directory of Objects
               
If you use different modules, Steroids will generate a different structure of files and directories.

This structure give a lot of freedom to developers: they can modify it without problems adapting the structure in base of what they do. Steroids structure is just an ordered way to create web services in python.

To **understand the structure** is suggested to enable the **examples** when initializing a project.

## Modules
Steroids is built around the concept of modules: the structure is defined but the content inside is modified by the modules. Each modules provide different functionality to the project.

By defaults Steroids uses Flask, Tornado, MongoDB and Honcho to provide a basic structure for a complete non-blocking web server. The project generated is **ready to be uploaded on [Heroku](https://www.heroku.com/)** or similar services.

You can use a small specific group of modules in base of your needs. For example to initialize a project using only *Flask and MongoDB*, run this command:

    steroids init ProjectName --modules flask mongodb --examples=True

A list of modules is available running this command:

    steroids modules list

To get help and read more about a module you can use this command:

    steroids modules MODULE

where *MODULE* is the name of the module get in the list ( ex: *flask* ).

### Modules Available
  * [Flask](http://flask.pocoo.org/) Web Server ( *flask* )
  * Flask using [Tornado web server](http://flask.pocoo.org/docs/deploying/wsgi-standalone/#tornado) ( *flasktornado* ) 
  * [MongoDB](http://www.mongodb.org/) objects implementation ( *mongodb* )
  * [Twitter Bootstrap](http://twitter.github.io/bootstrap/index.html) ( *bootstrap* )
  * [Topcoat](http://topcoat.io/) CSS ( *topcoat* )
  * [Honcho / Foreman](https://honcho.readthedocs.org/en/latest/) procfile ( *honcho* )
  * [Google App Engine](https://developers.google.com/appengine/) basic files ( *gae* )
  * [RethinkDB](http://rethinkdb.com/) objects implementation - [Alpha, not ready] ( *rethinkdb* )
  * [APScheduler](http://pythonhosted.org/APScheduler/) for clock and cron jobs ( *apscheduler* )
  * *…and more to come*

## License
Steroids is licensed under a Creative Commons Attribution-ShareAlike 3.0 Unported License. To view a copy of this license, visit [http://creativecommons.org/licenses/by-sa/3.0/](http://creativecommons.org/licenses/by-sa/3.0/)

## Liks

  * Project Site: [http://projects.setale.me/Steroids](http://projects.setale.me/Steroids)
  * GitHub: [https://github.com/koalalorenzo/Steroids](https://github.com/koalalorenzo/Steroids)
  * PyPi page: [https://pypi.python.org/pypi/steroids/](https://pypi.python.org/pypi/steroids/)    
  * Author Website: [http://who.is.lorenzo.setale.me/?](http://setale.me/)
  * Author Blog: [http://blog.setale.me/](http://blog.setale.me/)

<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-10395528-24', 'setale.me');
  ga('send', 'pageview');

</script>