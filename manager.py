# Backend File Handling Class
import os, sys

class FileManagement:

    def __init__(self): 
        
        self.data = "" # to store data that is read from the file (it is of string type)
    
    def database_exists(self):
        if not os.path.exists("database.txt"):
            print("database.txt doesn't exit/ can't be accessed/ can't be created.")
            sys.exit(0)
    
    def read_data(self): 
        self.database_exists()
        file = open("database.txt", 'r')
        data_chunk = file.read() # stores the whole chunk of data; gotta process it to display it nicely
        data_chunk_processed = data_chunk.split("\n\n") # split the whole data about \n\n; accepts string; returns list
        data_chunk_processed_processed = []
        for item in data_chunk_processed:
            contents = item.split("\n") # splits each data entry about \n to separate name, email and phone number
            data_chunk_processed_processed.append(contents)
        data_chunk_processed_processed.pop() # remove the last element ie: [""]
        file.close()
        return(data_chunk_processed_processed)

    def write_data(self, content): 
        # content = a list composed of name, email, phone number at 0th, 1st and 2nd position respectively
        self.database_exists()
        file = open("database.txt", 'a+')
        name = content[0] + "\n"
        email = content[1] + "\n"
        phone = content[2] + "\n\n"
        file.write(name + email + phone)
        file.close()

    def edit_data(self, name, new_entry): 
        # takes the name of the person whose data has to be deleted
        # 1) read all data and store on array
        # 2) delete 'that' entry
        # 4) add a new entry
        # 3) overwirte the contents in the file
        self.delete_data(name)
        self.write_data(new_entry)
        
    def search_data(self, key): 
        # search by name/email/phone function 
        status = 'not found'
        data = self.read_data()
        for item in data:
            if key in item:
                status = 'found'
                return item
        if status == 'not found':
            return False
        

    def delete_data(self, name): 
        # takes the name of the person whose data has to be deleted
        # 1) read all data and store on array
        # 2) delete an entry
        # 3) write it back 
        self.database_exists()
        file = open("database.txt", 'a+')
        data = self.read_data()
        ret = False # gotta asign some value
        for item in data:
            if item[0] == name:
                data.remove(item)
                ret = True
        if ret == True:
            file.truncate(0) # remove all contents of file
            for item in data: # write the new contents to the file
                self.write_data(item) 
        else:
            ret = False # ie: data to be deleted wasn't present in the file...
        return ret
        file.close()
    
    def ask_user(self):
        while True:
            user_choice = input("\n1: read data\n2: write data\n3: edit data\n4: search data\n5: exit\n6: delete")
            if user_choice == '1':
                print(self.read_data())
            elif user_choice == '2':
                n = input("\n Name: ")
                e = input("\n Email: ")
                p = input("\n Phone: ")
                self.write_data([n, e, p])
            elif user_choice == '3':
                name = input("Enter the name of the user for which the data needs to be edited: ")
                print("Enter the new details for user: ")
                new_name = input("New name: ")
                new_email = input("New email: ")
                new_phone = input("New phone: ")
                self.edit_data(name, [new_name, new_email, new_phone])
            elif user_choice == '4':
                key = input("Enter one of name/ email/ phone to searh in the database")
                x = self.search_data(key)
                if x == False:
                    print("No such record exits in the database")
                else:
                    print(x)
            elif user_choice == '5':
                print("\nThank you for using THE FILE MANAGER developed by Suyash Ji!")
                break
            elif user_choice == '6':
                name = input("Enter the name for wihch the data is to be deleted: ")
                x = self.delete_data(name)
                if x == False:
                    print("No such record exists!")
            else:
                print("invalid choice... Try again!")
                
import tkinter as tk

# GUI Class
class Custom_frame(tk.Frame):
    
    def __init__(self, parent, *args, **kwargs):
        
        super().__init__(parent, *args, **kwargs)
        
        self.root = parent
        
        self.buttons_ka_frame = tk.Frame(self, width = 40, height = 300, bg = 'light green')
        self.buttons_ka_frame.pack(side = 'left')
        self.insert_frame = tk.Frame(self, width = 580, height = 300, bg = 'light green')
        self.delete_frame = tk.Frame(self, width = 580, height = 300, bg = 'light green')
        self.search_frame = tk.Frame(self, width = 580, height = 300, bg = 'light green')
        self.view_frame = tk.Frame(self, width = 580, height = 300, bg = 'light green')
        self.edit_frame = tk.Frame(self, width = 580, height = 300, bg = 'light green')
        
        # insert button
        self.insert_button = tk.Button(self.buttons_ka_frame, fg = '#00D6AC', bg = 'blue', width = '10', height = '2', text = 'Insert', command = lambda: self.insert(f)) 
        self.insert_button.pack( side = "top" )
        # delete button
        self.delete_button = tk.Button(self.buttons_ka_frame, fg = '#00D6AC', bg = 'blue', width = '10', height = '2', text = 'Delete', command = lambda: self.delete(f)) 
        self.delete_button.pack( side = "top" )
        # search button
        self.search_button = tk.Button(self.buttons_ka_frame, fg = '#00D6AC', bg = 'blue', width = '10', height = '2', text = 'Search', command = lambda: self.search(f)) 
        self.search_button.pack( side = "top" )
        # view button
        self.view_button = tk.Button(self.buttons_ka_frame, fg = '#00D6AC', bg = 'blue', width = '10', height = '2', text = 'View', command = lambda: self.view(f)) 
        self.view_button.pack( side = "top" )
        # edit button
        self.edit_button = tk.Button(self.buttons_ka_frame, fg = '#00D6AC', bg = 'blue', width = '10', height = '2', text = 'Edit', command = lambda: self.edit(f)) 
        self.edit_button.pack( side = "top" )
        # exit button
        self.exit_button = tk.Button(self.buttons_ka_frame, fg = '#00D6AC', bg = 'blue', width = '10', height = '2', text = 'Exit', command = lambda: self.exit()) 
        self.exit_button.pack( side = "top" )
        # refresh button
        self.exit_button = tk.Button(self.buttons_ka_frame, fg = '#00D6AC', bg = 'blue', width = '10', height = '2', text = 'Refresh', command = lambda: self.refresh()) 
        self.exit_button.pack( side = "top" )
        
    def refresh(self):
        self.insert_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.search_frame.pack_forget()
        self.view_frame.pack_forget()
        self.edit_frame.pack_forget()
    
    # f -> reference of file...   
    
    def insert(self,f):
        
        self.refresh()
        self.insert_frame.pack()
        
        name_lbl = tk.Label(self.insert_frame, fg ="#000", bg = "#FFF", text = "Name: ")
        name_lbl.place(x = 0, y = 130)
        name_entry = tk.Entry(self.insert_frame, fg ="#000", bg = "#FFF")
        name_entry.place(x = 40, y = 130)
        
        email_lbl = tk.Label(self.insert_frame, fg ="#000", bg = "#FFF", text = "Email: ")
        email_lbl.place(x = 0, y = 160)
        email_entry = tk.Entry(self.insert_frame, fg ="#000", bg = "#FFF")
        email_entry.place(x = 40, y = 160)
        
        phone_lbl = tk.Label(self.insert_frame, fg ="#000", bg = "#FFF", text = "Phone: ")
        phone_lbl.place(x = 0, y = 190)
        phone_entry = tk.Entry(self.insert_frame, fg ="#000", bg = "#FFF")
        phone_entry.place(x = 40, y = 190)
        
        insert_now_btn = tk.Button(self.insert_frame, fg = '#00D6AC', bg = 'blue', width = '10', height = '2', text = 'Write now', command = lambda: insert_now_btn_click() ) 
        insert_now_btn.place(x = 0, y = 210)
        
        def insert_now_btn_click():
            f.write_data([name_entry.get(), email_entry.get(), phone_entry.get()])
            name_entry.delete(0, 'end')
            email_entry.delete(0, 'end')
            phone_entry.delete(0, 'end')

    def delete(self,f):
            
        self.refresh()
        self.delete_frame.pack()
        
        name_lbl = tk.Label(self.delete_frame, fg ="#000", bg = "#FFF", text = "Name: ")
        name_lbl.place(x = 0, y = 130)
        name_entry = tk.Entry(self.delete_frame, fg ="#000", bg = "#FFF")
        name_entry.place(x = 40, y = 130)
        
        delete_now_btn = tk.Button(self.delete_frame, fg = '#00D6AC', bg = 'blue', width = '10', height = '2', text = 'Delete now', command = lambda: delete_now_btn_click() ) 
        delete_now_btn.place(x = 0, y = 210)

        def delete_now_btn_click():
            f.delete_data(name_entry.get())
            name_entry.delete(0, 'end')
            
    def search(self,f):
        
        self.refresh()
        self.search_frame.pack()
        
        key_lbl = tk.Label(self.search_frame, fg ="#000", bg = "#FFF", text = "key: ")
        key_lbl.place(x = 0, y = 130)
        
        key_entry = tk.Entry(self.search_frame, fg ="#000", bg = "#FFF")
        key_entry.place(x = 40, y = 130)
        
        record_found_lbl = tk.Label(self.search_frame, fg ="#000", bg = "#FFF", text = "")
        record_found_lbl.place(x = 0, y = 160)
        
        search_now_btn = tk.Button(self.search_frame, fg = '#00D6AC', bg = 'blue', width = '10', height = '2', text = 'Search now', command = lambda: search_now_btn_click() ) 
        search_now_btn.place(x = 0, y = 210)

        def search_now_btn_click():
            item = f.search_data(key_entry.get())
            if item == False:
                record_found_lbl["text"] = "Not found"
            else:
                record_found_lbl["text"] = item
            key_entry.delete(0, 'end')
        
    def view(self,f):
        
        self.refresh()
        self.view_frame.pack()

        # Vertical (y) Scroll Bar
        scroll = tk.Scrollbar(self.view_frame)
        scroll.place(x = 0, y = 135)

        # Text Area Widget
        text_area = tk.Text(self.view_frame, height = 100, width = 50, wrap= "word", yscrollcommand = scroll.set)
        text_area.place(x = 0, y = 130)
        text_area.insert("insert", f.read_data())

        # Configure the scrollbars
        scroll.config(command = text_area.yview)

    def edit(self,f):
        
        self.refresh()
        self.edit_frame.pack()

        old_name_lbl = tk.Label(self.edit_frame, fg ="#000", bg = "#FFF", text = "Name: ")
        old_name_lbl.place(x = 0, y = 130)
        old_name_entry = tk.Entry(self.edit_frame, fg ="#000", bg = "#FFF")
        old_name_entry.place(x = 40, y = 130)

        name_lbl = tk.Label(self.edit_frame, fg ="#000", bg = "#FFF", text = "New Name: ")
        name_lbl.place(x = 0, y = 160)
        name_entry = tk.Entry(self.edit_frame, fg ="#000", bg = "#FFF")
        name_entry.place(x = 70, y = 160)

        email_lbl = tk.Label(self.edit_frame, fg ="#000", bg = "#FFF", text = "New Email: ")
        email_lbl.place(x = 0, y = 190)
        email_entry = tk.Entry(self.edit_frame, fg ="#000", bg = "#FFF")
        email_entry.place(x = 70, y = 190)

        phone_lbl = tk.Label(self.edit_frame, fg ="#000", bg = "#FFF", text = "New Phone: ")
        phone_lbl.place(x = 0, y = 210)
        phone_entry = tk.Entry(self.edit_frame, fg ="#000", bg = "#FFF")
        phone_entry.place(x = 70, y = 210)

        insert_now_btn = tk.Button(self.edit_frame, fg = '#00D6AC', bg = 'blue', width = '10', height = '2', text = 'Edit now', command = lambda: edit_now_btn_click() ) 
        insert_now_btn.place(x = 0, y = 240)

        def edit_now_btn_click():
            f.edit_data(old_name_entry.get(), [name_entry.get(), email_entry.get(), phone_entry.get()])
            old_name_entry.delete(0, 'end')
            name_entry.delete(0, 'end')
            email_entry.delete(0, 'end')
            phone_entry.delete(0, 'end')


    def exit(self):
        self.root.destroy() # quit the application
        

root = tk.Tk() # main widow of the application
root.title("File Manager By Suyash Gupta")
cf = Custom_frame(root, width = 580, height = 400)
cf.pack()
f = FileManagement()
root.mainloop()
