# python v3.9ではパイプ記法が使えないので、future機能を使えるようにする。python3.10^でパイプ記法が使えるようになる
from __future__ import annotations

from fastapi import Depends, HTTPException
from typing import NoReturn, Any, Dict
from api.consts.response_const import RESPONSE

# python v3.11^では、例外発生時の型としてtyping.Neverを使う
def not_found(model: Any | None) -> NoReturn:
    if model is not None:
        return

    response = RESPONSE.get('not_found')
    raise_http_exception(response)

def conflict(model: Any | None) -> NoReturn:
    if model is None:
        return

    response = RESPONSE.get('conflict')
    raise_http_exception(response)

def raise_http_exception(response: Dict) -> NoReturn:
    raise HTTPException(status_code=response.get('status'), detail=response.get('message'));

# class Response:
#     def __raise_http_exception(response: dict) -> NoReturn:
#         raise HTTPException(status_code=response.get('status'), detail=response.get('message'));

#     def not_found(model: Any | None, self) -> NoReturn:
#         if model is not None:
#             return

#         response = RESPONSE.get('not_found')
#         self.__raise_http_exception(response)
#     def bad_request(model: Any | None, self) -> NoReturn:
#         if model is not None:
#             return

#         response = RESPONSE.get('bad_request')
#         self.__raise_http_exception(response)
