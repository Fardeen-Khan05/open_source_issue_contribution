from fixit.cli import main


def test_version(capsys):
    try:
        main(["--version"])
    except SystemExit:
        pass
    assert "fixit" in capsys.readouterr().out


def test_palindrome_command(capsys):
    main(["palindrome", "level"])
    assert capsys.readouterr().out.strip() == "True"


def test_wc_file_option(tmp_path, capsys):
    file_path = tmp_path / "sample.txt"
    file_path.write_text("hello world\nhow are you", encoding="utf-8")

    result = main(["wc", "--file", str(file_path)])

    assert result == 0
    assert capsys.readouterr().out.strip() == "words=5 lines=2 chars=23"


def test_wc_file_not_found(capsys):
    result = main(["wc", "--file", "missing_file.txt"])

    assert result == 1
    assert "missing_file.txt" in capsys.readouterr().err
