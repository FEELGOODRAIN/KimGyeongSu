# 전역변수
import cx_Oracle as cx
conn = cx.connect('scott' , '1234','127.0.0.1:1521/xe')
cur = conn.cursor()
  
employee_num = list()

def view():
    sql = 'select 사원번호 from company order by 사원번호'
    cur.execute(sql)
    m = cur.fetchall()   
    employee_num.clear()

    for i in m:
        employee_num.append(i[0])

def add_employee():
    try:
        emp_num = int(input('사원번호 : '))
        name = input('이름 : ')
        age = int(input('나이 : '))
        dept = input('부서(비워도 됨) : ')
        rank = input('직급(비워도 됨) : ')
        join_year = input('입사년도(yyyy.mm.dd 형식) : ')
        address = input('주소(비워도 됨) : ')
        salary = int(input('월급(만원) : '))
        
    except:
        print('정보를 올바르게 입력하세요. 초기 화면으로 돌아갑니다.')
    else:
        if emp_num in employee_num:
            print('사원번호는 중복될 수 없습니다.')
        else:
            sql = 'insert into company values(:1,:2,:3,:4,:5,:6,:7,:8)'
            cur.execute(sql,[emp_num , name , age , dept , rank , join_year , address , salary])
 
            conn.commit()
            print('등록 완료')
        
def correction():
    
    try:
        num = int(input('수정할 사원의 사원번호를 입력하세요 : '))
    except:
        print('사원번호는 숫자로 입력해야 합니다. 초기 화면으로 돌아갑니다.')
    else:
        if num not in employee_num:
            print('사원번호가 존재하지 않습니다')
        else:
            print('1.이름 2.나이 3.부서 4.직급 5.입사년도 6.주소 7.월급')
            try:
                num2 = int(input('어떤 정보를 수정할지 번호를 고르세요 : '))
            except:
                print('숫자를 입력하셔야 합니다. 초기 화면으로 돌아갑니다.')
            else:
                a = ['이름','나이','부서','직급','입사년도','주소','월급']

                b = a[num2-1]

                num3 = input('수정할 정보를 입력하세요 : ')

                if num2 == 2 or num2 == 7:
                    sql = f'UPDATE company SET {b} = :1 WHERE 사원번호 = :2'
                    num4 = int(num3)
                    cur.execute(sql,[num4,num])
                    conn.commit()
                    print('수정 완료')
                elif num2 == 6 or num2 ==1 or num2 == 3 or num2 == 4 or num2 == 5:
                    sql = f'UPDATE company SET {b} = :1 WHERE 사원번호 = :2'

                    cur.execute(sql,[num3,num])
                    conn.commit()
                    print('수정 완료')
                else:
                    print('수정할 정보가 옳지 않습니다') 
          
        
def dele():
    try:
        inp = int(input('삭제할 사원의 사원번호를 입력하세요 : '))
    except:
        print('숫자를 입력하셔야 합니다. 초기 화면으로 돌아갑니다.')
    else:
        if inp in employee_num:
            sql = 'delete from company where 사원번호 = :1'

            cur.execute(sql, [inp])
            conn.commit()
            print('삭제 완료')
        else:
            print('사원번호가 존재하지 않습니다')
        
def employee_show():
    try:
        inp2 = int(input('보고 싶은 사원의 사원번호를 입력하세요 : '))
    except:
        print('숫자를 입력해야 합니다. 초기 화면으로 돌아갑니다.')
    else:
        if inp2 not in employee_num:
            print('사원번호가 존재하지 않습니다')
        else:
            sql = 'select * from company where 사원번호 = :1'

            cur.execute(sql,[inp2])
            a = cur.fetchall()
            print(a)

def show_all():
    sql = 'select * from company order by 사원번호'
    cur.execute(sql)
    m = cur.fetchall()
    for i in m:
        print(i)

def dbConnection():
    import cx_Oracle as cx
    conn = cx.connect('scott' , '1234','127.0.0.1:1521/xe')
    return conn



# def main2():
#     conn = dbConnection()
#     cur = conn.cursor()
#     while True:   
#         view()
#         print()
#         print('============menu===========')
#         print('1.신규 사원 추가')
#         print('2.사원 정보 수정')
#         print('3.사원 정보 삭제')
#         print('4.특정 사원 정보 보기')
#         print('5.전체 사원 정보 보기')
#         print('6.작업 종료')
#         print('===========================')
#         print()
#         try:
#             menu = int(input('업무를 선택하세요 : '))
#         except:
#             print('숫자를 입력하세요.')
#         else:
#             if menu==1:
#                 add_employee()
#             elif menu==2:
#                 correction()
#             elif menu==3:
#                 dele()
#             elif menu==4:
#                 employee_show()
#             elif menu==5:
#                 show_all()
#             elif menu==6:
#                 print('작업을 종료합니다')
#                 break
#             else:
#                 print('잘못된 메뉴 선택입니다')
                
# if __name__=='__main__':
#     main2()