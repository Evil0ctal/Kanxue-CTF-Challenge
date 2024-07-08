# 第四关

## 题目

```
○● ●○ ●○ ●● ●● ●○ ●○

●○ ○○ ○○ ○● ○○ ○○ ○●

○○ ●○ ○○ ●○ ●● ●● ○○
```

## 解题思路

这一关的题目看着首先会想到0和1的组合，但是这个题目的0和1的组合并不是正确答案，以下是猜测逻辑：

将这些二进制数字转换为十六进制：

```
第一行： 01101011111010 -> 1ABEA
第二行： 10000001000001 -> 4041
第三行： 00100010111100 -> 22BC
```

尝试将十六进制转换为ASCII字符：

```python
# Convert binary to hexadecimal and then to ASCII
bin_to_hex = {
    "01101011111010": "1BEA",
    "10000001000001": "4141",
    "00100010111100": "22BC"
}

# Convert hex to ASCII
hex_to_ascii = {key: bytes.fromhex(value).decode('ascii', errors='ignore') for key, value in bin_to_hex.items()}
hex_to_ascii
```

报错，因为转换的十六进制不是ASCII字符，所以这个逻辑是错误的。

在网上搜索了一下，发现这个题目是一个盲文字符表，以列为观察，盲文对照解出来的答案是：

![Braille](https://ingeniumcanada.org/sites/default/files/inline-images/braille_diagram.jpg)

```
ikanxue
```

## Flag

```
flag{ikanxue}
```

