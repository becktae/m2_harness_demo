"""sample.py — Claude가 M2 Step 3에서 산출한 코드 예시.

본 파일은 Claude Code 호출 1회로 생성된 후, Codex가 code_review Skill로 검토한다.
"""


def add(a: float, b: float) -> float:
    """두 수의 합을 반환한다.

    Args:
        a: 피연산자 1
        b: 피연산자 2

    Returns:
        a + b
    """
    return a + b


def multiply(a: float, b: float) -> float:
    """두 수의 곱을 반환한다.

    Args:
        a: 피연산자 1
        b: 피연산자 2

    Returns:
        a * b
    """
    return a * b


def divide(a: float, b: float) -> float:
    """두 수의 나눗셈을 반환한다.

    Note:
        본 함수는 의도적으로 ZeroDivisionError 방어가 없다.
        Codex의 review_report.md 에서 Finding 1 로 지적된다.
    """
    return a / b


if __name__ == "__main__":
    print(f"add(2, 3) = {add(2, 3)}")
    print(f"multiply(2, 3) = {multiply(2, 3)}")
