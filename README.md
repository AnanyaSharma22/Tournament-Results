# Tournament-Results

In this project, I have written a Python module that uses the **PostgreSQL** database to keep track of players and matches in a game tournament.

The game tournament will use the Swiss system for pairing up players in each round: players are not eliminated, and each player should be paired with another player with the same number of wins, or as close as possible.

This project has two parts: defining the database schema (SQL table definitions), and writing the code that will use it in python.

# Table of Contents

- Quickstart
- Documentation
- Requirements
- Usage of the project

# Quickstart



- The game tournament uses the Swiss system for pairing up players in each round.

    * Players are not eliminated
    * Each player should be paired with another player with the same number of wins, or as close as possible.
    
- The project has two main parts that uses the PostgreSQL database to keep track of players and matches in a game tournament. 

    * tournament.sql (For the database schema)
    * tournament.py
    
    
# Documentation
 
 **Code Templates**

 The templates for this project are the three files:
   
     - tournament.sql
     - tournament.py 
     - tournament_test.py.

 - The template file **tournament.sql** is where you will put the database schema, in the form of SQL create table commands. 

 - The template file **tournament.py** is where you will put the code of your module. I

 - Finally, the file **tournament_test.py** contains unit tests that will test the functions you’ve written in tournament.py. 
 
 **Functions in tournament.py**
 
 - registerPlayer(name)

   Adds a player to the tournament by putting an entry in the database. The database should assign an ID number to the player. 
   Different players may have the same names but will receive different ID numbers.
   
 - countPlayers()

   Returns the number of currently registered players. It should have the database count the players.
   
 - deletePlayers()

   Clear out all the player records from the database.
   
 - reportMatch(winner, loser)

   Stores the outcome of a single match between two players in the database.
   
 - deleteMatches()

   Clear out all the match records from the database.
   
 - playerStandings()

   Returns a list of (id, name, wins, matches) for each player, sorted by the number of wins each player has.
   
 - swissPairings()

   Given the existing set of registered players and the matches they have played, generates and returns a list of pairings 
   according to the Swiss system. Each pairing is a tuple (id1, name1, id2, name2), giving the ID and name of the paired 
   players. 
   
# Requirements


- Install Python.

- Next, Install all the required softwares:

    - sudo apt-get update
    - sudo apt-get install postgresql python-psycopg2
    - sudo apt-get install python-flask python-sqlalchemy
    - sudo apt-get install python-pip
    - pip install bleach
    - pip install oauth2client
    - pip install requests
    - pip install httplib2
    - pip install redis
    - pip install passlib
    - pip install itsdangerous
    - pip install flask-httpauth
 

# Usage of the project

- connecting to psql:

    * Creating your Database. 
    
    * Then you can connect **psql** to your new database and create your tables from the statements you've written in 
      **tournament.sql**. You can do this in either of two ways: 
      
         * Paste each statement in to **psql**.
          
         * Use the command \i tournament.sql to import the whole file into **psql** at once.

    * sudo -i -u postgres

    * createdb tournament

    * psql tournament -f /tournament/tournament.sql

 - You can run the tests from the command line, using the command :
   
    * python tournament_test.py.
