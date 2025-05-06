from pathlib import Path

from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet

ROOT_FOLDER = Path(__file__).parent
WORKBOOK_PATH = ROOT_FOLDER / "students.xlsx"

workbook = Workbook()
worksheet: Worksheet = workbook.active

worksheet.cell(1, 1, "Name")
worksheet.cell(1, 2, "Age")
worksheet.cell(1, 3, "GPA")

students = [["John", 14, 5.5], ["Jane", 13, 4.5], ["Bob", 15, 3.5], ["Alice", 12, 4.0]]


for i, students_row in enumerate(
    students, start=2
):  # start=2 para comecar na linha 2 do excel e nao na 1students:
    for j, students_col in enumerate(
        students_row, start=1
    ):  # start=1 para comecar na coluna 1 do excel e nao na 0
        worksheet.cell(i, j, students_col)

workbook.save(WORKBOOK_PATH)
