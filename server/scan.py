import cv2
import numpy as np

paper_width_px = 510
paper_height_px = 660

def correct_image(image):
    grayed = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #convert to grayscale
    blurred = cv2.GaussianBlur(grayed, (5, 5), 0) #blur to get rid of some noise
    ret, thresholded = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU) # automatic threshold with Otsu's method
    edged = cv2.Canny(thresholded, 75, 200) # Canny to find edges
    contours, _ = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE) # discover contours
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:5] # get 5 largest contours
    paper_contour = None
    for contour in contours:
        perimeter = cv2.arcLength(contour, True) # get length of contour
        approximated = cv2.approxPolyDP(contour, 0.02 * perimeter, True) #approximate it
        if len(approximated) == 4: #if approximated contour has 4 sides (like a piece of paper)...
            paper_contour = approximated # ...we found our contour!
            break
    #cv2.drawContours(image, [paper_contour], -1, (0, 255, 0), 2)
    pts1 = np.float32(paper_contour) # conversion for getPerspectiveTransform()
    pts2 = np.float32([[0, 0], [0, paper_height_px], [paper_width_px, paper_height_px], [paper_width_px, 0]]) # must be in order of top left, bottom left, bottom right, top right
    transformation_matrix = cv2.getPerspectiveTransform(pts1, pts2) # get matrix for transformation
    warped = cv2.warpPerspective(image, transformation_matrix, (paper_width_px, paper_height_px)) # do the transformation
    return warped

# just a little thing for testing. now you can run python scan.py <IMAGE>
if __name__ == '__main__':
    import sys
    img = cv2.imread(sys.argv[1])
    img = correct_image(img)
    cv2.imshow('test', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
