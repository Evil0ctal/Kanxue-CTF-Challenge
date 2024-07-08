# 第六关

凯撒留下了什么？

## 附件

```text
0110100101101111011001000110101001111011001101110011000100110001001101010110100100110010001101100011000101100101011010010110011100110111011010010011010000110010011001000011010101100110011001110011011100110100001100010011001001100110011010000011100000110110011001000110010101100100001101110110100001111101
```

## 解题思路

这是一个二进制字符串，将其转换为 ASCII 码即可。

```python
binary_data = "0110100101101111011001000110101001111011001101110011000100110001001101010110100100110010001101100011000101100101011010010110011100110111011010010011010000110010011001000011010101100110011001110011011100110100001100010011001001100110011010000011100000110110011001000110010101100100001101110110100001111101"

# 将二进制数据分割成每8位一组
bytes_list = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]

# 将每个字节转换为字符
decoded_string = ''.join([chr(int(byte, 2)) for byte in bytes_list])

print(decoded_string)

# 输出：iodj{7115i261eig7i42d5fg7412fh86ded7h}
```

## iodj应该是flag的一部分，但是这个flag是错误的，因此需要对其进行解密，由于题目中提到了凯撒，因此可以尝试使用凯撒密码进行解密。

```python
def caesar_cipher_decrypt(cipher_text, shift):
    decrypted_text = ""
    for char in cipher_text:
        if char.isalpha():  # 只解密字母字符
            # 确定是大写还是小写字母
            ascii_offset = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
        else:
            decrypted_text += char
    return decrypted_text

cipher_text = "iodj{7115i261eig7i42d5fg7412fh86ded7h}"

# 尝试所有可能的位移值（从1到25）
results = {shift: caesar_cipher_decrypt(cipher_text, shift) for shift in range(1, 26)}
print(results)
```

## 输出所有可能的解密结果，找到正确的解密结果

```json
{
   "1":"hnci{7115h261dhf7h42c5ef7412eg86cdc7g}",
   "2":"gmbh{7115g261cge7g42b5de7412df86bcb7f}",
   "3":"flag{7115f261bfd7f42a5cd7412ce86aba7e}",
   "4":"ekzf{7115e261aec7e42z5bc7412bd86zaz7d}",
   "5":"djye{7115d261zdb7d42y5ab7412ac86yzy7c}",
   "6":"cixd{7115c261yca7c42x5za7412zb86xyx7b}",
   "7":"bhwc{7115b261xbz7b42w5yz7412ya86wxw7a}",
   "8":"agvb{7115a261way7a42v5xy7412xz86vwv7z}",
   "9":"zfua{7115z261vzx7z42u5wx7412wy86uvu7y}",
   "10":"yetz{7115y261uyw7y42t5vw7412vx86tut7x}",
   "11":"xdsy{7115x261txv7x42s5uv7412uw86sts7w}",
   "12":"wcrx{7115w261swu7w42r5tu7412tv86rsr7v}",
   "13":"vbqw{7115v261rvt7v42q5st7412su86qrq7u}",
   "14":"uapv{7115u261qus7u42p5rs7412rt86pqp7t}",
   "15":"tzou{7115t261ptr7t42o5qr7412qs86opo7s}",
   "16":"synt{7115s261osq7s42n5pq7412pr86non7r}",
   "17":"rxms{7115r261nrp7r42m5op7412oq86mnm7q}",
   "18":"qwlr{7115q261mqo7q42l5no7412np86lml7p}",
   "19":"pvkq{7115p261lpn7p42k5mn7412mo86klk7o}",
   "20":"oujp{7115o261kom7o42j5lm7412ln86jkj7n}",
   "21":"ntio{7115n261jnl7n42i5kl7412km86iji7m}",
   "22":"mshn{7115m261imk7m42h5jk7412jl86hih7l}",
   "23":"lrgm{7115l261hlj7l42g5ij7412ik86ghg7k}",
   "24":"kqfl{7115k261gki7k42f5hi7412hj86fgf7j}",
   "25":"jpek{7115j261fjh7j42e5gh7412gi86efe7i}"
}
```

## 从上面的结果中可以看到，当位移值为3时，解密结果为flag{7115f261bfd7f42a5cd7412ce86aba7e}，因此正确的flag为flag{7115f261bfd7f42a5cd7412ce86aba7e}。

