#Steroids
## 
**Steroids** is a set of tools to **help python developers** to build **real-time ready**, **non-blocking**, **web application** reducing efforts and time.

##Quick install
If you are using Unix-like OS, to install Steroids use this command, right from your terminal:

    curl http://projects.setale.me/Steroids/install | sh 

In case the machine some requirements, the script will do it for you. 

Alternatively You can also install Steroids via *python pip* command:

    pip install Steroids

##Quick Use
To generate a new project with examples use this command:

    steroids init ProjectName --examples=True

If you need help you can use:

    steroids --help
    
## Structure
The structure of a Project built on Steroids is derived from Flask one. It provides Objects, Statics file, Views, Templates, Custom Decorators and others.

The following structure is based on the default modules used: Flask, MongoDB, Tornado and Honcho.

    ./configuration.py          # Configuration File
    ./server.py                 # script to start Server
    ./tornado.py                # script to start Tornado Server
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
Steroids is builted around the concept of modules: the structure is defined but the content inside is modified by the modules. Each modules provide different funcionality to the project.

By defaults Steroids uses Flask, Tornado, MongoDB and Honcho to provide a basic structure for a complete non-blocking web server. The project generated is **ready to be uploaded on [Heroku](https://www.heroku.com/)** or similar services.

You can use a small specific group of modules in base of your needs. For example to initialize a project using only *Flask and MongoDB*, run this command:

    steroids init ProjectName --modules flask mongodb --examples=True

A list of modules is available running this command:

    steroids modules list

To get help and read more about a module you can use this command:

    steroids modules MODULE

where *MODULE* is the name of the module get in the list ( ex: *flask* ).

## License
Steroids is licensed under a Creative Commons Attribution-ShareAlike 3.0 Unported License. To view a copy of this license, visit [http://creativecommons.org/licenses/by-sa/3.0/](http://creativecommons.org/licenses/by-sa/3.0/)

## Liks

  * Project Site: [http://projects.setale.me/Steroids](http://projects.setale.me/Steroids)
  * GitHub: [https://github.com/koalalorenzo/Steroids](https://github.com/koalalorenzo/Steroids)
  * PyPi page: [https://pypi.python.org/pypi/steroids/](https://pypi.python.org/pypi/steroids/)    
  * Author Website: [http://who.is.lorenzo.setale.me/?](http://setale.me/)
  * Author Blog: [http://blog.setale.me/](http://blog.setale.me/)
