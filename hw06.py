from collections import UserDict
import re

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        self.value = self.valid_name(value)

    def valid_name(self, name):
        if not name:
            raise ValueError("Name - required field.")
        return name

class Phone(Field):
    def __init__(self, value):
         self.value = self.valid_phone(value)

    def valid_phone(self, phone):
        regex = "^[0-9]{10}$"
        if not re.match(regex, phone):
            raise ValueError("It's not a phone number.")
        return phone

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(p.value for p in self.phones)}"
    
    def add_phone(self, phone):
        phone = Phone(phone)
        if phone not in self.phones:
            self.phones.append(phone)
            return self.phones
        else:
            raise ValueError('Phone {phone} already exists')

    def remove_phone(self, phone):
        phone = Phone(phone)
        for i in range(len(self.phones)):
            if self.phones[i].value == phone.value:
                self.phones.pop(i)
                return self.phones        
            else:
                return None
        

    def edit_phone(self, old_phone, new_phone):
        old_phone = Phone(old_phone)
        new_phone = Phone(new_phone)
        for i in range(len(self.phones)):
            if self.phones[i].value == old_phone.value:
                self.phones.pop(i)
                self.phones.insert(i, new_phone)
                return self.phones
            else:
                raise ValueError(f"{old_phone} is not found")

    def find_phone(self, phone):
        self.phone = Phone(phone)
        for i in range(len(self.phones)):
            if self.phones[i].value == self.phone.value:
                return self.phone
        return None

class AddressBook(UserDict):
    def __init__(self):
        self.data = {} 
    # реалізація класу
    def __str__(self):
        str_book = ''
        for key in self.data:
            str_book += self.data[key].__str__() + '\n'
        return str_book
 
    
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        name = Name(name)
        for key in self.data:
            if key == name.value:
                return self.data[key]
        else:
            return None
       
    def delete(self, name):
        name = Name(name)
        if name.value in self.data:
            del self.data[name.value]
        else:
            return ValueError(f"{name} is not found")
        return self.data

if __name__ == "__main__":
    # Створення нової адресної книги
    book = AddressBook()
        # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
        # Додавання запису John до адресної книги
    book.add_record(john_record)
        # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)
        # Виведення всіх записів у книзі
    print(book)
        # Знаходження та редагування телефону для John
    john = book.find("John")
    john_record.edit_phone("1234567890", "1112223333")
    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555
        # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555
        # Видалення запису Jane
    book.delete("Jane")


