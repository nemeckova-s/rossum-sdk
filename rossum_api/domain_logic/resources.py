from __future__ import annotations

from enum import Enum


class Resource(Enum):
    """Convenient representation of resources provided by Elis API.

    Value is always the corresponding URL part.
    """

    Annotation = "annotations"
    Auth = "auth"
    Connector = "connectors"
    Document = "documents"
    EmailTemplate = "email_templates"
    Group = "groups"
    Hook = "hooks"
    Inbox = "inboxes"
    Organization = "organizations"
    Queue = "queues"
    Schema = "schemas"
    Task = "tasks"
    Upload = "uploads"
    User = "users"
    Workspace = "workspaces"
    Engine = "engines"