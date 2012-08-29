AMD Module Dependency Editor
============================

AMD Module Editor is a plugin for Sublime Text 2 used to ease the editing of
your module definition's list of dependencies. It provides the ability to add,
edit, and delete modules from within Sublime Text using your own formatting
rules.


Installation
------------

### Package Control

The best way to install AMD Module Dependency Editor is to use [Sublime Package
Control](http://wbond.net/sublime_packages/package_control). Follow its
instructions for installation, and use the Package Control: Install Package
command to install AMD Module Dependency Editor.


### Manual Installation

To manually install AMD Module Dependency Editor, clone this repository into
your Sublime Text 2 `Packages` directory.


Usage
-----

There are two actions you can perform with AMD Module Editor, edit and delete.
Edit allows you to add, edit, or just view your module list. Delete allows you
to remove a module that is no longer required.

To add a new module, open the edit panel, and choose the first option that says
"Add New Module" and press enter. At the bottom of the window, you'll next be
prompted for one or more input values, according to the state. Finally, the new
module will be added to the end of your dependency list.

Editing and deleting a module works similarly to creating a new one.

The first thing you will be asked to input will be the path to the module. You
don't need to add quotes here, they'll be inserted automatically.

Next, you will be prompted for the argument to the module function if it would
be valid to do so. You will not be prompted if you've set disableArguments to
true or if you've left an argument blank for a previous module in the list.


Default Key Bindings
--------------------

### Windows/Linux:
Delete Panel `ctrl+alt+shift+a`  
Edit Panel `ctrl+alt+a`

### Mac OS X:
Delete Panel `cmd+alt+shift+a`  
Edit Panel `cmd+alt+a`


Configuration
-------------

To configure the plugin, use the Sublime Text menu to navigate to Preferences |
Package Settings | AMD Module Editor. From there, you can view the default
settings and key bindings (do NOT edit the default settings or bindings, they
will be overwritten when the plugin updates) to look for examples. Then you can
edit the user settings and bindings as you please.


Running Tests (for developers)
------------------------------

Tests can be run by going to the command line, changing to the package's directory, and running:

    python -m unittest discover -s tests


License
-------
All of AMD Module Editor is licensed under the MIT license.

Copyright (c) 2012 William Blasko <williamblasko@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
