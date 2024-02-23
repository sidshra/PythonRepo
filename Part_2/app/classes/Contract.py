from abc import ABC, abstractmethod

class Contract(ABC):
    """Represents a contract and a payment process for a particular employeee."""
    

    @abstractmethod
    def get_payment(self) -> float:
        """Compute how much to pay an employee under this contract."""
    