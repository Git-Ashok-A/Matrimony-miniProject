import cx_Oracle

class AdduserData():
    def __init__(self, *args):
        self.con = cx_Oracle.connect('MATRIMONY/admin123@localhost')
        cursor = self.con.cursor()

    def RegisterForm(self,fname,lname,gender,dob,age,religion,country,father,mother,father_occ,mother_occ,mother_tounge,qualification,occupation,salary,address,pincode,state,addhar,mobile_number):
        if gender == 'male':
            self.cursor.execute("INSERT INTO MALE VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(fname,lname,gender,dob,age,religion,country,father,mother,father_occ,mother_occ,mother_tounge,qualification,occupation,salary,address,pincode,state,addhar,mobile_number))
        elif gender == 'female':
            self.cursor.execute("INSERT INTO FEMALE VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(fname,lname,gender,dob,age,religion,country,father,mother,father_occ,mother_occ,mother_tounge,qualification,occupation,salary,address,pincode,state,addhar,mobile_number))
        self.con.commit()

    