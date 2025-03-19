import tkinter as tk
from tkinter import filedialog
#import MySQLdb
import csv 
from datetime import datetime

from sqlalchemy import create_engine, MetaData, Table, select, text, insert
from sqlalchemy.orm import sessionmaker, scoped_session

def open_file():
    filepath = filedialog.askopenfilename(
        initialdir="/home/kevin", 
        title="Select File",
        filetypes=(("csv files", "*.csv"), ("All files", "*.*"))
    )
    if filepath:
        print(f"Selected file: {filepath}")
        # Perform actions with the selected file, such as reading its content


        engine = create_engine("mysql://Kevin:Squogg27@localhost/sleepGenie")
        conn = engine.connect()

        with open(filepath, newline='') as csvfile:
  
            reader = csv.DictReader(csvfile)
            fieldnames = reader.fieldnames

            date_string = "Feb 08 2025"
            date_object = datetime.strptime(date_string, "%b %d %Y")
            print(date_object)
           

            counter = 0
            for row in reader:
                counter = counter+1
   
                for index, field in enumerate(fieldnames):
                    if index > 0: 
                        if row[field] != '--' :
                            values = {'Name' : lookupName(field, conn, 2),
                                    'Value': row[field],
                                    'Date': formatDate(row[fieldnames[0]]),
                                    'ServiceID': 2
                                    }
                            
                            
                            sql = text("select * from Attribute where Attribute.MetaId = :Name and Value = :Value and Date = :Date")
                            results = conn.execute(sql, values)

                            #for r in results:
                            #    print(r)
                    
                            if results.rowcount == 0:

                                print('Inserting Row .......' + str(counter))
                                
                                insertcmd = text("insert into Attribute (MetaId, Value, Date, ServiceID) VALUES(  :Name,:Value,:Date, :ServiceID)")
                                with engine.connect() as conn2:
                                    result = conn2.execute(insertcmd, values)
                                    
                                    conn2.commit()
                                            
          
    else:
        print("No file selected")

def lookupName(Name, conn, serviceid): 
    metavalue = {'metaName': Name, 'serviceID': serviceid}
    metasql = text("select id from Meta where Name = :metaName and serviceID = :serviceID")
    metarows = conn.execute(metasql, metavalue)
    id = 0
    if metarows.rowcount > 0:
        for row in metarows:
            id = row.id
    else :
        values = {"Name": Name, "serviceid": serviceid}
        insertcmd = text("insert into Meta (Name, serviceID) VALUES(  :Name,:serviceid)")
        #with engine.connect() as conn2:
        result = conn.execute(insertcmd, values)     
        conn.commit()

        metavalue = {'metaName': Name, 'serviceID': serviceid}
        metasql = text("select id from Meta where Name = :metaName and serviceID = :serviceID")
        metarows = conn.execute(metasql, metavalue)
        id = 0
        if metarows.rowcount > 0:
            for row in metarows:
                id = row.id
             
    return id

def formatDate(date_string):
    return datetime.strptime(date_string + ' 2025', "%b %d %Y").strftime('%Y-%m-%d')


root = tk.Tk()
root.withdraw() # Hide the main window

open_file()

root.destroy()