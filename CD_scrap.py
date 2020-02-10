import requests
import csv
from bs4 import BeautifulSoup

url = input("Enter reviews url from College Dunia: ")
pg = int(input("Number of pages: "))
for p in range(1, pg+1):
    url_p = url + str(p)
    res = requests.get(url_p)
    soup = BeautifulSoup(res.text, 'html.parser')
    eles_reviews = soup.find_all(class_='content_data avatar-container')
    for i in range(len(eles_reviews)):
        ele_review_content = eles_reviews[i].findChild(class_='review_content')
        review_blocks = ele_review_content.findChildren('p')
        for j in range(len(review_blocks)):
            review_block = review_blocks[j].text
            if(review_block.find('hostel')>-1):
                review = str(review_blocks[j].text).replace('\n', ' ').replace('\r', '')
                rating = str(eles_reviews[i].findChild(class_='author_details').findChild(class_='right').findChild(class_='rating').text).strip()
                #write in csv
                with open(r'D:\college_scrap\writeData.csv', mode='a') as file:
                    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow([review, rating])
                print(url_p)
print("Done.")