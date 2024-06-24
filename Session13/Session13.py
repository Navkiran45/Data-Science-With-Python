"""

MySQL
SQL -> Structured Query Language 
Object Relational Mapping(ORM)

#1. List Databases
show databases;

# 2. create your database
create database training; 

# 3. Select the database in which u wish to create ur table
use training; 

# 4. Create Table
create table Customer(
    cid int primary key auto_increment,
    name varchar(256),
    phone varchar(15),
    email varchar(256),
    age int,
    gender varchar(10)
    );
# 5. To check if table is created
show tables;
# 6.to see attributes
    decribe Customer;

# 7. Create Customer in table
insert into Customer values(null, 'John', '+91 99929 88808', 'john@gmail.com', 24, 'male');

# 8. Fetch Data from Customer
select * from customer;
select * from customer where cid = 1;
select name, email from customer;
select * from customer;

# 9. Update Operation
update customer set name= 'Johnnathan', email = 'john.jj@gmail.com' where cid = 1;

# 10. Delete Operation
delete from customer where cid = '1'


create table Address(
    aid int primary key auto increment
    houseno varchar(256),
    addressline1 varchar(256), 
    city varchar(256), 
    state varchar(256), 
    zipCode int, 
    landmark varchar(256)
    );

Customer: name, agr, phone, email, gender
Address: houseno, addressline1, addressline2, city, state, zipCode, landmark

"""

class Customer:
    def __init__(self, name, age, phone, email, gender):
        self.name = name
        self.age = age
        self.phone = phone
        self.email = email
        self.gender = gender

class Address:
    def __init__(self, houseno, addressline1, city, state, zipCode, landmark):
        self.houseno = houseno
        self.addressline1 = addressline1
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.landmark = landmark