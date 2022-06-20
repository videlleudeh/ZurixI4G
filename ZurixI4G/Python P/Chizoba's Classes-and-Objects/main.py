class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name: str, age: int, tracks: list, score: float):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name(self, name: str):
        self.name = name
        print (f"Hi my name is {name}.")

    def change_age(self, age: int):
        self.age = age
        print (f"I am {age} years old.")

    def add_track(self, track: list):
        self.tracks.append(track)
        print (f"I am enrolled in the {track} program at Zuri Training.")

    def get_score(self):
        print (f"My score is {self.score}.")


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("FullStack")
Bob.get_score()

print (Bob)