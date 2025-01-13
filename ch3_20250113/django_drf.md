# 📰 Django, DRF
</br>

## 📱 User와 Post 앱 개발 (MTV 패턴)

1. User 앱
- **사용자 모델(CustomUser) 구현**
    <details>
    <summary>기본 Django User 모델을 확장하여 커스텀 필드 추가</summary>
    <div markdown="1">

    - 프로필 이미지
    - 소개글

    </div>
    </details>

- **회원 구현**

    <details>
    <summary>회원 권한 기능 구현</summary>
    <div markdown="1">

    - 회원가입 (`signup`)
    - 로그인 (`login`)
    - 로그아웃 (`logout`)

    </div>
    </details>
    </br>

- **사용자 프로필 페이지 구현**
 
 </br>

2. Post 앱 (CRUD)
- **Post 모델 구현**

    <details>
    <summary>게시글 작성 모델의 기본 필드 구현</summary>
    <div markdown="1">

    - 제목
    - 내용
    - 작성자
    - 작성일
    - 수정일

    </div>
    </details>
    </br>

- **게시판 기능**

    <details>
    <summary>CRUD 구현</summary>
    <div markdown="1">

    - Read-List: 게시글 목록 보기 (`post_list`)
    - Read-Detail: 게시글 상세 보기 (`post_detail`)
    - Create: 게시글 작성 기능 (`post_create`)
    - Update: 게시글 수정 기능 (`post_update`)
    - Delete: 게시글 삭제 기능 (`post_delete`)

    </div>
    </details>
    </br>

### 필수앱 구현 참고
- views.py는 함수 or 클래스 (함수로 먼저 코딩)
- 베이스 템플릿: base.html
- 네비게이션 바: navbar.html
- 푸터: footer.html
- 데이터베이스: SQLite3
</br>


## 📜 DRF(Django Rest Framework)로 변환

1. **DRF(Django Rest Framework)로 변환**

    <details>
    <summary>API 변환 및 기능 구현</summary>
    <div markdown="1">

    - User와 Post 앱을 API로 변환
    - Serializer 구현
        -`UserSerialize`, `PostSerializer`
    - APIView 사용하여 CRUD 기능 구현
    - URL 설정 및 라우팅

    </div>
    </details>
    </br>

2. **좋아요 기능**

    <details>
    <summary>게시글의 좋아요 기능 구현</summary>
    <div markdown="1">

    - Post 모델에 좋아요 필드 추가
    - 좋아요 개수 표시

    </div>
    </details>
    </br>

3. **댓글 기능**

    <details>
    <summary>게시글의 댓글 기능 구현</summary>
    <div markdown="1">

    - Comment 모델 구현
    - 댓글 기능 (작성, 수정, 삭제)
    - 게시글 상세 페이지에 댓글 목록 표시

    </div>
    </details>
    </br>   

4. **데이터베이스**
- SQLite3에서 PostgreSQL or MySQL로 마이그레이션
   
