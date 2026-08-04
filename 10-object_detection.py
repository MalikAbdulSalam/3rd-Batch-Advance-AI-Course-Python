from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model("C:/Users/PC/Desktop/1.jpg")

results[0].show()      # Display image
results[0].save("output.jpg")