#!/usr/bin/env python

import psycopg2


def connect(database_name="news"):
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        c = db.cursor()
        return db, c
    except:
        print("Cannot connect to databse news")


def articles():
    db, c = connect()
    query = "select * from popular_articles limit 3"
    c.execute(query)
    article = c.fetchall()
    db.close()
    for a in range(0, len(article), 1):
        print article[a][0] + ": " + str(article[a][1]) + ' views'


def authors():
    db, c = connect()
    query = "select * from third_view;"
    c.execute(query)
    author = c.fetchall()
    db.close()
    for a in range(0, len(author), 1):
        print author[a][0] + ": " + str(author[a][1]) + ' views'


def log():
    db, c = connect()
    query = "select * from sixth_view where errors >= 1.0"
    c.execute(query)
    log = c.fetchall()
    db.close()
    for a in range(0, len(log), 1):
        print str(log[a][0]) + " " + str(log[a][1]) + "%"


if __name__ == '__main__':
    print "Most popular articles:\n"
    articles()
    print "Most popular authors:\n"
    authors()
    print "Days with more than 1% errors\n"
    log()
    print "\n------End------\n"
