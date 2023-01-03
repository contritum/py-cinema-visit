from __future__ import annotations
from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
            self,
            movie_name: str,
            customers: list,
            cleaning_staff: Cleaner
    ) -> None:
        print(f'"{movie_name}" started in hall number {self.number}.')
        for i in range(len(customers)):
            customers[i].watch_movie(movie=movie_name)
        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(hall_number=self.number)