import io
import logging

from aiohttp import ClientError, ClientSession, ClientTimeout, FormData

# telegra.ph disabled anonymous media uploads, so photos are hosted on catbox.moe
# (free, no API key, permanent storage, short URLs that fit String(100) columns).
UPLOAD_URL = 'https://catbox.moe/user/api.php'


async def upload_photo(bytes_photo: io.BytesIO) -> str | None:
    """Upload a photo and return its public URL, or None if the upload fails."""
    bytes_photo.seek(0)
    form = FormData()
    form.add_field('reqtype', 'fileupload')
    form.add_field('fileToUpload', bytes_photo, filename='photo.jpg', content_type='image/jpeg')
    try:
        async with ClientSession(timeout=ClientTimeout(total=30)) as session:
            async with session.post(UPLOAD_URL, data=form) as resp:
                text = (await resp.text()).strip()
    except (ClientError, TimeoutError) as e:
        logging.warning(f"Photo upload failed: {e!r}")
        return None

    if resp.status == 200 and text.startswith('https://') and len(text) <= 100:
        return text

    logging.warning(f"Unexpected photo upload response ({resp.status}): {text[:200]!r}")
    return None
