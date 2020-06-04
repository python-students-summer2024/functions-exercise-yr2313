"""
Do not run this file directly!  It won't work.
Run it using the Test panel in Visual Studio Code.
"""

import app_functions

class Tests:

    def test_is_square(self, monkeypatch):
        """
        Check whether the function returns True when length and height are the same, False otherwise.
        """
        # test equal length / height
        input_values = ["10", "10"]
        monkeypatch.setattr("builtins.input", lambda x: input_values.pop(0))
        actual = app_functions.is_square()
        assert actual == True
