class Country:
    def __init__(self):
        self.name = ""
        self.capital = ""
        self.population = 0
        self.area = 0.0
        self.language = ""
        self.is_un_member = False
        self.development_level = ""

    def get_population_density(self):
        return self.population / self.area

country = Country()

print("Введіть назву країни:")
country.name = input()

print("Введіть столицю:")
country.capital = input()

print("Введіть кількість населення:")
country.population = int(input())

print("Введіть площу (в квадратних кілометрах):")
country.area = float(input())

print("Введіть мову:")
country.language = input()

print("Чи є країна членом ООН? (true/false):")
country.is_un_member = input().lower() == "true"

print("Введіть рівень розвитку (низький/середній/високий):")
country.development_level = input()

population_density = country.get_population_density()

print("\nІнформація про країну:")
print(f"Назва країни: {country.name}")
print(f"Столиця: {country.capital}")
print(f"Населення: {country.population} осіб")
print(f"Площа: {country.area} км²")
print(f"Мова: {country.language}")
print(f"Член ООН: {country.is_un_member}")
print(f"Рівень розвитку: {country.development_level}")
print(f"Густота населення: {population_density:.0f} осіб/км²")

