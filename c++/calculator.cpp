#include <iostream>

// function
int main() {

    char op;
    double num1, num2;
    double result;

    std::cout << "it's calculator!";
    std::cout << "+, -, *, / 입력";
    std::cin >> op;

    std::cout << "첫 번째 숫자 입력";
    std::cin >> num1;

    std::cout << "두 번째 숫자 입력";
    std::cin >> num2;

    switch (op) {
        case '+' :
        result = num1 + num2; 
        std::cout << "결과" << num1 << " + " << num2 << " = " << result << std::endl;
        break;

        case '-' :
        result = num1 - num2;
        std::cout << "결과" << num1 << " - " << num2 << " = " << result << std::endl;
        break;

        case '*' :
        result = num1 * num2;
        std::cout << "결과" << num1 << " * " << num2 << " = " << result << std::endl;
        break;

        case '/' : 
        if (num2 != 0) {
            result = num1 / num2;
            std::cout << "결과" << num1 << " / " << num2 << " = " << result << std::endl;
        } else {
            std::cout << "error" << std::endl;
        } 
        break;

        default :
        std::cout << "error" << std::endl;
        break;
    }

    return 0;
}