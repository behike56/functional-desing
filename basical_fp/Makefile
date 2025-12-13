# basical-fp 用 Makefile

# ==== 設定 ====
PYTHON ?= python
UV ?= uv
PKG_DIR := src/basical_fp
TEST_DIR := tests

.PHONY: help install dev test lint format clean

help:
	@echo "利用可能なターゲット:"
	@echo "  make install   - ランタイム依存関係のインストール (uv)"
	@echo "  make dev       - 開発用依存関係 (dev グループ) のインストール"
	@echo "  make test      - pytest を実行"
	@echo "  make lint      - ruff lint を実行"
	@echo "  make format    - ruff format を実行"
	@echo "  make clean     - キャッシュ類の削除"

# ==== 依存関係インストール ====

install:
	$(UV) sync --frozen

# 開発用依存関係 (dependency-groups.dev) も含めてインストール
dev:
	$(UV) sync --group dev

# ==== 品質管理 ====

# テスト
# 例: make test

 test:
	$(UV) run pytest $(TEST_DIR)

# Lint (ruff)
# 例: make lint
lint:
	$(UV) run ruff check $(PKG_DIR) $(TEST_DIR)

# フォーマット (ruff format)
# 例: make format
format:
	$(UV) run ruff format $(PKG_DIR) $(TEST_DIR)

# ==== メンテナンス ====

clean:
	find . -name "__pycache__" -type d -exec rm -rf {} +
	find . -name "*.pyc" -delete
	rm -rf .pytest_cache
