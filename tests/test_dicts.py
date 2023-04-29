import pytest

from utils import dicts

def test_get_val():
    assert dicts.get_val({"vcs": "mercurial"}, "vcs") == "mercurial"
    assert dicts.get_val({"vcs": "mercurial"}, "vcs", "git") == "mercurial"
    assert dicts.get_val({"vcs": "mercurial"}, "ere", "git") == "git"
    assert dicts.get_val({}, "vcs", "bazaar") == "bazaar"
