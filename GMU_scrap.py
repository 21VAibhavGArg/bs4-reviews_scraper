import requests
import csv
import json
url = "https://www.getmyuni.com/review/get_category_review"
data = {
    "college_id": 141, #141 is for vit vellore
    "category": 6 #6 is for hostel
}
res = json.loads(str(requests.post(url, data).text))
for i in range(len(res['reviews'])):
    review = str(res['reviews'][i]['review']).replace("/li", "").replace("/ul", "").replace("&lt;li&gt;", "")
    rating = str(res['reviews'][i]['ra3'])
    with open(r'D:\college_scrap\writeData.csv', mode='a') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([review, rating])