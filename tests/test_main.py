"""
Do not run this file directly!  It won't work.
Run it using the Test panel in Visual Studio Code.
"""

import app_functions


class Tests:
    def test_main(self, capsys, monkeypatch):
        """
        Check whether the main function calls the correct functions and outputs the correct text.
        """

        monkeypatch.setattr("app_functions.roll_die", lambda: 5)
        monkeypatch.setattr("app_functions.get_question_type", lambda: "sum")
        monkeypatch.setattr(
            "app_functions.print_question",
            lambda x, y, z: print(
                "You rolled a 3 and a 5... What is the sum of 3 and 5?"
            ),
        )
        monkeypatch.setattr("app_functions.input_answer", lambda: 7)
        monkeypatch.setattr("app_functions.is_correct_answer", lambda w, x, y, z: False)
        monkeypatch.setattr(
            "app_functions.print_congratulations",
            lambda: print("Yes! Congratulations on the successful addition!"),
        )
        monkeypatch.setattr(
            "app_functions.print_correct_answer",
            lambda x, y, z: print("No! The sum of 3 and 5 is 8!"),
        )
        monkeypatch.setattr(
            "app_functions.print_error_message",
            lambda: print("Sorry - that is an invalid answer.  Bye Bye!"),
        )

        import main

        captured = capsys.readouterr()  # capture print output
        actual = captured.out.strip()
        actual = " ".join(actual.split())
        print(actual)
        expected = """
Welcome to the Math App!!!

You rolled a 3 and a 5... What is the sum of 3 and 5?
No! The sum of 3 and 5 is 8!

Game over!!!
Thank you for playing!!!
        """.strip()
        expected = " ".join(expected.split())
        assert actual == expected
