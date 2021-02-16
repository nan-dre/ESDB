# ESDB
A little discord bot written in Python, that plays a web stream (in this case [jazzradio](https://www.jazzradio.fr/))

## Installation

```pip3 install -r requirements.txt```

You will also need ffmpeg

```apt install ffmpeg``` - on Ubuntu

Put this inside a .env file

```DISCORD_TOKEN=<your-token>```

## Docker

I also wrote a Dockerfile for this. Just run ```docker build --tag esb .``` to build it.
Don't forget to put the discord token in the .env file.
