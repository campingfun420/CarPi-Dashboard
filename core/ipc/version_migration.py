import logging

logger = logging.getLogger("version_migration")

class VersionMigration:
    """
    Handles per-message type version migration.
    """

    def __init__(self):
        self._migrations = {}

    def register_migration(self, message_type: str, from_version: int, to_version: int, migration_func):
        self._migrations[(message_type, from_version)] = (to_version, migration_func)

    def migrate(self, message):
        key = (message.message_type, message.version)
        if key in self._migrations:
            new_version, func = self._migrations[key]
            message = func(message)
            message.version = new_version
            logger.info(f"Migrated {message.message_type} to v{new_version}")
        return message
