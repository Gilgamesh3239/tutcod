import requests
import os
import uuid

async def get_cat():
    uri = "https://cataas.com/cat/gif"
    response = requests.get(uri)
    path = str(uuid.uuid4())
    if response.status_code == 200:
        with open("media/test.gif","wb") as f:
            f.write(response.content)
        return f"media/test.gif"
    else:
        return None
    

def delete_cat(file_path):
    print("DELETEING FILE :")
    if os.path.exists(file_path):
        os.remove(file_path)
        print("DELETED")

if __name__ == "__main__":
    # cat_gif = get_cat()
    # if cat_gif:
    #     print(f"Cat gif saved to {cat_gif}")
    # else:
        # print("Failed to fetch cat gif")
    print("Testing")