from abc import ABC, abstractmethod
from typing import Optional

import pandas as pd


class FromSource(ABC):
    """
    Abstract base class that defines the minimum requirements for a FromSource child class.
    """

    @property
    @abstractmethod
    def production(self) -> pd.DataFrame:
        raise NotImplementedError(
            "The production property is required to be implemented in a FromSource class."
        )

    @property
    @abstractmethod
    def coordinates(self) -> pd.DataFrame:
        raise NotImplementedError(
            "The coordinates property is required to be implemented in a FromSource class."
        )

    @property
    @abstractmethod
    def faults(self) -> Optional[pd.DataFrame]:
        raise NotImplementedError(
            "The faults property is required to be implemented in a FromSource class."
        )
