from typing import Tuple

import cv2
import os


def videos_to_frame(base_dir: str,
                    filename_pattern: str = 'frame%03d.jpg',
                    log: bool = True,
                    supported_video_ext: Tuple[str] = ('mp4', ),
                    frame_edit_func=None):
    '''
    Given a base directory that contains several frame directories, the
    funciton merges the frames into videos and save them to base directory
    '''

    for file in os.listdir(base_dir):
        name, ext = os.path.splitext(file)
        if ext not in supported_video_ext:
            continue
        video_path = os.path.join(base_dir, file)
        frame_dir = os.path.join(base_dir, name)
        video_to_frame(video_path, frame_dir, filename_pattern, log,
                       frame_edit_func)


def video_to_frame(video_path: str,
                   frame_dir: str,
                   filename_pattern: str = 'frame%03d.jpg',
                   log: bool = True,
                   frame_edit_func=None):
    os.makedirs(frame_dir, exist_ok=True)

    vidcap = cv2.VideoCapture(video_path)
    success, image = vidcap.read()

    if log:
        print('img shape: ', image.shape[0:2])

    count = 0
    while success:
        if frame_edit_func is not None:
            image = frame_edit_func(image)

        cv2.imwrite(os.path.join(frame_dir, filename_pattern % count), image)
        success, image = vidcap.read()
        if log:
            print('Read a new frame: ', success, count)
        count += 1

    vidcap.release()
