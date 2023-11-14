import cv2

t1 = cv2.getTickCount() # Запуск таймера времени работы программы

# Загрузка изображения из корневой папки исполняемого файла
upload_1024 = "peepohappy 1024 768.jpg"
upload_1280 = "peepohappy 1280 960.jpg"
upload_2048 = "peepohappy 2048 1536.jpg"

upload = upload_1024 # Поменять переменную для выбора разрешения

image_original         = cv2.imread(upload)
image_inverse          = cv2.imread(upload)
image_inverse_contrast = cv2.imread(upload)

# Делаем обратную фазу изображения
def inverse_phase(image):
    height, width, channels = image.shape

    for row in range(height):
        for list in range(width):
            for c in range(channels):
                pv = image[row, list, c]
                image[row, list, c] = 255 - pv # Вычитаем исходные RGB-значения из 255
    cv2.imshow("Inverse", image)               # Выводим отредактированное изображение в окне

inverse_phase(image_inverse)

image_inverse_contrast = image_inverse.copy()

# Накидываем контраста на отредактированное изображение
cv2.addWeighted(image_inverse_contrast, 2, image_inverse_contrast, 0, 0, image_inverse_contrast)

cv2.imshow("Contrasted inverse", image_inverse_contrast)    # Выводим контрастное изображение в окне   
cv2.imshow('Original', image_original)                      # Выводим оригинальное изображение в окне

match upload: # Сохранение изображений в зависимости от выбора разрешения
    case "peepohappy 1024 768.jpg":

        cv2.imwrite("1024x768 original.png", image_original)
        cv2.imwrite("1024x768 inverse.png", image_inverse)
        cv2.imwrite("1024x768 inverse_contrast.png", image_inverse_contrast)

        t2 = cv2.getTickCount() # Стоп таймер
        print("Время обработки изображений разрешением 1024x768: ", (t2-t1)/cv2.getTickFrequency(), " секунд.") # Вывод времени обработки в консоль

    case "peepohappy 1280 960.jpg":

        cv2.imwrite("1280x960 original.png", image_original)
        cv2.imwrite("1280x960 inverse.png", image_inverse)
        cv2.imwrite("1280x960 inverse_contrast.png", image_inverse_contrast)

        t2 = cv2.getTickCount() # Стоп таймер
        print("Время обработки изображений разрешением 1280x960: ", (t2-t1)/cv2.getTickFrequency(), " секунд.") # Вывод времени обработки в консоль

    case "peepohappy 2048 1536.jpg":

        cv2.imwrite("2048x1536 original.png", image_original)
        cv2.imwrite("2048x1536 inverse.png", image_inverse)
        cv2.imwrite("2048x1536 inverse_contrast.png", image_inverse_contrast)
        
        t2 = cv2.getTickCount() # Стоп таймер
        print("Время обработки изображений разрешением 2048х1536: ", (t2-t1)/cv2.getTickFrequency(), " секунд.") # Вывод времени обработки в консоль

cv2.waitKey()
