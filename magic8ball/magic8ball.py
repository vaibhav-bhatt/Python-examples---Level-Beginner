import json
import random
from tqdm import tqdm
from time import sleep

with open('responses.json') as json_file:
    data = json.load(json_file)


def generate_answer():
    input("Please ask your question !\n")
    answer = data[random.randint(0, len(data) - 1)]
    for i in tqdm(range(0, 100), desc="Thinking"):
        sleep(0.01)
    print(answer)


user_decision = True

while user_decision:
    generate_answer()
    decision = input("Do you want to continue - Press Y/N \n")
    if decision == "N" or decision == "n":
        user_decision = False
