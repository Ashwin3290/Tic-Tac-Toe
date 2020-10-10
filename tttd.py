import mysql.connector as myc
mysql=myc.connect(host='localhost',user='root',password='12345',database='testdb')
cursor=mysql.cursor()
def connect():
    mysql=myc.connect(host='localhost',user='root',password='12345',database='testdb')
    cursor=mysql.cursor()

#cursor.execute('show  databases')
#d=cursor.fetchall()
#if 'testdb' not in d:
    #cursor.execute('create database testdb')\
    #cursor.execute('use testdb')
#cursor.execute('show  tables')
#d=cursor.fetchall()
#if 'testdb' not in d:
  #  cursor.execute('create table player_record (name varchar(25),wins int ,losses int ,draws int)')
if mysql.is_connected():
    print('Database connected')

def insert(name,w,l,d):
    connect()
    v="insert into player_record (name,wins,losses,draws) values('{}',{},{},{})".format(name,w,l,d)
    cursor.execute(v)
    mysql.commit()
def update(name,w,l,d):
    cursor.execute("select * from player_record where name='{}'".format(name))
    a=cursor.fetchall()
    if w==1:
        x=int(a[1])
        x+=1
        cursor.execute("update player_record set wins={0} where name='{1}'".format(x,name))
        mysql.commit()
    if l==1:
        x=int(a[0])
        x+=1
        cursor.execute("update player_record set losses={0} where name='{1}'".format(x,name))
        mysql.commit()

    if d==1:
        x=int(a[3])
        x+=1
        cursor.execute("update player_record set draws={0} where name='{1}'".format(x,name))
        mysql.commit()
    
def show(name):
    try:
        u=str("select * from player_record where name='{}'".format(name))
        cursor.execute("select * from player_record where name='{}'".format(name))
        data=cursor.fetchall()
        s='_'*90
        m=int(15)
        w=' '
        for row in data:
            for i in row:
                h=0
                o=len(str(i))
                h=15-o
                print(i,w*h,'|' , end='')
            print('\n')
            print(s)
        return True
    except:
        return False
def delete (name):
    try:
        cursor.execute("delete from player_record where name='{}'".format(name))
        mysql.close()
        return True
    except:
        print('Player  name does not exist')
        return False

def check(name,w,l,d):
    connect()
    cursor.execute("select name from player_record where name='{}'".format(name))
    data=cursor.fetchall()
    i=0
    while i<len(data):
        if name in data[i] :
            update(name,w,l,d)
            break
        i+=1
    else:
        insert(name,w,l,d)
def graph(name):
    connect()
    name=str(name)
    try:
        cursor.execute("select wins,losses,draws from player_record where name='{}'".format(name))
        data=cursor.fetchall()
        data=list(data)
        activities=['wins','losses','draws']
        pl.pie(data,labels=['wins','losses','draws'],shadow=True,explode=(0.1,0,0),autopct='%1.1f%%' ,startangle=90)
        pl.show()
        return True
    except:
        return False
