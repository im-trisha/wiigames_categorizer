from pydantic import BaseModel, Field

class DiscGame(BaseModel):
    id: str
    title: str | None = Field(alias="original title")
    size: int | None = Field(alias="size")
    hash: str | None = Field(alias="md5 hash")
    region: str | None = Field(alias="region")
    file_type: str | None = Field(alias="file type")
    partition_code: str | None = Field(alias="partition code")
    ios_version: str | None = Field(alias="ios version")
    date: int | None = Field(alias="date")
    developer: str | None = Field(alias="developer")
    publisher: str | None = Field(alias="publisher")
