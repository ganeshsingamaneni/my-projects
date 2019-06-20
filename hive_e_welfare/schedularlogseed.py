from config import db
from models.hive.schedularlogs import Schedularlogs
from sqlalchemy_seed import (
    load_fixtures,
    load_fixture_files,
)


def main():
    path = '/home/caratred/my projects/e_welfare/hive_e_welfare'
    fixtures = load_fixture_files(path, ['accounts.json'])
    load_fixtures(db.session, fixtures)


if __name__ == '__main__':
    main()
