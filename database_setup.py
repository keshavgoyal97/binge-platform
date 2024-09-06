from app.utils.config import get_config
from yoyo import get_backend, read_migrations


def setup_db():
    backend = get_backend(get_config("PROD_OTHERS_DB_WRITER_URL"))
    migrations = read_migrations("migrations")
    with backend.lock():
        backend.apply_migrations(backend.to_apply(migrations))
