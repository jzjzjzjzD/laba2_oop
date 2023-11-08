class User:
	def show(self,name, salary):
		return name + ' ' + salary
user = User()
print(user.show('john', "5000"))