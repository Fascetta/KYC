import cv2 as cv

def find_rectangle(image_path):
    # Load the image
    image = cv.imread(image_path)

    image = cv.resize(image, (750, 750))
    
    # Convert the image to grayscale
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    # cv.imshow('Gray', gray)

    # Blur the grayscale image
    blurred = cv.bilateralFilter(gray, 10, 55, 55)
    cv.imshow('blurred', blurred)
    
    # Apply edge detection (Canny algorithm)
    edges = cv.Canny(blurred, 50, 200)
    cv.imshow('Edges', edges)

    dilated = cv.dilate(edges, (3,3), iterations=3)
    cv.imshow('dilated', dilated)
    
    # Find contours
    contours, _ = cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        epsilon = 0.1 * cv.arcLength(contour, True)
        approx = cv.approxPolyDP(contour, epsilon, True)
        
        # If the contour has four vertices, it's a rectangle
        if len(approx) == 4:
            # Draw the rectangle on the original image
            cv.drawContours(image, [approx], 0, (0, 255, 0), 2)
    
    # Display the image with the detected rectangle
    cv.imshow('Rectangle Detection', image)
    cv.waitKey(0)
    cv.destroyAllWindows()

# Replace 'path/to/your/photo.jpg' with the actual path to your photo
find_rectangle('src/test/photo.jpg')