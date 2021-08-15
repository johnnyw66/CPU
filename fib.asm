

; Fibonacci Sequence generator - fits into 16 bytes.

 .ORG 0

 0  60 01 LDI 0x01
 2  35    STA 5
 3  3A    STA A
; Loop Starts here
 4  60 00 LDI 01  ; operand is self-modified
 6  1A    ADD A
 7  E0    OUT
 8  3F    STA F
 9  60 00 LDI 0x00 ; self-modified
 B  35    STA 5
 C  0F    LDA F
 D  3A    STA A
 E  44    JMP 4  ; Could save a byte by removing above opcode and using 'JMP 3'

 .ORG F

DB 00 ; Temp storage
