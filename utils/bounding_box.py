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


def get_absolute_bounding_box(bbox, resized_dimensions, page_dimensions):

        # Extract resized and page dimensions
        resized_height, resized_width = resized_dimensions
        page_height, page_width,_ = page_dimensions

        # Extract bounding box coordinates
        (x1, y1), (x2, y2) = bbox

        # Convert bounding box coordinates to absolute coordinates
        absolute_x1 = int(x1 / resized_width * page_width)
        absolute_y1 = int(y1 / resized_height * page_height)
        absolute_x2 = int(x2 / resized_width * page_width)
        absolute_y2 = int(y2 / resized_height * page_height)
        print("abs",  (absolute_x1, absolute_y1), (absolute_x2, absolute_y2) )
        return (absolute_x1, absolute_y1), (absolute_x2, absolute_y2)