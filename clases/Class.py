class User:
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def show_username(self,pwd):
        if pwd == self.__password:
            return self.__username
        return "no te puedo mostrar el username"
    
    def show_password

    def change_password(self,pwd,new_value):
        if pwd == self.__password:
            self.__password = new_value
            return "cambio exitoso"
        return "cambio fallido"