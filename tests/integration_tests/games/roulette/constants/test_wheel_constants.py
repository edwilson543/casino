from games.roulette.constants.wheel_constants import WheelParameters, WheelIds, WheelPrompts
from dataclasses import fields


class TestWheelConstantsConsistent:
    """
    Class to test that the same list of wheels, using the same names, has been defined in the WheelsIds Enum,
    the WheelPrompts Enum, and the WheelParameters data class.
    """

    # Test IDs are 1 to 1 with parameters data class
    def test_all_wheels_with_ids_have_parameters(self):
        for wheel in WheelIds:
            wheel_name = WheelIds(wheel).name
            assert hasattr(WheelParameters, wheel_name)

    def test_all_wheels_with_parameters_have_ids(self):
        for wheel_name in fields(WheelParameters):
            assert hasattr(WheelIds, wheel_name)

    # Test IDs are 1 to 1 with prompts
    def test_all_wheels_with_ids_have_prompts(self):
        for wheel in WheelIds:
            wheel_name = WheelIds(wheel).name
            assert hasattr(WheelPrompts, wheel_name)

    def test_all_wheels_with_prompts_have_ids(self):
        for wheel in WheelPrompts:
            wheel_name = WheelPrompts(wheel).name
            assert hasattr(WheelIds, wheel_name)
