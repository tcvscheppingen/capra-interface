"""Module used for defining a DrivingInstruction"""
from dataclasses import dataclass


@dataclass
class DrivingInstruction:
    """Class for defining a DrivingInstruction"""

    angle: float = 0.0
    speed: int = 1

    @property
    def speed(self) -> int:
        """Speed at which the Capra Hircus drives (m/s)"""
        return self.speed

    @speed.setter
    def speed(self, value: int) -> None:
        if not -2 <= value <= 2:
            raise ValueError("Speed must be between -2 and 2")

    def get_formatted_instruction(self):
        """Returns a driving instruction in the correct format for Capra Hircus"""

        return {
            "header": {
                "frame_id": "frame_id"
            },
            "twist": {
                "linear": {
                    "x": self.speed
                },
                "angular": {
                    "z": self.angle
                }
            }
        }
