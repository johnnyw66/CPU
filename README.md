# CPU using LogiSim Evolution
SAP1 Enhanced Version - (with JMP instructions and writing to RAM)
---
The LogiSim Evolution circuit called **sap1.circ** is a version of the SAP1 microprocessor from Albert Malvino's book **'Digital Computer Electronics - An introduction to Microcomputers'** (pub: 1983)

Instructions on how to program the unit are shown in the circuit design.
For those who have the book - I have referred to the 'WBUS' reference in Malvino's book as 'DBUS'.

My 16-bit address bus and enhanced ALU instructions are not being used in this design.


15th August 2021</br>

**SAP1 Enhanced.**

This enhanced version is now Turing Complete. It supports Write to Memory, Conditional Jumps.
For what it's worth - I have also added in a Load Immediate Instruction 'LDI', which is a two byte instruction.
The second byte - is the 8-bit value to which the A reg takes.

            .ORG 0

            LDI 0x01    
            STA E
            LDI 0xC9  ; loop 201 times - printing the decremented A Reg    
     LOOP:  OUT
            SUB E
            JPNZ LOOP
            HLT

            .ORG F
            .DB 0

(byte code: 60 01 3E 60 C1 E0 2E 55 F0)     

You can checkout the original Malvino SAP1 design with -

**git checkout sap1en**


14th August 2021</br>

I've tested this with a couple of simple programs - and it seems to behave as expected.
Please do let me know if you find any problems.

**Known Problems.**
If I run the CPU with a very high frequency - I noticed that erroneous LED segments were sometimes
being lit.</br>

After spending some time debugging the circuit (using Logisim logic to 'watch' for a particular segment pin going 'high')- I've come to the conclusion that the problem is with LogiSim. I'm still investigating!

**SAP1 Enhanced.**

The enhanced version is now Turing Complete (15th August 2021)
It supports Write to memory and conditional jumps.
For what it's worth - I have also added in a load immediate instruction 'LDI', which is a two byte instruction.
The second byte - is the 8-bit value to which the A reg takes.

            .ORG 0

            LDI 0x01
            STA E
            LDI 0xC9  ; loop 201 times - printing the decremented A Reg
     LOOP:  
            SUB E
            OUT
            JPNZ LOOP
            HLT

            .ORG F
            .DB 0

(byte code: 60 01 3E 60 C9 2E E0 55 F0)


15th August 2021

I have now included a simple programmer - (next to the RAM module).

Although it can address 16-bits, 12-bits are masked off for the original SAP1 machine.

I personally prefer to program the CPU with the LogiSim GUI.



Previous Posts
----





10th August 2021 </br>
Currently - newcpu.circ is the version running with latest LogiSim, 'LogiSim Evolution'.</br>





Control Lines  -


Data BUS (DBUS) Output

**clENREGR**	  - ALU Results Register onto DBUS</br>
**clEN4REG**    - Bank Register used with 2'b{clSelBank1,clSelBank0}</br>
**clENREGF**    - Flag Register - Perhaps to Save on stack?</br>
**clENKeyDBUS** - Keyboard input (For Debugging)</br>
**clENCons**    - Constants Bank </br>


DBUS (Writing From)
-----
**clWREGA** -- Write to A Register</br>
**clWREGB** -- Write to B Register</br>
**clWREGO** -- Write to Output Register (on Display)</br>
**clWREGF** -- Write to Flag Reg</br>
**clWREGR**	-- Write to Results Register</br>
**clWREGB0** -- Write to RegBank reg 0</br>
**clWREGB1** -- Write to RegBank reg 1</br>
**clWREGB2** -- Write to RegBank reg 2</br>
**clWREGB3** -- Write to RegBank reg 3</br>
**clWAL8BUS**   - ABUSL (low) 8-bit Reg  (Note: Output mapped onto to LOW end of Address Bus)+</br>
**clWAH8BUS**   - ABUSH (High) 8-bit Reg (Note: Output mapped onto to High end of Address Bus)+</br>
+ Set both these bits high to get full 16 bit address onto bus before doing a write. Data comes from DBUS</br>

**clWREGI** -- Write to Instruction Register **@TODO**</br>



ABUS16 Support   Address BUS (ABUS16) Output
------

**clNotEnPCReg** - PC Register (ACTIVE LOW!)</br>
**clEnSPReg**	- SP Register</br>
**clEnAL8BUS**  - 8 bits of AL8 Reg onto low end of ABUS16</br>
**clEnAH8BUS**  - 8 bits of AL8 Reg onto high end of ABUS16</br>




ABUS16 Support Writing
-----

**clWPCReg**  - Write to PC Register</br>
**clWSPReg**  - Write to SP Register</br>
**clWMAReg**  - Write to Memory Address Register **@TODO**</br>


Need
----

Instruction Register (8-bit)</br>
Memory Address Register (16-bit)?</br>
