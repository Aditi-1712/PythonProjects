import cv2

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");

img = cv2.imread("news.jpg");     #keeping the image in it's original state
grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY);


faces = faceCascade.detectMultiScale(grayImg,
scaleFactor = 1.05,
minNeighbors = 5);

for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0),3);


print(type(faces));
print(faces);

resizedImg = cv2.resize(img,(int(img.shape[1]/3), int(img.shape[0]/3)));
cv2.imshow("Gray",resizedImg);
cv2.waitKey(0);
cv2.destroyAllWindows();
