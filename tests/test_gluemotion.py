from gluemotion import Gluemotion


def test_add_emotions():
    gm = Gluemotion(text_col='text')
    rec = {'text': '彼のことは嫌いではない！(;´Д`)'}
    output = gm.add_emotions(rec)
    assert 'text' in output
    assert 'orientation' in output
    assert 'emotion_representative' in output
    assert 'emotion_all' in output
    assert 'emoticons' in output


if __name__ == "__main__":
    test_add_emotions()
