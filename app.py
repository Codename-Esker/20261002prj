# 1번 예제
#------------------------------------
import tkinter as tk

def change_message():
    """
    버튼을 눌렀을 때 실행되는 함수입니다.
    message_label의 글자를 새로운 문장으로 바꿉니다.
    """
    message_label.config(text="버튼을 눌렀습니다!")

root = tk.Tk()

root.title("예제 1 - Tkinter 기본 화면")

root.geometry("500x300")

title_label = tk.Label(
    root,
    text="교과 7 Tkinter 첫 번째 실습",
    font=("Arial", 18)
)
title_label.pack(pady=30)

message_label = tk.Label(
    root,
    text="아래 버튼을 눌러보세요.",
    font=("Arial", 12)
)
message_label.pack(pady=10)

change_button = tk.Button(
    root,
    text="메시지 변경",
    command=change_message,
    width=15,
    height=2
)
change_button.pack(pady=20)

root.mainloop()

#------------------------------------

# 2번 예제
#------------------------------------
# import tkinter as tk
# from tkinter import ttk

# def show_result():
#     """
#     Entry와 Combobox에서 현재 값을 읽어서
#     result_label에 표시합니다.
#     """

#     file_name = file_name_var.get()
#     class_name = class_var.get()

#     if file_name == "":
#         result_label.config(
#             text="파일명을 입력하세요."
#         )
#         return

#     if class_name == "":
#         result_label.config(
#             text="Class를 선택하세요."
#         )
#         return

#     result_text = (
#         f"파일명: {file_name}\n"
#         f"선택 Class: {class_name}"
#     )

#     result_label.config(text=result_text)

# root = tk.Tk()
# root.title("예제 2 - 라벨 정보 입력")
# root.geometry("550x350")

# file_name_var = tk.StringVar()
# class_var = tk.StringVar()

# title_label = tk.Label(
#     root,
#     text="라벨링 정보 입력 연습",
#     font=("Arial", 18)
# )

# title_label.grid(
#     row=0,
#     column=0,
#     columnspan=2,
#     pady=25
# )

# file_label = tk.Label(
#     root,
#     text="이미지 파일명:"
# )

# file_label.grid(
#     row=1,
#     column=0,
#     padx=20,
#     pady=10,
#     sticky="e"
# )

# file_entry = tk.Entry(
#     root,
#     textvariable=file_name_var,
#     width=30
# )

# file_entry.grid(
#     row=1,
#     column=1,
#     padx=20,
#     pady=10
# )

# class_label = tk.Label(
#     root,
#     text="Class:"
# )

# class_label.grid(
#     row=2,
#     column=0,
#     padx=20,
#     pady=10,
#     sticky="e"
# )

# class_combo = ttk.Combobox(
#     root,
#     textvariable=class_var,
#     values=[
#         "leaf",
#         "plastic",
#         "metal",
#         "disease"
#     ],
#     state="readonly",
#     width=27
# )

# class_combo.grid(
#     row=2,
#     column=1,
#     padx=20,
#     pady=10
# )

# save_button = tk.Button(
#     root,
#     text="입력 확인",
#     command=show_result,
#     width=20,
#     height=2
# )

# save_button.grid(
#     row=3,
#     column=0,
#     columnspan=2,
#     pady=20
# )

# result_label = tk.Label(
#     root,
#     text="파일명과 Class를 입력해 주세요.",
#     font=("Arial", 11)
# )

# result_label.grid(
#     row=4,
#     column=0,
#     columnspan=2,
#     pady=10
# )

# root.mainloop()
#------------------------------------

# 3번 예제

# import tkinter as tk


# # --------------------------------------------------
# # 마우스 시작 좌표와 Rectangle ID를 저장할 변수
# # --------------------------------------------------

# start_x = 0
# start_y = 0

# current_rect = None

# def on_mouse_down(event):
#     """
#     마우스 왼쪽 버튼을 누른 순간 실행됩니다.

#     event.x
#     event.y

#     는 Canvas 안에서 현재 마우스 좌표를 의미합니다.
#     """

#     global start_x, start_y, current_rect

#     start_x = event.x
#     start_y = event.y

#     # 이전에 만들던 임시 Rectangle이 있다면 삭제합니다.
#     if current_rect is not None:
#         canvas.delete(current_rect)

#     # 처음에는 크기가 0인 Rectangle을 만듭니다.
#     current_rect = canvas.create_rectangle(
#         start_x,
#         start_y,
#         start_x,
#         start_y,
#         outline="red",
#         width=2
#     )

#     status_label.config(
#         text=f"시작 좌표: ({start_x}, {start_y})"
#     )

# def on_mouse_drag(event):
#     """
#     마우스 왼쪽 버튼을 누른 채 움직일 때 실행됩니다.

#     마우스의 현재 위치에 맞춰 Rectangle 크기를 계속 변경합니다.
#     """

#     if current_rect is None:
#         return

#     current_x = event.x
#     current_y = event.y

#     canvas.coords(
#         current_rect,
#         start_x,
#         start_y,
#         current_x,
#         current_y
#     )

# def on_mouse_up(event):
#     """
#     마우스 버튼을 놓았을 때 실행됩니다.

#     이 순간을 BBox가 확정된 시점으로 생각합니다.
#     """

#     end_x = event.x
#     end_y = event.y

#     # 사용자가 오른쪽 → 왼쪽,
#     # 아래쪽 → 위쪽으로 드래그할 수도 있기 때문에
#     # min, max를 사용해 좌표를 정리합니다.

#     x1 = min(start_x, end_x)
#     y1 = min(start_y, end_y)

#     x2 = max(start_x, end_x)
#     y2 = max(start_y, end_y)

#     bbox_width = x2 - x1
#     bbox_height = y2 - y1

#     result_text = (
#         f"BBox 좌표: "
#         f"({x1}, {y1}) ~ ({x2}, {y2})\n"
#         f"Width: {bbox_width}, "
#         f"Height: {bbox_height}"
#     )

#     status_label.config(text=result_text)
# def clear_bbox():
#     """
#     Canvas의 모든 Rectangle을 삭제합니다.
#     """

#     global current_rect

#     canvas.delete("all")
#     current_rect = None

#     status_label.config(
#         text="BBox를 다시 그려보세요."
#     )

# # --------------------------------------------------
# # 1. Window 생성
# # --------------------------------------------------

# root = tk.Tk()

# root.title("예제 3 - BBox 그리기")
# root.geometry("800x650")

# # --------------------------------------------------
# # 2. 제목
# # --------------------------------------------------

# title_label = tk.Label(
#     root,
#     text="마우스로 BBox를 그려보세요.",
#     font=("Arial", 18)
# )

# title_label.pack(pady=15)

# # --------------------------------------------------
# # 3. Canvas
# # --------------------------------------------------

# canvas = tk.Canvas(
#     root,
#     width=700,
#     height=450,
#     bg="white"
# )

# canvas.pack(pady=10)

# # --------------------------------------------------
# # 4. Mouse Event 연결
# # --------------------------------------------------

# canvas.bind(
#     "<ButtonPress-1>",
#     on_mouse_down
# )

# canvas.bind(
#     "<B1-Motion>",
#     on_mouse_drag
# )

# canvas.bind(
#     "<ButtonRelease-1>",
#     on_mouse_up
# )

# # --------------------------------------------------
# # 5. 상태 Label
# # --------------------------------------------------

# status_label = tk.Label(
#     root,
#     text="흰색 영역에서 마우스를 드래그하세요.",
#     font=("Arial", 11)
# )

# status_label.pack(pady=10)

# # --------------------------------------------------
# # 6. 삭제 Button
# # --------------------------------------------------

# clear_button = tk.Button(
#     root,
#     text="BBox 지우기",
#     command=clear_bbox,
#     width=20,
#     height=2
# )

# clear_button.pack(pady=10)

# # --------------------------------------------------
# # 7. GUI 실행
# # --------------------------------------------------

# root.mainloop()

