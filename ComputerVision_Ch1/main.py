import cv2
from PIL import Image

# =========================
# 1. Đọc ảnh
# =========================
img = cv2.imread("shark.jpg")

# =========================
# 2. Hiển thị ảnh gốc
# =========================
cv2.imshow("Shark", img)

# =========================
# 3. Lưu ảnh sang định dạng khác
# =========================
cv2.imwrite("shark.png", img)

# =========================
# 4. Chuyển sang Grayscale
# =========================
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale", gray)
cv2.imwrite("shark_gray.jpg", gray)

# =========================
# 5. Chuyển sang HSV
# =========================
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)
cv2.imwrite("shark_hsv.jpg", hsv)

# =========================
# 6. Chuyển sang LAB
# =========================
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow("LAB", lab)
cv2.imwrite("shark_lab.jpg", lab)

# 7. Cắt một vùng ảnh
crop = img[50:300, 100:500]
cv2.imshow("Crop", crop)
cv2.imwrite("shark_crop.jpg", crop)

# 8. Thay đổi kích thước ảnh
resize = cv2.resize(img, (800, 500))

cv2.imshow("Resize", resize)
cv2.imwrite("shark_resize.jpg", resize)

# 9. Vẽ hình cơ bản
drawing = img.copy()

# Vẽ đường thẳng
cv2.line(drawing, (50, 50), (500, 50), (255, 0, 0), 3)

# Vẽ hình tròn
cv2.circle(drawing, (350, 180), 50, (0, 255, 0), 3)

# Vẽ hình chữ nhật
cv2.rectangle(drawing, (100, 100), (500, 300), (0, 0, 255), 3)

# Thêm văn bản
cv2.putText(
    drawing,
    "SHARK",
    (100, 330),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (255, 255, 255),
    2
)

# Hiển thị ảnh đã vẽ
cv2.imshow("Drawing", drawing)

# Lưu ảnh
cv2.imwrite("shark_drawing.jpg", drawing)

# Chờ người dùng bấm phím
cv2.waitKey(0)
cv2.destroyAllWindows()