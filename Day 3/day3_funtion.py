def greeting():
    print("Hi")
greeting()

def greeting(name, city):
    print("Hi " + name + " How is your city " + city)
greeting("Nilkanth","Pune")

def greeting(name, city):
    print("Hi " + name + " How is your city " + city)
greeting(city = "Pune", name = "Nilkanth")

greeting("Pune" , city = "abc")

def greeting(city = "Pune", name = "Nilkanth"):
    print("Hi " + name + " How is your city " + city)
greeting()

def greeting(country, city = "Pune", name = "Nilkanth"):
    print("Hi " + name + " How is your city " + city)
greeting("India")
