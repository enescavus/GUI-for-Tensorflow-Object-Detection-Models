'''
===============================================================
@ Title:  Tensorflow Object Detection GUI - Tkinter / Detection Page
@ Author: Enes Çavuş
@ Date:   27 June 2020 

'''

'''
NOTE: I assumed that you already have the knowledge about Tensorflow object detection, then you can implement your model to this perfect GUI.
'''

# See the original Page from Tensorflow Object Detectin
# https://github.com/tensorflow/models/tree/master/research/object_detection




##################################################################################

# Follow these instructions to implement your model to this perfect GUI

##################################################################################

# CHANGE THE "YUOR_MODEL_NAME_PATH" - THE PATH WHERE YOUR MODEL IS
# PROBABLY YOU HAVE THIS FILE IN 'SAVED MODEL' FOLDER   "frozen_inference_graph.pb"
# YOU MUSt HAVE A LABELMAP LIKE -> object-detection.pbtxt


# you will see ++++++++++++++++++++++++++ this pattern for the paths you have to change
##################################################################################




# Import Packages
import os
import cv2
import numpy as np
import tensorflow as tf
import sys


sys.path.append("..")

from utils import label_map_util
from utils import visualization_utils as vis_util


def detect_objects(IMAGE_NAME, SCORE_THRESHOLD):

# ++++++++++++++++++++++++++ change it
    MODEL_NAME = 'YUOR_MODEL_NAME_PATH'

    CWD_PATH = os.getcwd()
                                                    # ++++++++++++++++++++++++++ change it
    PATH_TO_CKPT = os.path.join(CWD_PATH,MODEL_NAME,'frozen_inference_graph.pb')

                                                    # ++++++++++++++++++++++++++ change it
    PATH_TO_LABELS = os.path.join(CWD_PATH,'training','object-detection.pbtxt')

    PATH_TO_IMAGE = os.path.join(CWD_PATH,IMAGE_NAME)


    NUM_CLASSES = 1 # I only detect faces in this project so the number is one but you can modify it for yours

    label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
    categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
    category_index = label_map_util.create_category_index(categories)


    detection_graph = tf.Graph()
    with detection_graph.as_default():
        od_graph_def = tf.GraphDef()
        with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
            serialized_graph = fid.read()
            od_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(od_graph_def, name='')

        sess = tf.Session(graph=detection_graph)

    image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')

    detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')

    detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
    detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')

    num_detections = detection_graph.get_tensor_by_name('num_detections:0')

    image = cv2.imread(PATH_TO_IMAGE)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_expanded = np.expand_dims(image_rgb, axis=0)


    (boxes, scores, classes, num) = sess.run(
        [detection_boxes, detection_scores, detection_classes, num_detections],
        feed_dict={image_tensor: image_expanded})

    vis_util.visualize_boxes_and_labels_on_image_array(
        image,
        np.squeeze(boxes),
        np.squeeze(classes).astype(np.int32),
        np.squeeze(scores),
        category_index,
        use_normalized_coordinates=True,
        line_thickness=8,
        min_score_thresh=SCORE_THRESHOLD)
	#when detection ended you will have a temporary picture in this 'imgWeWorkingOn' folder.
        # This repository already has included this folder
    cv2.imwrite('imgWeWorkingOn/temp.jpg',image)






