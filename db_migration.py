import tkinter as tk
from tkinter import filedialog
#import MySQLdb
import csv 
from datetime import datetime

from sqlalchemy import create_engine, MetaData, Table, select, text, insert
from sqlalchemy.orm import sessionmaker, scoped_session

def migrate():

    engine = create_engine("mysql://Kevin:Squogg27@localhost/sleepGenie")
    conn = engine.connect()

    values = {'ServiceId': 2}

    sql = text("select * from Attribute where Attribute.ServiceID = :ServiceId")
    rows = conn.execute(sql, values)

    for row in rows:
        metaname = row.Name

        metavalue = {'metaName': metaname, 'serviceID': row.ServiceID}
        metasql = text("select id from Meta where Name = :metaName and serviceID = :serviceID")
        metarows = conn.execute(metasql, metavalue)

        for r in metarows:
            metaid = r.id

            updatevalue = {'Meta_Id': metaid, 'id': row.ID}
            print (updatevalue)
            updatecmd = text("update Attribute set 1 = :Meta_Id and ID = :id")

            with engine.connect() as conn2:
                updateresults = conn2.execute(updatecmd, updatevalue)
                conn2.commit()

    
    


   # values = {'Name' : 'Score',
   #             'Value': '86',
   #             'Date': formatDate('Feb 28'),
   #             'ServiceID': 2
   #                                  }
   # sql = text("select * from Attribute where Attribute.Name = :Name and Value = :Value and Date = :Date")
   # results = conn.execute(sql, values)

   # print(results.rowcount)

  #  print('Inserting Row .......' + str(counter))
  #  insertcmd = text("insert into Attribute (Name, Value, Date, ServiceID) VALUES(  :Name,:Value,:Date, :ServiceID)")
  #  with engine.connect() as conn2:
  #      result = conn2.execute(insertcmd, values)
  #      conn2.commit()



def formatDate(date_string):
    return datetime.strptime(date_string + ' 2025', "%b %d %Y").strftime('%Y-%m-%d')

migrate()

#root = tk.Tk()
#root.withdraw() # Hide the main window

#open_file()

#root.destroy()