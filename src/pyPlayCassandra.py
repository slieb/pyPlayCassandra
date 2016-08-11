from cassandra.cluster import Cluster

# set up cluster and connect to Cassandra instance
cluster = Cluster()
session = cluster.connect('demo')

# update users table with new record
session.execute("""
insert into users (lastname, age, city, email, firstname) values ('Jones', 35, 'Austin', 'bob@example.com', 'Bob')
""")

# query the table for the record we just inserted
result = session.execute("select * from users where lastname='Jones' ")[0]
print result.firstname, result.age

# list everyone's name and age
result = session.execute("select * from users")
for x in result:
    print x.firstname, x.age