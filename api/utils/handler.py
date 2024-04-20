# python v3.9ではパイプ記法が使えないので、future機能を使えるようにする。python3.10^でパイプ記法が使えるようになる
from __future__ import annotations

from fastapi import Depends, HTTPException
from typing import NoReturn, Any
from api.consts.response_const import RESPONSE

# python v3.11^では、例外発生時の型としてtyping.Neverを使う
def not_found(model: Any | None) -> NoReturn:
    if model is not None:
        return

    response = RESPONSE.get('not_found')
    raise HTTPException(status_code=response.get('status'), detail=response.get('message'));
