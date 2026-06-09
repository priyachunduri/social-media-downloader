from flask import Flask, request, render_template_string
import yt_dlp

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>SeeUrReel Downloader</title>
    <style>
        body{
            font-family: Arial,sans-serif;
            max-width:800px;
            margin:auto;
            padding:40px;
            text-align:center;
            background:#f7f7f7;
        }
        input{
            width:80%;
            padding:12px;
            font-size:16px;
        }
        button{
            padding:12px 20px;
            background:#ff4b4b;
            color:white;
            border:none;
            cursor:pointer;
        }
        .box{
            background:white;
            padding:20px;
            border-radius:10px;
            margin-top:20px;
        }
    </style>
</head>
<body>

<h1>🎬 SeeUrReel Downloader</h1>

<form method="POST">
    <input type="text" name="url" placeholder="Paste YouTube URL">
    <button type="submit">Get Link</button>
</form>

{% if link %}
<div class="box">
    <h3>{{title}}</h3>
    <a href="{{link}}" target="_blank">
        Download Video
    </a>
</div>
{% endif %}

{% if error %}
<div class="box">
{{error}}
</div>
{% endif %}

</body>
</html>
"""

@app.route("/", methods=["GET","POST"])
def home():

    if request.method == "POST":

        url = request.form.get("url")

        try:
            ydl_opts = {
                "quiet": True,
                "format": "best"
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)

            return render_template_string(
                HTML,
                link=info.get("url"),
                title=info.get("title")
            )

        except Exception as e:
            return render_template_string(
                HTML,
                error=str(e)
            )

    return render_template_string(HTML)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host
