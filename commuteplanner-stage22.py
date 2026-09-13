# === Stage 22: Add favorite records and quick favorite listing ===
# Project: CommutePlanner
class Favorite:
    """A single favorite record."""
    def __init__(self, id, route_id, label):
        self.id = id
        self.route_id = route_id
        self.label = label

    def __repr__(self):
        return f"Favorite({self.id}, route_id={self.route_id}, label={self.label!r})"


class FavoriteStore:
    """Manages a collection of favorite records."""
    def __init__(self):
        self._favorites = []

    def add(self, route_id, label):
        fav = Favorite(len(self._favorites), route_id, label)
        self._favorites.append(fav)
        return fav

    def get(self, index):
        if 0 <= index < len(self._favorites):
            return self._favorites[index]
        raise IndexError("Favorite index out of range")

    def list_all(self):
        return list(self._favorites)

    def remove(self, index):
        if 0 <= index < len(self._favorites):
            return self._favorites.pop(index)
        raise IndexError("Favorite index out of range")

    def __len__(self):
        return len(self._favorites)
