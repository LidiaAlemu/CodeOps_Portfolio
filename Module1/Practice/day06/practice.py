# 1. Spot the SRP violation – split Report class

print("1. SRP  splitting a Report class")

class ReportBuilder:
    
    def build(self, data):
        return f"Report: {data}"

class ReportSaver:
    
    def save(self, content, filename):
        with open(filename, "w") as f:
            f.write(content)
        print(f"Saved report to {filename}")

class ReportMailer:
    
    def send(self, content, email):
        print(f"Sent '{content}' to {email}")


builder = ReportBuilder()
saver = ReportSaver()
mailer = ReportMailer()

content = builder.build("Daily totals")
saver.save(content, "report.txt")
mailer.send(content, "almaz@example.com")
print("-" * 30)



# 2. Refactor to OCP – shape area without if/elif

print("2. OCP  shapes via polymorphism")

class Shape:
    def area(self):
        raise NotImplementedError

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height


shapes = [Circle(5), Square(4), Triangle(3, 6)]
for s in shapes:
    print(f"{s.__class__.__name__} area: {s.area()}")
print("-" * 30)



# 3. Write a Singleton – AppSettings

print("3. Singleton  AppSettings")

class AppSettings:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.currency = "ETB"
            cls._instance.bank_name = "Addis Bank"
        return cls._instance

a = AppSettings()
b = AppSettings()
print(f"Same instance? {a is b}")          
print(f"Currency: {a.currency}")
print("-" * 30)



# 4. Write a Factory – ShapeFactory

print("4. Factory  ShapeFactory")

class ShapeFactory:
    @staticmethod
    def create(kind, *args):
        if kind == "circle":
            return Circle(*args)
        if kind == "square":
            return Square(*args)
        if kind == "triangle":
            return Triangle(*args)
        raise ValueError(f"Unknown shape: {kind}")

c = ShapeFactory.create("circle", 3)
s = ShapeFactory.create("square", 5)
t = ShapeFactory.create("triangle", 4, 7)
print(f"Circle area: {c.area()}")
print(f"Square area: {s.area()}")
print(f"Triangle area: {t.area()}")
print("-" * 30)



# 5. Write an Observer pair – NewsAgency and Subscribers

print("5. Observer  NewsAgency")

class NewsAgency:
    def __init__(self):
        self._observers = []

    def subscribe(self, observer):
        self._observers.append(observer)

    def _notify(self, news):
        for obs in self._observers:
            obs.update(news)

    def publish(self, news):
        print(f"NewsAgency: publishing '{news}'")
        self._notify(news)

class TVStation:
    def update(self, news):
        print(f"[TV] Breaking news: {news}")

class RadioStation:
    def update(self, news):
        print(f"[Radio] Tune in: {news}")

agency = NewsAgency()
agency.subscribe(TVStation())
agency.subscribe(RadioStation())
agency.publish("Ethiopia launches new satellite")