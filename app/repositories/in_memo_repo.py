from uuid import UUID, uuid4

NOT_FOUND_MESSAGE = {"message": "Not found"}


class InMemoryRepository:
    items: list[dict] = []

    def __repr__(self) -> None:
        return self.items

    @classmethod
    def __set_bigint(cls):
        big_int = 0
        for item in cls.items:
            if item["_id"] > big_int:
                big_int = item["_id"]
        return big_int + 1

    @classmethod
    def __set_uuid(cls):
        return uuid4()

    def create(self, item: dict, pk_type: str | None):
        item["_id"] = self.__set_uuid() if pk_type == "uuid" else self.__set_bigint()
        self.items.append(item)

    def find(self, **kwargs):
        if kwargs:
            return self.find_by(**kwargs)
        else:
            return self.items

    def find_by(self, **kwargs):
        memory_match: list = [value for value in self.items]
        for key in kwargs.keys():

            memory_match = [
                value for value in memory_match if value[key] == UUID(kwargs[key])
            ]
        return memory_match if len(memory_match) > 0 else NOT_FOUND_MESSAGE

    def find_one_by(self, **kwargs):
        data_retrieved = self.find_by(**kwargs)
        if type(data_retrieved) == list:
            return data_retrieved[0]
        else:
            return data_retrieved

    def update(self, id: int | str, updates: dict):
        for user in self.items:
            if user["_id"] == (UUID(id) if type(id) == str else int(id)):
                user.update(updates)
                return user
        return NOT_FOUND_MESSAGE, 404

    def delete(self, id: int | str):
        for user in self.items:
            if user["_id"] == (UUID(id) if type(id) == str else int(id)):
                self.items.remove(user)
                return ""
        return NOT_FOUND_MESSAGE, 404
