from AnimalShelter import AnimalShelter

a = AnimalShelter()
animal_data = [
    {
        "name":"test456",
        "type":"dogTest123123"
    },
    {
        "name":"test2",
        "type":"cat123"
    },
    {
        "name":"test4564566",
        "type":"dogTest123123"
    }
]

for i in animal_data:
    a.create(i)

dogs = a.read( {"type":"dogTest123123"}  )
for dog in dogs:
    print(dog)