import cv2

def get_bounding_box(image,resize_parameter):
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
                cv2.imshow("Bounding Box *** INSTRUCTIONS : [-q to Quit, -r to ReDraw, -a to AddBoxes, -s to Save] ***", img_temp)

        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False
            bottom_right_pt = (x, y)
            cv2.rectangle(img, (x_init, y_init), (x, y), (0, 255, 0), 2)
            cv2.imshow("Bounding Box *** INSTRUCTIONS : [-q to Quit, -r to ReDraw, -a to AddBoxes, -s to Save] ***", img)

            # Store bounding box coordinates
            bbox = (top_left_pt, bottom_right_pt)

    # Initialize variables
    drawing = False
    x_init, y_init = 0, 0
    top_left_pt, bottom_right_pt = (-1, -1), (-1, -1)
    bbox = None

    # Load the image
    img = image.copy()
    img = cv2.resize(img, resize_parameter)
    cv2.imshow("Bounding Box *** INSTRUCTIONS : [-q to Quit, -r to ReDraw, -a to AddBoxes, -s to Save] ***", img)
    cv2.setMouseCallback("Bounding Box *** INSTRUCTIONS : [-q to Quit, -r to ReDraw, -a to AddBoxes, -s to Save] ***", draw_rectangle)

    bboxes = []
    while True:
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        
        elif key == ord('r'):  # Reset the bounding box
            img = image.copy()
            img = cv2.resize(img, resize_parameter)
            cv2.imshow("Bounding Box *** INSTRUCTIONS : [-q to Quit, -r to ReDraw, -a to AddBoxes, -s to Save] ***", img)
            top_left_pt, bottom_right_pt = (-1, -1), (-1, -1)
            bbox = None
        
        elif key == ord('a'):  # Save bounding box info
            if bbox is not None:
                # print("Bounding box coordinates:", bbox)
                bboxes.append(bbox)
            else:
                print("No bounding box created yet!")

        elif key == ord('s'):  # Save bounding box info
            if bboxes is not None:
                # print("Bounding box coordinates:", bbox)
                cv2.destroyAllWindows()
                return bboxes
            else:
                print("No bounding box created yet!")

    cv2.destroyAllWindows()