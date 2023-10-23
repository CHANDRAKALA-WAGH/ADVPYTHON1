class Stud:
   def set_data(self, org, code):
       self.org = org
       self.code = code

class Sports(Stud):
   def set_name(self, sport, marks ):
      self.sport = sport
      self.marks = marks

class sub (Stud):