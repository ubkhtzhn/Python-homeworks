############################################### TO DO LIST APPLICATION ###############################################


class Task:
    def __init__(self, title, description, due_date, status = 'not finished'):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status


class ToDoList:
    def __init__(self):
        self.tasks = []
        pass
    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_complete(self, task_title):
        for t in self.tasks:
            if t.title.lower() == task_title.lower():
                t.status = 'finished'
                return True
        return False
    
    def list_all_tasks(self):
        return self.tasks
    
    def list_incomplete_tasks(self):
        incomplete_tasks = []
        for t in self.tasks:
            if t.status.lower() == 'not finished':
                incomplete_tasks.append(t)
        return incomplete_tasks

tdo = ToDoList()


try:
    while True:
        print(f"\n\n1.Add task \n2.Show all \n3.Show only incomplete \n4.Mark as complete \n5.Exit")

        no = int(input('Choose the task: '))

        if no == 1:
            t = input('You choose to add task. Please enter your task title: ')
            d = input('Enter your task description: ')
            dt = input('Enter your task due date(dd/mm/yyyy):' )
            s = input('Enter your task status: ')

            new_task = Task(t, d, dt)
            tdo.add_task(new_task)
        elif no == 2:
            print('All tasks: ')
            print('Title | Due date | Status')
            for k in tdo.list_all_tasks():
                q = k.title
                w = k.due_date
                e = k.status
                print(f"{q} | {w} | {e} ")
        elif no == 3:
            incomplete = tdo.list_incomplete_tasks()
            if not incomplete:
                print("All tasks completed!")
            else:
                print('Incomplete tasks: ')
                print('Title | Due date | Status')
                for k in tdo.list_incomplete_tasks():
                    q = k.title
                    w = k.due_date
                    e = k.status
                    print(f"{q} | {w} | {e} ")
        elif no == 4:
            t = input('Enter the completed task: ')
            if tdo.mark_task_complete(t):
                print("Done!")
            else:
                print("This task not founded!")
        elif no == 5:
            break
        else:
            print('Enter only 1-4!')
except:
    print('Error!')


############################################### SIMPLE BLOG SYSTEM ###############################################

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

class Blog:
    def __init__(self):
        self.posts = []
    def add_post(self, post):
        self.posts.append(post)
    def list_posts(self):
        if not self.posts:
            print("No posts available!")
            return []
        else:
            return self.posts

    def post_by_author(self, a):
        by_author = []
        for n in self.posts:
            if n.author.lower() == a.lower():
                by_author.append(n)
        return by_author
    def delete_post(self, a):
        for n in self.posts:
            if n.title.lower() == a.lower():
                self.posts.remove(n)
                return True
        return False
    def edit_post(self, a):
            for n in self.posts:
                if n.title.lower() == a.lower():
                    print(f"1.Edit the title \n2.Edit the content \n3.Edit the author")
                    ch = int(input(f"Choose 1-3 to edit: "))
                    if ch == 1:
                        new_title = input("Enter the new title: ")
                        n.title = new_title
                    elif ch == 2:
                        new_content = input("Enter the new content: ")
                        n.content = new_content
                    elif ch == 3:
                        new_author = input("Enter the new author: ")
                        n.author = new_author
                    else:
                        print("Choose only 1-3!")
                    return True
            return False
    def latest_posts(self):
        if not self.posts:
            print("No posts available! ")
        else: 
            for n in self.posts[-3:][::-1]:
                t = n.title
                c = n.content
                a = n.author
                print(f"{t} | {c} | {a}")
        
               

blg = Blog()

while True:
    print(f"\n\n\n1.Add posts \n2.Show all posts \n3.Display post by a specific author \n4.Delete post \n5.Edit the post \n6.Show latest posts \n7.Exit")

    choice = int(input("Please choose the task 1-5: "))

    if choice == 1:
        t = input("Please enter your task title: ")
        c = input("Enter your content: ")
        a = input("Enter the author: ")
        
        new_post = Post(t,c,a)
        blg.add_post(new_post)
    elif choice == 2:
        for k in blg.list_posts():
            p = k.title
            l = k.content
            m = k.author
            print(f"{p} | {l} | {m}")
    elif choice == 3:
        f = input("Enter the author: ")
        for k in blg.post_by_author(f):
            p = k.title
            l = k.content
            m = k.author
            print(f"{p} | {l} | {m}")

    elif choice == 4:
        p = input("Enter the post title: ")
        if blg.delete_post(p):
            print("Done!")
        else:
            print("Post not found!")
    elif choice == 5:
        title_to_edit = input("Enter the title of the post to edit: ")
        if not blg.edit_post(title_to_edit):
            print("Post not found!")
    elif choice == 6:
        blg.latest_posts()
    elif choice == 7:
        print("Thank you!")
        break


############################################### SIMPLE BANKING SYSTEM ###############################################


class Account:
    def __init__(self, number, name, balance=0):
        self.number = number
        self.name = name
        self.balance = balance

class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def find_account(self, number):
        for acc in self.accounts:
            if acc.number == number:
                return acc
        return None

    def check_balance(self, number):
        acc = self.find_account(number)
        if acc:
            return acc.balance
        return None

    def deposit(self, number, amount):
        acc = self.find_account(number)
        if acc:
            acc.balance += amount
            return True
        return False

    def withdraw(self, number, amount):
        acc = self.find_account(number)
        if acc and acc.balance >= amount:
            acc.balance -= amount
            return True
        return False

    def transfer(self, from_acc, to_acc, amount):
        sender = self.find_account(from_acc)
        receiver = self.find_account(to_acc)
        if sender and receiver and sender.balance >= amount:
            sender.balance -= amount
            receiver.balance += amount
            return True
        return False

    def show_details(self, number):
        acc = self.find_account(number)
        if acc:
            print(f"Name: {acc.name}, Number: {acc.number}, Balance: {acc.balance}")
        else:
            print("Account not found.")


bank = Bank()

print("Simple Banking System")
print("1. Add Account\n2. Check Balance\n3. Deposit\n4. Withdraw\n5. Transfer\n6. Show Account Details\n7. Exit")

while True:
    choice = int(input("Choose (1-7): "))
    if choice == 1:
        num = input("Account Number: ")
        name = input("Account Holder Name: ")
        bal = float(input("Initial Balance: "))
        acc = Account(num, name, bal)
        bank.add_account(acc)
    elif choice == 2:
        num = input("Account Number: ")
        bal = bank.check_balance(num)
        if bal is not None:
            print(f"Balance: {bal}")
        else:
            print("Account not found.")
    elif choice == 3:
        num = input("Account Number: ")
        amt = float(input("Amount to Deposit: "))
        if bank.deposit(num, amt):
            print("Deposited successfully!")
        else:
            print("Account not found.")
    elif choice == 4:
        num = input("Account Number: ")
        amt = float(input("Amount to Withdraw: "))
        if bank.withdraw(num, amt):
            print("Withdrawn successfully!")
        else:
            print("Not enough balance or account not found.")
    elif choice == 5:
        from_acc = input("Sender Account Number: ")
        to_acc = input("Receiver Account Number: ")
        amt = float(input("Amount to Transfer: "))
        if bank.transfer(from_acc, to_acc, amt):
            print("Transfer successful!")
        else:
            print("Transfer failed. Check accounts or balance.")
    elif choice == 6:
        num = input("Account Number: ")
        bank.show_details(num)
    elif choice == 7:
        print("Thank you!")
        break
