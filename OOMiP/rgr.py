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

    # Создание метода для вывода всей информации о компьютере
    def conclusion(self):
        print(
            "\n",
            "Тактовая частота ЦП =",
            self.cpu_clock_speed,
            "\n",
            "Количество ядер ЦП =",
            self.cpu_cores_numbers,
            "\n",
            "Объём ОЗУ =",
            self.ram_amount,
            "\n",
            "Объём VRAM =",
            self.gpu_vram_amount,
            "\n",
            "Размер свободного места на HDD =",
            self.hdd_amount_free_space,
            "\n",
            "Версия OS =",
            self.os_version,
        )


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

# Вывод всей информации о всех компьютерах

Computer1.conclusion()
Computer2.conclusion()
Computer3.conclusion()
