import asyncio
import requests
import aiohttp

def site_is_online(url, timeout=2):
    # Return True if the target URL is online. 
    # Raise an exception otherwise.

    error = Exception("unknown error")
    connection = requests.get(url, timeout=timeout)
    try:
        connection.status_code
        return True
    except Exception as e:
        error = e
        return error
    finally:
        connection.close()

async def site_is_online_async(url, timeout=2):
    """Return True if the target URL is online.

    Raise an exception otherwise.
    """
    error = Exception("unknown error")
    connection = requests.get(url, timeout=timeout)
    async with aiohttp.ClientSession() as connection:
        try:
            await connection.head(url, timeout=timeout)
            return True
        except asyncio.exceptions.TimeoutError:
            error = Exception("timed out")
            return error
        except Exception as e:
            error = e
            return error


