// Imports Java Scanner
import java.util.Scanner;

public class CSC320_CTModule3_Jonathan {
    public static void main(String[] args) {
        // Scanner
        Scanner input = new Scanner(System.in);
        // Declared Variables for income, tax rate, and tax amount
        double income;
        double taxRate;
        double taxAmount;
        // Asks user for weekly income amount
        System.out.print("Please enter the weekly income: $");
        // Takes user input then stores in income variable
        income = input.nextDouble();

        // IF ELSE Loop for tax withholding percentage based on amount 
        if (income < 500) {
           taxRate = 0.10;
        } else if (income < 1500) {
            taxRate = 0.15;
        } else if (income < 2500) {
            taxRate = 0.20;
        } else {
            taxRate = 0.30;
        }
        // Calculates witheld tax by calculating user income and multiplying it by tax rate then stores in vaiable
        taxAmount = income * taxRate;
        // Prints weekly income entered
        System.out.println("Weekly income amount you entered: $" + income);
        // Prints tax witholding rate
        System.out.println("Tax Witholding Rate: " + (taxRate * 100) + "%");
        // Prints witheld tax amount
        System.out.println("Weekly income tax witheld: $" + taxAmount);
        // Closes Scanner
        input.close();
    }
}
