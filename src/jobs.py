import csv

from functools import lru_cache


@lru_cache
def read(path):
    with open(path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


if __name__ == "__main__":
    dados = read("src/jobs.csv")
    print(dados[:2])
