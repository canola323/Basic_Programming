//
public class BankAccount {
    // Holds account balance
    private double balance = 0.0;
    // Adds money
    public void deposit(double amount) {
        balance = balance + amount;
    }
    // 
    public void withdraw(double amount) {
        balance = balance - amount;
    }
    // Checks balance
    public double getBalance() {
        return balance;
    }
}