Inferencing과 Socket통신이 동시에 되는지 확인하기 위함
###순서
#1. git clone https://github.com/ChoiSeu/Test_Cap.git

#2. vi Makefile

#3. 'a' 누르면 수정 모드
=> ADDRESS랑 FILE 부분 맞게 수정
=> ADDRESS: 연결할 ip주소
=> FILE: 주고받을 파일 이름(원래는 입력받게 해놨는데 미리 정하게 해놓음. default는 output.pcap)

#4. esc 누르고 ':wq' 하면 저장하고 종료

#5. make clean

#6. make run

##+) 추론하는 샘플은 /samples에 있는 test_sample로 고정되어있음
##   터미널에서 예측결과가 출력되면서 소켓통신이 되는지만 확인하면 됨
