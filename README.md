# hardware-backend

## uvの使い方

pythonの実行
```sh
uv run hello.py
```
パッケージの追加

```sh
uv add numpy
```

## ローカルでのテスト

```sh
uv run uvicorn main:app --reload

