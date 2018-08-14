#install xampp server and run mysql server if you are working on windows
#for linux and mac user just install and configure mariadb server
#run command on shell as #python -m pip install pymysql before executing this
import pymysql as sql

db = sql.connect('localhost','root','')
c = db.cursor()

c.execute('create database bank')
c.execute('use bank')
c.execute('create table user(acc int(6) primary key auto_increment,name varchar(50) not null,password varchar(30) not null, balance double not null)')
c.execute("create user 'bank'@'localhost' identified by 'bank'")
c.execute("grant all privileges on bank.user to 'bank'@'localhost'")
c.execute('insert into user values(1001,"sachin","redhat",50000)')
c.execute('insert into user(name,password,balance) values("rajat","grras@432",70000), ("gaurav","g@123",60000)')

db.commit()

c.close()
db.close()
