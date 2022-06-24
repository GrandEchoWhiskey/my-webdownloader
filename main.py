import requests
import shutil
import sys

def main():

    img = []
    for img_url in input("Addresses: ").split(';'):
        filename = img_url.split("/")[-1]
        img.append({
            "name": filename,
            "url": img_url
        })

    for img_item in img:
        request = requests.get(img_item['url'], stream = True)

        if request.status_code == 200:
            request.raw.decode_content = True
            
            with open(img_item['name'], 'wb') as file:
                shutil.copyfileobj(request.raw, file)
                
            print('Image downloaded to: ', img_item['name'])
        else:
            print('Error!')

if __name__ == "__main__":
    main()