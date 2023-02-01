import datetime


def beker():
    print("I/A:")
    auto = str(input("\tAutó neve: "))
    datum = int(input("\tGyártási dátum: "))
    print("\nI/B:")
    if datum == datetime.datetime.today().year:
        print(f"\tEz a(z) {auto} friss gyártás.")
    elif datum < 2000:
        print(f"\tEz a(z) {auto} öreg autó.")
    else:
        print(f"\tEz a(z) {auto} átlagos korú.")
