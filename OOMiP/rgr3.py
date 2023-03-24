class Computer:
    def __init__(
        self,
        cpu_clock_speed,
        cpu_cores_numbers,
        ram_amount,
        gpu_vram_amount,
        hdd_amount_free_space,
        os_version,
    ):
        self.cpu_clock_speed = cpu_clock_speed  # Тактовая частота ЦП
        self.cpu_cores_numbers = cpu_cores_numbers  # Количество ядер ЦП
        self.ram_amount = ram_amount  # Объём ОЗУ
        self.gpu_vram_amount = gpu_vram_amount  # Объём VRAM
        self.hdd_amount_free_space = (
            hdd_amount_free_space  # Размер свободного места на HDD
        )
        self.os_version = os_version  # Версия OS

    # Создание метода получения значения объёма ОЗУ
    def get_ram_amount(self):
        return self.ram_amount

    # Создание метода изменения значения объёма ОЗУ
    def set_ram_amount(self, newName):
        self.ram_amount = newName


# Информация о компьютерах
Computer1 = Computer(
    cpu_clock_speed="2.4 GHz",
    cpu_cores_numbers="4 cores",
    ram_amount="8 GB",
    gpu_vram_amount="2 GB",
    hdd_amount_free_space="500 GB",
    os_version="Windows 10",
)

Computer2 = Computer(
    cpu_clock_speed="4.7 GHz",
    cpu_cores_numbers="6 cores",
    ram_amount="16 GB",
    gpu_vram_amount="8 GB",
    hdd_amount_free_space="1 TB",
    os_version="Windows 10 Pro",
)

Computer3 = Computer(
    cpu_clock_speed="2.8 GHz",
    cpu_cores_numbers="6 cores",
    ram_amount="12 GB",
    gpu_vram_amount="4 GB",
    hdd_amount_free_space="2 TB",
    os_version="Windows 7",
)

# Вывод изначального объёма ОЗУ
print("\n", "Изначальный объём ОЗУ =", Computer1.get_ram_amount())

# Изменение значения через вызов метода «set_ram_amount»
Computer1.set_ram_amount("24 GB")

# Вывод итогового объёма ОЗУ
print("\n", "Итоговый объём ОЗУ =", Computer1.get_ram_amount())
