#!/usr/bin/env python
# coding: utf-8

# # ISM 647 Assignment 2: 
# ## Cognitive Computing and Artificial Intelligence Application Development and Tutorial
# 
# ### Group Members: Yanan Liu, Indu Thiyagarajan, Shivani Goverdhan, and Vijayalakshmi E. C. Gari
# 
# This application shows you how to use the cognitive services [Face API](https://azure.microsoft.com/services/cognitive-services/face/) from Microsoft Azure to detect faces in an image. The API also returns various attributes such as the gender and age of each person. The sample images used in this application are from the [How-Old Robot](http://www.how-old.net) that uses the same APIs.
# 
# ### How to run this application
# A valid subscription key and endpoint url (achieved by our group member) are provided in this application. So no prerequisites is needed to run this application. You can try with the default image url or use your own image url.
# 
# To run this application step by step, click the "Run" button above in each cell with proper input(i.e., image url).
# 
# To run this whole application, click "Restart & Run All" under the kernel option above.
# 
# To clear the output and restart the application, click "Restart & Clear Output" under the kernel option above.

# #### Step 1: assert valid subscription key and endpoint url;

# In[ ]:


subscription_key = '6851331e1f814eccae1f4b0c2fff7406'
assert subscription_key

face_api_url = 'https://eastus.api.cognitive.microsoft.com/face/v1.0/detect'


# #### Step 2: Import python library for functions will be used in this application and initialize parameters;

# In[ ]:


import requests
from IPython.display import HTML

import matplotlib.pyplot as plt
from matplotlib import patches
from PIL import Image
from io import BytesIO

headers = { 'Ocp-Apim-Subscription-Key': subscription_key }
    
params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
}


# #### Step 3: Define face detection function using the Face API in Microsoft Azure;

# In[ ]:


def face_detection(image_url):
    response = requests.post(face_api_url, params=params, headers=headers, json={"url": image_url})
    faces = response.json()

    image_file = BytesIO(requests.get(image_url).content)
    image = Image.open(image_file)

    plt.figure(figsize=(8,8))
    ax = plt.imshow(image, alpha=0.6)
    for face in faces:
        fr = face["faceRectangle"]
        fa = face["faceAttributes"]
        origin = (fr["left"], fr["top"])
        p = patches.Rectangle(origin, fr["width"],                               fr["height"], fill=False, linewidth=2, color='b')
        ax.axes.add_patch(p)
        plt.text(origin[0], origin[1], "%s, %d"%(fa["gender"].capitalize(), fa["age"]),                  fontsize=12, weight="bold", color='r', va="bottom")
    plt.axis("off")
    return(HTML("<font size=5>Detected <font color='blue'>%d</font> faces in this image</font>"%len(faces)))


# #### Step 4: Have fun with the images you provided! (Simply replace the url with the image url you want to test) :)

# In[ ]:


face_detection("https://how-old.net/Images/faces2/main006.jpg")

