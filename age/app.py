
# # # from flask import Flask, render_template

# # # app = Flask(__name__)

# # # # Your age detection code
# # # import cv2
# # # import time

# # # faceProto = "opencv_face_detector.pbtxt"
# # # faceModel = "opencv_face_detector_uint8.pb"

# # # ageProto = "age_deploy.prototxt"
# # # ageModel = "age_net.caffemodel"

# # # faceNet = cv2.dnn.readNet(faceModel, faceProto)
# # # ageNet = cv2.dnn.readNet(ageModel, ageProto)

# # # MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
# # # ageList = ['(0-2)', '(4-6)', '(8-12)', '(15-18)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']
# # # padding = 20

# # # detected_age = None

# # # def faceBox(faceNet, frames):
# # #     frameHeight = frames.shape[0]
# # #     frameWidth = frames.shape[1]
# # #     blob = cv2.dnn.blobFromImage(frames, 1.0, (300, 300), [104, 117, 123], swapRB=False)
# # #     faceNet.setInput(blob)
# # #     detection = faceNet.forward()
# # #     bboxs = []
# # #     for i in range(detection.shape[2]):
# # #         confidence = detection[0, 0, i, 2]
# # #         if confidence > 0.7:
# # #             x1 = int(detection[0, 0, i, 3] * frameWidth)
# # #             y1 = int(detection[0, 0, i, 4] * frameHeight)
# # #             x2 = int(detection[0, 0, i, 5] * frameWidth)
# # #             y2 = int(detection[0, 0, i, 6] * frameHeight)
# # #             bboxs.append([x1, y1, x2, y2])
# # #             cv2.rectangle(frames, (x1, y1), (x2, y2), (0, 255, 0), 1)
# # #     return frames, bboxs

# # # def get_detected_age():
# # #     global detected_age
# # #     return detected_age

# # # def DisplayVid():
# # #     global detected_age
# # #     cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# # #     fourcc = cv2.VideoWriter_fourcc(*'XVID')
# # #     out = cv2.VideoWriter('testvideo', fourcc, 20.0, (640, 480))

# # #     cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
# # #     cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

# # #     start_time = time.time()

# # #     while (time.time() - start_time) < 10:  # Capture frames for 10 seconds
# # #         ret, frame = cap.read()
# # #         frameFace, bboxes = faceBox(faceNet, frame)
# # #         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# # #         out.write(frame)

# # #         for bbox in bboxes:
# # #             face = frame[bbox[1]:bbox[3], bbox[0]:bbox[2]]

# # #             blob = cv2.dnn.blobFromImage(face, 1.0, (227, 227), MODEL_MEAN_VALUES, swapRB=False)

# # #             ageNet.setInput(blob)
# # #             agePreds = ageNet.forward()
# # #             detected_age = ageList[agePreds[0].argmax()]

# # #             label = "{}".format(detected_age)
# # #             cv2.rectangle(frameFace, (bbox[0], bbox[1] - 30), (bbox[2], bbox[1]), (0, 255, 0), -1)
# # #             cv2.putText(frameFace, label, (bbox[0], bbox[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2,
# # #                         cv2.LINE_AA)
# # #         cv2.imshow("age detection system", frameFace)
# # #         k = cv2.waitKey(1)
# # #         if cv2.waitKey(1) & 0xFF == ord('q'):
# # #             break

# # #         if not (cap.isOpened()):
# # #             print("Could not open video device")

# # #     cap.release()
# # #     out.release()
# # #     cv2.destroyAllWindows()

# # # @app.route('/')
# # # def index():
# # #     return render_template('underage.html')

# # # @app.route('/harddrinks')
# # # def harddrinks():
# # #     detected_age = get_detected_age()
# # #     return render_template('harddrinks.html', detected_age=detected_age)

# # # if __name__ == '__main__':
# # #     DisplayVid()  # Run video capture in a separate thread
# # #     app.run(debug=True)
# # from flask import Flask, render_template, session, jsonify
# # from flask_session import Session
# # import cv2
# # import time

# # app = Flask(__name__)
# # app.secret_key = 'your_secret_key'
# # app.config['SESSION_TYPE'] = 'filesystem'
# # Session(app)

# # faceProto = "opencv_face_detector.pbtxt"
# # faceModel = "opencv_face_detector_uint8.pb"

# # ageProto = "age_deploy.prototxt"
# # ageModel = "age_net.caffemodel"

# # faceNet = cv2.dnn.readNet(faceModel, faceProto)
# # ageNet = cv2.dnn.readNet(ageModel, ageProto)

# # MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
# # ageList = ['(0-2)', '(4-6)', '(8-12)', '(15-18)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']
# # padding = 20

# # detected_age = None

# # def faceBox(faceNet, frames):
# #     frameHeight = frames.shape[0]
# #     frameWidth = frames.shape[1]
# #     blob = cv2.dnn.blobFromImage(frames, 1.0, (300, 300), [104, 117, 123], swapRB=False)
# #     faceNet.setInput(blob)
# #     detection = faceNet.forward()
# #     bboxs = []
# #     for i in range(detection.shape[2]):
# #         confidence = detection[0, 0, i, 2]
# #         if confidence > 0.7:
# #             x1 = int(detection[0, 0, i, 3] * frameWidth)
# #             y1 = int(detection[0, 0, i, 4] * frameHeight)
# #             x2 = int(detection[0, 0, i, 5] * frameWidth)
# #             y2 = int(detection[0, 0, i, 6] * frameHeight)
# #             bboxs.append([x1, y1, x2, y2])
# #             cv2.rectangle(frames, (x1, y1), (x2, y2), (0, 255, 0), 1)
# #     return frames, bboxs

# # def get_detected_age():
# #     global detected_age
# #     return detected_age

# # def DisplayVid():
# #     global detected_age
# #     cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# #     fourcc = cv2.VideoWriter_fourcc(*'XVID')
# #     out = cv2.VideoWriter('testvideo', fourcc, 20.0, (640, 480))

# #     cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
# #     cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

# #     start_time = time.time()

# #     while (time.time() - start_time) < 10:  # Capture frames for 10 seconds
# #         ret, frame = cap.read()
# #         frameFace, bboxes = faceBox(faceNet, frame)
# #         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# #         out.write(frame)

# #         for bbox in bboxes:
# #             face = frame[bbox[1]:bbox[3], bbox[0]:bbox[2]]

# #             blob = cv2.dnn.blobFromImage(face, 1.0, (227, 227), MODEL_MEAN_VALUES, swapRB=False)

# #             ageNet.setInput(blob)
# #             agePreds = ageNet.forward()
# #             detected_age = ageList[agePreds[0].argmax()]

# #             label = "{}".format(detected_age)
# #             cv2.rectangle(frameFace, (bbox[0], bbox[1] - 30), (bbox[2], bbox[1]), (0, 255, 0), -1)
# #             cv2.putText(frameFace, label, (bbox[0], bbox[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2,
# #                         cv2.LINE_AA)
# #         cv2.imshow("age detection system", frameFace)
# #         k = cv2.waitKey(1)
# #         if cv2.waitKey(1) & 0xFF == ord('q'):
# #             break

# #         if not (cap.isOpened()):
# #             print("Could not open video device")

# #     cap.release()
# #     out.release()
# #     cv2.destroyAllWindows()

# # @app.route('/')
# # def index():
# #     return render_template('underage.html')

# # @app.route('/detect_age')
# # def detect_age():
# #     global detected_age
# #     return jsonify({'age': detected_age})

# # @app.route('/harddrinks')
# # def harddrinks():
# #     detected_age = get_detected_age()
# #     if detected_age is not None and detected_age >= 18:
# #         return render_template('harddrinks.html', detected_age=detected_age)
# #     else:
# #         return render_template('underage.html')

# # if __name__ == '__main__':
# #     DisplayVid()  # Run video capture in a separate thread
# #     app.run(debug=True)



# from flask import Flask, render_template, session, jsonify
# from flask_session import Session
# import cv2
# import time

# app = Flask(__name__)
# app.secret_key = 'your_secret_key'
# app.config['SESSION_TYPE'] = 'filesystem'
# Session(app)

# faceProto = "opencv_face_detector.pbtxt"
# faceModel = "opencv_face_detector_uint8.pb"

# ageProto = "age_deploy.prototxt"
# ageModel = "age_net.caffemodel"

# faceNet = cv2.dnn.readNet(faceModel, faceProto)
# ageNet = cv2.dnn.readNet(ageModel, ageProto)

# MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
# ageList = ['(0-2)', '(4-6)', '(8-12)', '(15-18)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']
# padding = 20

# detected_age = None

# def faceBox(faceNet, frames):
#     frameHeight = frames.shape[0]
#     frameWidth = frames.shape[1]
#     blob = cv2.dnn.blobFromImage(frames, 1.0, (300, 300), [104, 117, 123], swapRB=False)
#     faceNet.setInput(blob)
#     detection = faceNet.forward()
#     bboxs = []
#     for i in range(detection.shape[2]):
#         confidence = detection[0, 0, i, 2]
#         if confidence > 0.7:
#             x1 = int(detection[0, 0, i, 3] * frameWidth)
#             y1 = int(detection[0, 0, i, 4] * frameHeight)
#             x2 = int(detection[0, 0, i, 5] * frameWidth)
#             y2 = int(detection[0, 0, i, 6] * frameHeight)
#             bboxs.append([x1, y1, x2, y2])
#             cv2.rectangle(frames, (x1, y1), (x2, y2), (0, 255, 0), 1)
#     return frames, bboxs

# def get_detected_age():
#     global detected_age
#     return detected_age

# def DisplayVid():
#     global detected_age
#     cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
#     fourcc = cv2.VideoWriter_fourcc(*'XVID')
#     out = cv2.VideoWriter('testvideo', fourcc, 20.0, (640, 480))

#     cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
#     cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

#     start_time = time.time()

#     while (time.time() - start_time) < 10:  # Capture frames for 10 seconds
#         ret, frame = cap.read()
#         frameFace, bboxes = faceBox(faceNet, frame)
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         out.write(frame)

#         for bbox in bboxes:
#             face = frame[bbox[1]:bbox[3], bbox[0]:bbox[2]]

#             blob = cv2.dnn.blobFromImage(face, 1.0, (227, 227), MODEL_MEAN_VALUES, swapRB=False)

#             ageNet.setInput(blob)
#             agePreds = ageNet.forward()
#             detected_age = ageList[agePreds[0].argmax()]

#             label = "{}".format(detected_age)
#             cv2.rectangle(frameFace, (bbox[0], bbox[1] - 30), (bbox[2], bbox[1]), (0, 255, 0), -1)
#             cv2.putText(frameFace, label, (bbox[0], bbox[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2,
#                         cv2.LINE_AA)
#         cv2.imshow("age detection system", frameFace)
#         k = cv2.waitKey(1)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#         if not (cap.isOpened()):
#             print("Could not open video device")

#     cap.release()
#     out.release()
#     cv2.destroyAllWindows()

# @app.route('/')
# def index():
#     return render_template('underage.html')

# @app.route('/detect_age')
# def detect_age():
#     global detected_age
#     return jsonify({'age': detected_age})

# @app.route('/harddrinks')
# def harddrinks():
#     detected_age = get_detected_age()
#     if detected_age is not None and detected_age in ('(15-18)', '(25-32)', '(38-43)', '(48-53)', '(60-100)'):
#         return render_template('harddrinks.html', detected_age=detected_age)
#     else:
#         return render_template('underage.html')

# if __name__ == '__main__':
#     DisplayVid()  # Run video capture in a separate thread
#     app.run(debug=True)


from flask import Flask, render_template, jsonify
import cv2
import time

app = Flask(__name__)




faceProto = "opencv_face_detector.pbtxt"
faceModel = "opencv_face_detector_uint8.pb"

ageProto = "age_deploy.prototxt"
ageModel = "age_net.caffemodel"

faceNet = cv2.dnn.readNet(faceModel, faceProto)
ageNet = cv2.dnn.readNet(ageModel, ageProto)

MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
ageList = ['(0-3)', '(4-10)', '(11-17)', '(18-25)', '(26-35)', '(36-65)', '(66-100)']
padding = 20

detected_age = None

def faceBox(faceNet, frames):
    frameHeight = frames.shape[0]
    frameWidth = frames.shape[1]
    blob = cv2.dnn.blobFromImage(frames, 1.0, (300, 300), [104, 117, 123], swapRB=False)
    faceNet.setInput(blob)
    detection = faceNet.forward()
    bboxs = []
    for i in range(detection.shape[2]):
        confidence = detection[0, 0, i, 2]
        if confidence > 0.7:
            x1 = int(detection[0, 0, i, 3] * frameWidth)
            y1 = int(detection[0, 0, i, 4] * frameHeight)
            x2 = int(detection[0, 0, i, 5] * frameWidth)
            y2 = int(detection[0, 0, i, 6] * frameHeight)
            bboxs.append([x1, y1, x2, y2])
            cv2.rectangle(frames, (x1, y1), (x2, y2), (0, 255, 0), 1)
    return frames, bboxs

def get_detected_age():
    global detected_age
    return detected_age

def DisplayVid():
    global detected_age
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    if not cap.isOpened():
        print("Could not open video device")
        return

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('testvideo', fourcc, 20.0, (640, 480))

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    start_time = time.time()

    try:
        while (time.time() - start_time) < 50:  # Capture frames for 10 seconds
            ret, frame = cap.read()
            if not ret:
                print("Error reading frame from the video source")
                break

            frameFace, bboxes = faceBox(faceNet, frame)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            out.write(frame)

            for bbox in bboxes:
                face = frame[bbox[1]:bbox[3], bbox[0]:bbox[2]]

                blob = cv2.dnn.blobFromImage(face, 1.0, (227, 227), MODEL_MEAN_VALUES, swapRB=False)

                ageNet.setInput(blob)
                agePreds = ageNet.forward()
                detected_age = ageList[agePreds[0].argmax()]

                label = "{}".format(detected_age)
                cv2.rectangle(frameFace, (bbox[0], bbox[1] - 30), (bbox[2], bbox[1]), (0, 255, 0), -1)
                cv2.putText(frameFace, label, (bbox[0], bbox[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2,
                            cv2.LINE_AA)
            cv2.imshow("age detection system", frameFace)
            k = cv2.waitKey(1)
            if k == ord('q'):
                break
    except Exception as e:
        print(f"Error in video capture loop: {str(e)}")
    finally:
        cap.release()
        out.release()
        cv2.destroyAllWindows()

@app.route('/')
def index():
    return render_template('underage.html')

@app.route('/detect_age')
def detect_age():
    global detected_age
    try:
        return jsonify({'age': detected_age})
    except Exception as e:
        print(f"Error in detect_age route: {str(e)}")
        return jsonify({'error': 'An unexpected error occurred'})

@app.route('/harddrinks')
def harddrinks():
    detected_age = get_detected_age()
    if detected_age is not None and detected_age in ('(15-18)', '(25-32)', '(38-43)', '(48-53)', '(60-100)'):
        return render_template('harddrinks.html', detected_age=detected_age)
    else:
        return render_template('underage.html')

if __name__ == '__main__':
    DisplayVid()  # Run video capture in a separate thread
    app.run()
