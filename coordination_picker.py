"""
사용법:
  1. 이 스크립트를 실행합니다.
  2. 좌석 구역의 좌측 상단 모서리를 클릭합니다.
  3. 좌석 구역의 우측 하단 모서리를 클릭합니다.
  → macro.py의 region 값으로 사용할 (x, y, width, height)가 출력됩니다.
"""

from pynput import mouse

saved_points = []


def on_click(x, y, button, pressed):
    if not pressed:
        return

    saved_points.append((x, y))
    labels = ["좌측 상단", "우측 하단"]
    print(f"{labels[len(saved_points) - 1]} 저장: ({x}, {y})")

    if len(saved_points) == 2:
        x1, y1 = saved_points[0]
        x2, y2 = saved_points[1]
        region = (x1, y1, x2 - x1, y2 - y1)
        print(f"\nregion = {region}")
        print("위 값을 macro.py의 region에 붙여넣으세요.")
        return False


with mouse.Listener(on_click=on_click) as listener:
    print("좌석 구역의 좌측 상단 → 우측 하단 순서로 클릭하세요.")
    listener.join()
