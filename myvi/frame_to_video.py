import cv2
import os


def frame_to_video(video_path: str, frame_dir: str, fps=30, log=True):

    first_img = True

    file_list = sorted(os.listdir(frame_dir))
    for file_name in file_list:
        fn = os.path.join(frame_dir, file_name)
        curImg = cv2.imread(fn)

        if first_img:
            img_size = curImg.shape[0:2]
            fourcc = cv2.VideoWriter_fourcc(*'X264')
            vid_out = cv2.VideoWriter(video_path, fourcc, fps, img_size)
            first_img = False

        vid_out.write(curImg)
        if log:
            print(fn)

    vid_out.release()
