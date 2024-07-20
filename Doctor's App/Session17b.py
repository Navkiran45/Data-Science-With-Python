import datetime
"""
create table Consultation(
cid int primary key auto_increment,
pid int, 
remarks varchar(256),
medicines varchar(256),
next_followup datetime,
created_on datetime,
FOREIGN KEY(pid) REFERENCES Doc_Patient(pid)
);
"""
class Consultation:
    def __init__(self, cid=0, pid=0, remarks= "",medicines="", next_followup="" ):
        self.pid = pid
        self.cid = cid
        self.remarks = remarks
        self.medicines = medicines
        self.next_followup = next_followup
        self.created_on = datetime.datetime.now()

    def add_consultation_details(self):
        self.pid = input("Enter Patient's ID: ")
        self.remarks = input("Enter Consultation Remarks: ")
        self.medicines = input("Enter Medicines: ")
        self.next_followup = input("Enter Next Followup (yyyy-mm-dd hh:mm:ss): ")

    def show(self):
        print("------------CONSULTATION-----------------")
        consultation = """
        {cid} |{pid} 
        {remarks} | {medicines}
        {next_followup} | {created_on}
        """.format_map(vars(self))
        
        print(consultation)
        