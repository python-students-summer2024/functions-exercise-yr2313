"""
Do not run this file directly!  It won't work.
Run it using the Test panel in Visual Studio Code.
"""

import app_functions


class Tests:
    def test_roll_die(self, monkeypatch):
        """
        Check whether the function pseudo-randomly generates numbers between 1 and 6, inclusive.
        """

        def mock_randint(low, high):
            return low == 1 and high == 6

        monkeypatch.setattr("random.randint", lambda x, y: mock_randint(x, y))
        actual = app_functions.roll_die()
        assert actual == True

    def test_get_question_type(self, monkeypatch):
        """
        Check whether the function pseudo-randomly returns either "sum" or "difference"
        """
        # keep track of some status properties necessary to evaluate test
        status = {
            "using_random": False,
            "got_sum": False,
            "got_difference": False,
            "got_other": False,
        }

        # mock the random-related functions
        def mock_randint(low, high):
            status["using_random"] = True
            return 0

        def mock_random():
            status["using_random"] = True
            return 0

        # call the function 100 times
        for i in range(100):
            qtype = app_functions.get_question_type()
            if qtype == "sum":
                status["got_sum"] = True
            elif qtype == "difference":
                status["got_difference"] = True
            else:
                status["got_other"] = True
        # mock the raadom-related functions
        monkeypatch.setattr("random.randint", lambda x, y: mock_randint(x, y))
        monkeypatch.setattr("random.random", lambda: mock_random())
        # call the function now with the mocks in place
        app_functions.get_question_type()
        # determine if it's functioning correctly, based on the status properties
        assert status["using_random"] == True
        assert status["got_sum"] == True
        assert status["got_difference"] == True
        assert status["got_other"] == False

    def test_print_question(self, capsys):
        """
        Check whether the question is printed correctly.
        """
        app_functions.print_question(4, 3, "sum")
        captured = capsys.readouterr()  # capture print output
        assert (
            captured.out.strip()
            == "You rolled a 4 and a 3... What is the sum of 4 and 3?"
        )

        app_functions.print_question(1, 6, "sum")
        captured = capsys.readouterr()  # capture print output
        assert (
            captured.out.strip()
            == "You rolled a 1 and a 6... What is the sum of 1 and 6?"
        )

        app_functions.print_question(4, 3, "difference")
        captured = capsys.readouterr()  # capture print output
        assert (
            captured.out.strip()
            == "You rolled a 4 and a 3... What is the difference between 4 and 3?"
        )

        app_functions.print_question(1, 6, "difference")
        captured = capsys.readouterr()  # capture print output
        assert (
            captured.out.strip()
            == "You rolled a 1 and a 6... What is the difference between 1 and 6?"
        )

    def test_input_answer(self, monkeypatch):
        """
        Check whether the question is printed correctly.
        """
        input_values = ["6", "", "foo"]
        monkeypatch.setattr("builtins.input", lambda x: input_values.pop(0))

        actual = app_functions.input_answer()
        assert actual == 6

        actual = app_functions.input_answer()
        assert actual == -1

        actual = app_functions.input_answer()
        assert actual == -1

    def test_is_correct_answer(self):
        """
        Check whether the answers are judged as correct or incorrect accurately.
        """
        actual = app_functions.is_correct_answer(4, 2, "sum", 6)
        assert actual == True

        actual = app_functions.is_correct_answer(4, 2, "sum", 3)
        assert actual == False

        actual = app_functions.is_correct_answer(4, 2, "difference", 2)
        assert actual == True

        actual = app_functions.is_correct_answer(4, 2, "difference", 3)
        assert actual == False

        actual = app_functions.is_correct_answer(2, 4, "difference", 2)
        assert actual == True

    def test_print_congratulations(self, capsys):
        """
        Check whether the congratulatory message is output correctly.
        """

        app_functions.print_congratulations("sum")
        captured = capsys.readouterr()  # capture print output
        assert (
            captured.out.strip() == "Yes! Congratulations on the successful addition!"
        )

        app_functions.print_congratulations("difference")
        captured = capsys.readouterr()  # capture print output
        assert (
            captured.out.strip()
            == "Yes! Congratulations on the successful subtraction!"
        )

    def test_print_correct_answer(self, capsys):
        """
        Verify that the correct answer is output correctly.
        """

        app_functions.print_correct_answer(2, 3, "sum")
        captured = capsys.readouterr()  # capture print output
        assert captured.out.strip() == "No! The sum of 2 and 3 is 5!"

        app_functions.print_correct_answer(0, 6, "sum")
        captured = capsys.readouterr()  # capture print output
        assert captured.out.strip() == "No! The sum of 0 and 6 is 6!"

        app_functions.print_correct_answer(2, 3, "difference")
        captured = capsys.readouterr()  # capture print output
        assert captured.out.strip() == "No! The difference between 2 and 3 is 1!"

        app_functions.print_correct_answer(3, 2, "difference")
        captured = capsys.readouterr()  # capture print output
        assert captured.out.strip() == "No! The difference between 3 and 2 is 1!"

        app_functions.print_correct_answer(0, 6, "difference")
        captured = capsys.readouterr()  # capture print output
        assert captured.out.strip() == "No! The difference between 0 and 6 is 6!"

    def test_print_error(self, capsys):
        app_functions.print_error_message()
        captured = capsys.readouterr()  # capture print output
        assert captured.out.strip() == "Sorry - that is an invalid answer.  Bye Bye!"
