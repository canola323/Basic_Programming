public class CheckingAccount extends BankAccount {

    private double interestRate;

    public CheckingAccount() {
        super();
        interestRate = 0.0;
    }

    public void setInterestRate(double interestRate) {
        this.interestRate = interestRate;
    }

    public double getInterestRate() {
        return interestRate;
    }

    public void processWithdrawal(double amount) {
        withdrawal(amount);

        if (getBalance() < 0) {
            withdrawal(30.0);
            System.out.println("Overdraft fee of $30 has been assessed.");
        }
    }

    public void displayAccount() {
        accountSummary();
        System.out.println("Interest Rate: " + interestRate + "%");
    }
}