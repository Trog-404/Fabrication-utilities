def test_importing_app():
    # this will raise an exception if pydantic model validation fails for th app
    from apps import app_entry_point_to_test

    assert app_entry_point_to_test.app.label == 'Remove steps'
