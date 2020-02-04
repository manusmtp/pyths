import cmd

#gives us a simple command line handler which calls the respective custom handler when we call the function

class HelloW(cmd.Cmd):
	"""simple command line processor example"""
	""" here the do_<function_name> and the arguments which are defined are important and pre-defined"""
	cmd.prompt='$'
	def do_hello(self,line):
		'''this just welcomes the user'''
		print("hello welcome to python")
	def do_goodM(self,line):
		print("Good day to you")
	def do_hru(self,line):
		print("AM fine ! how are you?")

if __name__ == '__main__':
	HelloW().cmdloop()