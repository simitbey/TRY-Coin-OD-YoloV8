from ultralytics import YOLO

model = YOLO("TR-Coin-OD-v1.pt")
results = model.predict(source="input_image.jpg", save=True, show=True)
result = results[0]
box = result.boxes[0]

sum = 0
for box in result.boxes:
  objectList = []
  class_id = result.names[box.cls[0].item()]
  cords = box.xyxy[0].tolist()
  cords = [round(x) for x in cords]
  conf = round(box.conf[0].item(), 2)
  print("Object type:", class_id)
  print("Coordinates:", cords)
  print("Probability:", conf)
  print("---")
  if conf > 0.51:
      sum += int(class_id)
  else:
    continue
print(sum)

sumPrice = sum/100
sumPriceSplit = str(sumPrice).split('.')
if len(sumPriceSplit[1]) == 1:
  print(f"{sumPriceSplit[0]} lira, {sumPriceSplit[1]}0 kuruş.")
else:
  print(f"{sumPriceSplit[0]} lira, {sumPriceSplit[1]} kuruş.")
