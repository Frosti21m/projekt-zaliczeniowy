from src.history_manager import HistoryManager


def test_save_operation_and_read_history(tmp_path):
    test_file = tmp_path / "history.txt"
    history_manager = HistoryManager(str(test_file))

    history_manager.save_operation(
        "Investment - Simple Interest",
        "principal=1000, rate=10, years=2",
        "1200.0"
    )

    history = history_manager.read_history()

    assert len(history) == 1
    assert "Investment - Simple Interest" in history[0]
    assert "principal=1000, rate=10, years=2" in history[0]
    assert "1200.0" in history[0]


def test_read_history_from_nonexistent_file(tmp_path):
    test_file = tmp_path / "missing_history.txt"
    history_manager = HistoryManager(str(test_file))

    history = history_manager.read_history()

    assert history == []