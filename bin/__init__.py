import pandas as pd
import os
import re
import tabula
from datetime import datetime
from typing import (
    Iterable,
    Optional,
    Union,
)


class ExtractStatistics:
    def __init__(
        self,
        file_path: Union[str, os.PathLike],
        pages: Optional[Union[str, int, Iterable[int]]] = "all",
        area: Optional[Union[Iterable[float], Iterable[Iterable[float]]]] = None,
        password: Optional[str] = None,
        date_format: Optional[str] = "%d-%m-%Y %H:%M:%S",
        log: Optional[bool] = False,
    ) -> None:
        self._date_format = date_format
        self._logging = log

        if file_path.lower().endswith(".pdf"):
            self._read_pdf(file_path, pages, area, password)

    # def __del__(self) -> None:
    #     self._content

    def __str__(self) -> str:
        return self._content.to_string()

    def __getitem__(self, value: str) -> pd.DataFrame:
        return self._content[value].to_string(index=False)

    @property
    def shape(self) -> tuple[int, int]:
        return self._content.shape

    @property
    def columns(self) -> list:
        return list(self._content.columns)

    @columns.setter
    def columns(self, new_value: list) -> None:
        length = len(new_value)
        expected_length = len(self.columns)

        if expected_length != length:
            raise ValueError(
                f"Expected length is {expected_length}, but new object's length is {length}"
            )
        self._content.columns = new_value

    @property
    def data_types(self) -> list:
        list(self._content.dtypes)

    @data_types.setter
    def data_types(self, new_value: list) -> None:
        length = len(new_value)
        expected_length = len(self.data_types)

        if expected_length != length:
            raise ValueError(
                f"Expected length is {expected_length}, but new object's length is {length}"
            )
        self._content.dtypes = new_value

    def _log(
        self,
        *values: object,
        type: str | None = "info",
        sep: str | None = " ",
        end: str | None = "\n",
    ) -> None:
        current_time = datetime.now()

        print(
            f"[{current_time.strftime(self._date_format)}][{type.upper()}]\t",
            *values,
            sep=sep,
            end=end,
        )

    def _read_pdf(
        self,
        file_path: Union[str, os.PathLike],
        pages: Optional[Union[str, int, Iterable[int]]] = "all",
        area: Optional[Union[Iterable[float], Iterable[Iterable[float]]]] = None,
        password: Optional[str] = None,
    ) -> None:
        try:
            tables = tabula.read_pdf(
                file_path,
                pages=pages,
                area=area,
                password=password,
            )

        except FileNotFoundError:
            self._log(f"File '{file_path}' not exists", type="error")
            raise

        except ValueError:
            self._log(f"File '{file_path}' is empty", type="error")
            raise

        except Exception:
            self._log("Unknown error. More details below", type="error")
            raise

        if self._logging:
            self._log(f"File '{file_path}' read correctly")

        merged_table = tables[0].copy()

        for table in tables[1:]:
            table.columns = merged_table.columns
            merged_table = pd.concat([merged_table, table])

        merged_table.reset_index(drop=True, inplace=True)

        self._content = merged_table

        if self._logging:
            self._log("Data processing finished. No problems found")

    def _is_integer(self, object: str) -> bool:
        pattern = r"^-?\d+$"
        return bool(re.match(pattern, object))

    def _is_float(self, object: str) -> bool:
        pattern = r"^[-+]?\d*[\.,]\d+$"
        return bool(re.match(pattern, object))

    def _is_string(self, object: str) -> bool:
        pattern = r"^[a-zA-Z\s]+$"
        return bool(re.match(pattern, object))
