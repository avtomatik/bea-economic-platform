import io
from dataclasses import dataclass
from enum import Enum
from http import HTTPStatus
from typing import Any

import requests


class URL(Enum):
    BEA_NIPA_URL = "https://apps.bea.gov/national/Release/TXT/NipaDataA.txt"
    BEA_FIXED_ASSETS_URL = (
        "https://apps.bea.gov/national/FixedAssets/Release/TXT/FixedAssets.txt"
    )

    def get_kwargs(self) -> dict[str, Any]:
        COLUMNS = ["series_ids", "period", "value"]
        kwargs = {
            "header": 0,
            "names": COLUMNS,
            "index_col": 1,
            "thousands": ",",
        }
        if requests.head(self.value).status_code == HTTPStatus.OK:
            kwargs["filepath_or_buffer"] = io.BytesIO(
                requests.get(self.value).content
            )
        else:
            kwargs["filepath_or_buffer"] = self.value.split("/")[-1]
        return kwargs


@dataclass(frozen=True, eq=True)
class SeriesID:
    series_id: str
    source: URL
