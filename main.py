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

    index = 0
    for img_item in img:
        request = requests.get(img_item['url'], stream = True)
        index += 1
        if request.status_code == 200:
            request.raw.decode_content = True
            
            with open(f"download_{index}.png", 'wb') as file:
                shutil.copyfileobj(request.raw, file)
                
            print('Image downloaded to: ', f"download_{index}.png")
        else:
            print('Error!')

if __name__ == "__main__":
    main()