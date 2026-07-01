from cloudmortem.cli import main


def test_main_success(capsys):
    main([])
    captured = capsys.readouterr()

    assert "CloudMortem service executed successfully" in captured.out
    assert "CloudMortemService run started" in captured.out


def test_main_failure(capsys):
    main(["--fail"])
    captured = capsys.readouterr()

    assert "CloudMortem service failed intentionally" in captured.out
    assert "CloudMortemService run started" in captured.out
