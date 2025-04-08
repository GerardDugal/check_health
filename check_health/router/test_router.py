from fastapi import APIRouter

router = APIRouter()

@router.post("/{test_id}")
def test(test_id: int):
    return {"test_id": test_id}