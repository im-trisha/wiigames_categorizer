from pydantic import BaseModel

def _to_snake_case(string: str) -> str:
    return ''.join(['_' + i.lower() if i.isupper() else i for i in string]).lstrip('_')



class USBGXModel(BaseModel):
    class Config:
        populate_by_name = True
        alias_generator = _to_snake_case