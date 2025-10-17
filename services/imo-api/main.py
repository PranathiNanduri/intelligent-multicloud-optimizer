import os
import sys
import traceback
import uvicorn

def run():
    port_str = os.getenv("PORT", "8080")
    try:
        port = int(port_str)
    except ValueError:
        print(f"Invalid PORT value: {port_str!r}. Falling back to 8080.", file=sys.stderr)
        port = 8080

    try:
        uvicorn.run(
            app,                    # your FastAPI app variable
            host="0.0.0.0",
            port=port,
            reload=False,
        )
    except Exception:
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    run()
