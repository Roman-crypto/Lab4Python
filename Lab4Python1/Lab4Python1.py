class Town:
    def __init__(self):
        self.name = ""
        self.country = ""
        self.region = ""
        self.population = 0
        self.year_income = 0.0
        self.square = 0.0
        self.has_port = False
        self.has_airport = False

    def get_year_income_per_inhabitant(self):
        return self.year_income / self.population

town = Town()

print("Введіть назву міста:")
town.name = input()

print("Введіть назву країни:")
town.country = input()

print("Введіть назву регіону:")
town.region = input()

print("Введіть кількість населення:")
town.population = int(input())

print("Введіть річний дохід:")
town.year_income = float(input())

print("Введіть площу:")
town.square = float(input())

print("Має порт? (true/false):")
town.has_port = input().lower() == "true"

print("Має аеропорт? (true/false):")
town.has_airport = input().lower() == "true"

year_income_per_inhabitant = town.get_year_income_per_inhabitant()

print("\nІнформація про місто:")
print(f"Назва міста: {town.name}")
print(f"Назва країни: {town.country}")
print(f"Назва регіону: {town.region}")
print(f"Населення: {town.population}")
print(f"Річний дохід: {town.year_income}")
print(f"Площа: {town.square}")
print(f"Має порт: {town.has_port}")
print(f"Має аеропорт: {town.has_airport}")
print(f"Річний дохід на одного мешканця: {year_income_per_inhabitant:.2f}")

