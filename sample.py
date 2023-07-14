import csv
from drags import Drag, DragLogger


class CsvDragRepository:
    def __init__(self, file_path: str):
        self.file_path = file_path
        with open(file_path, mode="a") as f:
            writer = csv.writer(f)
            writer.writerow(
                [
                    "click_time",
                    "click_x",
                    "click_y",
                    "release_time",
                    "release_x",
                    "release_y",
                ]
            )

    def save(self, drag: Drag):
        with open(self.file_path, mode="a") as f:
            writer = csv.writer(f)
            strformat = "%H:%M:%S.%f"
            writer.writerow(
                [
                    drag.click.time.strftime(strformat),
                    drag.click.x,
                    drag.click.y,
                    drag.release.time.strftime(strformat),
                    drag.release.x,
                    drag.release.y,
                ]
            )
        print(f"{drag}")


repository = CsvDragRepository("./sample.csv")
logger = DragLogger(on_drag=repository.save)
logger.start()
