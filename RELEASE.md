# Release Instructions

These build and release instructions are intended for the maintainers and future maintainers of this project.

## Preparing a new version

* a version update in `packet/__init__.py`
* Update CHANGELOG.md with the new release notes
* Add a stub for the next set of Unreleased changes
* Create a PR with these changes
* Merge

## Tagging and Building

Pull down the merged changes:

```bash
git fetch origin
git checkout origin/master
```

Tag the commit:

```bash
git tag -a vAA.BB.CC origin/master -m vAA.BB.CC
```

Build the package using `setuptools`:

```bash
python setup.py sdist bdist_wheel
```

## Publishing

Make sure you have `~/.pypirc` correctly populated, as of today should look something like:

```
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username: username-here
password: password-here

[testpypi]
repository: https://test.pypi.org/legacy/
username: username-here (not necessarily same as real pypi)
password: password-here (not necessarily same as real pypi)
```

Then upload using twine to testpypi first:

```bash
twine upload -r testpypi dist/*
```

If everything looks good, push the tag to GH, and then push to the real
pypi:

```bash
git push origin --tags vAA.BB.CC
twine upload dist/*
```

Congratulations, you published `packet-python`, :raised_hands:!

