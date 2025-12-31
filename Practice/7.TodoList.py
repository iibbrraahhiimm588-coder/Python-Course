# 1) Start Program:
#    - Ek empty list banate ho jisme tasks store honge: todo_list = []

# 2) Loop Start:
#    - Ye loop tab tak chalega jab tak user "Exit" choose na kare

# 3) Show Menu:
#    - show_menu() function call hota hai
#    - Menu options print hoti hain:
#         1: Add Task
#         2: View Tasks
#         3: Delete Task
#         4: Exit
#    - User se choice input li jaati hai

# 4) Choice ke hisaab se actions:
#    a) If user_input == "1" (Add Task):
#         - Add_Task(todo_list) call hota hai
#         - User se task input liya jata hai
#         - Task list me add hota hai
#         - Confirmation print hota hai
#         - Updated list wapas main_program me stored rehti hai

#    b) If user_input == "2" (View Tasks):
#         - View_Tasks(todo_list) call hota hai
#         - Agar list empty → print "No tasks"
#         - Agar list me tasks → numbered list me print
#         - Manual counter ya number print hota hai

#    c) If user_input == "3" (Delete Task):
#         - delete_task(todo_list) call hota hai
#         - Pehle current tasks show hote hain
#         - User se task number input liya jata hai
#         - Input valid hai ya nahi check hota hai
#              - Valid → task remove hota hai, confirmation print
#              - Invalid → error message print
#         - Updated list wapas main_program me stored rehti hai

#    d) If user_input == "4" (Exit):
#         - Loop break hota hai
#         - Program terminate hota hai
#         - Goodbye message print hota hai

#    e) Else:
#         - Agar input invalid ho → "Invalid choice" print hota hai
#         - Loop continue hota hai

# 5) Repeat Until Exit:
#    - User multiple tasks ek session me add, view aur delete kar sakta hai
#    - Functions me list parameter ke through pass hoti hai → global variable ki zarurat nahi

def show_menu():
    print("\n--- Todo List Menu ---")
    print("1: Add Task")
    print("2: View Tasks")
    print("3: Delete Task")
    print("4: Exit")
    user_choice = input('Enter your choice here: ')
    return user_choice

def Add_Task(task_list):
    task = input('Enter your task here: ')
    task_list.append(task)
    print('Task added successfully!\n')
    return task_list

def View_Tasks(task_list):
    if not task_list:
        print('No tasks.\n')
    else:
        print("\nYour Tasks:")
        number = 1
        for task in task_list:
            print(f"{number}. {task}")
            number += 1
        print()  # extra line for readability

def delete_task(task_list):
    View_Tasks(task_list)
    
    if not task_list:  # list empty check
        return task_list

    try:
        delete_input = int(input("Enter task number to delete: "))
        if delete_input < 1 or delete_input > len(task_list):
            print('Invalid task number.\n')
        else:
            removed_task = task_list.pop(delete_input - 1)
            print(f"Task '{removed_task}' deleted successfully!\n")
    except ValueError:
        print("Please enter a valid number.\n")
    
    return task_list

def main_program():
    todo_list = []

    while True:
        user_input = show_menu()

        if user_input == '1':
            Add_Task(todo_list)
        elif user_input == '2':
            View_Tasks(todo_list)
        elif user_input == '3':
            delete_task(todo_list)
        elif user_input == '4':
            print("Exiting Todo List. Goodbye!")
            break
        else:
            print('Invalid Choice. Please try again.\n')

main_program()
