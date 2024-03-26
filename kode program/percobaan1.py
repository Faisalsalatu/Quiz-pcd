import cv2
# membaca citra digital dari komputer
citra = cv2.imread("C:/Users/hp/Desktop/Pengolahan citra digital/kode program/Quiz-pcd.jpg")

#menampilkan citra digitaL yang sudah di baca
cv2.imshow("faisal-blue", citra[:,:,0])
cv2.imshow("faisal-green", citra[:,:,1])
cv2.imshow("faisal-reed", citra[:,:,2])

#menampilkan matrix citra
print(citra)    #print semua channel warna
print(citra[:,:,0]) #print channel warna biru
print(citra[:,:,1]) #print channel warna hijau
print(citra[:,:,2]) #print channel warna merah



#menunggu sampai user menekan sembarang tombol
cv2.waitKey()