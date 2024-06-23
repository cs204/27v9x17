def main():
    v = feet2meter(input("Сколько футов:"))
    print(f"Это будет {v:.2f} метров.")

def feet2meter(v):
    meters = v * 0.3048
    return meters
s = (input("Введите количество футов:"))
s = s.replace('ft','')
v = float (s)
meters = feet2meter(v)
print(f"Это будет {meters:.2f} метров")
