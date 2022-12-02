from tkinter import *
def add_contact():
    new_contact = '{name} {surname}: {phone_number}'\
                .format(name=entryName.get(), surname=entrySurName.get(), phone_number=entryPhoneNumber.get())
    allContacts.insert(END, new_contact)
    write_contacts()


def delete_contact():
    select = allContacts.curselection()
    allContacts.delete(select[0])
    write_contacts()

def write_contacts():
    data = open('phonebook.txt', 'w+', encoding='utf-8')
    for row in allContacts.get(0, END):
        data.writelines(row + '\n')
    data.close()

def print_contacts():
    try:
        data = open('phonebook.txt', 'r', encoding='utf-8')
        for contact in data.readlines():
            allContacts.insert(END, contact)
        data.close()
    except FileNotFoundError:
        print('Файл не найден')


root = Tk()

root.geometry('400x300')

buttonAddContact  = Button(root, text='Добавить контакт', command=add_contact)
buttonAddContact.grid(row=3, column=0, columnspan=2)
buttonDeleteContact  = Button(root, text='Удалить контакт', command=delete_contact)
buttonDeleteContact.grid(row=4, column=1)

labelName = Label(root, text='введите имя')
labelName.grid(row=0, column=0)
labelSurName = Label(root, text='введите фамилию')
labelSurName.grid(row=1, column=0)
labelPhoneNumber = Label(root, text='введите номер телефона')
labelPhoneNumber.grid(row=2, column=0)

entryName = Entry(root, width=15)
entryName.grid(row=0, column=1)
entrySurName = Entry(root, width=15)
entrySurName.grid(row=1, column=1)
entryPhoneNumber = Entry(root, width=15)
entryPhoneNumber.grid(row=2, column=1)

allContacts = Listbox(root, height=8, width=45, selectmode=EXTENDED)
allContacts.grid(row=4, column=0)





root.mainloop()