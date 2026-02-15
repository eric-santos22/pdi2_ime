import cv2

img = cv2.imread("C:/Users/ericd/PDI_novo/PDI II/pdi2_ime/trabalho_1/top_mosaic_09cm_area17.tif")

B, G, R = cv2.split(img)

cv2.imshow("Canal Azul (B)", B)
cv2.imshow("Canal Verde (G)", G)
cv2.imshow("Canal Vermelho (R)", R)

cv2.waitKey(0)
cv2.destroyAllWindows()
