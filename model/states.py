from dataclasses import dataclass

@dataclass
class State:
    id: int
    Name: str
    Capital: str
    Lat: float
    Lng: float
    Area: int
    Population: int
    Neighbors: list

    def __str__(self):
        return f"{self.Name}"

    def __hash__(self):
        return hash(self.id)