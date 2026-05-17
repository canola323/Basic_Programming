/*
---------------------------------------------------------
Pseudocode
---------------------------------------------------------
1. Start
2. Create Scanner
3. Create counter set to 0
4. Start While Loop counter < 5
5. Ask user input for number
6. Add number to total
7. IF counter is == to 0 max = number min = number END IF
8. IF number > max then max = number END IF
9. IF number < min then min = number END IF
10. Counter increase
11. End WHILE Loop
12. Calculate Average
13. Calculate interest 20%
14. Display result
15. End
*/ 

import java.util.Scanner;

public class CSC320_CTModule4_Jonathan {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        int counter = 0;

        double number;
        double total = 0;
        double average;
        double max = 0;
        double min = 0;
        double interest;


        while(counter < 5) {
            System.out.println("Please enter a number:");

            number = input.nextDouble();

            total += number;

            if(counter == 0) {
                max = number;
                min = number;
            } 
            
            if(number > max) {
                max = number;
            }

            if(number < min) {
                min = number;
            }

            counter++;
        }

        average = total / 5;
        interest = total * 0.20;


        System.out.println("Total: " + total);
        System.out.println("Average: " + average);
        System.out.println("Maximum: " + max);
        System.out.println("Minimum: " + min);
        System.out.println("Interest: " + interest);

        input.close();
    }
}
