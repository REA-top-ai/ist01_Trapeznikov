def get_force(train_mass, train_acceleration):
    force = train_mass * train_acceleration
    return force

def get_energy(train_mass, c=3*10**8):
    return train_mass * c ** 2

def get_work(mass, acceleration, distance):
    force = get_force(mass, acceleration)
    return force * distance

train_force = get_force(100, 1)
print(f"Поезд GE поставляет {train_force} ньютонов силы")

bomb_mass = 1
bomb_energy = get_energy(bomb_mass)
print(f"1 кг бомбы составляет {bomb_energy} Джоулей")

train_distance = 100
train_mass = 22680
train_acceleration = 10
train_work = get_work(train_mass, train_acceleration, train_distance)
print(f"Поезд выполняет {train_work} Джоулей за {train_distance} метров")
