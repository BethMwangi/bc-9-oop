class Student(object): #instantiate

	def __init__ (self,  id, first_name, last_name):
		# generate sequential unique ids
	    self.__reg = id  #fake private
		self.first_name = first_name
		self.last_name = last_name

	def attend_class(self, **kwargs):
		# default values 
		# bc = location
		# date = current_date
		# ta = name 
		pass


