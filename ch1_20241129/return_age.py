#필수: 이름, 성별, 나이를 입력받고, 이를 출력하는 프로그램
#도전: 사용자의 성별 입력값에 대한 유효성 검사하기, 나잇대에 맞는 인사 메시지 출력하기

class Person:     #클래스 정의
  def __init__(self, name, gender, age):
    #변수 설정
    self.name = name
    self.gender = gender
    self.age = age

  #정보 출력 함수
  def display(self):
    #print(f"이름: {self.name}, 성별: {self.gender}\n나이: {self.age}")   #정보 출력

    #성별 입력값에 대한 유효성 검사
    while True:
      if self.gender == 'male' or self.gender == 'female':    #gender 값이 male 또는 female일 경우, 정보 출력
        #이름과 성별은 같은 행에 출력하고, 나이는 다음 행에 출력
        print(f"이름: {self.name}, 성별: {self.gender}\n나이: {self.age}")
        break
      else:     #gender에 잘못된 값을 입력한 경우, 오류 메세지 출력 및 올바른 성별 입력 받을 때까지 질문 반복
        print("잘못된 성별을 입력하셨습니다. 'male' 또는 'female'을 입력해주세요.")
        self.gender = input("성별: ").lower()     #성별 입력값 소문자로 변환

  #나잇대에 맞는 인사 메세지 출력 함수
  def greet(self):
    if self.age < 8:
      print(f"안녕하세요, {self.name}:) 어린이시군요!")
    elif self.age < 20:
      print(f"안녕하세요, {self.name}:) 학생이시군요!")
    else:
      print(f"안녕하세요, {self.name}:) 성인이시군요!")

#사용자로부터 정보 입력받기
age = int(input("나이: "))    #나이 입력값 정수형으로 변환
name = input("이름: ")
gender = input("성별(male/female): ").lower()   #성별 입력값 소문자로 변환


user_data = Person(name, gender, age)   #Person 객체 생성
user_data.display()     #객체 정보 출력
user_data.greet()       #인사 메세지 출력
