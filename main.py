import cv2

haarcascade = "cars.xml"
video = "car1.mp4"

car_video = cv2.VideoCapture(video)

carcascade = cv2.CascadeClassifier(haarcascade)

while True:
    status,frame = car_video.read()
    grey_car = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cars = carcascade.detectMultiScale(grey_car)

    for(x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y), (x+w,y+h), (255,0,0), 3)


    cv2.imshow("car detection", frame)
    if cv2.waitKey(10) == 27:
        break