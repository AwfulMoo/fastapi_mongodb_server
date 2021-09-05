import uvicorn

if __name__ == '__main__':
    uvicorn.run(
        "app:main", port=8000, host="0.0.0.0"
    )
