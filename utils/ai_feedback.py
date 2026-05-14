import os
import json
import re
from openai import OpenAI


client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)


def _extract_string_value(text: str, key: str, default: str = "") -> str:
    """
    JSON이 조금 잘려도 특정 key의 문자열 값을 최대한 뽑는다.
    """
    pattern = rf'"{key}"\s*:\s*"([\s\S]*?)"(?=\s*,\s*"|\s*\}}|$)'
    match = re.search(pattern, text)

    if match:
        return match.group(1).strip()

    # 마지막 따옴표가 잘린 경우 대비
    pattern_unclosed = rf'"{key}"\s*:\s*"([\s\S]*)'
    match = re.search(pattern_unclosed, text)

    if match:
        value = match.group(1).strip()

        # 다음 key가 섞여 들어오면 자르기
        next_key_match = re.search(r'",\s*"[a-zA-Z_]+":', value)
        if next_key_match:
            value = value[:next_key_match.start()]

        return value.strip().strip('"').strip(",")

    return default


def _extract_int_value(text: str, key: str, default: int = 0) -> int:
    pattern = rf'"{key}"\s*:\s*(\d+)'
    match = re.search(pattern, text)

    if not match:
        return default

    return int(match.group(1))


def _extract_bool_value(text: str, key: str, default: bool = False) -> bool:
    pattern = rf'"{key}"\s*:\s*(true|false)'
    match = re.search(pattern, text, re.IGNORECASE)

    if not match:
        return default

    return match.group(1).lower() == "true"


def _parse_ai_result(text: str, sample_answer: str, max_score: int, pass_score: int) -> dict:
    """
    1순위: 완성된 JSON으로 파싱
    2순위: JSON이 잘려도 정규식으로 필요한 값만 추출
    """
    text = text.strip()

    if text.startswith("```"):
        text = text.replace("```json", "").replace("```", "").strip()

    # 1순위: 정상 JSON 파싱
    try:
        result = json.loads(text)

        score = int(result.get("score", 0))
        score = max(0, min(score, max_score))

        return {
            "score": score,
            "passed": score >= pass_score,
            "good": str(result.get("good", "")),
            "improve": str(result.get("improve", "")),
            "recommended_answer": str(result.get("recommended_answer", sample_answer)),
            "one_line_feedback": str(result.get("one_line_feedback", "")),
        }

    except Exception:
        pass

    # 2순위: 깨진 JSON에서 값 추출
    score = _extract_int_value(text, "score", 0)
    score = max(0, min(score, max_score))

    return {
        "score": score,
        "passed": score >= pass_score,
        "good": _extract_string_value(text, "good", ""),
        "improve": _extract_string_value(text, "improve", ""),
        "recommended_answer": _extract_string_value(
            text,
            "recommended_answer",
            sample_answer,
        ),
        "one_line_feedback": _extract_string_value(
            text,
            "one_line_feedback",
            "AI 피드백을 일부만 불러왔습니다.",
        ),
    }


def evaluate_short_answer(
    question: str,
    student_answer: str,
    key_points: list[str],
    sample_answer: str,
    max_score: int = 25,
    pass_score: int = 15,
) -> dict:
    api_key = os.environ.get("OPENAI_API_KEY")
    model_name = os.environ.get("OPENAI_MODEL", "gpt-5-mini")

    if not api_key:
        return {
            "score": 0,
            "passed": False,
            "good": "",
            "improve": "OPENAI_API_KEY가 설정되어 있지 않습니다.",
            "recommended_answer": sample_answer,
            "one_line_feedback": "API 키를 먼저 설정해 주세요.",
        }

    key_points_text = ", ".join(key_points)

    prompt = f"""
너는 의사과학자 연구설계 교육 사이트의 채점 튜터다.
학생의 주관식 답변을 평가하고 점수를 부여한다.

[문제]
{question}

[학생 답변]
{student_answer}

[포함하면 좋은 핵심 개념]
{key_points_text}

[예시 답안]
{sample_answer}

[채점 기준]
- 만점: {max_score}점
- 통과 기준: {pass_score}점 이상
- 핵심 개념이 충분히 포함되면 높은 점수를 준다.
- 답변이 너무 짧거나 핵심 개념이 부족하면 낮은 점수를 준다.
- 의학적으로 부정확한 내용이 있으면 감점한다.
- 학생을 비난하지 말고 교육적으로 피드백한다.
- good은 50자 이내로 써라.
- improve는 80자 이내로 써라.
- recommended_answer는 150자 이내로 써라.
- one_line_feedback은 50자 이내로 써라.

반드시 JSON 객체 하나만 출력해라.
JSON 밖에는 어떤 설명도 쓰지 마라.
마크다운 코드블록도 쓰지 마라.

형식은 반드시 아래와 같아야 한다.

{{
  "score": 0,
  "passed": false,
  "good": "좋은 점",
  "improve": "보완할 점",
  "recommended_answer": "추천 답변",
  "one_line_feedback": "한 줄 피드백"
}}

score는 반드시 0부터 {max_score} 사이의 정수로 써라.
passed는 score가 {pass_score} 이상이면 true, 미만이면 false로 써라.
"""

    try:
        response = client.responses.create(
            model=model_name,
            input=prompt,
            max_output_tokens=1200,
        )

        raw_text = response.output_text

        return _parse_ai_result(
            text=raw_text,
            sample_answer=sample_answer,
            max_score=max_score,
            pass_score=pass_score,
        )

    except Exception as e:
        return {
            "score": 0,
            "passed": False,
            "good": "",
            "improve": f"AI 채점 중 오류가 발생했습니다: {e}",
            "recommended_answer": sample_answer,
            "one_line_feedback": "AI 채점을 불러오지 못했습니다.",
        }