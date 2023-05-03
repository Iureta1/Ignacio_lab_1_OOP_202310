class ParseOptions:

    
    @classmethod
    def display_menu(cls):
        print("MENU")
        print("1. Cantidad de mesas por region")
        print("2. Resultados generales")
        print("3. Resultados por local elegido")
        

    @classmethod   
    def get_option(cls):

        opcion = input("Elige una opcion: ")
        return opcion