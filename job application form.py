from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd

red = 'red'
title = ('Calibri',25)
heading = ('Calibri', 14)
sub_heading = ('Calibri',11)
hint = ('Calibri', 8)
button_font = ('Helvetica', 15, 'bold')

horizontal_padding = 10
label_width = 20

window = Tk()

Frame(window, bg = red, height = 5).pack(fill = X)

Label(window, text = 'Job Application',font = title).pack(fill = X)

Label(window, text = 'Personal Information', font = heading, fg = red,  anchor = 'w').pack(fill = X)

# Name
name_input_frame = Frame(window)
Label(name_input_frame, text = 'Name', anchor = 'nw', font = sub_heading, width = label_width).grid(row = 0 , column = 0, sticky = 'nwe')
name_input_frame.pack(fill = X)

# First Name
first_name = Entry(name_input_frame)
first_name.grid(row = 0, column = 1, sticky = 'we', padx = horizontal_padding)
Label(name_input_frame,text = 'First Name', anchor = 'w', font = hint).grid(row = 1, column = 1, sticky = 'we', padx = horizontal_padding)

# Last Name
last_name = Entry(name_input_frame)
last_name.grid(row = 0, column = 2, sticky = 'we', padx = horizontal_padding)
Label(name_input_frame,text = 'Last Name', anchor = 'w', font = hint).grid(row = 1, column = 2, sticky = 'we', padx = horizontal_padding)

name_input_frame.grid_columnconfigure(1, weight = 1)
name_input_frame.grid_columnconfigure(2, weight = 1)

name_input_frame.grid_rowconfigure(0, weight = 1)
name_input_frame.grid_rowconfigure(1, weight = 1)

# Email
email_frame = Frame(window)
email_frame.pack(fill = X)
Label(email_frame ,text = 'Email', anchor = 'w', font = sub_heading, width = label_width).grid(row = 0, column = 0, sticky = 'w')
email = Entry(email_frame)
email.grid(row = 0, column = 1, sticky = 'we', padx = horizontal_padding)
email_frame.grid_columnconfigure(1, weight = 1)

# Education
education_frame = Frame(window)
education_frame.pack(fill = X)
Label(education_frame, text = 'Education', anchor = 'w', font = sub_heading, width = label_width).grid(row=0, column = 0, sticky = 'w')
education = ttk.Combobox(education_frame, values = ['College','Shcool'])
education.grid(row = 0, column = 1, padx = horizontal_padding)

def file_chooser(label):
    filename = fd.askopenfilename()
    label.configure(text = filename)
    label.update()

#Resume
resume_frame = Frame(window)
resume_frame.pack(fill = X)
Label(resume_frame, text = 'Resume', anchor = 'w', font = sub_heading, width = label_width).grid(row = 0, column = 0, sticky = 'we')
resume_path_label = Label(resume_frame, anchor= 'w', text = 'No File Chosen')
Button(resume_frame, text = 'Choose File', command = lambda label = resume_path_label: file_chooser(label)). grid(row = 0, column = 1, sticky = 'we', padx = horizontal_padding)
resume_path_label.grid(row = 0, column = 2 , sticky = 'we', padx = horizontal_padding)



# Address 
address_frame = Frame(window)
address_frame.pack(fill = X)
Label(address_frame, text = 'Address', anchor = 'w', font = sub_heading, width = label_width).grid(row = 0, column = 0, sticky = 'w')
address1 = Entry(address_frame)
address2 = Entry(address_frame)

address1.grid(row = 0, column = 1, columnspan = 3, sticky = 'we', padx = horizontal_padding)
Label(address_frame, text = "Address 1", font = hint).grid(row = 1, column = 1, columnspan = 3, padx = horizontal_padding)

address2.grid(row = 2, column = 1, columnspan = 3, sticky = 'we', padx = horizontal_padding)
Label(address_frame, text = "Address 2", font = hint).grid(row = 3, column = 1, columnspan = 3, padx = horizontal_padding)

country = ttk.Combobox(address_frame, values = ['India','USA'])
country.grid(row = 4, column = 1, stick = 'we', columnspan = 3, padx = horizontal_padding)
Label(address_frame, text = "Country", font = hint).grid(row = 5, column = 1, columnspan = 3, padx = horizontal_padding)


city = Entry(address_frame)
city.grid(row = 6, column = 1, sticky = 'we', padx = horizontal_padding)
Label(address_frame, text = 'City', font = hint).grid(row = 7, column = 1, sticky = 'we', padx = horizontal_padding)

state = Entry(address_frame)
state.grid(row = 6, column = 2, sticky = 'we', padx = horizontal_padding)
Label(address_frame, text = 'State', font = hint).grid(row = 7, column = 2, sticky = 'we', padx = horizontal_padding)


zip_code = Entry(address_frame)
zip_code.grid(row = 6, column = 3, sticky = 'we', padx = horizontal_padding)
Label(address_frame, text = 'Zip Code', font = hint).grid(row = 7, column = 3, sticky = 'we', padx = horizontal_padding)


address_frame.grid_columnconfigure(1, weight = 50)
address_frame.grid_columnconfigure(2, weight = 3)
address_frame.grid_columnconfigure(3, weight = 15)

# Phone Number
phone_frame = Frame(window)
phone_frame.pack(fill = X)
Label(phone_frame, text = 'Phone Number', anchor = 'w', font = sub_heading, width = label_width).grid(row = 0, column = 0, sticky = 'we')

std_code = Entry(phone_frame)
std_code.grid(row = 0, column = 1, sticky = 'we', padx = horizontal_padding)

phone_number = Entry(phone_frame)
phone_number.grid(row = 0, column = 2, sticky = 'we', padx = horizontal_padding)

phone_frame.grid_columnconfigure(1, weight = 1)
phone_frame.grid_columnconfigure(2, weight = 50)

# Hobbies
Label(window, text = 'What are your hobbies ?', anchor = 'w', font = sub_heading).pack(fill = X)
hobbies = Entry(window)
hobbies.pack(fill = X, padx = horizontal_padding)

Label(window, text = 'Previous/Current Emplyment Details', font = heading, fg = red,  anchor = 'w').pack(fill = X)

# Company Name
company_frame = Frame(window)
company_frame.pack(fill = X)
Label(company_frame, text = 'Company Name', anchor = 'w', font = sub_heading, width = label_width).grid(row = 0, column = 0, sticky = 'we')
company_name = Entry(company_frame)
company_name.grid(row = 0, column = 1, sticky = 'we', padx = horizontal_padding)

company_frame.grid_columnconfigure(1, weight = 1)

# Job Title
job_frame = Frame(window)
job_frame.pack(fill = X)
Label(job_frame, text = 'Job Title', anchor = 'w', font = sub_heading, width = label_width).grid(row = 0, column = 0, sticky = 'we')
job_title = Entry(job_frame)
job_title.grid(row = 0, column = 1, sticky = 'we', padx = horizontal_padding)

job_frame.grid_columnconfigure(1, weight = 1)

# Years Lived
years_lived_frame = Frame(window)
years_lived_frame.pack(fill = X)
Label(years_lived_frame, text = 'How long were you here ?', anchor = 'w', font = sub_heading, width = label_width, wraplength = 150).grid(row = 0, column = 0, sticky = 'we')
years_lived = Entry(years_lived_frame)
years_lived.grid(row = 0, column = 1, sticky = 'we', padx = horizontal_padding)

years_lived_frame.grid_columnconfigure(1, weight = 1)

# Reference 1
Label(window, text = 'Reference #1', font = heading, fg = red,  anchor = 'w').pack(fill = X)

# Reference 1 Name
reference1_name_frame = Frame(window)
reference1_name_frame.pack(fill = X)
Label(reference1_name_frame, text = 'Name', anchor = 'w', font = sub_heading, width = label_width).grid(row = 0, column = 0, sticky = 'we')
reference1_name = Entry(reference1_name_frame)
reference1_name.grid(row = 0, column = 1, sticky = 'we', padx = horizontal_padding)

reference1_name_frame.grid_columnconfigure(1, weight = 1)

# Reference 1 Phone
reference1_phone_frame = Frame(window)
reference1_phone_frame.pack(fill = X)
Label(reference1_phone_frame, text = 'Phone', anchor = 'w', font = sub_heading, width = label_width).grid(row = 0, column = 0, sticky = 'we')
reference1_phone = Entry(reference1_phone_frame)
reference1_phone.grid(row = 0, column = 1, sticky = 'we', padx = horizontal_padding)

reference1_phone_frame.grid_columnconfigure(1, weight = 1)

# Reference 2
Label(window, text = 'Reference #2', font = heading, fg = red,  anchor = 'w').pack(fill = X)

# Reference 2 Name
reference2_name_frame = Frame(window)
reference2_name_frame.pack(fill = X)
Label(reference2_name_frame, text = 'Name', anchor = 'w', font = sub_heading, width = label_width).grid(row = 0, column = 0, sticky = 'we')
reference2_name = Entry(reference2_name_frame)
reference2_name.grid(row = 0, column = 1, sticky = 'we', padx = horizontal_padding)

reference2_name_frame.grid_columnconfigure(1, weight = 1)

# Reference 2 Phone
reference2_phone_frame = Frame(window)
reference2_phone_frame.pack(fill = X)
Label(reference2_phone_frame, text = 'Phone', anchor = 'w', font = sub_heading, width = label_width).grid(row = 0, column = 0, sticky = 'we')
reference2_phone = Entry(reference2_phone_frame)
reference2_phone.grid(row = 0, column = 1, sticky = 'we', padx = horizontal_padding)

reference2_phone_frame.grid_columnconfigure(1, weight = 1)

# Apply Button
apply_frame= Frame(window)
apply_frame.pack(fill = X, pady = 10)
apply_button = Button(apply_frame, text = 'Apply', bg = red, fg = 'white', font = button_font )
apply_button.pack()

window.mainloop()