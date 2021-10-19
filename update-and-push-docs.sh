#!/bin/bash
poetry run python generate_docs.py && poetry run python -m sphinx -b html source docs && {
    git add -A && git commit -m "Update docs" && git push
}