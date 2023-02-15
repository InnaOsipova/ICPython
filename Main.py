import Controllers

class Main_figures ():

    def run (self):
     controller = Controllers.Controller()
     print("Выберите пункт :")
     print("1 - ввести новую заметку")
     print("2 - прочитать все заметки")
     print("3 - прочитать одну заметку по ее названию")
     print("4 - удалить заметку")
     n = int(input())
     if n == 1:
        controller.write_note()
     elif n == 2:
        controller.read_notes()
     elif n == 3:
        name = input('Введите название заметки: ')
        controller.read_note(name)
     elif n == 4:
        name = input('Введите название заметки: ')
        controller.del_note(name)
     else:
        print('Не корректный выбор')

m = Main_figures()
m.run()
