#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")
 


def deleteMatches():
    """Remove all the match records from the database."""
    database = connect()

    cur = database.cursor()

    cur.execute("DELETE FROM matches")

    database.commit()

    database.close()


def deletePlayers():
    """Remove all the player records from the database."""
    database = connect()

    cur = database.cursor()

    cur.execute("DELETE FROM player")

    database.commit()

    database.close()

def countPlayers():
    """Returns the number of players currently registered."""
    database = connect()

    cur = database.cursor()

    cur.execute("SELECT count(*) FROM player")

    outcome = cur.fetchall()

    database.close()

    return outcome[0][0]

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
 
    database = connect()

    cur = database.cursor()

    cur.execute("INSERT into player (name) VALUES (%s)",
              (name,))

    database.commit()

    database.close()

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    database = connect()

    cur = database.cursor()

    cur.execute("SELECT * from rankings order by total_wins desc")

    result = cur.fetchall()

    database.close()

    return result

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
   
    database = connect()

    cur = DB.cursor()

    cur.execute("INSERT into matches (m_id, winner, loser) values (default, %s, %s)",
              (winner, loser,))

    database.commit()

    database.close()
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    combinations = []

    rank = playerStandings()   
    
    for r in range(0, len(rank), 2):

         if len(rank) % 2 == 0:

             pairs = rank[r][0], rank[r][1], rank[r+1][0], rank[i+1][1]

             combinations.append(pairs)

    return combinations
     
