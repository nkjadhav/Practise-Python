def greeting():
    print("Hi")
greeting()

def greeting(name, city):
    print("Hi " + name + " How is your city " + city)
greeting("Jay","Pune")

def greeting(name, city):
    print("Hi " + name + " How is your city " + city)
greeting(city = "Pune", name = "Jay")

greeting("Pune" , city = "abc")

def greeting(city = "Pune", name = "Jay"):
    print("Hi " + name + " How is your city " + city)
greeting()

def greeting(country, city = "Pune", name = "Jay"):
    print("Hi " + name + " How is your city " + city)
greeting("India")
