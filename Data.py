import sqlite3


def createWorkersTable():
    connection = sqlite3.connect("myData.db")
    cursor = connection.cursor()
    query = '''
    CREATE TABLE workers (
        id INTEGER PRIMARY KEY,
        firstname TEXT NOT NULL,
        surname TEXT NOT NULL,
        age INTEGER
      
    )
    '''

    cursor.execute(query)
    connection.commit()
    connection.close()

def createConstraintTable():
  connection = sqlite3.connect("myData.db")
  cursor = connection.cursor()
  cursor.execute("PRAGMA foreign_keys = ON")
  query = '''
  CREATE TABLE constraints (
      id_constraint INTEGER PRIMARY KEY,
      worker_id INTEGER,
      day_num INTEGER NOT NULL,
      FOREIGN KEY (worker_id) REFERENCES workers(id)

  )
  '''

  cursor.execute(query)
  connection.commit()
  connection.close()

def addWorker(worker_id, firstname, surname, age):
  connection = sqlite3.connect("myData.db")
  cursor = connection.cursor()
  sqlite_insert_query = """INSERT INTO workers (id, firstname, surname, age) 
                           VALUES (?, ?, ?, ?)"""
  values = (int(worker_id), firstname, surname, int(age))
  cursor.execute(sqlite_insert_query, values)
  connection.commit()
  connection.close()

def addConstraint(worker_id, day_num):
  connection = sqlite3.connect("myData.db")
  cursor = connection.cursor()
  cursor.execute("PRAGMA foreign_keys = ON")

  cursor.execute("SELECT COUNT(*) FROM constraints")
  constraint_id = cursor.fetchall()[0][0]
  print(constraint_id)

  sqlite_insert_query = """INSERT INTO constraints (id_constraint, worker_id, day_num) 
                           VALUES (?, ?, ?)"""
  values = (constraint_id, int(worker_id), int(day_num))
  cursor.execute(sqlite_insert_query, values)
  connection.commit()
  connection.close()


def ShowAllWorkers():
  connection = sqlite3.connect("myData.db")
  cursor = connection.cursor()
  sql_select_Query = "select * from workers"
  cursor.execute(sql_select_Query)

  # get all records
  records = cursor.fetchall()
  connection.commit()
  connection.close()
  return records

def GetAllConstraints():
  connection = sqlite3.connect("myData.db")
  cursor = connection.cursor()
  cursor.execute("PRAGMA foreign_keys = ON")
  sql_select_Query = "select * from constraints"
  cursor.execute(sql_select_Query)

  # get all records
  records = cursor.fetchall()
  connection.commit()
  connection.close()
  return records



def ShowWorkerByID(worker_id):
    connection = sqlite3.connect("myData.db")
    cursor = connection.cursor()


    cursor.execute("select * from workers WHERE id=?",(worker_id,))

    # get all records
    records = cursor.fetchall()
    connection.commit()
    connection.close()
    return records


def ShowConstraintsByID(worker_id):
    connection = sqlite3.connect("myData.db")
    cursor = connection.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute("select * from constraints WHERE worker_id=?",(worker_id,))

    # get all records
    records = cursor.fetchall()
    connection.commit()
    connection.close()
    return records

def ShowConstraintsByIDOfConst(constraint_id):
    connection = sqlite3.connect("myData.db")
    cursor = connection.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute("select * from constraints WHERE id_constraint=?",(constraint_id,))

    # get all records
    records = cursor.fetchall()
    connection.commit()
    connection.close()
    return records