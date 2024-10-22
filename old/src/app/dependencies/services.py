from typing import Annotated
from fastapi import Depends
from old.src.domain.auth.auth_service import AuthService
from old.src.domain.invitation.invitation_service import InvitationService


IAuthService = Annotated[AuthService, Depends()]
IInvitationService = Annotated[InvitationService, Depends()]
