#include <iostream>
#include <map>
#include <sstream>
using namespace std;

/*
字符	电码	字符	电码	字符	电码	字符	电码
A	.-	B	-...	C	-.-.	D	-..
E	.	F	..-.	G	--.	H	....
I	..	J	.---	K	-.-	L	.-..
M	--	N	-.	O	---	P	.--.
Q	--.-	R	.-.	S	...	T	-
U	..-	V	...-	W	.--	X	-..-
Y	-.--	Z	--..				
0	-----	1	.----	2	..---	3	...--
4	....-	5	.....	6	-....	7	--...
8	---..	9	----.				
.	.-.-.-	:	---...	,	--..--	;	-.-.-.
?	..--..	=	-...-	'	.----.	/	-..-.
!	-.-.--	-	-....-	_	..--.-	"	.-..-.
(	-.--.	)	-.--.-	$	...-..-	&	....
@	.--.-.			
*/

int main() {
    string code; // 存放摩斯密码
    // 摩斯密码解码映射表
    map<string, string> morseCodeDecoded = {
        {".-", "A"}, {"-...", "B"}, {"-.-.", "C"}, {"-..", "D"}, {".", "E"},
        {"..-.", "F"}, {"--.", "G"}, {"....", "H"}, {"..", "I"}, {".---", "J"},
        {"-.-", "K"}, {".-..", "L"}, {"--", "M"}, {"-.", "N"}, {"---", "O"},
        {".--.", "P"}, {"--.-", "Q"}, {".-.", "R"}, {"...", "S"}, {"-", "T"},
        {"..-", "U"}, {"...-", "V"}, {".--", "W"}, {"-..-", "X"}, {"-.--", "Y"},
        {"--..", "Z"}, {"-----", "0"}, {".----", "1"}, {"..---", "2"}, {"...--", "3"},
        {"....-", "4"}, {".....", "5"}, {"-....", "6"}, {"--...", "7"}, {"---..", "8"},
        {"----.", "9"}, {".-.-.-", "."}, {"---...", ":"}, {"--..--", ","}, {"-.-.-.", ";"},
        {"..--..", "?"}, {"-...-", "="}, {".----.", "'"}, {"-..-.", "/"}, {"-.-.--", "!"},
        {"-....-", "-"}, {"..--.-", "_"}, {".-..-.", "\""}, {"-.--.", "("}, {"-.--.-", ")"},
        {"...-..-", "$"}, {"....", "&"}, {".--.-.", "@"}
    };

    // 定义↑ 说明↓  -------
    cout << "---摩斯密码解码器---" << endl;
    cout << "(目前仅支持字母，数字，部分符号)" << endl;
    cout << "(支持字符以及对应的电码请见小工具目录下的说明)" << endl;
    cout << "--- Code by DuckStudio | 鸭鸭「カモ」 ---" << endl;

    // 说明↑ 程序↓ -------

    cout << "请输入需要解码的摩斯密码:";
    getline(cin, code); // 读取一行输入

    stringstream ss(code);
    string token;
    while (getline(ss, token, ' ')) {
        if (morseCodeDecoded.count(token) > 0) {
            cout << morseCodeDecoded[token];
        } else {
            cout << "*不受支持的电码*";
        }
    }

    // 程序↑ 说明↓  -------
    cout << endl;
    cout << "解码完毕！";

    cout << endl;
    system("pause"); // 结束前等待按下任意键，要放在return前面
    return 0;
}
