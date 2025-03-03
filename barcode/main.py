import cv2
from pyzbar import pyzbar

image = cv2.imread('bar.jpeg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

barcodes = pyzbar.decode(gray)

for barcode in barcodes:
    (x, y, w, h) = barcode.rect
    cv2.rectangle(image, (x,y), (x+w, y+h), (0, 255, 0), 2)

    barcode_data = barcode.data.decode('utf-8')
    barcode_type = barcode.type

    text = f'{barcode_type}: {barcode_data}'

    cv2.putText(image, text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    print(f'Found: {barcode_type} barcode: {barcode_data}')

#cv2.imshow('barcode results', image)
cv2.imwrite('results.jpg', image)
#cv2.waitKey(0)