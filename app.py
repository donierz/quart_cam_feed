from quart import Quart, render_template, Response
from cams import gen_frame_from_default_cam

app = Quart(__name__)

@app.route("/")
async def index():
    return await render_template('index.html')

@app.route('/video_feed')
async def video_feed():
    return Response(gen_frame_from_default_cam(),
        content_type='multipart/x-mixed-replace; boundary=frame')
        # multipart/x-mixed-replace is an HTTP header

if __name__ == "__main__":
    app.run(port=5000)
