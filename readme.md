Aivle Schoool 3기 AI Track Team 11 BigProject
---
# 🐶 강아지킴
![Logoview](https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/76936390/ef567dce-5d1a-4dd2-9b41-2ab90c23fea7)

## 😊 Members
#### 곽채원, 김민수, 박예은, 류홍규, 박지환, 이윤열, 이태훈, 이혜주

## 📜 서비스 내용

**반려동물의 피부질환을 AI가 진단해주고, 수의사에게 물어볼 수 있는 서비스입니다.**

🌱 **유저 시나리오**

1. 반려동물의 피부질환 의심부위를 찍고 업로드한다.
2. 해당 의심부위의 피부질환을 AI가 진단한 결과를 알려준다.  
    2-1. AI 예상 질환에 대한 ChatGPT의 설명을 볼 수 있다.
3. 추가적인 질문사항이 있는 경우 Q&A 게시판에 질문을 올린다.  
    3-1. 질문당 하나의 ChatGPT의 답변이 작성된다.
4. 수의사의 답변을 확인한다.

🌱 **수의사 시나리오**

1. AI 피부질환 진단 서비스는 마찬가지로 사용할 수 있다.
2. Q&A 게시판에 올라오는 질문들에 답변을 작성한다.
3. 답변 개수와 퀄리티를 바탕으로 메인페이지에 병원 광고를 게시할 수 있으며, 사용자들의 AI 진단 후 추천 병원으로 광고할 수 있다.

## 🛠 기술 스택

🌟 **[Front](https://github.com/AIVLE-School-Third-Big-Project/Team11-Project-front)** 

- Android Studio (Java)

🌟 **[Backend](https://github.com/AIVLE-School-Third-Big-Project/Team11-Project-back)**

- Django
- AWS (EC2, RDS, S3)
- MySQL
- NGINX

## 🖥 개발 내용

**Frontend**는 **Android Studio**를 사용하여 **Android APP**을 구현했습니다.  
**Frontend**에서 **Backend**로의 통신은 **Retrofit2**를 이용하여 구현했습니다.  

**Backend**는 **Django REST Framwork** 를 사용하여 **REST API**를 구현하였고,  
**Backend 서버**의 경우 **AWS EC2**를 사용하고, DB와 Storage를 **RDS**와 **S3**로 분리해서 구현했습니다.  
DB는 **MySQL**을 사용했고, API 서버는 **NGINX**로 배포 하였습니다.

**AWS Architecture**

<img src="https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/76936390/e8881d14-809e-46a7-9b6d-97f693f8b4e3" width=75%>


### ✅ API 명세서

API에 대한 내용들은 Notion에 API 명세서를 작성하여 관리하고 있습니다. [[API 명세서 링크]](https://www.notion.so/957e66a93eee468b9ad01613f041ea0a?pvs=21)
![api명세서](https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/76936390/c3a723da-e594-43db-ada2-b922289de0e4)

### ✅ 로그인 관련 구현

Django REST Auth를 활용하여 기본적인 회원가입, 로그인, 로그아웃 등을 구현했습니다.

하지만 기본으로 제공해주는 User가 아니라, 아래와 같은 Field들을 추가하여 Custom User를 구현했습니다.

- Email을 로그인 시 사용 (기본은 Username)
- 수의사 여부 Field 추가
- 프로필 이미지 Field 추가 → Default로 pydenticon 이미지 사용

✔️ **JWT Token**

로그인할 때에는 `AccessToken` 과 `RefreshToken` 을 발급해 해당 토큰으로 사용자 정보를 확인할 수 있도록 구현했습니다.

✔️ **기타 User 관련 API**

회원가입 시 Email 중복 확인을 하는 API와, 비밀번호를 까먹었을 때 해당 아이디로 Email을 전송하여 비밀번호를 초기화할 수 있는 API를 구현했습니다. Front에서와 마찬가지로 비밀번호는 `SHA256` 암호화를 수행한 후 전달되도록 구현했습니다.

|비밀번호 초기화 메일|비밀번호 초기화 화면|
|---|---|
|![image](https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/76936390/ea45c4c8-2a2a-4c51-bb27-4bf21f1f8c64)|![image](https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/76936390/2899f85b-1dea-4f25-b664-033b187f4f4f)|


### ✅ Pet, Hospital API

User 별로 Pet 정보를 등록하는 API와 수의사일 경우 Hospital 정보를 등록하는 API를 구현했습니다.

Pet과 Hospital 은 UserID와 외래키로 연결되어있어, 로그인한 정보를 바탕으로 데이터 생성 시 자동으로 UserID를 가져오도록 구현했습니다.

**✔ Hospital 광고 API**

메인 화면에 답변 작성이 우수한 병원들을 광고하고 있습니다. 지금은 답변에 대한 Rank 알고리즘이 없어 ChatGPT를 제외한 병원들에서 랜덤하게 보여주고 있습니다. 

### ✅ Picture, Question, Answer API

우리의 핵심 기능인 사진을 찍어서 AI 진단을 받는 부분과 Q&A 게시판 부분을 담당하는 API 입니다.

**✔ Picture**

Picture는 유저의 PetID를 외래키로 가지기 때문에 사진을 찍어서 올릴 때 자신의 Pet만을 선택하도록 구현했습니다. 사진을 올린 후에는 AI 모델의 결과가 DB에 저장되도록 했습니다.

이후 해당 병명에 대한 설명을 ChatGPT API를 통해 받아와 DB에 저장하고 사용자에게 보여줍니다.

**✔ Question**

Question의 경우 마찬가지로 PictureID를 외래키로 가지기 때문에 해당 유저의 사진에만 접근하여 질문을 등록하도록 하였고, 조회는 누구나 가능하지만 쓰기, 수정, 삭제 기능은 유저 본인만 가능하도록 구현했습니다.

또한, Question이 등록될 때 해당 질문 내용을 바탕으로 ChatGPT에게 답변을 받을 수 있도록 했습니다. ChatGPT의 경우 응답이 오는 시간이 대략 10초 이상 걸리기 때문에 쓰레드로 구현하여 질문이 등록되는 것에 지연이 발생하지 않도록 했습니다.

**✔ Answer**

Answer의 경우 수의사의 경우에만 답변을 달 수 있도록 구현하였습니다.

### ✅ 아키텍처, ERD, Service Flow, UI/UX 흐름도 

|아키텍처|ERD|Service Flow|UI/UX 흐름도|
|---|---|---|---|
|![architecture](https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/30362867/44f10a37-b3cb-4b75-b071-91c8d7165565)|![erd](https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/76936390/3daa9449-c11f-4549-a373-a68f94f4935f)|![ServiceFlow](https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/30362867/0c3e4223-6e90-49c6-9ffd-a7f26dfbab0c)|![UI/UX](https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/30362867/62fc0f89-6c0c-4285-867f-97055b0bc3c4)|

### ✅ AI
무증상, 유증상 분류 후 유증상으로 분류된 데이터를 6가지의 Class로 분류하는 Flow를 가지고 있습니다.

✔️ **데이터**  
[AI HUB 반려동물 피부 질환 데이터](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=561)를 사용했습니다.  
~~AI HUB 데이터에서 무증상 데이터를 제공하지 않고 있어 **DALLE API**를 사용해 ***무증상 데이터를 생성***하여 학습을 진행했습니다.~~  
=> 뒤늦게 반려동물 무증상 데이터가 AI HUB에 올라와서 해당 데이터로 학습을 진행하였습니다.

✔️ **모델**  
모델은 pretrained InceptionV3를 사용했습니다.  ++ 이때까지 했던거 적어줍시다 (Unet, YOLO 등등)




## 👀 서비스 화면

![아이콘]https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/30362867/b065ebd2-5f48-4b87-bc32-b52d2c469f3d)
- 어플리케이션을 설치하면 위와 같은 아이콘이 나타납니다.

![로딩 화면](https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/30362867/6b8c76c4-b882-4aff-ab23-fadc0b01d678)
![로그인 화면](https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/30362867/4f898b67-f5e5-4d52-a779-c4fbfa588939)
- 아이콘을 눌러 실행하면 로딩화면을 거치고 로그인 화면에 도달합니다.

![회원가입 화면](https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/30362867/d814bc39-bc13-4f43-b87f-26f2b40d9d64)
![수의사 화면](https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/30362867/f1569f70-0abd-4150-ab7b-9e5493dcac34)
![약관 화면](https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/30362867/ead674fb-8369-41ae-b3b7-4036c2059ac4)
- 로그인 화면에서 회원가입 버튼을 누르면 위와 같은 화면에 도달합니다. 수의사 버튼을 누르면 병원 정보를 입력할 수 있는 화면이 나타나고, 약관 확인하기 문구를 클릭하면 약관을 확인 할 수 있는 화면이 나타납니다.

![이메일 화면](https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/30362867/35743f28-327e-4b44-aa0f-4e7355da6a67)
![로딩 화면](https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/30362867/8ff934ee-4455-4d6a-8361-800ec69bc830)
- 로그인 화면에서 비밀번호 초기화 문구를 클릭하면 이메일을 입력할 수 있는 화면이 나타나고 초기화 이메일 보내기 버튼을 누르면 위와 같은 메일을 받을 수 있습니다.




