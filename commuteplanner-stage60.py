# === Stage 60: Add saved views for frequently used filters ===
# Project: CommutePlanner
class SavedView:
    def __init__(self, name, filters):
        self.name = name
        self.filters = filters

    def to_dict(self):
        return {"name": self.name, "filters": self.filters}

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["filters"])


class SavedViewManager:
    def __init__(self):
        self.views = []

    def add_view(self, name, filters):
        self.views.append(SavedView(name, filters))

    def get_view(self, name):
        for view in self.views:
            if view.name == name:
                return view
        return None

    def delete_view(self, name):
        self.views = [v for v in self.views if v.name != name]

    def list_views(self):
        return self.views

    def save_to_file(self, filename):
        import json
        with open(filename, "w") as f:
            json.dump([v.to_dict() for v in self.views], f, indent=2)

    def load_from_file(self, filename):
        import json
        if not os.path.exists(filename):
            return
        with open(filename, "r") as f:
            data = json.load(f)
        self.views = [SavedView.from_dict(d) for d in data]


saved_views = SavedViewManager()


def apply_saved_view(view_name):
    view = saved_views.get_view(view_name)
    if view:
        return view.filters
    return None


def export_saved_views(filename="saved_views.json"):
    saved_views.save_to_file(filename)


def import_saved_views(filename="saved_views.json"):
    saved_views.load_from_file(filename)
