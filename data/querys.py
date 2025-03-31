create_query = """
    create table
    if not exists
    `user_info`
    (
        `id` varchar(32) primary key,
        `password` varchar(32) not null,
        `name` varchar(16)
    )
"""

# 로그인 쿼리
login_query = """
    select * from `user_info`
    where `id` = %s and `password` = %s
"""

# 회원 가입 쿼리
signup_query = """
    insert into `user_info`
    values (%s, %s, %s)
"""

# 아이디 중복 체크 쿼리
check_query = """
    select * from `user_info`
    where `id` = %s
"""