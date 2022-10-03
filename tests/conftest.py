import os
import tempfile

import pytest
from application import create_app
from application.commands import initialize, populate


@pytest.fixture(scope="session")
def app():
    db_fd, db_path = tempfile.mkstemp()

    app = create_app()
    app.config.update({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': "sqlite:///" + db_path + '.sqlite',
        "WTF_CSRF_ENABLED": False
    })

    with app.app_context():
        initialize()
        populate()

    yield app

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture(scope="session")
def client(app):
    return app.test_client()


@pytest.fixture(scope="session")
def runner(app):
    return app.test_cli_runner()
