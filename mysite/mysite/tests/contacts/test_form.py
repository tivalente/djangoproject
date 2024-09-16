from contacts.forms import NameForm


def test_name_form_sucess():
    data = {"your_name": "Tiago"}
    form = NameForm(data)
    result = form.is_valid()

    assert result is True


def test_name_form_fail():
    data = {}
    form = NameForm(data)
    result = form.is_valid()

    assert result is False
