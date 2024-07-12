import cv2

class VideoSlowMoConverter:
    def __init__(self, input_video_path, output_video_path, slow_factor=2):
        self.input_video_path = input_video_path
        self.output_video_path = output_video_path
        self.slow_factor = slow_factor

    def convert_to_slow_motion(self):
        cap = cv2.VideoCapture(self.input_video_path)
        if not cap.isOpened():
            print("Error: Couldn't open video file.")
            return

        # Get video details
        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        # Create VideoWriter object to save slow motion video
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for MP4 format
        out = cv2.VideoWriter(self.output_video_path, fourcc,2000, (frame_width, frame_height))

        frame_skip = self.slow_factor - 1  # Number of frames to skip between writes
        frame_counter = 0

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame_counter += 1
            if frame_counter % self.slow_factor != 0:
                continue

            # Process frame here (if needed)
            # Example: frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            out.write(frame)

            cv2.imshow('Slow Motion Video', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release resources
        cap.release()
        out.release()
        cv2.destroyAllWindows()

        print(f"Slow motion video saved to {self.output_video_path}")

# Example usage:
input_path = r'd:\KKK\Download\Fluid cloud\vid (1).mp4'
output_path = r'd:\KKK\Download\Fluid cloud\slow_mo.mp4'
converter = VideoSlowMoConverter(input_path, output_path, slow_factor=2)
converter.convert_to_slow_motion()
