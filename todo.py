class GUI:
    def __init__(self):
        self.list = []

    def add(self, task):
        self.list.append(task)

    def view(self):
        if self.list:
            print("To-Do List:")
            for lists in self.list:
                print(lists)
        else:
            print("Your to-do list is empty.")

    def update(self, index, updates):
        if index > 0 and index<= len(self.list):
            self.list[index - 1] = updates
            print("List updated successfully.")
        else:
            print("Invalid list index.")

    def delete(self, index):
        if index > 0 and index<= len(self.list):
            del self.list[index - 1]
            print("list deleted successfully.")
        else:
            print("Invalid list index.")


def start():
    todo =GUI()
    while True:
        print("\n 1 Add New List \n 2 View List \n 3 Update List \n 4 Delete List \n 5 Exit")
        ch = input("Enter your choice: ")
        
        if ch == "1":
            new = input("Enter new list: ")
            todo.add(new)
        elif ch == "2":
            todo.view()
        elif ch == "3":
            index = int(input("Enter index of list to update: "))
            updates = input("Enter new task: ")
            todo.update(index,updates)
        elif ch == "4":
            index = int(input("Enter index of list to delete: "))
            todo.delete(index)
        elif ch == "5":
            print("Exiting ")
            break
        else:
            print("Invalid choice")

start()

  
