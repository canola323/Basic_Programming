/*
------------------------------------------------------------------
Pseudocode
1. START
2. IMPORT Scanner
3. IMPORT ArrayList
4. Create Scanner
5. Create days ArrayList<String>
6. Create temperature ArrayList<Double>
7. add days Monday-Friday
8. add temperatures
9. Create STRING variable 
10. Ask user input for day or week
11. Set STRING variable to = user input
12. Create IF ELSE statement
13. Create FOR loop IF user input = week PRINT array list for days an temperature
14. ELSE boolean = false
15. Create FOR loop IF user input enters day of the week PRINT day with temperature boolean = true
16. IF not valid input PRINT error
17. Close IF ELSE statement
18. END
------------------------------------------------------------------
 */
// Import Tools Scanner & ArrayList
import java.util.Scanner;
import java.util.ArrayList;

public class CSC320_CTModule5_Jonathan {
    public static void main(String[] args) {
        // Start Scanner
        Scanner input = new Scanner(System.in);
        // Array list that contains a string
        ArrayList<String> days = new ArrayList<>();
        // Array list that contains numbers with decimals
        ArrayList<Double> temperatures = new ArrayList<>();
        // Adds days for days array list
        days.add("Monday");
        days.add("Tuesday");
        days.add("Wednesday");
        days.add("Thursday");
        days.add("Friday");
        days.add("Saturday");
        days.add("Sunday");
        // Adds temps to temperatures array list
        temperatures.add(72.0);
        temperatures.add(70.0);
        temperatures.add(72.0);
        temperatures.add(83.0);
        temperatures.add(76.0);
        temperatures.add(74.0);
        temperatures.add(74.0);
        // Empty string variable for user input
        String daysTemp;
        // Prompts user for input 
        System.out.println("Please enter a week day or for the full weeks temperature type week:");
        // Takes user input and adds to string variable daysTempe
        daysTemp = input.nextLine();
        // Statement for deciding output based on user input if input is "week" pirnts full week
        if (daysTemp.equalsIgnoreCase("week")) {
            double total = 0;
            // Loops though days and temps array to display week
            for (int i = 0; i < days.size(); i++){

                System.out.println(days.get(i) + ": " + temperatures.get(i));

                total += temperatures.get(i);
            }
            // Calculates average temp 
            double averageTemp = total / temperatures.size();
            // Prints average weekly temp
            System.out.println("Weekly average temperature: " + averageTemp);
        } else {
            // Sets boolean to false so if user input is not a valid selection from array list then prints error message
            boolean found = false;

            for (int i = 0; i < days.size(); i++) {
                
                if (daysTemp.equalsIgnoreCase(days.get(i))) {

                    System.out.println(days.get(i) + ": " + temperatures.get(i));

                    found = true;
                }
            }

            if (!found) {
                System.out.println("Invalid entry. Please enter a valid day or week.");
            }
        }
        input.close();
    }
}
