/*
-------------------------------------------------------------------
Psuedocode
1. Start
2. 
-------------------------------------------------------------------
*/
public class Home {
    
    private int square_feet;
    private String address;
    private String city;
    private String state;
    private int zip_code;
    private String model_name;
    private String sale_status;

    public Home(int square_feet, String address, String city, String state, int zip_code, String model_name, String sale_status) {
        try {
            this.square_feet = square_feet;
            this.address = address;
            this.city = city;
            this.state = state;
            this.zip_code = zip_code;
            this.model_name = model_name;
            this.sale_status = sale_status;
        } catch (Exception e) {
            System.out.println("Error creating home: " + e.getMessage());
        }
    }

    public String listHome() {
        try {
            String info = "Square Feet: " + square_feet;
            return info;
        } catch (Exception e) {
            System.out.println("Error no sqaure feet listed.");
        }
    }
}
