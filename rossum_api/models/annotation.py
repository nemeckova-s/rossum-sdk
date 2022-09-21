import datetime as dt
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Union

from rossum_api.models.automation_blocker import AutomationBlocker, AutomationBlockerContent
from rossum_api.models.document import Document
from rossum_api.models.user import User


@dataclass
class Annotation:
    url: str
    status: str
    schema: str
    modifier: Union[str, User]
    content: Union[List[AutomationBlockerContent], str]
    id: Optional[int] = None
    queue: Optional[str] = None
    creator: Optional[str] = None
    created_at: Optional[str] = None
    rir_poll_id: Optional[str] = None
    email: Optional[str] = None
    email_thread: Optional[str] = None
    has_email_thread_with_replies: bool = False
    has_email_thread_with_new_replies: bool = False
    suggested_edit: Optional[str] = None
    messages: List[Dict] = field(default_factory=list)
    time_spent: float = 0
    relations: List[str] = field(default_factory=list)
    pages: List[str] = field(default_factory=list)
    document: Optional[Union[str, Document]] = None
    confirmed_at: Optional[dt.datetime] = None
    modified_at: Optional[str] = None
    exported_at: Optional[str] = None
    arrived_at: Optional[str] = None
    assigned_at: Optional[str] = None
    organization: Optional[str] = None
    metadata: Dict[Any, Any] = field(default_factory=dict)
    automated: bool = False
    automation_blocker: Optional[Union[AutomationBlocker, str]] = None
    related_emails: List[str] = field(default_factory=list)