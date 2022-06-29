import sqlite3
conn = sqlite3.connect('students.db')
conn.execute("INSERT INTO STUDENT (ID,NAME,ROLL,ADDRESS,CLASS) "
             "VALUES (3, 'John', '001', 'Bangalore', '10th')")
conn.execute("INSERT INTO STUDENT (ID,NAME,ROLL,ADDRESS,CLASS) "
             "VALUES (4, 'Naren', '002', 'Hyd', '12th')")
conn.commit()
conn.close()