# Playwright E2E 테스트 과제

## 테스트 목적
Playwright 공식 TodoMVC 데모(https://demo.playwright.dev/todomvc)에서
할 일 추가, 완료 처리, 개수 표시가 정상 동작하는지 E2E로 검증합니다.

## 테스트 목록
| 테스트 | 내용 |
|---|---|
| test_add_todo | 할 일을 입력하고 Enter를 누르면 목록에 추가된다 |
| test_complete_todo | 체크박스를 클릭하면 완료 상태가 된다 |
| test_todo_count | 3개를 추가하면 개수가 3으로 표시된다 |

## 실행 방법
```bash
pip install -r requirements.txt
playwright install chromium
pytest
```
<img width="855" height="799" alt="과제" src="https://github.com/user-attachments/assets/40f25147-72f2-43d9-b91f-35b470024075" />
