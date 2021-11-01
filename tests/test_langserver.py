import subprocess


# TODO: more tests


def test_entry_point() -> None:
    proc = subprocess.run(
        ['pyright-langserver'],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    assert proc.returncode == 1
    output = proc.stdout.decode('utf-8')
    assert 'Connection input stream is not set' in output
