import mysql.connector
from datetime import datetime
from connection import connection
from Student import Student
from Teacher import Teacher
from Class import Class


class DbManager:
    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()


    def getStudentById(self, id):
        sql ="select * from students where id = %s"
        value = (id,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchone()
            return Student.CreateStudent(obj)
        except mysql.connector.Error  as err:
            print("Error",err) 


    def deleteStudent(self,studentid):
        sql = "delete from student where id=%s"
        value = (studentid,)
        self.cursor.execute(sql,value)

    def getStudentByClassId(self, id):
        sql ="select * from students where classid = %s"
        value = (id,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchall()
            return Student.CreateStudent(obj)
        except mysql.connector.Error  as err:
            print("Error",err)  

    def getClasses(self):
        sql = "select * from classes"
        self.cursor.execute(sql)
        try:
            obj = self.cursor.fetchall()
            return Class.CreateClass(obj)
        except mysql.connector.Error as err:
            print('Error:', err)

    def addStudent(self, student: Student):
        sql = "INSERT INTO Students(StudentNumber,Name,Surname,Birthdate,Gender,ClassId) VALUES (%s,%s,%s,%s,%s,%s)"
        value = (student.StudentNumber,student.name, student.surname,student.birthdate,student.gender,student.classid)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt eklendi.')
        except mysql.connector.Error as err:
            print('hata:', err) 

    def editStudent(self, student: Student):
        sql = "update students set StudentNumber=%s,name=%s,surname=%s,birthdate=%s,gender=%s,classid=%s where id=%s"
        value = (student.StudentNumber,student.name, student.surname,student.birthdate,student.gender,student.classid,student.id)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt güncellendi.')
        except mysql.connector.Error as err:
            print('hata:', err)

    def addTeacher(self, teacher: Teacher):
        pass

    def editTeacher(self, teacher: Teacher):
        pass

    def __del__(self):
        self.connection.close()
        print ("db silindi")



# db = DbManager()

# student = db.getStudentById(1)

# student[0].surname = "Hakan"


# #print(student[0].StudentNumber)
# # print(student[0].name)
# # print(student[0].surname)
# # print(student[0].birthdate)
# db.editStudent(student[0])




# # print(student[0].name)

# # student = db.getStudentByClassId(1)
# # print(student[0].surname)