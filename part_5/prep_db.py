import sqlite3
from random import random
from math import floor

# Sample origins
origins = [
    "Sweden", "Spain", "United Kingdom", "USA", "Canada",
    "Brazil", "France", "Portugal", "Germany", "Finland",
    "Norway", "Italy", "Estonia", "Switzerland",
    "Poland", "Lithuania", "Netherlands", "Belgium",
    "China", "Vietnam", "Thailand", "Malaysia"
]

# Connect to database
cx = sqlite3.connect("metadata.db")
cu = cx.cursor()

# create a table
cu.execute("CREATE TABLE metadata(sample_name, input_dna, origin)")

# insert values into a table
for idx in range(1, 48):
    cu.execute(
        "INSERT INTO metadata VALUES (?, ?, ?)",
        (
            f"SAMPLE_{idx:02d}",
            floor(random()*300),
            origins[floor(random()*len(origins))]
        )
    )

# execute a query and iterate over the result
for row in cu.execute("SELECT * FROM metadata"):
    print(row)

cx.commit()
cx.close()
