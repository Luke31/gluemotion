from gluemotion import Gluemotion


def test_add_covid_check():
    gm = Gluemotion(text_col='text')
    rec = {'text': '彼のことは嫌いではないcovid！(;´Д`)'}
    output = gm.add_covid_check(rec)
    assert 'text' in output
    assert output['covid_mentioned'] is True


def test_add_covid_check_false():
    gm = Gluemotion(text_col='text')
    rec = {'text': '彼のことは嫌いではない！(;´Д`)'}
    output = gm.add_covid_check(rec)
    assert 'text' in output
    assert output['covid_mentioned'] is False


if __name__ == "__main__":
    test_add_covid_check()
    test_add_covid_check_false()
