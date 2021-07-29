# 카카오코딩 1
# 아이디 길이는 3자 이상, 15자 이하
# 아이디는 알파벳 소문자, 숫자, 빼기(-), 마침표(.) 문자만 사용할 수 있음.
# 단, 마침표(.)는 처음과 끝에 사용할 수 없으며, 연속으로 사용할 수 없습니다.
# 규칙에 맞는지 검사하고, 맞지 않는 경우 새로운 아이디를 추천해줌.

# 
import re
def createID(): # 아이디 생성
    new_id = input("신규 ID를 입력하세요 : ")
    new_id = new_id.lower() # 소문자로 변환
    new_id = re.sub(r"[^a-z0-9-_.]","",new_id)
    return new_id

        
def checkDot(new_id): # 연속된 마침표 제거 함수          
    new_id = new_id.replace("..","")
    print(new_id)
    return new_id # 연속된 온점 중복삭제 후의 id를 반환

def recheckDot(id_checkrule): # 온점이 처음이나 마지막에 위치하면 제거
    id_recheckdot = [] # 수정된 배열을 새로삽입할 배열 생성
    if(id_checkrule[0] == '.'): # 처음이 온점이면 삭제
        (id_checkrule).remove(id_checkrule[0])
    if(id_checkrule[len(id_checkrule) == '.']): # 마지막이 온점이면 삭제
        id_checkrule.remove((id_checkrule[len(id_checkrule)]))
    id_recheckdot = id_checkrule # 수정된 배열을 새로운 배열에 대입 
    return id_recheckdot # 수정된 아이디 반환

def checkSpace(id_recheckdot):
    id_checkspace = [] # 공백을 a로 치환한 후 대입할 배열
    for i in range(0,id_recheckdot):
        if((id_recheckdot[i]) == ' '): # 공백이면
            (id_recheckdot[i]) = 'a' # a로 치환
    id_checkspace = id_recheckdot # 대입
    return id_checkspace

def checkLong(id_checkspace): # 문자열이 16자 이상이면 실행
    id_long = [] # 16자 이상인 경우 수정 후 대입할 배열
    for i in range(15,len(id_checkspace)): # 15번째 인덱스부터 삭제
        (id_checkspace).remove(id_checkspace[i])    
    id_long = id_checkspace
    return id_long

def checkShort(id_checkspace): # 문자열이 2자 이하이면 실행
    id_short = [] # 2자 이하일 경우 수정 후 대입할 배열
    while(len(id_checkspace) == 3): # 길이가 3자가 될때까지 반복
        (id_checkspace).append((id_checkspace[len(id_checkspace)]))
        #마지막 문자를 대입
    id_short = id_checkspace
    return id_short

id = createID() # 아이디 생성 함수 실행

checkDot(id) # 연속된 온점 검사 함수 실행 - 매개변수 : 규칙 의거 수정 아이디

recheckDot(checkDot) # 처음과 마지막 온점 검사 함수 실행 - 매개변수 : 연속된 중복온점 수정 아이디

checkSpace(recheckDot) # 공백 - a 치환 함수 실행 - 매개변수 : 최종 온점 수정 아이디

if(len(checkSpace) > 15): # 최종 수정 아이디의 길이가 16이상일 때 실행
    checkLong(checkSpace) # 규격 외 길이 제거 함수 실행 - 매개변수 : 최종 규칙수정 아이디
    print(checkLong) # 최종 추천 아이디 출력

elif(len(checkSpace) < 3): # 최종 수정 아이디의 길이가 2 이하일 때 실행
    checkShort(checkSpace) # 규격 외 길이 추가 함수 실행 - 매개변수 : 최종 규칙수정 아이디
    print(checkShort) # 최종 추천 아이디 출력

else:
    print(checkSpace) # 길이가 규격 내라면 최종 규칙수정 아이디 출력


        



    
        



        

