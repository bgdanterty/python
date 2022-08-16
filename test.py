import requests

KEY = "9c489a1eb0a7c7331a42250f3389b23d"
TOKEN = "547ed417ff1c9df76fe53863105461b7be34a6f77f1048552ee341035defb4a2"


class GreenBoard:

    def __init__(self):
        self.ID_BOARD = "560157093dfb3d7e3ca00d4a"
        self.ID_LIST_WAITING = "571e42c12fac2b9f94f30b65"
        self.ID_LIST_NO_REPLY = "5a5dbb12d73bb5c6421e4241"
        self.ID_LIST_UNPROCESSED = "565432005e7e3f7ebcc4a09d"
        self.ID_LABEL_HARDWARE = "5d9dcd4108d6e38919498203"
        self.params = {
            "key": KEY,
            "token": TOKEN
        }

    def move_list_of_cards(self, list_from, list_to):
        # from
        url = f"https://api.trello.com/1/lists/{list_from}/moveAllCards"
        # to
        self.params["idBoard"] = self.ID_BOARD
        self.params["idList"] = list_to
        # request
        return requests.post(url, params=self.params).json()

    def collect_cards_from_list(self, list_from):
        # cards in waiting
        url = f"https://api.trello.com/1/lists/{list_from}/cards"
        # request
        return requests.get(url, params=self.params).json()

    def move_card_from_list_to_list(self, card_id, list_to):
        # from
        url = f"https://api.trello.com/1/cards/{card_id}"
        # to
        self.params["idList"] = list_to
        # request
        return requests.put(url, params=self.params).json()
