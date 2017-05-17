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
    db,c = connect()
    query = "select * from popular_articles"
    c.execute(query)
    article = c.fetchall()
    db.close()
    for a in range(0,len(article),1):
        print article[a][0] + ": " + str(article[a][1]) + ' views'

def authors():
    db,c = connect()
    query = "select * from third_view;"
    c.execute(query)
    author = c.fetchall()
    db.close()
    for a in range(0,len(author),1):
        print author[a][0] + ": " + str(author[a][1]) + ' views'

def log():
    db,c = connect()
    query = "select * from sixth_view order by errors desc;"
    c.execute(query)
    log = c.fetchone()
    db.close()
    print str(log[0]) + " " + str(log[1]) + "%"

if __name__ == '__main__':
    print "\n"
    articles()
    print "\n"
    authors()
    print "\n"
    log()
    print "------End------"