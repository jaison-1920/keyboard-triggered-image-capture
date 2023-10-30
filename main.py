import cv2
import os
import keyboard

def capture_and_save_image(camera, save_path):
    ret, frame = camera.read()
    if not ret:
        print("Error capturing the image.")
        return

    # Perform image processing (e.g., resizing)
    processed_frame = cv2.resize(frame, (640, 480))

    # Save the processed image to the specified folder
    image_name = "captured_image.jpg"
    image_path = os.path.join(save_path, image_name)
    cv2.imwrite(image_path, processed_frame)
    print(f"Image saved to {image_path}")

     # Display the captured image
    cv2.imshow("Captured Image", processed_frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Remove the captured image file
    os.remove(image_path)
    print(f"Image removed from {image_path}")


def main():
    # Define the camera source (0 for webcam)
    camera = cv2.VideoCapture(0)

    # Define the folder where the images will be saved
    save_folder = "C:/Users/Jaison P/Documents/foto project"
    os.makedirs(save_folder, exist_ok=True)

    is_enter_pressed = False  # Flag to track if 'enter' is pressed

    while True:
        if keyboard.is_pressed('enter') and not is_enter_pressed:
            capture_and_save_image(camera, save_folder)
            is_enter_pressed = True
        elif not keyboard.is_pressed('enter'):
            is_enter_pressed = False

        if keyboard.is_pressed('q'):
            break

    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
