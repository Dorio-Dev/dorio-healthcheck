# dorio-healthcheck [가제]
AWS와 같은 Cloud 환경에서 WEB/WAS 없이 Auto Healing(Min, MAX 가 1인 Auto Scaling)을 사용하기 쉽지 않다. 
Health check를 프로세스 단위를 할 수 없기 때문에 간단하게 프로세스를 체크 하고 프로세스의 상태를 return해주는 프로젝트를 간단히 만든다.