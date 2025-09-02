import requests
import json
from bs4 import BeautifulSoup

url = "https://ind.nl/en/public-register-recognised-sponsors/public-register-regular-labour-and-highly-skilled-migrants"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

table = soup.find("table")

table_data = {}
for row in table.find_all("tr"):
    first_cell = row.find("th")
    if first_cell:
        cell_text = first_cell.get_text().replace(" B.V.", "").strip().lower()
        print(cell_text)
        if cell_text:
            first_letter = cell_text[0]
            if first_letter not in table_data:
                table_data[first_letter] = []
            table_data[first_letter].append(cell_text)

print(table_data)

try:
    with open("data.js", "w") as f:
        data = json.dumps( table_data )
        f.write("const data = " + data)
except Exception as e:
    print("cannot write to file data.json")
    print(e)
