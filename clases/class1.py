from Class import User

u = User("username","password")
print(u.show_username("password"))
print(u.show_username(" "))
#print(u.__password)
u.password = "nueva clave"
#print(u.password)
print(u.change_password("pass","nueva_clave"))
print(u.change_password("password","nueva_clave"))
print(u.__username)