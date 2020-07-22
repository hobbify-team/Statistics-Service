# 📢  Statistics-Service

This repository is created as alternative hobbify-api  such that frontend development can make data representation of each user in app. 

Remember that Hobbify is a habits tracker system, what does that mean? Well, you can create a habit and give it a frequency, a start and end date, and start updating it to track your process all over the habit.

How to run this complement ?

To run this repository, you need docker installed in your system and follow the next steps:

1. Clone this repository:
    ```sh
     $ git clone git@github.com:hobbify-team/Statistics-Service.git
    ```
2. Move to the root of the folder and build the docker images with the next command:
    ```sh
     $ sudo  docker-compose -f production.yml up --build
    ```
### Development Environments

It is important to add the .production folder to .env which contains the instance variables to be used for postgres.

```sh
$ cd Hobbify-Statistics/.env
$ mkdir .production && cd .production
$ touch .postgres
$ touch .flask
```

The following variables must be added in the .postgres file:

```sh
POSTGRES_HOST=
POSTGRES_PORT=
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
```
and the .flask file:

```
#Flask
FLASK_PORT=5000
FLASK_HOST='0.0.0.0'
```


License
----

MIT
