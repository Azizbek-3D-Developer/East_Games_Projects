from fastapi import Request, HTTPException, Depends
from api.auth.jwt_auth import decode_access_token
from api.crud.user_crud import get_user_by_useremail  # async DB lookup

async def get_current_user(request: Request):
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    
    user_email = payload.get("sub")
    if not user_email:
        raise HTTPException(status_code=401, detail="Token missing user info")
    
    user = await get_user_by_useremail(user_email)
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    
    return user  # Returning full user object
