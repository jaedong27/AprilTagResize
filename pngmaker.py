import cv2

for i in range(10):
    input_path = "0000" + str(i) + ".png"
    output_path = "0000" + str(i) + "_.png"
    img = cv2.imread(input_path)
    img = cv2.resize(img, None, fx=80, fy=80, interpolation=cv2.INTER_NEAREST)
    cv2.imwrite(output_path,img)
