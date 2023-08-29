import random

from ultralytics import YOLO
ptfile = "TR-Coin-OD-v2.pt"
model = YOLO(ptfile)
results = model.predict(source="test_image3.png", save=True, show=True)
result = results[0]
box = result.boxes[0]
debug = False
lowConf = False

sum = 0
for box in result.boxes:
  objectList = []
  class_id = result.names[box.cls[0].item()]
  cords = box.xyxy[0].tolist()
  cords = [round(x) for x in cords]
  conf = round(box.conf[0].item(), 2)
  if debug:
    print("[DEBUG] Object type:", class_id)
    print("[DEBUG] Coordinates:", cords)
    print("[DEBUG] Probability:", conf)

  else:
    pass

  if lowConf:
    if conf > 0.51:
      sum += int(class_id)
    else:
      continue
  else:
    if conf > 0.80:
      sum += int(class_id)
    else:
      if debug:
        print("[DEBUG] Low confidence, skipping...")
      else:
        pass
  print("---")



print("Result:")
sumPrice = sum/100
sumPriceSplit = str(sumPrice).split('.')
if len(sumPriceSplit[1]) == 1:
  print(f"{sumPriceSplit[0]} lira, {sumPriceSplit[1]}0 kuruş.")
else:
  print(f"{sumPriceSplit[0]} lira, {sumPriceSplit[1]} kuruş.")
if random.randint(0,3) == 1:
  print("TIP: You can use the debug mode by setting debug to True.")
if debug:
  if ptfile == "TR-Coin-OD-v1.pt":
    print("[DEBUG] Using outdated model, please update to v2 for better results.")
  elif ptfile == "TR-Coin-OD-v2.pt":
    print("[DEBUG] Using latest model, v2.")
    if not lowConf:
        print("[DEBUG] Using high confidence mode. Note that this may cause 5 or 10 kuruş coins to be ignored.")
