from pyct.cmd import fetch_data, clean_data
import pytest

DATASETS_CONTENT = """
data:
  - url: foo
    title: 'Fake Data'
    files:
      - foo.csv
"""

FOO_TEST_FILE_CONTENT = """
name,score,rank\n
Alice,100.5,1\n
Bob,50.3,2\n
Charlie,25,3\n
"""

FOO_REGULAR_FILE_CONTENT = """
name,score,rank\n
Alice,100.5,1\n
Bob,50.3,2\n
Charlie,25,3\n
Dave,28,4\n
Eve,25,3\n
Frank,75,9\n
"""


@pytest.fixture(scope='function')
def tmp_project(tmp_path):
    project = tmp_path / "test_project"
    project.mkdir()
    datasets = project / "datasets.yml"
    datasets.write_text(DATASETS_CONTENT)
    (project / "data").mkdir()
    return project

@pytest.fixture(scope='function')
def tmp_project_with_stubs(tmp_project):
    project = tmp_project
    data_stubs = project / "data" / ".data_stubs"
    data_stubs.mkdir()
    return project

@pytest.fixture(scope='function')
def tmp_project_with_test_file(tmp_project_with_stubs):
    project = tmp_project_with_stubs
    data_stub = project / "data" / ".data_stubs" / "foo.csv"
    data_stub.write_text(FOO_TEST_FILE_CONTENT)
    return project


def test_fetch_data_using_test_data_with_no_file_in_data_copies_from_stubs(tmp_project_with_test_file):
    project = tmp_project_with_test_file
    name = path = str(project)
    fetch_data(name=name, path=path, use_test_data=True)
    assert (project / "data" / "foo.csv").is_file()
    assert (project / "data" / "foo.csv").read_text() == FOO_TEST_FILE_CONTENT

def test_fetch_data_using_test_data_with_file_in_data_skips(tmp_project_with_test_file):
    project = tmp_project_with_test_file
    name = path = str(project)
    data = project / "data" / "foo.csv"
    data.write_text(FOO_REGULAR_FILE_CONTENT)
    fetch_data(name=name, path=path, use_test_data=True)
    assert (project / "data" / "foo.csv").is_file()
    assert (project / "data" / "foo.csv").read_text() == FOO_REGULAR_FILE_CONTENT

def test_fetch_data_using_test_data_and_force_with_file_in_data_over_writes(tmp_project_with_test_file):
    project = tmp_project_with_test_file
    name = path = str(project)
    data = project / "data" / "foo.csv"
    data.write_text(FOO_REGULAR_FILE_CONTENT)
    fetch_data(name=name, path=path, use_test_data=True, force=True)
    assert (project / "data" / "foo.csv").is_file()
    assert (project / "data" / "foo.csv").read_text() == FOO_TEST_FILE_CONTENT

def test_clean_data_when_data_file_is_real_does_nothing(tmp_project_with_test_file):
    project = tmp_project_with_test_file
    name = path = str(project)
    data = project / "data" / "foo.csv"
    data.write_text(FOO_REGULAR_FILE_CONTENT)
    clean_data(name=name, path=path)
    assert (project / "data" / "foo.csv").is_file()
    assert (project / "data" / "foo.csv").read_text() == FOO_REGULAR_FILE_CONTENT

def test_clean_data_when_data_file_is_from_stubs_removes_file_from_data(tmp_project_with_test_file):
    project = tmp_project_with_test_file
    name = path = str(project)
    data = project / "data" / "foo.csv"
    data.write_text(FOO_TEST_FILE_CONTENT)
    clean_data(name=name, path=path)
    assert not (project / "data" / "foo.csv").is_file()
    assert (project / "data" / ".data_stubs" / "foo.csv").is_file()
    assert (project / "data" / ".data_stubs" / "foo.csv").read_text() == FOO_TEST_FILE_CONTENT

def test_clean_data_when_file_not_in_data_does_nothing(tmp_project_with_test_file):
    project = tmp_project_with_test_file
    name = path = str(project)
    clean_data(name=name, path=path)
    assert not (project / "data" / "foo.csv").is_file()
    assert (project / "data" / ".data_stubs" / "foo.csv").is_file()
    assert (project / "data" / ".data_stubs" / "foo.csv").read_text() == FOO_TEST_FILE_CONTENT

def test_clean_data_when_stubs_is_empty_does_nothing(tmp_project_with_stubs):
    project = tmp_project_with_stubs
    name = path = str(project)
    data = project / "data" / "foo.csv"
    data.write_text(FOO_REGULAR_FILE_CONTENT)
    clean_data(name=name, path=path)
    assert (project / "data" / "foo.csv").is_file()
    assert not (project / "data" / ".data_stubs" / "foo.csv").is_file()

def test_clean_data_when_no_stubs_dir_does_nothing(tmp_project):
    project = tmp_project
    name = path = str(project)
    data = project / "data" / "foo.csv"
    data.write_text(FOO_REGULAR_FILE_CONTENT)
    clean_data(name=name, path=path)
    assert (project / "data" / "foo.csv").is_file()
