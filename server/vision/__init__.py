import cv2

def get_fullness_percent(img):
    grayed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert to grayscale
    _, thresholded = cv2.threshold(grayed, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU) # automatic threshold with Otsu's method
    image_width = thresholded.shape[0]
    image_height = thresholded.shape[1]

    white_count = 0
    black_count = 0

    for x in xrange(image_width):
        for y in xrange(image_height):
            pixel = thresholded[x, y]
            if pixel == 0:
                black_count += 1
            elif pixel == 255:
                white_count += 1
            else:
                raise Exception("Didn't get grayscale image. Hmm...")

    return float(white_count) / (black_count + white_count)
