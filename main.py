from chapters.chapter_1 import start_chapter_1
from chapters.chapter_2 import start_chapter_2
from chapters.chapter_3 import start_chapter_3
from chapters.chapter_4 import start_chapter_4_quidditch

def main():
    houses = {
        "Gryffindor": 0,
        "Slytherin": 0,
        "Hufflepuff": 0,
        "Ravenclaw": 0
    }

    character = start_chapter_1()
    start_chapter_2(character)
    start_chapter_3(character, houses)
    start_chapter_4_quidditch(character, houses)

    print("")
    print("=== END ===")
    print("Final houses scores:")
    for h in houses:
        print(h + ": " + str(houses[h]) + " points")

if __name__ == "__main__":
    main()
