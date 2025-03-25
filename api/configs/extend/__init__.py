import decimal
from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings


class ExtendInfo(BaseSettings):

    OAUTH2_CLIENT_ID: Optional[str] = Field(
        description="OA client id for OAuth",
        default=None,
    )

    OAUTH2_CLIENT_SECRET: Optional[str] = Field(
        description="OA client secret key for OAuth2",
        default=None,
    )

    OAUTH2_CLIENT_URL: Optional[str] = Field(
        description="OA client url for OAuth2",
        default=None,
    )

    OAUTH2_TOKEN_URL: Optional[str] = Field(
        description="OA token url for OAuth2",
        default=None,
    )

    OAUTH2_USER_INFO_URL: Optional[str] = Field(
        description="OA user_info url for OAuth2",
        default=None,
    )

    EMAIL_DOMAIN: Optional[str] = Field(
        description="邮箱域名",
        default=None,
    )

    ADMIN_GROUP_ID: Optional[str] = Field(
        description="后台超级管理员权限组id",
        default="888",
    )

    RMB_TO_USD_RATE: Optional[decimal.Decimal] = Field(
        description="人民币兑美元汇率",
        default="7.26",
    )

    DEFAULT_LANGUAGE: Optional[str] = Field(
        description="默认语言",
        default="zh-Hans",
    )


class ExtendConfig(ExtendInfo):
    pass
