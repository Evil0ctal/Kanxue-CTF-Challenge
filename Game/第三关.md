# 错误的MD5

错误的MD5:
ZmxhZ3tiOTc2OGEzN2I0N2JlYjJkODhlMmRib2U3NmEzOWJiM30=

# 解题思路

1. 通过题目给出的错误的MD5，可以知道这个MD5是一个base64编码的字符串，所以我们需要先对这个MD5进行base64解码。

- base64解码后的字符串为：
   - ZmxhZ3tiOTc2OGEzN2I0N2JlYjJkODhlMmRib2U3NmEzOWJiM30= -> flag{b9768a37b47beb2d88e2dboe76a39bb3}

2. 提交flag{b9768a37b47beb2d88e2dboe76a39bb3}发现不正确，所以我们需要对flag进行进一步处理。

3. 通过题目给出的错误的MD5，我们来判断这个MD5是否合法。MD5值是32位由数字“0-9”和字母“a-f”所组成的字符串，所以把里面的唯一可能有问题的字符修改一下。
    - b9768a37b47beb2d88e2dboe76a39bb3 -> b9768a37b47beb2d88e2db0e76a39bb3

4. 提交flag{b9768a37b47beb2d88e2db0e76a39bb3}，正确。