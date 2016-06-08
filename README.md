# Parsey McParseface server

A simple Python Flask app to provide Parsey McParseface over HTTP as an API.

This will not work with the standard tensorflow models package.

To get this working:

* Follow [my tensorflow/models installation steps for Ubuntu 14.04 x64](https://github.com/tensorflow/models/pull/115/files).
* HOWEVER, in the git clone step, you will need to clone from [my repository](https://github.com/JoshData/models) and then checkout my [online-parsing branch](https://github.com/JoshData/models/tree/online-parsing), where I've modified the Parsey McParseface example code to stay running across parses.
* The server script here won't work with anything but my branch ^.
 
Please get in touch (open an issue) if you use this project for anything interesting.
