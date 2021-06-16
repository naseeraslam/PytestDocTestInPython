import os
import random
from datetime import datetime


class StudentData(object):
    def __init__(self):
        self.FNam = ''
        self.LName = ''
        self.MobileNo = ''
        self.City = ''
        self.Email = ''
        self.Profession = ''
        self.f_r = open("Student Record.txt", mode='a')

    def AdressBook(self, firstName, lastName, Mb, City, Email, Profession):
        """Basic Data Search Example.
          >>> obj=StudentData()
          >>> x=obj.AdressBook("Naseer", "Aslam", "03062403761", "Kasur", "bitf17a039@pucit.edu.pk", "Software Engineer")
          >>> print(x)
          Saved

          >>> obj=StudentData()
          >>> x=obj.AdressBook("Sohaib", "Aslam", "03062403761", "Kasur", "bitf17a039@pucit.edu.pk", "Software Engineer")
          >>> print(x)
          Saved
           >>> obj=StudentData()
          >>> x=obj.SearchByFirstName("Sohaib")
          >>> print(x)
          Found
          """
        f_W = open("Student Record.txt", mode='a')
        self.FName = firstName
        self.LName = lastName
        self.MobileNo = Mb
        self.City = City
        self.Email = Email
        self.Profession = Profession
        f_W.write(
            self.FName + "," + self.LName + "," + self.MobileNo + "," + self.City + "," + self.Email + "," + self.Profession + '\n')
        return "Saved"
        # f_W.close()

    def SearchByFirstName(self, FName_S):

        """Basic Data Search Example.
          >>> obj=StudentData()
          >>> x=obj.SearchByFirstName("Naseer")
          >>> print(x)
          Found

          """
        f_r = open("Student Record.txt", mode='r')
        s = ' '
        count = 0
        while (s):
            s = f_r.readline()
            L = s.split(",")
            if len(s) > 0:
                if (L[0] == FName_S):
                    count = count + 1
                    return "Found"
        # if count == 0:
        #     return "Not Found"
        # f_r.close()

    def SearchByMobile(self, Mobile_S):
        f_r = open("Student Record.txt", mode='r')
        s = ' '
        count = 0
        while (s):
            s = f_r.readline()
            L = s.split(",")
            if len(s) > 0:
                if (L[2] == Mobile_S):
                    count = count + 1
                    return "Found"
        # if count == 0:
        #     return "Not Found"
        # f_r.close()

    def SearchByEmail(self, Email_S):
        f_r = open("Student Record.txt", mode='r')
        s = ' '
        count = 0
        while (s):
            s = f_r.readline()
            L = s.split(",")
            if len(s) > 0:
                if (L[4] == Email_S):
                    count = count + 1
                    return "Found"
        # if count == 0:
        #     return "Not Found"
        # f_r.close()

    def SpecialSearchByFirstName(self, FName_S):
        f_r = open("Student Record.txt", mode='r')
        s = ' '
        count = 0
        while (s):
            s = f_r.readline()
            L = s.split(",")
            if len(s) > 0:
                if (L[0].find(FName_S) != -1):
                    count = count + 1
                    return "Found"
        # if count == 0:
        #     return "Not Found"
        # f_r.close()

    def UpdateRecord(self, FName_SU, Updated_fname, Updated_lname, Updated_mb, Updated_city, Updated_email,
                     Updated_Prof):
        f_r = open("Student Record.txt", mode='r')
        f_w = open("UpdateStudent Record.txt", mode='w')
        s = ' '
        count = 0
        while (s):
            s = f_r.readline()
            L = s.split(",")
            if len(s) > 0:
                if (L[0] == FName_SU):
                    count = count + 1
                    self.FName = Updated_fname
                    self.LName = Updated_lname
                    self.MobileNo = Updated_mb
                    self.City = Updated_city
                    self.Email = Updated_email
                    self.Profession = Updated_Prof
                    f_w.write(
                        self.FName + "," + self.LName + "," + self.MobileNo + "," + self.City + "," + self.Email + "," + self.Profession + '\n')
                else:
                    f_w.write(s)
        # if count == 0:
        #     return "Not Updated"
        # else:
        if count > 0:
            return "Updated"
        # f_r.close()
        # f_w.close()
        # os.remove("Student Record.txt")
        # os.rename(r'E:\Semester 8\WEB\Labs\UpdateStudent Record.txt', "Student Record.txt")

    def clear(self):
        self.f_r.close()
        os.remove("Student Record.txt")

    def ReturnObject(self):
        """Basic Object Return Example.
        >>> obj = StudentData()
        >>> x= obj.ReturnObject()
        >>> print(x) #doctest: +ELLIPSIS
        <Student_Record.StudentData object at 0x...>
        """
        return StudentData()

    def StudentRegistrationTime(self):
        """Basic Object Return Example.
        >>> obj = StudentData()
        >>> x= obj.StudentRegistrationTime() #doctest: +ELLIPSIS
        Date & Time = ...   at that moment
        """
        current = datetime.now()
        formatOFTime = current.strftime("%d/%m/%Y %H:%M:%S")
        print("Date & Time =", formatOFTime, "  at that moment")

    def StudentIDGenerator(self):
        """Basic ID Generator Example.
        >>> obj = StudentData()
        >>> print(obj.StudentIDGenerator()) #doctest: +ELLIPSIS
        BSITF17A0...
        """
        print("BSITF17A0" + str(random.randint(0, 60)))

    def MultipleStudentIDGenerator(self):
        """
        >>> obj = StudentData()
        >>> obj.MultipleStudentIDGenerator("Naseer Aslam") #doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
         ...
        TypeError: 'str' object a a cannot be interpreted as an integer
            """
        print("BSITF17A0" + str([random.randint(0, 60) for i in range(number)]))
