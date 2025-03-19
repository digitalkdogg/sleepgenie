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

        #sql = text('SELECT * FROM table1')
        #results = conn.execute(sql)

        #for record in results:
        #    print("\n", record)

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
                            values = {'Name' : field,
                                    'Value': row[field],
                                    'Date': formatDate(row[fieldnames[0]]),
                                    'ServiceID': 2
                                    }
                            sql = text("select * from Attribute where Attribute.Name = :Name and Value = :Value and Date = :Date")
                            results = conn.execute(sql, values)
                    
                            if results.rowcount == 0:
                                print('Inserting Row .......' + str(counter))
                                insertcmd = text("insert into Attribute (Name, Value, Date, ServiceID) VALUES(  :Name,:Value,:Date, :ServiceID)")
                                with engine.connect() as conn2:
                                    result = conn2.execute(insertcmd, values)
                                    conn2.commit()
                                            
                    #elif index == 0:
                      
           # insertcmd = text("insert into table1 (id, table1col) VALUES (3, 'Cardinal')")
           # insertcmd = insert(table1).values(id=2, table1col="testing")
            #insresults = conn.execute(insertcmd)
         

                #print(values)
                #sql = text('SELECT * FROM Attribute where Name = \'Score\' and DateTime = \'2/28/2025\'')
               # sql = text("select * from Attribute where Attribute.Name = :Name and Value = :Value and Date = :Date")
                #results = conn.execute(sql, values)
                
                #print(results.rowcount)
                #for record in results:
                #    print(record)

              #  print(row[fieldnames[0]], row[fieldnames[1]])
           #     print(row['Score'], row['Resting Heart Rate'])
            #    print(reader[0])
           


      #  with open(filepath, 'r') as file:
      #      content = file.read()
      #      print("File Content:")
      #      print(content)
    else:
        print("No file selected")

def formatDate(date_string):
    return datetime.strptime(date_string + ' 2025', "%b %d %Y").strftime('%Y-%m-%d')


root = tk.Tk()
root.withdraw() # Hide the main window

open_file()

root.destroy()