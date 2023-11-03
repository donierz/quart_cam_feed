from typing import Generator
import cv2 as cv

def gen_frame_from_default_cam() -> Generator[bytes, None, None]:
    """
    Generates web camera image frames from the default web camera attached to the computer that is running this code.
    Yields: Generator[bytes, None, None]: Web camera JPEG byte data webcam frames.
    """
    
    # Tells system to use the default webcam
    webcam = cv.VideoCapture(0)
    
    if not webcam.isOpened():
        print("Cannot open camera")
        exit()

    # While camera is on
    while True:
        # Capture frame-by-frame
        success, frame = webcam.read()
        # if frame is read correctly ret is True
        if not success:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        
        # attain buffer images from webcam?
        _, buffer = cv.imencode(".jpg", frame)
        frame = buffer.tobytes()

        # \r\n is a carriage return and line feed, used to separate lines in the HTTP protocol.
        # yield a sequence of bytes that represent a multipart response, used for streaming data over HTTP.
        yield (
                # byte literal, sequence of bytes instead of characters, images are binary data, not text
                b"--frame\r\n" # boundary string, indicating the start of a new part of the response
                b"Content-Type: image/jpeg\r\n\r\n" + frame # headers indicating that the binary data is an image in JPEG format.
                + b"\r\n"
            )    
        
    # When everything done, release the capture
    webcam.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    gen_frame_from_default_cam()
