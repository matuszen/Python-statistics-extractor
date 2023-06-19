import pandas as pd
import numpy as np
import PyPDF2


class ExtractStatistics:
    def __init__(self, file_path: str) -> None:
        if file_path.lower().endswith(".pdf"):
            self._read_pdf(file_path)

        self._extract_legend()
        self._extract_types()

    def __del__(self) -> None:
        self.content = ""
        self.header = tuple()

    def _read_pdf(self, file_path) -> None:
        with open(file_path, "rb"):
            reader = PyPDF2.PdfReader(file_path)
            text = ""

            for page in reader.pages:
                text = f"{text}{page.extract_text()}"

        self.content = text

    def _extract_legend(self) -> None:
        max_length = 0

        for line in self.content.split("\n"):
            data = [
                element.strip().replace(" ", "")
                for element in line.split(" ")
                if element.strip()
            ]

            if len(data) > max_length:
                max_length = len(data)

        for line in self.content.split("\n"):
            data = [
                element.strip().replace(" ", "")
                for element in line.split(" ")
                if element.strip()
            ]

            if len(data) == max_length:
                self.header = data.copy()
                break

    def _extract_types(self) -> None:
        bufor = self.content
        self.content = np.array()

        for line in bufor.split("\n"):
            line = [
                element.strip().replace(" ", "")
                for element in line.split(" ")
                if element.strip()
            ]
            self.content = f"{self.content}{line}"
            print(line)


data = ExtractStatistics("PP-W-ST-lista-2023.06.19-teoria.pdf")

print(data.header)
# print(data.content)

# for line in formated_data.split("\n"):
#     if len(line) > 2 and "page" not in line.lower():
#         data = line.split(" ")
#         print(data)
