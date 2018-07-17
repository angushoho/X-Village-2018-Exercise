import time

class Computer:
    def boot(self):
        self.load_BIOS()
        self.load_bootloader()
        self.load_OS()
    def poweron(self):
        print('Power turned on')
    def load_BIOS(self):
        time.sleep(1)
        print('BIOS loaded')
    def load_bootloader(self):
        time.sleep(1)
        print('Bootloader loaded')
    def load_OS(self):
        time.sleep(3)
        print('OS loaded')

pc = Computer()
pc.boot()


"""
pc = Computer()
pc.poweron()
print('Power turned on')
pc.load_BIOS()
print('BIOS loaded')
pc.load_bootloader()
print('Bootloader loaded')
pc.load_OS()
print('OS loaded')
print('Boot complete')
"""