public class BankTest {

    public static void main(String[] args) {

        CheckingAccount checking = new CheckingAccount();

        checking.setFirstName("Jonathan");
        checking.setLastName("Canola");
        checking.setAccountID(100001);
        checking.setInterestRate(3.5);

        checking.deposit(15000.00);

        System.out.println("Before withdrawal:");
        checking.displayAccount();

        System.out.println();

        checking.processWithdrawal(1500.00);

        System.out.println();

        System.out.println("After withdrawal:");
        checking.displayAccount();
    }
}