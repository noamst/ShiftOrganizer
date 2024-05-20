# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




import tkinter as tk
import Data as database
import networkx as nx
import re


class Worker:
  def __init__(self, firstname, surname, id, age):
    self.firstname = firstname
    self.surname = age
    self.id = id
    self.age = age




def CalcDecoding1(flow_value,flow_dict):
    with open('filename.txt', 'w') as file:
        file.write('Here is the current scheduling:')


    list = []
    print(f"Maximum flow value: {flow_value}")
    print("Flow values on each edge:")
    for source, flows in flow_dict.items():
        for target, flow_value in flows.items():
            if source == 's' or target == 't':
                continue
            else:
                worker_data = database.ShowWorkerByID(int(source[1:]))
                if flow_value == 0:
                    with open('filename.txt', 'a') as file:
                        file.write(f"\n{target} remains unmanned")
                else:
                    with open('filename.txt', 'a') as file:
                        file.write(f"\n{worker_data} -> {target}: {flow_value}")

def CalcDecoding(flow_value,flow_dict):
    with open('filename.txt', 'w') as file:
        file.write('Here is the current scheduling:')

    for source, flows in flow_dict.items():
        for target, flow_value in flows.items():
            if source == 's' or target == 't':
                continue
            else:
                worker_data = database.ShowWorkerByID(int(source[1:]))
                if flow_value == 0:
                   continue
                else:
                    with open('filename.txt', 'a') as file:
                        file.write(f"\n{worker_data} -> {target}: {flow_value}")






def CalcSchedule(max_shifts,num_of_shifts):
    workers = database.ShowAllWorkers()
    constraints = database.GetAllConstraints()
    G = nx.DiGraph()
    #creating worker vertices
    for worker in workers:
        G.add_edge('s', "w"+str(worker[0]), capacity=max_shifts)
    # creating constraint vertices
    for i in range(1,num_of_shifts+1):
        G.add_edge("d"+str(i), 't', capacity=1)

    # connecting worker to constraints
    for worker in workers:
        worker_constraints1 = database.ShowConstraintsByID(worker[0])
        worker_constraints = []
        for tuple_constraint in worker_constraints1:
            worker_constraints = worker_constraints+[tuple_constraint[2]]
        for i in range(1,num_of_shifts+1):
            if i in worker_constraints:
                continue
            else:
                G.add_edge("w"+str(worker[0]), "d"+str(i), capacity=1)

    flow_value, flow_dict = nx.maximum_flow(G, 's', 't')
    CalcDecoding(flow_value, flow_dict)




def BuildSchedule():
    schedulepage = tk.Toplevel()

    label = tk.Label(schedulepage, text="max_shifts")
    label.pack(pady=5, padx=5)

    max_shifts = tk.StringVar()
    text_bar1 = tk.Entry(schedulepage, textvariable=max_shifts)
    text_bar1.pack(pady=20, padx=20)

    label = tk.Label(schedulepage, text="num_of_shifts")
    label.pack(pady=5, padx=5)

    num_of_shifts = tk.StringVar()
    text_bar2 = tk.Entry(schedulepage, textvariable=num_of_shifts)
    text_bar2.pack(pady=20, padx=20)

    def CalcScheduleHelper():
        CalcSchedule(int(max_shifts.get()) , int(num_of_shifts.get()) )


    button = tk.Button(schedulepage, text="BuildSchedule", command=CalcScheduleHelper)
    button.pack(pady=20)




def close_window():
    root.destroy()

def ShowAllWorkers():
    records=database.ShowAllWorkers()
    for worker in records:
        txt = "id : {worker_id} , firstname:{firstname} , surname: {surname} , age:{age}".format(worker_id=worker[0],firstname=worker[1],surname=worker[2],age=worker[3])
        print(txt)





def ConstraintPage():
    constraintpage = tk.Toplevel()
    constraintpage.title("Add Constraints")
    label = tk.Label(constraintpage, text="worker_id")
    label.pack(pady=5, padx=5)

    worker_id = tk.StringVar()
    text_bar1 = tk.Entry(constraintpage, textvariable=worker_id)
    text_bar1.pack(pady=20, padx=20)

    def ShowWorker():
        records = database.ShowWorkerByID(int(worker_id.get()))
        for worker in records:
            txt = "id : {worker_id} , firstname:{firstname} , surname: {surname} , age:{age}".format(
                worker_id=worker[0], firstname=worker[1], surname=worker[2], age=worker[3])
            print(txt)

    button = tk.Button(constraintpage, text="Verify", command=ShowWorker)
    button.pack(pady=20)

    day_num = tk.StringVar()
    text_bar2 = tk.Entry(constraintpage, textvariable=day_num)
    text_bar2.pack(pady=20, padx=20)

    def AddConstraint():
        database.addConstraint(worker_id.get(), day_num.get())

    button = tk.Button(constraintpage, text="Add", command=AddConstraint)
    button.pack(pady=20)

    worker_to_show = tk.StringVar()
    text_bar2 = tk.Entry(constraintpage, textvariable=worker_to_show)
    text_bar2.pack(pady=20, padx=20)

    def ShowAllConstraints():
        worker_id_show = worker_to_show.get()
        records = database.ShowConstraintsByID(int(worker_id_show))
        worker = database.ShowWorkerByID(int(worker_id_show))[0]
        worker_details = "id : {worker_id} , firstname:{firstname} , surname: {surname} , age:{age}".format(
            worker_id=worker[0], firstname=worker[1], surname=worker[2], age=worker[3])
        print(worker_details)
        print("cant work in:")
        for constraint in records:
           print("day:"+str(constraint[2]))

    button = tk.Button(constraintpage, text="ShowAllConstraints", command=ShowAllConstraints)
    button.pack(pady=20)


def WorkerPage():
    workerpage = tk.Toplevel()
    workerpage.title("Add Workers")
    label = tk.Label(workerpage, text="In this window you are meant to address workers")
    label.pack(pady=20, padx=20)

    label = tk.Label(workerpage, text="firstname")
    label.pack(pady=5, padx=5)

    firstname = tk.StringVar()
    text_bar1 = tk.Entry(workerpage, textvariable=firstname)
    text_bar1.pack(pady=20, padx=20)

    label = tk.Label(workerpage, text="surname")
    label.pack(pady=5, padx=5)

    surname = tk.StringVar()
    text_bar2 = tk.Entry(workerpage, textvariable=surname)
    text_bar2.pack(pady=20, padx=20)

    label = tk.Label(workerpage, text="id")
    label.pack(pady=5, padx=5)

    worker_id = tk.StringVar()
    text_bar3 = tk.Entry(workerpage, textvariable=worker_id)
    text_bar3.pack(pady=20, padx=20)

    label = tk.Label(workerpage, text="age")
    label.pack(pady=5, padx=5)

    age = tk.StringVar()
    text_bar4 = tk.Entry(workerpage, textvariable=age)
    text_bar4.pack(pady=20, padx=20)

    def addWorker1():
        # Check if worker_id and age are not empty and are digits
        if not worker_id.get().isdigit() or not age.get().isdigit():
            print("Invalid ID or Age. Please enter valid numbers.")
            return
        # Convert to appropriate data types
        id_value = int(worker_id.get())
        age_value = int(age.get())
        firstname_value = firstname.get()
        surname_value = surname.get()
        database.addWorker(id_value, firstname_value, surname_value, age_value)

    button = tk.Button(workerpage, text="AddWorker", command=addWorker1)
    button.pack(pady=20)
    button1 = tk.Button(workerpage, text="ShowAllWorkers", command=ShowAllWorkers)
    button1.pack(pady=20)
    workerpage.mainloop()



if __name__ == '__main__':

    #database.createWorkersTable()
    #database.createConstraintTable()
    root = tk.Tk()
    root.title("Shift Management System")
    label = tk.Label(root, text="Click the button to close the window.")
    label.pack(pady=20, padx=20)
    button1 = tk.Button(root, text="Close", command=close_window)
    button1.pack(pady=20)

    # Create a button to display the entered text
    button2 = tk.Button(root, text="AddWorker / RemoveWorker", command=WorkerPage)
    button2.pack(pady=20)



    button3 = tk.Button(root, text="AddConstraint / RemoveConstraints", command=ConstraintPage)
    button3.pack(pady=20)

    button4 = tk.Button(root, text="BuildSchedule", command=BuildSchedule)
    button4.pack(pady=20)

    root.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
