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

print("������ ����� ����:")
town.name = input()

print("������ ����� �����:")
town.country = input()

print("������ ����� ������:")
town.region = input()

print("������ ������� ���������:")
town.population = int(input())

print("������ ����� �����:")
town.year_income = float(input())

print("������ �����:")
town.square = float(input())

print("�� ����? (true/false):")
town.has_port = input().lower() == "true"

print("�� ��������? (true/false):")
town.has_airport = input().lower() == "true"

year_income_per_inhabitant = town.get_year_income_per_inhabitant()

print("\n���������� ��� ����:")
print(f"����� ����: {town.name}")
print(f"����� �����: {town.country}")
print(f"����� ������: {town.region}")
print(f"���������: {town.population}")
print(f"г���� �����: {town.year_income}")
print(f"�����: {town.square}")
print(f"�� ����: {town.has_port}")
print(f"�� ��������: {town.has_airport}")
print(f"г���� ����� �� ������ ��������: {year_income_per_inhabitant:.2f}")

