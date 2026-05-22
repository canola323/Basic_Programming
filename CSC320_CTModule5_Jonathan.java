/*
------------------------------------------------------------------
Pseudocode
1. Start
2. IMPORT Scanner
3. IMPORT ArrayList
4. Create Scanner
5. Create days ArrayList<String>
6. Create temperature ArrayList<Double>
7. add days Monday-Friday
8. add temperatures
9.

------------------------------------------------------------------
 */
import java.util.Scanner;
import java.util.ArrayList;

public class CSC320_CTModule5_Jonathan {
    public static void mainb(String[] args) {

        Scanner input = new Scanner(System.in);

        ArrayList<String> days = new ArrayList<>();
        ArrayList<Double> temperatures = new ArrayList<>();

        days.add("Monday");
        days.add("Tuesday");
        days.add("Wednesday");
        days.add("Thursday");
        days.add("Friday");
        days.add("Saturday");
        days.add("Sunday");
        
        temperatures.add(72.0);
        temperatures.add(70.0);
        temperatures.add(72.0);
        temperatures.add(83.0);
        temperatures.add(76.0);
        temperatures.add(74.0);
        temperatures.add(74.0);

        String daysTemp;

        System.out.println("Please enter a week day or for the full weeks temperature type week:");

        daysTemp = input.nextLine();

        if (daysTemp.equalsIgnoreCase("week")) {
            double total = 0;

            for (int i = 0; i < days.size(); i++){

                System.out.println(days.get(i) + ": " + temperatures.get(i));

                total += temperatures.get(i);
            }

            double averageTemp = total / temperatures.size();

            System.out.println("Weekly average temperature: " + averageTemp);
        } else {

            boolean found = false;

            for (int i = 0; i < days.size(); i++) {
                
                if (daysTemp.equalsIgnoreCase(days.get(i))) {

                    System.out.println(days.get(i) + ": " + temperatures.get(i));

                    found = true;
                }
            }

            if (!found) {
                System.out.println("Invalidd day entered.");
            }
        }
        input.close();
    }
}
