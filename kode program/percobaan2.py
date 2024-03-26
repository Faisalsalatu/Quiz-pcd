import cv2
import numpy as np

# membaca citra digital dari komputer
citra = cv2.imread("C:/Users/hp/Desktop/Pengolahan citra digital/kode program/Quiz-pcd.jpg")

#membaca channel warna dan menyimpanya ke dalam variabel terpisah
b = citra[:,:,0]
g = citra[:,:,1]
r = citra[:,:,2]

#menyimpan jumlah baris dan kolom dari citra
jum_baris = len(citra)
jum_kolom = len(citra[0])

#menyiapkan citra baru dengan nilai 0
citra_gray = np.zeros((jum_baris, jum_kolom))

#menghitung nilai pixel grayscale
for i in range(jum_baris):
    for j in range(jum_kolom):
        citra_gray[i, j] = round(0.299 * r[i,j] + 0.587 * g[i,j] + 0.114 * b[i,j])

citra_gray = citra_gray.astype(np.uint8)

cv2.imshow("faisal gray", citra_gray)
print(citra_gray)

cv2.waitKey()