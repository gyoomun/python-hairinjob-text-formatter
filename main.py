import re
import sys


def format_contact_text(text):
    """
    연락처 정보 텍스트를 포맷팅합니다.

    변환 규칙:
    - 업체주소, 전화번호, 채용담당자, 담당자연락처 키워드 뒤에 콜론(:)과 공백 추가
    - 각 키워드 앞에 줄바꿈 추가
    """
    # 키워드 목록
    keywords = ['업체주소', '전화번호', '채용담당자', '담당자연락처']

    # 각 키워드를 찾아서 변환
    for keyword in keywords:
        # 키워드 뒤에 공백이 오는 경우를 찾아 "키워드: "로 변환
        text = re.sub(f'{keyword} ', f'\n{keyword}: ', text)

    # 첫 번째 키워드 앞의 불필요한 줄바꿈 제거 (업체명 바로 다음)
    text = re.sub(r'(\S+)\n\n업체주소:', r'\1\n업체주소:', text)

    return text


def main():
    # 입력 텍스트 받기
    if len(sys.argv) > 1:
        # 파일에서 읽기
        input_file = sys.argv[1]
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                input_text = f.read()
        except FileNotFoundError:
            print(f"오류: 파일 '{input_file}'을 찾을 수 없습니다.")
            sys.exit(1)
        except Exception as e:
            print(f"오류: 파일을 읽는 중 문제가 발생했습니다: {e}")
            sys.exit(1)
    else:
        # 표준 입력에서 읽기
        print("텍스트를 입력하세요 (입력 완료 후 Ctrl+D 또는 Ctrl+Z를 누르세요):")
        input_text = sys.stdin.read()

    # 입력이 비어있는지 확인
    if not input_text.strip():
        print("오류: 입력 텍스트가 비어있습니다.")
        sys.exit(1)

    # 텍스트 포맷팅
    formatted_text = format_contact_text(input_text)

    # 결과 출력
    print(formatted_text)

    # 파일로 저장
    with open('output.txt', 'w', encoding='utf-8') as f:
        f.write(formatted_text)

    print("\n" + "="*50)
    print("결과가 output.txt 파일에 저장되었습니다.")


if __name__ == "__main__":
    main()
