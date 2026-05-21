# Code Review Report

**Reviewer**: Codex CLI v0.x
**Target**: sample.py
**Generated**: 2026-05-20T15:32:01Z

## 1. Summary

- Files changed: 1
- Lines added: +47
- Lines removed: 0
- Risk level: **Medium**

## 2. Findings

| # | File | Line | Severity | Issue |
|---|------|------|----------|-------|
| 1 | sample.py | 35 | High | `divide()` 함수의 ZeroDivisionError 방어 부재 |
| 2 | sample.py | 5–13 | Low | type hint는 있으나 None 입력 시 동작 미정 |
| 3 | sample.py | 47 | Low | `divide()` 호출 예시가 main 가드에 누락 |

## 3. Detailed Recommendations

### Finding 1 — `divide()` 의 ZeroDivisionError 방어 부재 (line 35)

```python
def divide(a: float, b: float) -> float:
    """두 수의 나눗셈을 반환한다."""
    return a / b   # ← b == 0 일 때 ZeroDivisionError 발생
```

**Suggested fix**:
```python
def divide(a: float, b: float) -> float:
    """두 수의 나눗셈을 반환한다.

    Raises:
        ValueError: b 가 0 일 때
    """
    if b == 0:
        raise ValueError("divisor must be non-zero")
    return a / b
```

### Finding 2 — None 입력 방어 (line 5–13, 16–27)

`add()` 와 `multiply()` 가 `float` type hint 를 보유하나, 런타임에 None 이 전달되면 `TypeError` 가 발생한다. 명시적 검증을 추가하는 것이 안전하다.

**Suggested fix**:
```python
def add(a: float, b: float) -> float:
    if a is None or b is None:
        raise ValueError("operands must not be None")
    return a + b
```

### Finding 3 — `divide()` 호출 예시 누락 (line 47)

`if __name__ == "__main__":` 블록에서 `divide()` 호출 예시가 없다. Finding 1 수정 후 다음 호출을 추가하여 동작을 검증한다:

```python
if __name__ == "__main__":
    print(f"add(2, 3) = {add(2, 3)}")
    print(f"multiply(2, 3) = {multiply(2, 3)}")
    print(f"divide(10, 2) = {divide(10, 2)}")
    # divide(1, 0)  # ValueError 발생 확인
```

## 4. 권고 적용 우선순위

| 우선순위 | Finding | 사유 |
|---|---|---|
| **즉시** | Finding 1 | 런타임 충돌 발생 가능 |
| **단기** | Finding 2 | API 견고성 향상 |
| **선택** | Finding 3 | 동작 검증 보강 |
