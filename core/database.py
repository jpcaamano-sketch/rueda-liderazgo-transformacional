import uuid
from supabase import create_client


def _get_creds():
    from core.config import _get
    return _get("SUPABASE_URL"), _get("SUPABASE_KEY")


def get_db():
    url, key = _get_creds()
    return create_client(url, key)


def crear_participante(nombre: str, email: str) -> dict:
    token = str(uuid.uuid4())
    data  = (
        get_db()
        .table("lider_participantes")
        .insert({"nombre": nombre, "email": email, "token": token})
        .execute()
    )
    return data.data[0]


def get_participante_por_token(token: str) -> dict | None:
    data = (
        get_db()
        .table("lider_participantes")
        .select("*")
        .eq("token", token)
        .execute()
    )
    return data.data[0] if data.data else None


def guardar_respuestas(participante_id: int, respuestas: dict):
    rows = [
        {"participante_id": participante_id, "comportamiento_id": cid, "puntaje": val}
        for cid, val in respuestas.items()
    ]
    get_db().table("lider_respuestas").insert(rows).execute()


def marcar_completado(participante_id: int):
    (
        get_db()
        .table("lider_participantes")
        .update({"completado": True})
        .eq("id", participante_id)
        .execute()
    )
