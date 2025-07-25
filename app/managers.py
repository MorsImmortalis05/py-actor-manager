import sqlite3

from app.models import Actor


class ActorManager:

    def __init__(
            self, db_name: str = "actor_manager_db",
            table_name: str = "actors"
    ) -> None:
        self._connection = sqlite3.connect("actor_manager")
        self.db_name = db_name
        self.table_name = table_name

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} "
            f"(first_name, last_name) VALUES (?)",
            (first_name, last_name,)
        )

    def all(self) -> list[Actor]:
        actor_manager_cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        return [
            Actor(*row) for row in actor_manager_cursor
        ]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            "SET new_first_name, new_last_name = (?, ?) "
            "WHERE pk = ?",
            (new_first_name, new_last_name, pk)
        )
        self._connection.commit()

    def __delete__(self, pk: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} WHERE pk = ?",
            (pk, )
        )
        self._connection.commit()
