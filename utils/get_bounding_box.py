import cv2

def get_bounding_box(image):
    def draw_rectangle(event, x, y, flags, params):
        nonlocal x_init, y_init, drawing, top_left_pt, bottom_right_pt, bbox, img

        if event == cv2.EVENT_LBUTTONDOWN:
            drawing = True
            x_init, y_init = x, y
            top_left_pt = (x_init, y_init)

        elif event == cv2.EVENT_MOUSEMOVE:
            if drawing:
                img_temp = img.copy()
                cv2.rectangle(img_temp, (x_init, y_init), (x, y), (0, 255, 0), 2)
                cv2.imshow("Bounding Box", img_temp)

        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False
            bottom_right_pt = (x, y)
            cv2.rectangle(img, (x_init, y_init), (x, y), (0, 255, 0), 2)
            cv2.imshow("Bounding Box", img)

            # Store bounding box coordinates
            bbox = (top_left_pt, bottom_right_pt)

    # Initialize variables
    drawing = False
    x_init, y_init = 0, 0
    top_left_pt, bottom_right_pt = (-1, -1), (-1, -1)
    bbox = None

    # Resize the image
    img = cv2.resize(image, (1920, 1080))

    # Create a window and set the mouse callback
    cv2.namedWindow("Bounding Box")
    cv2.setMouseCallback("Bounding Box", draw_rectangle)

    while True:
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('r'):  # Reset the bounding box
            img = cv2.resize(image, (1920, 1080))
            cv2.imshow("Bounding Box", img)
            top_left_pt, bottom_right_pt = (-1, -1), (-1, -1)
            bbox = None
        elif key == ord('s'):  # Save bounding box info
            if bbox is not None:
                print("Bounding box coordinates:", bbox)
            else:
                print("No bounding box created yet!")

    cv2.destroyAllWindows()
