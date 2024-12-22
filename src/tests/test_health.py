from httpx import AsyncClient, Response


async def test_health(ac: AsyncClient):
    response: Response = await ac.get(url="/health")
    assert response.status_code == 200
    assert response.json() == "I'm alive"
