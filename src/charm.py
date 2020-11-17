#! /usr/bin/env python3
"""libraries needed for charm."""
from ops.charm import CharmBase
from ops.main import main
from ops.model import ActiveStatus


class CharmCharm(CharmBase):
    """Generic Charm Template."""
    def __init__(self, *args):
        """Initialize charm and configure states and events to observe."""
        super().__init__(*args)

        event_handler_bindings = {
            self.on.install:
            self._on_install,

            self.on.start:
            self._on_start,

        }
        for event, handler in event_handler_bindings.items():
            self.framework.observe(event, handler)

    def _on_install(self, event):
        self.unit.status = ActiveStatus("Charm Installed")

    def _on_start(self, event):
        self.unit.status = ActiveStatus("Charm Available")

if __name__ == "__main__":
    main(CharmCharm)
