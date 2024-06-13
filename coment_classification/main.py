from requests import get
import csv

filename = 'data.csv'
fields = ['body', 'rating']
rows = []

with open(filename, newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    rows = list(reader)
    
while True:
    inp = input("> Command/ID: ")
    if (inp == "exit"):
        break
    else:
        for i in range(400, 440):
            print(str(i) + " " + f"https://api.digikala.com/v1/search/?q=laptop&page={i}")
            
            products = get(f'https://api.digikala.com/v1/search/?q=laptop&page={i}').json()['data']['products']
            for product in products:
                try:
                    productId = product['id']
                    data = get(f'https://api.digikala.com/v1/product/{productId}/comments/').json()
                    commentList = data['data']['comments']
                    for comment in commentList:
                        if (comment['rate'] <= 3):
                            rows.append([comment['body'].replace("\n", ""), comment['rate']])
                except:
                    continue
                
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            file = csv.writer(file)
            # file.writerow(fields)
            file.writerows(rows)
        
        break
                
