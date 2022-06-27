import requests
import time

KEY = "2b0235409da09869e9e56dcaed994c07"
TOKEN = "b96b972e380a001e23012ccc3e94139b2aa51865c1d5a02d360c9a93dab06921"
BOARD_ID = "62b03d05f08023558b3f8796"
LIST_ID = "62b03d16c479312e6e211b59"
LABEL_ID = "62b03d05f08023558b3f87db"
ENDPOINT = f"https://api.trello.com/1/boards/{BOARD_ID}"

params = {
    "key": KEY,
    "token": TOKEN
}
response = requests.get(ENDPOINT, params=params).json()
print(response)


def get_cards_id_qa():
    list_endpoint = f"https://api.trello.com/1/lists/{LIST_ID}/cards"
    data = requests.get(list_endpoint, params=params)
    return data


while True:
    time.sleep(3)
    cards_id = get_cards_id_qa().json()
    print(cards_id)
    if len(cards_id) > 0:
        for card in cards_id:
            card_id = card["id"]
            print(card_id)
