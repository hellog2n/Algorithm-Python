# Algorithm-Python-2021



### (1) Repository에 이미 올라와 있는 파일을 지우는 방법.
Github Repository에 push 후 제거하고 싶은 파일이 있을 경우, `.gitignore`를 변경하여도 반영이 되지 않는다면?
이미 올라와 있는 파일은 Tracking이 되고 있기 때문에 Tracking 중인 파일 리스트를 삭제 해야한다.



~~~
$ git rm -r --cached .
$ git add .
$ git commit -m '커밋 메시지'
$ git push {remote} {branch}
