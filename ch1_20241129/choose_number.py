#숫자 맞추기 게임
#필수: 플레이어는 숫자를 입력하고 컴퓨터가 생각한 숫자와 비교하여“작다" 혹은 "크다" 힌트를 받아가며 숫자를 맞추는 게임
#도전: 플레이어가 입력한 숫자가 범위를 벗어날 경우 유효한 범위 내의 숫자를 입력하도록 유도하고, 게임 재시작 여부에 따라 초기화/종료 기능 추가

import random     #random 모듈 호출

computer_choose_number = random.randint(1,10)   #1부터 10 사이의 랜덤한 숫자 생성
print("1부터 10 사이의 숫자를 선택했습니다.\n이 숫자는 무엇일까요?")

choose_numbers = []      #플레이어가 입력한 숫자를 저장하는 리스트

while True:      #플레이어가 숫자를 맞힐 때까지 반복
  try:
    player_choose_number = int(input("예상 숫자: "))     #플레이어가 숫자를 입력, 정수형으로 받기

    if player_choose_number < 1 or player_choose_number > 10:   #범위에 벗어난 숫자를 입력했을 경우, 다시 입력
      print("1부터 10 사이의 숫자를 입력해주세요.")
      continue

    if player_choose_number in choose_numbers:          #중복된 숫자를 입력했을 경우, 다시 입력
      print("중복된 숫자를 선택했습니다. 다시 입력해주세요 :)")
      continue

    choose_numbers.append(player_choose_number)  #플레이어가 입력한 숫자 리스트에 추가

    if player_choose_number < computer_choose_number:     #플레이어가 입력한 숫자가 컴퓨터가 생각한 숫자보다 작을 경우
      print("더 큰 숫자입니다.")
    elif player_choose_number > computer_choose_number:   #플레이어가 입력한 숫자가 컴퓨터가 생각한 숫자보다 클 경우
      print("더 작은 숫자입니다.")
    else:        #플레이어가 입력한 숫자와 컴퓨터가 생각한 숫자가 같을 경우
      print(f"정답입니다! 컴퓨터가 선택한 숫자는 {computer_choose_number}입니다.")
      #print("게임을 종료합니다.")        #묻지 않고 게임 종료
      #break

      #플레이어에게 게임을 다시 할 지 물어보기
      player_choose_retry = input("게임을 다시 하시겠습니까? (y/n): ").lower()    #재시작 여부 묻기, 입력값 소문자로 변환
      
      if player_choose_retry == 'y':    #재시작을 원할 때
        #게임 초기화
        print("-"*35)
        computer_choose_number = random.randint(1,10)   #1부터 10 사이의 랜덤한 숫자 생성
        print("1부터 10 사이의 숫자를 선택했습니다.\n이 숫자는 무엇일까요?")
        choose_numbers = []      #플레이어가 입력한 숫자를 저장하는 리스트 초기화
        continue 
      elif player_choose_retry == 'n':    #종료를 원할 때
        #게임 종료
        print("게임을 종료합니다. 다음에 다시 만나요:)")
        break
      else:
        #잘못된 입력을 했을 경우, 게임 종료
        print("잘못된 입력입니다. 게임을 종료합니다.")
        break
      
  except ValueError:      # 숫자가 아닌 값을 입력했을 경우, 다시 입력
    print("숫자만 입력해주세요.")
