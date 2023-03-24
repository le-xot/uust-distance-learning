# Инициализация класса Работник
class Employee:
    def __init__(self, name, surename, discharge=6):
        self.name = name
        self.surename = surename
        self.discharge = discharge

    # Создание метода для вывода всей информации о сотруднике
    def conclusion(self):
        print(
            "\n",
            "Имя =",
            self.name,
            "\n",
            "Фамилия =",
            self.surename,
            "\n",
            "Разряд =",
            self.discharge,
        )

    # Создание деструктора
    def __del__(self):
        print("\n", "Всего доброго,", self.name, self.surename)


# Информация о сотрудниках
worker1 = Employee("Иван", "Иванов", 3)
worker2 = Employee("Петр", "Петров", 5)
worker3 = Employee("Петр", "Сидоров", 2)

# Вывод всей информации о всех сотрудниках
worker1.conclusion()
worker2.conclusion()
worker3.conclusion()

# Прощаемся с сотрудником, имеющим минимальное значение разряда
if worker1.discharge < worker2.discharge and worker1.discharge < worker3.discharge:
    del worker1
elif worker2.discharge < worker1.discharge and worker2.discharge < worker3.discharge:
    del worker2
elif worker3.discharge < worker1.discharge and worker3.discharge < worker2.discharge:
    del worker3
input()
