# 3번: 로그 파일 재정렬

https://leetcode.com/problems/reorder-data-in-log-files/

## 람다 표현식

람다 표현식은 지나치게 사용하면 코드가 길어지고 가독성이 떨어질 수 있으므로 주의가 필요하다

```python
def func(x):
    return x.split()[1], x.split()[0]

s.sort(key=func) # func 을 사용
s.sort(key=lambda x: (x.split()[1], x.split()[0])) # 람다를 사용
```
