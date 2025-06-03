from flask import Blueprint, request, jsonify
from openai import OpenAI
import os

oracle_bp = Blueprint("oracle", __name__)
openai = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@oracle_bp.route("/", methods=["POST"])
def ask():
    data = request.json
    question = data.get("question", "")

    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are the Oracle of Aetherion. Speak with poetic wisdom."},
                {"role": "user", "content": question}
            ]
        )
        answer = response.choices[0].message.content
        return jsonify(answer=answer)
    except Exception as e:
        return jsonify(error="The Grove is silent..."), 500
