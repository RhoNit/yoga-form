from apis import user

from db.config import setting
import fastapi as _fastapi


app = _fastapi.FastAPI(
    title=setting.TITLE,
    description=setting.DESCRIPTION,
    version=setting.VERSION,
    contact={
        "name": setting.NAME,
        "email": setting.EMAIL
    },
    redoc_url=None
)

app.include_router(user.router)