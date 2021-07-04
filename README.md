# django bot server

# What is this useful for?

- Get an idea how to get django-channels working
- Get some sample code for a simple working front end that uses web sockets for a connection

# How to use this branch

This part of the seminar involves installing and getting started with django channels.

To get this running, simply run the  the following 

## Step 1: Install requirements.txt

`pip install -r requirements.txt`

## Step 2: Create databases

create database on postgres and update credentials in settings.py file

## create migrations

`python manage.py makemigrations`
`python manage.py migrate`

## Step 3: Run server

And start the server with 

`python manage.py runserver`

You should now be able to go to localhost:8000/chat/ and chat with the bot
